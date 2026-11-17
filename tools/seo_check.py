import os,re,json,sys,html
B='new/'; OLD='backup-20261116-0540/assets/'
bad=0
def P(*a):
    global bad; bad+=1; print('FAIL',*a)
files=[os.path.relpath(os.path.join(d,f),B) for d,_,fs in os.walk(B) for f in fs]
htmls=[f for f in files if f.endswith('.html')]
REDIR={'/sandalwood-farming-returns/','/farmland-vs-gold-investment/','/nri-farmland-investment-karnataka/'}
titles={};descs={}
def text(s): return html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S)))
for f in htmls:
    s=open(B+f,encoding='utf-8').read()
    for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(j)
        except Exception as e: P('jsonld',f,e)
    for h in re.findall(r'href="(/[^"#?]*)',s):
        if h in REDIR: P('link to redirect',f,h); continue
        p=h.lstrip('/')
        if not (p=='' or os.path.exists(B+p) or os.path.exists(B+p+'index.html') or os.path.exists(B+p+'.html') or p in ('thank-you',)): P('broken link',f,h)
    for im in re.findall(r'<img [^>]*>',s):
        if 'id="lbi"' in im: continue
        if not re.search(r'alt="[^"]+"',im): P('noalt',f,im[:80])
        if 'width=' not in im or 'height=' not in im: P('nowh',f,im[:80])
        if 'decoding=' not in im: P('nodecoding',f,im[:80])
    if f.startswith(('kn/','te/')) or f in ('google8f375ef84259a8e5.html',): continue
    m=re.search(r'<main.*?</main>',s,re.S)
    if m:
        lv=[int(x) for x in re.findall(r'<h([1-6])',m.group(0))]
        if lv.count(1)!=1: P('h1 count',f,lv.count(1))
        for a,b in zip(lv,lv[1:]):
            if b>a+1: P('heading skip',f,a,b)
        # lazy: every img in main after the first should be lazy
        ims=re.findall(r'<img [^>]*>',m.group(0))
        for im in ims[1:]:
            if 'loading="lazy"' not in im and f!='index.html': P('notlazy',f,im[:70])
    t=re.search(r'<title>(.*?)</title>',s,re.S).group(1); d=re.search(r'<meta name="description" content="([^"]*)"',s)
    if 'noindex' not in s:
        titles.setdefault(t,[]).append(f)
        if d: descs.setdefault(d.group(1),[]).append(f)
        if len(html.unescape(t))>70: print('WARN long title',len(html.unescape(t)),f,t)
        if d and not 70<=len(html.unescape(d.group(1)))<=175: print('WARN desc len',len(d.group(1)),f)
        if 'rel="canonical"' not in s and f not in ('thank-you.html',): P('nocanonical',f)
    for a in re.findall(r'<p class="ans">(.*?)</p>',s,re.S):
        n=len(text(a).split())
        if not 38<=n<=62: print('WARN ans words',n,f,text(a)[:60])
for k,v in titles.items():
    if len(v)>1: P('dup title',k,v)
for k,v in descs.items():
    if len(v)>1: P('dup desc',v)
# banned text: everywhere (text files), and "farmhouse"/stay words only in NEW text vs old
BAN=[r'98866',r'99000 92996',r'\b349\b',r'13,15,600',r'\breturns?\b(?! to)',r'payout',r'\byield',r'profit',r'\bROI\b',r'buy-?back',r'\[CONFIRM',r'Sobha',r'Prestige',r'WhatsApp',r'\binvest',r'\bincome\b',r'apprecia',r'15 ?L\b|15 lakh|25 ?L\b|10 ?L\b']
for f in files:
    if not f.endswith(('.html','.txt','.xml','.js')): continue
    s=open(B+f,encoding='utf-8').read()
    vis=text(s) if f.endswith('.html') else s
    vis=vis.replace('sandalwood-farming-returns','').replace('farmland-vs-gold-investment','').replace('nri-farmland-investment-karnataka','')
    for b in BAN:
        for m in re.finditer(b,vis,re.I):
            ctx=vis[max(0,m.start()-50):m.end()+40].replace('\n',' ')
            print('BANNED?',f,b,'|',ctx)
# new copy only: farmhouse/stay/overnight/build/slot words
import difflib
NEWBAN=r'farm ?house|overnight|\bstay|cottage|resort|\bbuild|9 ?am|6 ?pm|time slot|pick ?up|collect you|RERA|title in your name|registered in your name|guarantee|best\b'
for f in htmls+[x for x in files if x.endswith('.txt')]:
    new=open(B+f,encoding='utf-8').read(); old=open(OLD+f,encoding='utf-8').read() if os.path.exists(OLD+f) else ''
    nt=text(new) if f.endswith('.html') else new; ot=text(old) if f.endswith('.html') else old
    ow=set(re.split(r'(?<=[.!?])\s+',re.sub(r'\s+',' ',ot)))
    for sent in re.split(r'(?<=[.!?])\s+',re.sub(r'\s+',' ',nt)):
        if sent in ow: continue
        for m in re.finditer(NEWBAN,sent,re.I): print('NEWCOPY?',f,'|',m.group(0),'|',sent[:160])
print('FAILS',bad)
