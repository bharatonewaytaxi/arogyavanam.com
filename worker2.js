import { EmailMessage } from "cloudflare:email";
const J=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:{"content-type":"application/json"}});
const esc=s=>String(s||"").replace(/[\r\n]+/g," ");
function ist(){return new Date(Date.now()+19800000).toISOString().replace("T"," ").slice(0,19)+" IST"}
async function enquiry(r,env){
  if(r.method!=="POST")return J({ok:false,error:"Method not allowed"},405);
  let d;try{d=await r.json()}catch{return J({ok:false,error:"Invalid request"},400)}
  if(d.website)return J({ok:true});
  const name=String(d.name||"").trim().slice(0,100),phone=String(d.phone||"").trim().slice(0,20),email=String(d.email||"").trim().slice(0,120),plot=String(d.plot||"").slice(0,80),msg=String(d.message||"").slice(0,2000),page=String(d.page||"").slice(0,300);
  if(name.length<2)return J({ok:false,error:"Please enter your name"},400);
  if(!/^\+?[0-9 ()-]{8,20}$/.test(phone))return J({ok:false,error:"Please enter a valid phone number"},400);
  if(email&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email))return J({ok:false,error:"Please enter a valid email"},400);
  const ip=r.headers.get("cf-connecting-ip")||"",now=Date.now(),ua=(r.headers.get("user-agent")||"").slice(0,300);
  const c=await env.DB.prepare("SELECT COUNT(*) n FROM ratelimit WHERE ip=? AND ts>?").bind(ip,now-600000).first();
  if(c.n>=5)return J({ok:false,error:"Too many enquiries, please try again later"},429);
  await env.DB.prepare("INSERT INTO ratelimit VALUES(?,?)").bind(ip,now).run();
  await env.DB.prepare("DELETE FROM ratelimit WHERE ts<?").bind(now-86400000).run();
  const t=ist();
  const res=await env.DB.prepare("INSERT INTO enquiries(name,phone,email,plot_interest,message,page,created_at_ist,user_agent,ip) VALUES(?,?,?,?,?,?,?,?,?)").bind(name,phone,email,plot,msg,page,t,ua,ip).run();
  let mailed=false;
  try{
    const body=`New enquiry from arogyavana.com\n\nName: ${name}\nPhone: ${phone}\nEmail: ${email||"-"}\nPlot interest: ${plot}\nMessage: ${msg||"-"}\nPage: ${page}\nTime: ${t}\nUser agent: ${ua}\nID: ${res.meta.last_row_id}\n`;
    const raw=["From: Arogya Vana Website <enquiry@arogyavana.com>","To: arogyavanablr@gmail.com",email?`Reply-To: ${esc(email)}`:null,`Subject: New enquiry: ${esc(name)} (${esc(phone)})`,`Message-ID: <${crypto.randomUUID()}@arogyavana.com>`,`Date: ${new Date().toUTCString()}`,"MIME-Version: 1.0","Content-Type: text/plain; charset=utf-8","",body].filter(x=>x!==null).join("\r\n");
    await env.MAIL.send(new EmailMessage("enquiry@arogyavana.com","arogyavanablr@gmail.com",raw));mailed=true;
  }catch(e){console.log("mail fail",e.message)}
  return J({ok:true,id:res.meta.last_row_id,mailed});
}
export default{async fetch(r,env){const u=new URL(r.url);
  if(u.hostname==="www.arogyavana.com"){u.hostname="arogyavana.com";return Response.redirect(u.toString(),301)}
  if(u.pathname==="/api/enquiry")return enquiry(r,env);
  const a=await env.ASSETS.fetch(r);
  if(u.pathname.startsWith("/img/")){const h=new Headers(a.headers);h.set("cache-control","public, max-age=604800");return new Response(a.body,{status:a.status,headers:h})}
  return a}}
