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
const SLOTS=["09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"];
async function visit(r,env){
  if(r.method!=="POST")return J({ok:false,error:"Method not allowed"},405);
  let d;try{d=await r.json()}catch{return J({ok:false,error:"Invalid request"},400)}
  if(d.website)return J({ok:true});
  const name=String(d.name||"").trim().slice(0,100),phone=String(d.phone||"").trim().slice(0,20),date=String(d.date||""),slot=String(d.slot||""),lang=String(d.lang||"en").slice(0,5),page=String(d.page||"").slice(0,300);
  if(name.length<2)return J({ok:false,error:"Please enter your name"},400);
  if(!/^\+?[0-9 ()-]{8,20}$/.test(phone)||phone.replace(/\D/g,"").length<10)return J({ok:false,error:"Please enter a valid phone number"},400);
  if(!/^\d{4}-\d{2}-\d{2}$/.test(date))return J({ok:false,error:"Please choose a date"},400);
  const today=new Date(Date.now()+19800000).toISOString().slice(0,10),dd=new Date(date+"T00:00:00Z");
  if(isNaN(dd)||date<today)return J({ok:false,error:"Please choose a future date"},400);
  if((dd-new Date(today+"T00:00:00Z"))/86400000>60)return J({ok:false,error:"Please choose a date within the next 60 days"},400);
  if(dd.getUTCDay()===2)return J({ok:false,error:"We are closed on Tuesdays, please choose another day"},400);
  if(!SLOTS.includes(slot))return J({ok:false,error:"Please choose a time slot"},400);
  const ip=r.headers.get("cf-connecting-ip")||"",now=Date.now(),ua=(r.headers.get("user-agent")||"").slice(0,300);
  const c=await env.DB.prepare("SELECT COUNT(*) n FROM ratelimit WHERE ip=? AND ts>?").bind(ip,now-600000).first();
  if(c.n>=5)return J({ok:false,error:"Too many requests, please try again later"},429);
  await env.DB.prepare("INSERT INTO ratelimit VALUES(?,?)").bind(ip,now).run();
  const t=ist();
  const res=await env.DB.prepare("INSERT INTO site_visits(name,phone,visit_date,visit_slot,lang,page,created_at_ist,user_agent,ip) VALUES(?,?,?,?,?,?,?,?,?)").bind(name,phone,date,slot,lang,page,t,ua,ip).run();
  let mailed=false;
  if(!d.test){try{
    const body=`New site visit request from arogyavana.com\n\nName: ${name}\nPhone: ${phone}\nDate: ${date}\nTime slot: ${slot} IST\nLanguage: ${lang}\nPage: ${page}\nRequested: ${t}\nID: ${res.meta.last_row_id}\n`;
    const raw=["From: Arogya Vana Website <enquiry@arogyavana.com>","To: arogyavanablr@gmail.com",`Subject: Site visit request: ${esc(name)} on ${date} ${slot}`,`Message-ID: <${crypto.randomUUID()}@arogyavana.com>`,`Date: ${new Date().toUTCString()}`,"MIME-Version: 1.0","Content-Type: text/plain; charset=utf-8","",body].join("\r\n");
    await env.MAIL.send(new EmailMessage("enquiry@arogyavana.com","arogyavanablr@gmail.com",raw));mailed=true;
  }catch(e){console.log("mail fail",e.message)}}
  return J({ok:true,id:res.meta.last_row_id,mailed});
}
const REDIRECTS={"/sandalwood-farming-returns":"/sandalwood-growth-cycle/","/sandalwood-farming-returns/":"/sandalwood-growth-cycle/","/farmland-vs-gold-investment":"/farmland-vs-gold/","/farmland-vs-gold-investment/":"/farmland-vs-gold/","/nri-farmland-investment-karnataka":"/farmland-for-nris-karnataka/","/nri-farmland-investment-karnataka/":"/farmland-for-nris-karnataka/"};
export default{async fetch(r,env){const u=new URL(r.url);
  const rd=REDIRECTS[u.pathname];
  if(u.hostname==="www.arogyavana.com"||rd){if(u.hostname==="www.arogyavana.com")u.hostname="arogyavana.com";if(rd)u.pathname=rd;return Response.redirect(u.toString(),301)}
  if(u.pathname==="/google8f375ef84259a8e5.html")return new Response("google-site-verification: google8f375ef84259a8e5.html",{headers:{"content-type":"text/html; charset=utf-8"}});
  if(u.pathname==="/api/enquiry")return enquiry(r,env);
  if(u.pathname==="/api/site-visit")return visit(r,env);
  const a=await env.ASSETS.fetch(r);
  if(a.status===404&&r.method==="GET"){
    const accept=r.headers.get("accept")||"",looksLikeFile=/\.[a-zA-Z0-9]{2,5}$/.test(u.pathname);
    if(accept.includes("text/html")||!looksLikeFile){
      const nf=await env.ASSETS.fetch(new Request(new URL("/404",r.url),{method:"GET"}));
      const h=new Headers(nf.headers);h.set("content-type","text/html; charset=utf-8");h.set("cache-control","no-store");h.set("x-robots-tag","noindex, follow");
      return new Response(nf.body,{status:404,headers:h});
    }
  }
  if(u.pathname.startsWith("/img/")){const h=new Headers(a.headers);h.set("cache-control","public, max-age=2592000");return new Response(a.body,{status:a.status,headers:h})}
  return a}}
