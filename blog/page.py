import re,json,html
s=open('dist/index.html').read()
M=json.load(open('blog/meta.json'));body=open('blog/body.html').read()
style=re.search(r'<style>.*?</style>',s,re.S).group()
nav=s[s.index('<nav'):s.index('<header')]
foot=s[s.index('<footer'):s.index('<div class="mcta')]
wa=re.search(r'<a class="wa".*?</a>',s,re.S).group()
def fix(x):
  x=re.sub(r'href="#([a-z]+)"',r'href="/#\1"',x).replace('href="#"','href="/"')
  x=re.sub(r'<ul class="lng".*?</ul>','<ul class="lng" aria-label="Language"><li><a href="/blog/" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a></li></ul>',x,flags=re.S)
  return x.replace(' data-brochure','')
nav,foot=fix(nav),fix(foot)
nav=nav.replace('<nav class="nav"','<nav class="nav s"').replace('<li><a href="/#faq">FAQ</a></li></ul>','<li><a href="/#faq">FAQ</a></li><li><a href="/blog/" aria-current="page">Blog</a></li></ul>',1)
CSS='''<style>
body.pg{background:var(--cr,#f7f4ee)}.nav.s{background:#fff}
.art{max-width:760px;margin:0 auto;padding:120px 20px 40px}.crumb{font-size:.85rem;margin-bottom:14px}.crumb a{color:inherit}
.art h1{font-size:clamp(1.8rem,4vw,2.6rem);line-height:1.2;margin:.2em 0 .5em}.meta{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.9rem;color:#4b5a50;margin-bottom:22px}
.art figure{margin:26px 0}.art figure img{width:100%;height:auto;border-radius:12px;display:block}.art figcaption{font-size:.85rem;color:#4b5a50;margin-top:6px}
.prose{font-size:1.06rem;line-height:1.75}.prose h2{font-size:1.5rem;margin:1.8em 0 .5em;line-height:1.3;scroll-margin-top:90px}.prose h3{font-size:1.15rem;margin:1.4em 0 .4em}.prose p{margin:0 0 1em}.prose ul{margin:0 0 1.2em 1.2em;padding:0}.prose li{margin:.35em 0}.prose a{color:#14321f;font-weight:600}
.share{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:26px 0}.share a,.share button{min-height:44px;min-width:44px;display:inline-flex;align-items:center;justify-content:center;padding:0 14px;border:1px solid #14321f;border-radius:8px;color:#14321f;background:#fff;font:inherit;font-weight:600;text-decoration:none;cursor:pointer}
.cta{background:#14321f;color:#fff;border-radius:14px;padding:28px;margin:34px 0}.cta h2{color:#fff;margin:0 0 8px;font-size:1.4rem}.cta p{margin:0 0 16px}.cta .row{display:flex;flex-wrap:wrap;gap:10px}.cta .btn{background:#fff;color:#14321f}.cta .btn.ln{background:transparent;color:#fff;border-color:#fff}
.note{font-size:.85rem;color:#4b5a50;border-top:1px solid #ddd;padding-top:14px;margin-top:30px}
.cards{display:grid;gap:22px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}.card{background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.06)}.card img{width:100%;height:auto;display:block}.card div{padding:18px}.card h2{font-size:1.2rem;margin:.3em 0}.card a{color:#14321f}
</style>'''
U='https://arogyavana.com/blog/managed-farmland-benefits/'
T='Investing in Managed Farmland: Financial & Environmental Benefits'
D='Discover the financial and environmental benefits of investing in managed farmland – land appreciation, agricultural income, diversification, soil health and biodiversity – and what to check before you invest.'
def head(title,desc,url,ld,img='https://arogyavana.com/img/blog.webp',typ='article'):
  e=html.escape
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#14321f">
<meta property="og:type" content="{typ}"><meta property="og:site_name" content="Arogya Vana"><meta property="og:url" content="{url}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{img}"><meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:image" content="{img}">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&display=swap">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
{style}{CSS}</head>'''
pub={"@type":"Organization","name":"Arogya Vana by Saptha Ventures","url":"https://arogyavana.com/","logo":{"@type":"ImageObject","url":"https://arogyavana.com/img/arogyavana-logo.webp"}}
ld={"@context":"https://schema.org","@graph":[{"@type":"Article","headline":T,"description":D,"image":["https://arogyavana.com/img/blog.webp","https://arogyavana.com/img/sandal-real.webp"],"datePublished":"2026-10-16","dateModified":"2026-11-02","author":pub,"publisher":pub,"mainEntityOfPage":U,"inLanguage":"en-IN","wordCount":M['words'],"timeRequired":f"PT{M['mins']}M"},
{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub(r'<[^>]+>','',a)}} for q,a in M['faq']]},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://arogyavana.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://arogyavana.com/blog/"},{"@type":"ListItem","position":3,"name":T,"item":U}]}]}
from urllib.parse import quote
q=quote(U,safe='');qt=quote(T,safe='')
JS='''<script>var n=document.getElementById('nav'),bg=n.querySelector('.burger'),mn=document.getElementById('mnav');function mt(o){bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu');mn.hidden=!o;n.classList.toggle('open',o);document.body.style.overflow=o?'hidden':'';document.body.classList.toggle('mopen',o)}bg.addEventListener('click',function(){mt(mn.hidden)});mn.addEventListener('click',function(e){if(e.target.closest('a'))mt(false)});addEventListener('keydown',function(e){if(e.key==='Escape'&&!mn.hidden){mt(false);bg.focus()}});
var sb=document.getElementById('shr');if(sb){if(navigator.share)sb.hidden=false;sb.addEventListener('click',function(){navigator.share({title:document.title,url:location.href}).catch(function(){})})}
var cp=document.getElementById('cpy');if(cp)cp.addEventListener('click',function(){navigator.clipboard.writeText(location.href).then(function(){cp.textContent='Link copied';setTimeout(function(){cp.textContent='Copy link'},2000)})});</script>'''
MC='<div class="mcta"><a href="tel:+919886670006" class="btn ln">Call Now</a><a href="/#visit" class="btn">Book Visit</a></div>'
art=f'''<body class="pg"><a class="skip" href="#main">Skip to content</a>
{nav}<main id="main"><article class="art">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/blog/">Blog</a> › <span aria-current="page">Managed farmland benefits</span></nav>
<h1>{html.escape(T)}</h1>
<div class="meta"><span>By <b>Arogya Vana by Saptha Ventures</b></span><span><time datetime="2026-10-16">16 Oct 2026</time></span><span>{M['mins']} min read</span></div>
<figure><img src="/img/blog.webp" alt="Investing in Managed Farmland: Financial and Environmental Benefits – illustrated banner" width="1100" height="619" fetchpriority="high" decoding="async"></figure>
<div class="share" aria-label="Share this article"><b>Share:</b><a href="https://wa.me/?text={qt}%20{q}" target="_blank" rel="noopener" aria-label="Share on WhatsApp">WhatsApp</a><a href="https://www.facebook.com/sharer/sharer.php?u={q}" target="_blank" rel="noopener" aria-label="Share on Facebook">Facebook</a><a href="https://twitter.com/intent/tweet?url={q}&amp;text={qt}" target="_blank" rel="noopener" aria-label="Share on X">X</a><a href="https://www.linkedin.com/sharing/share-offsite/?url={q}" target="_blank" rel="noopener" aria-label="Share on LinkedIn">LinkedIn</a><button type="button" id="cpy">Copy link</button><button type="button" id="shr" hidden>More…</button></div>
<div class="prose">{body}</div>
<section class="cta" aria-labelledby="cta-h"><h2 id="cta-h">Explore Arogya Vana Phase 3</h2><p>Managed sandalwood farmland about 2 hours from Bengaluru – 4400 sq.ft plots on the ₹25 lakh plan (₹15L land + ₹10L investment). See the land in person before you decide.</p><div class="row"><a class="btn" href="/#enquire">Register Interest</a><a class="btn" href="/#visit">Book a Site Visit</a><a class="btn ln" href="/#plan">Try the plan calculator</a></div></section>
<p class="note">This article is general information, not financial or legal advice. Returns and appreciation are not guaranteed; review all project documents and seek independent advice before investing. Arogya Vana is a project of Saptha Ventures.</p>
</article></main>
{foot}{MC}{wa}{JS}</body></html>'''
open('dist/blog/managed-farmland-benefits/index.html','w').write(head(T+' | Arogya Vana Blog',D,U,ld)+art)
# index
BU='https://arogyavana.com/blog/'
ld2={"@context":"https://schema.org","@type":"Blog","name":"Arogya Vana Blog","url":BU,"publisher":pub,"blogPost":[{"@type":"BlogPosting","headline":T,"url":U,"datePublished":"2026-10-16","image":"https://arogyavana.com/img/blog.webp","author":pub}]}
idx=f'''<body class="pg"><a class="skip" href="#main">Skip to content</a>
{nav}<main id="main"><div class="art" style="max-width:1100px"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <span aria-current="page">Blog</span></nav>
<h1>Arogya Vana Blog</h1><p class="meta">Guides on managed farmland, sandalwood and land ownership from the Arogya Vana team.</p>
<div class="cards"><article class="card"><a href="/blog/managed-farmland-benefits/" tabindex="-1" aria-hidden="true"><img src="/img/blog.webp" alt="" width="1100" height="619" fetchpriority="high"></a><div><small><time datetime="2026-10-16">16 Oct 2026</time> · {M['mins']} min read</small><h2><a href="/blog/managed-farmland-benefits/">{html.escape(T)}</a></h2><p>Discover the financial and environmental benefits of investing in managed farmland, and what to check before you invest.</p><a class="btn ln" href="/blog/managed-farmland-benefits/" aria-label="Read the article: {html.escape(T)}">Read the article</a></div></article></div>
</div></main>{foot}{MC}{wa}{JS}</body></html>'''
open('dist/blog/index.html','w').write(head('Blog | Arogya Vana – Managed Farmland by Saptha Ventures','Articles on managed farmland, sandalwood and land ownership from Arogya Vana by Saptha Ventures.',BU,ld2,typ='website')+idx)
print('ok')
