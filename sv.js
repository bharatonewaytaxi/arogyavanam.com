(function(){var F=document.getElementById('sv');if(!F)return;var T=JSON.parse(document.getElementById('svt').textContent),L=document.documentElement.lang||'en',LC=L+'-IN';
var cal=document.getElementById('svd'),sl=document.getElementById('svs'),M=document.getElementById('svmsg'),sel={d:'',s:''};
var SL=['09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00'];
function p2(n){return(n<10?'0':'')+n}function iso(d){return d.getFullYear()+'-'+p2(d.getMonth()+1)+'-'+p2(d.getDate())}
var wd=new Intl.DateTimeFormat(LC,{weekday:'short'}),mo=new Intl.DateTimeFormat(LC,{month:'short'}),full=new Intl.DateTimeFormat(LC,{weekday:'long',day:'numeric',month:'long',year:'numeric'}),tf=new Intl.DateTimeFormat(LC,{hour:'numeric',minute:'2-digit'});
var t0=new Date();t0.setHours(0,0,0,0);var h='';
for(var k=0;k<7;k++){var x=new Date(2024,0,1+k);h+='<span class="wh" aria-hidden="true">'+wd.format(x)+'</span>'}
var off=(t0.getDay()+6)%7;for(k=0;k<off;k++)h+='<span class="bl" aria-hidden="true"></span>';
for(k=0;k<35;k++){var d=new Date(t0);d.setDate(t0.getDate()+k);var g=d.getDay(),tue=g===2,we=g===0||g===6,lbl=full.format(d)+(tue?' – '+T.closed:we?' – '+T.weekend:'');
h+='<button type="button" data-d="'+iso(d)+'" class="'+(we?'we':'')+(tue?' tu':'')+'" aria-pressed="false" aria-label="'+lbl+'"'+(tue?' disabled':'')+'><small>'+wd.format(d)+'</small><b>'+d.getDate()+'</b><small>'+(tue?T.closedS:mo.format(d))+'</small></button>'}
cal.innerHTML=h;
function slots(){var now=new Date(),td=sel.d===iso(now),o='';SL.forEach(function(s){var hh=+s.slice(0,2),dis=td&&hh<=now.getHours(),dt=new Date(2024,0,1,hh);o+='<button type="button" data-s="'+s+'" aria-pressed="'+(sel.s===s)+'"'+(dis?' disabled':'')+'>'+tf.format(dt)+'</button>'});sl.innerHTML=o;if(td&&sel.s&&+sel.s.slice(0,2)<=now.getHours())sel.s=''}
slots();
cal.addEventListener('click',function(e){var b=e.target.closest('button');if(!b||b.disabled)return;cal.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});sel.d=b.dataset.d;document.getElementById('sve-d').textContent='';slots()});
sl.addEventListener('click',function(e){var b=e.target.closest('button');if(!b||b.disabled)return;sl.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});sel.s=b.dataset.s;document.getElementById('sve-s').textContent=''});
function vf(x){var e=document.getElementById(x.getAttribute('aria-describedby')),m='';if(x.validity.valueMissing)m=x.name==='name'?T.eName:T.ePhone;else if(x.name==='phone'&&x.value.replace(/\D/g,'').length<10||x.validity.patternMismatch)m=T.ePhone2;e.textContent=m;x.setAttribute('aria-invalid',m?'true':'false');return !m}
F.querySelectorAll('input[aria-describedby]').forEach(function(x){x.addEventListener('blur',function(){vf(x)})});
F.addEventListener('submit',async function(ev){ev.preventDefault();var ok=true,first=null;
if(!sel.d){document.getElementById('sve-d').textContent=T.eDate;ok=false;first=first||cal.querySelector('button:not([disabled])')}
if(!sel.s){document.getElementById('sve-s').textContent=T.eSlot;ok=false;first=first||sl.querySelector('button:not([disabled])')}
[].forEach.call(F.querySelectorAll('input[aria-describedby]'),function(x){if(!vf(x)){ok=false;first=first||x}});if(!ok){first&&first.focus();return}
var b=F.querySelector('button[type=submit]');b.disabled=true;b.textContent=T.sending;var d=Object.fromEntries(new FormData(F));d.date=sel.d;d.slot=sel.s;d.lang=L;d.page=location.href;
try{var r=await fetch('/api/site-visit',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(d)});var j=await r.json();if(!(r.ok&&j.ok))throw new Error(j.error||'Error');
location.href='/thank-you?type=visit&lang='+L+'&date='+sel.d+'&slot='+sel.s+'&id='+(j.id||'')}
catch(e){b.disabled=false;b.textContent=T.submit;M.innerHTML='<p class="er2"></p>';M.firstChild.textContent=(e.message||'Error')+'. '+T.fail}})})();
