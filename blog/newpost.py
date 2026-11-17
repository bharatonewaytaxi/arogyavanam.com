# Usage: python3 blog/newpost.py blog/posts/<slug>.json  (run from arogyavana-site/)
# Clones the live template post (dist/blog/managed-farmland-benefits) for a new post, adds it to blog index + sitemap.
import re,json,html,math,sys,os
from urllib.parse import quote
P=json.load(open(sys.argv[1]));slug=P['slug'];T=P['title'];D=P['desc']
body=open(P['body']).read()
s=open('dist/blog/managed-farmland-benefits/index.html').read()
U=f'https://arogyavana.com/blog/{slug}/';OU='https://arogyavana.com/blog/managed-farmland-benefits/'
words=len(re.sub(r'<[^>]+>',' ',body).split());mins=math.ceil(words/220)
faq=re.findall(r'<h3>\d+\. ([^<]*\?)</h3>\s*<p>(.*?)</p>',body.split('frequently-asked-questions')[1],re.S)
e=html.escape;dt=P['date'];dtl=P['date_label'];img=P['img'];W,H=P['img_wh']
auth={"@type":"Organization","name":"Arogya Vana team","url":"https://arogyavana.com/"}
pub={"@type":"Organization","name":"Arogya Vana by Saptha Ventures","url":"https://arogyavana.com/","logo":{"@type":"ImageObject","url":"https://arogyavana.com/img/arogyavana-logo.webp"}}
ld={"@context":"https://schema.org","@graph":[{"@type":"Article","headline":T,"description":D,"image":["https://arogyavana.com"+img],"datePublished":dt,"dateModified":dt,"author":auth,"publisher":pub,"mainEntityOfPage":U,"inLanguage":"en-IN","wordCount":words,"timeRequired":f"PT{mins}M"},
{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub(r'<[^>]+>','',a)}} for q,a in faq]},
{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://arogyavana.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://arogyavana.com/blog/"},{"@type":"ListItem","position":3,"name":T,"item":U}]}]}
hd,rest=s[:s.index('<style>')],s[s.index('<style>'):]
hd=hd[:hd.index('<title>')]+f'''<title>{e(T)} | Arogya Vana Blog</title><meta name="description" content="{e(D)}"><link rel="canonical" href="{U}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#14321f">
<meta property="og:type" content="article"><meta property="og:site_name" content="Arogya Vana"><meta property="og:url" content="{U}"><meta property="og:title" content="{e(T)} | Arogya Vana Blog"><meta property="og:description" content="{e(D)}"><meta property="og:image" content="https://arogyavana.com{img}"><meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(T)} | Arogya Vana Blog"><meta name="twitter:image" content="https://arogyavana.com{img}">
'''+hd[hd.index('<link rel="icon"'):hd.index('<script type="application/ld+json">')]+'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>\n'
a=rest.index('<article class="art">');b=rest.index('</article>')
q=quote(U,safe='');qt=quote(T,safe='')
art=f'''<article class="art">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/blog/">Blog</a> › <span aria-current="page">{e(P['crumb'])}</span></nav>
<h1>{e(T)}</h1>
<div class="meta"><span>By <b>Arogya Vana team</b></span><span><time datetime="{dt}">{dtl}</time></span><span>{mins} min read</span></div>
<figure><img src="{img}" alt="{e(P['img_alt'])}" width="{W}" height="{H}" fetchpriority="high" decoding="async"></figure>
<div class="share" aria-label="Share this article"><b>Share:</b><a href="https://wa.me/?text={qt}%20{q}" target="_blank" rel="noopener" aria-label="Share on WhatsApp">WhatsApp</a><a href="https://www.facebook.com/sharer/sharer.php?u={q}" target="_blank" rel="noopener" aria-label="Share on Facebook">Facebook</a><a href="https://twitter.com/intent/tweet?url={q}&amp;text={qt}" target="_blank" rel="noopener" aria-label="Share on X">X</a><a href="https://www.linkedin.com/sharing/share-offsite/?url={q}" target="_blank" rel="noopener" aria-label="Share on LinkedIn">LinkedIn</a><button type="button" id="cpy">Copy link</button><button type="button" id="shr" hidden>More…</button></div>
<div class="prose">{body}</div>
<section class="cta" aria-labelledby="cta-h"><h2 id="cta-h">Explore Arogya Vana Phase 3</h2><p>Managed sandalwood farmland about 2 hours from Bengaluru – 4,400 sq.ft plots on the ₹25 lakh plan (₹15L land + ₹10L managed investment, returns as per agreement). Phase 1 is sold out and Phase 2 is about 75% sold. See the land in person before you decide.</p><div class="row"><a class="btn" href="/#visit">Book a Site Visit</a><a class="btn" href="https://wa.me/919886670006?text=Hello%2C%20I%20am%20interested%20in%20Arogya%20Vana%20Phase%203" target="_blank" rel="noopener">WhatsApp us</a><a class="btn ln" href="{P['pillar']}">{e(P['pillar_label'])}</a></div></section>
<p class="note">This article is general information, not financial or legal advice. Returns and appreciation are not guaranteed; review all project documents and seek independent advice before investing. Arogya Vana is a project of Saptha Ventures.</p>
'''
out=hd+rest[:a]+art+rest[b:]
assert OU not in out and 'managed-farmland-benefits' not in out.split('<footer')[0].split('<main')[1], 'template leak'
os.makedirs(f'dist/blog/{slug}',exist_ok=True);open(f'dist/blog/{slug}/index.html','w').write(out)
# blog index: prepend card + BlogPosting
ix=open('dist/blog/index.html').read()
if f'/blog/{slug}/' not in ix:
  card=f'<article class="card"><a href="/blog/{slug}/" tabindex="-1" aria-hidden="true"><img src="{img}" alt="" width="{W}" height="{H}" loading="lazy" decoding="async"></a><div><small><time datetime="{dt}">{dtl}</time> · {mins} min read</small><h2><a href="/blog/{slug}/">{e(T)}</a></h2><p>{e(P["card"])}</p><a class="btn ln" href="/blog/{slug}/" aria-label="Read the article: {e(T)}">Read the article</a></div></article>'
  ix=ix.replace('<div class="cards">','<div class="cards">'+card,1)
  ix=ix.replace('"blogPost": [','"blogPost": ['+json.dumps({"@type":"BlogPosting","headline":T,"url":U,"datePublished":dt,"image":"https://arogyavana.com"+img,"author":auth},ensure_ascii=False)+', ',1)
  open('dist/blog/index.html','w').write(ix)
sm=open('dist/sitemap.xml').read()
if U not in sm:
  ent=re.search(r'<url>\s*<loc>https://arogyavana.com/blog/managed-farmland-benefits/</loc>.*?</url>',sm,re.S).group()
  new=re.sub(r'<loc>[^<]*</loc>',f'<loc>{U}</loc>',ent);new=re.sub(r'<lastmod>[^<]*</lastmod>',f'<lastmod>{dt}</lastmod>',new);new=re.sub(r'<image:loc>[^<]*</image:loc>',f'<image:loc>https://arogyavana.com{img}</image:loc>',new)
  sm=sm.replace(ent,ent+'\n'+new,1)
  bl=re.search(r'<url>\s*<loc>https://arogyavana.com/blog/</loc>.*?</url>',sm,re.S).group()
  sm=sm.replace(bl,re.sub(r'<lastmod>[^<]*</lastmod>',f'<lastmod>{dt}</lastmod>',bl))
  open('dist/sitemap.xml','w').write(sm)
print(slug,words,mins,len(faq))
