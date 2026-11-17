import json,sys
sys.path.insert(0,'.');from svsec import CSS,section
def R(s,a,b,n=1):
  assert s.count(a)>=1,a[:80]
  return s.replace(a,b) if n==0 else s.replace(a,b,n)
def apply(s,T,lang,L):
  # L: dict of ui strings for this lang
  s=R(s,"(a[0]==4?' / month':'')","(a[0]==4?' /mo':'')")
  s=R(s,'</style>',CSS+'\n.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}\n.lng{display:flex;list-style:none;gap:2px;margin:0 6px}.lng a{display:inline-flex;align-items:center;min-height:44px;min-width:44px;justify-content:center;padding:0 8px;font-size:.78rem;font-weight:600}.lng a[aria-current=true]{text-decoration:underline;text-underline-offset:4px}\n.nav .lng a{color:inherit}@media(max-width:1180px){.nav .lng{display:none}}.mnav .lng{margin:0 0 12px;flex-wrap:wrap}.mnav .lng a{border:1px solid var(--line);border-radius:var(--r)}\n.fsl .lng{margin:0}.fsl .lng a{color:#d7e2db}\n</style>',1)
  # hreflang
  hl='<link rel="alternate" hreflang="en-IN" href="https://arogyavana.com/"><link rel="alternate" hreflang="kn-IN" href="https://arogyavana.com/kn/"><link rel="alternate" hreflang="te-IN" href="https://arogyavana.com/te/"><link rel="alternate" hreflang="x-default" href="https://arogyavana.com/">'
  s=R(s,'<meta name="robots"',hl+'<meta name="robots"')
  def sw(cls=''):
    o=f'<ul class="lng" aria-label="{L["langlabel"]}">'
    for c,href,n in [('en','/','EN'),('kn','/kn/','ಕನ್ನಡ'),('te','/te/','తెలుగు')]:
      o+=f'<li><a href="{href}" hreflang="{c}" lang="{c}"'+(' aria-current="true"' if c==lang else '')+(' aria-label="English"' if c=='en' else '')+f'>{n}</a></li>'
    return o+'</ul>'
  s=R(s,'<a class="btn" href="#enquire" data-brochure>',sw()+'<a class="btn" href="/brochure.pdf" download="Arogya-Vana-Phase-3-Brochure.pdf" data-brochure>',1)
  s=R(s,'<div id="mnav" class="mnav" hidden>','<div id="mnav" class="mnav" hidden>'+sw())
  s=R(s,'href="#enquire" data-brochure>','href="/brochure.pdf" download="Arogya-Vana-Phase-3-Brochure.pdf" data-brochure>')
  s=R(s,'<div class="fsl">','<div class="fsl">'+sw())
  # site visit CTA
  s=R(s,'<li><a href="#faq">FAQ</a></li><li><a href="#enquire">Contact</a></li></ul>','<li><a href="#faq">FAQ</a></li><li><a href="#visit">'+L['svnav']+'</a></li><li><a href="#enquire">Contact</a></li></ul>')
  s=R(s,'<div class="ctas"><a class="btn wh" href="#enquire">Register Interest</a>','<div class="ctas"><a class="btn wh" href="#enquire">Register Interest</a><a class="btn gh" href="#visit">'+L['svcta']+'</a>')
  s=R(s,'<a href="#enquire" class="btn">Enquire Now</a></div>','<a href="#visit" class="btn">'+L['svmob']+'</a></div>')
  s=R(s,'<h2>Book a Farm Tour</h2><p>Call or WhatsApp us</p>','<h2>Book a Farm Tour</h2><p>Call or WhatsApp us, or <a href="#visit" style="text-decoration:underline;color:#fff">pick a date and time online</a>.</p>')
  # section before enquire
  i=s.index('<section class="sec off" id="enquire">');s=s[:i]+section(T,lang)+s[i:]
  s=R(s,'</body>','<script src="/sv.js" defer></script>\n</body>')
  # brochure click: allow download then go to form
  s=R(s,"document.querySelectorAll('[data-brochure]').forEach(function(a){a.addEventListener('click',function(){","document.querySelectorAll('[data-brochure]').forEach(function(a){a.addEventListener('click',function(){setTimeout(function(){var e=document.getElementById('enquire');e&&e.scrollIntoView({behavior:RM?'auto':'smooth'})},300);")
  # enquiry success -> thank-you
  i=s.index("if(r.ok&&j.ok){var w=wa(F);");j=s.index("else throw new Error",i)
  s=s[:i]+"if(r.ok&&j.ok){location.href='/thank-you?type=enquiry&lang='+(document.documentElement.lang||'en')+'&id='+(j.id||'');}\n"+s[j:]
  return s
if __name__=='__main__':
  T=json.load(open('/workspace/svt.json'))['en']
  L=dict(langlabel='Language',svnav='Site Visit',svcta='Book Site Visit',svmob='Book Visit')
  s=apply(open('index-v10.html').read(),T,'en',L);open('index.html','w').write(s);print('ok',len(s))
