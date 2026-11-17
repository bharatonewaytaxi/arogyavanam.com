# Helpers for tools/seo.py (SEO/AEO/GEO pass, 16 Nov 2026).
import re,json,os
B='/workspace/arogyavana-site/new/'
SITE='https://arogyavana.com'
LOG=[]
def rd(rel): return open(B+rel,encoding='utf-8').read()
def wr(rel,s): open(B+rel,'w',encoding='utf-8').write(s)
def R(s,a,b,n=1):
    assert s.count(a)==n,(a[:80],s.count(a)); return s.replace(a,b)
def ea(x): return x.replace('&','&amp;').replace('"','&quot;')
def strip(x): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip()
def set_meta(s,title,desc,img_alt=None):
    t=ea(title); d=ea(desc)
    s=re.sub(r'<title>.*?</title>',lambda m:f'<title>{t}</title>',s,count=1,flags=re.S)
    s,n=re.subn(r'<meta name="description" content="[^"]*">',lambda m:f'<meta name="description" content="{d}">',s,count=1); assert n==1
    s=re.sub(r'<meta property="og:title" content="[^"]*">',lambda m:f'<meta property="og:title" content="{t}">',s,count=1)
    s=re.sub(r'<meta property="og:description" content="[^"]*">',lambda m:f'<meta property="og:description" content="{d}">',s,count=1)
    s=re.sub(r'<meta name="twitter:title" content="[^"]*">',lambda m:f'<meta name="twitter:title" content="{t}">',s,count=1)
    if '<meta name="twitter:description"' in s:
        s=re.sub(r'<meta name="twitter:description" content="[^"]*">',lambda m:f'<meta name="twitter:description" content="{d}">',s,count=1)
    else:
        s=re.sub(r'(<meta name="twitter:title" content="[^"]*">)',lambda m:m.group(1)+f'<meta name="twitter:description" content="{d}">',s,count=1)
    if img_alt and '<meta property="og:image:alt"' not in s:
        s=re.sub(r'(<meta property="og:image" content="[^"]*">)',lambda m:m.group(1)+f'<meta property="og:image:alt" content="{ea(img_alt)}">',s,count=1)
    return s
LDRE=re.compile(r'<script type="application/ld\+json">(.*?)</script>',re.S)
def ld_get(s):
    m=LDRE.search(s); return json.loads(m.group(1))
def ld_set(s,obj):
    j=json.dumps(obj,ensure_ascii=False); assert '</' not in j
    return LDRE.sub(lambda m:f'<script type="application/ld+json">{j}</script>',s,count=1)
def nodes(obj,typ):
    out=[]
    for n in obj.get('@graph',[]):
        t=n.get('@type'); t=t if isinstance(t,list) else [t]
        if typ in t: out.append(n)
    return out
def faq_items_html(items): return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)
def faq_add(s,items):
    """append Q&As to the first visible .faq block and to the FAQPage JSON-LD"""
    i=s.index('<div class="faq">'); j=s.index('</div>',i)
    s=s[:j]+faq_items_html(items)+s[j:]
    o=ld_get(s); f=nodes(o,'FAQPage')
    if not f: f=[{"@type":"FAQPage","mainEntity":[]}]; o['@graph'].append(f[0])
    have={q['name'] for q in f[0]['mainEntity']}
    for q,a in items:
        if strip(q) in have: continue
        f[0]['mainEntity'].append({"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}})
    return ld_set(s,o)
def faq_sync(s):
    """rebuild FAQPage mainEntity from every visible <details> on the page (keeps schema = visible text)"""
    qs=re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>',s,re.S)
    o=ld_get(s); f=nodes(o,'FAQPage')
    if not qs: return s
    if not f: f=[{"@type":"FAQPage"}]; o['@graph'].append(f[0])
    seen=set(); me=[]
    for q,a in qs:
        q2=strip(q)
        if q2 in seen: continue
        seen.add(q2); me.append({"@type":"Question","name":q2,"acceptedAnswer":{"@type":"Answer","text":strip(a)}})
    f[0]['mainEntity']=me
    return ld_set(s,o)
def ins_before_first(s,anchors,html):
    for a in anchors:
        if a in s:
            i=s.index(a); return s[:i]+html+s[i:]
    raise AssertionError('no anchor '+str(anchors))
def prose_start(s,html):
    a='<div class="prose">'; i=s.index(a)+len(a); return s[:i]+html+s[i:]
def h1(s,new):
    s,n=re.subn(r'<h1>.*?</h1>',lambda m:f'<h1>{new}</h1>',s,count=1,flags=re.S); assert n==1; return s
def hero_alt(s,alt):
    # first <figure><img ...> inside main
    i=s.index('<main'); m=re.compile(r'(<figure><img [^>]*?alt=")([^"]*)(")').search(s,i)
    assert m; return s[:m.start(2)]+ea(alt)+s[m.end(2):]
def fig(src,alt,w,h,cap=None):
    c=f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure><img src="{src}" alt="{ea(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async">{c}</figure>'
def related(s,links):
    html='<p class="rel"><b>Related guides:</b> '+' · '.join(f'<a href="{u}">{t}</a>' for u,t in links)+'</p>'
    m=re.search(r'<p>Related: .*?</p>',s)
    if m: return s[:m.start()]+html+s[m.end():]
    return ins_before_first(s,['<h2>Frequently asked questions</h2>','</div>\n<section class="cta"','<section class="cta"'],html)
def qa(q,a,idn=None):
    i=f' id="{idn}"' if idn else ''
    return f'<h2{i}>{q}</h2><p class="ans">{a}</p>'
