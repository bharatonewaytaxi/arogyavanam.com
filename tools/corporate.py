# Bengaluru working-professionals refresh, 16 Nov 2026 (Karthick: "implement all", 5:33 AM IST).
# Runs after pages.py. Homepage (en) hero/title/meta + "Buying in 5 steps"; "Book a Saturday site visit" CTA on every English page.
# No form/script changes. kn/te untouched. No "farmhouse"/overnight wording, no visit time slots.
import os,re
B='/workspace/arogyavana-site/new/'
def R(s,a,b,n=1):
    assert s.count(a)==n,(a,s.count(a)); return s.replace(a,b)
CSS=('<style>.satbar{margin:0 0 1.2em;padding:12px 16px;border:1px solid #e4e2dc;border-radius:10px;background:#f6f5f0;font-size:.95rem}'
     '.satbar a{font-weight:700;text-decoration:underline;text-underline-offset:4px}'
     '.steps5{counter-reset:s;list-style:none;margin:0 0 1.4em;padding:0;display:grid;gap:10px}'
     '.steps5 li{counter-increment:s;position:relative;padding:12px 14px 12px 52px;background:#fff;border:1px solid #e4e2dc;border-radius:10px}'
     '.steps5 li:before{content:counter(s);position:absolute;left:14px;top:50%;transform:translateY(-50%);width:28px;height:28px;border-radius:50%;background:#14321f;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem}'
     '.prose ol.steps5,ol.steps5{padding:0;margin-left:0}.hsteps{max-width:760px;margin:0 auto}.hsteps .c{text-align:center;margin-top:20px}</style>')
SATBAR='<p class="satbar"><a href="/#visit">Book a Saturday site visit</a> · see the land for yourself, about 2 hours from Bengaluru.</p>'
LOG=[]
# ---------- homepage (English) ----------
f=B+'index.html'; s=open(f,encoding='utf-8').read()
T='Weekend Farmland near Bangalore for Working Professionals | Arogya Vana'
D='Your own farmland about 2 hours from Bengaluru, near Bagepalli. A weekend escape for working professionals, with a clear buying process. Phase 2 plots: 4,400 sq ft at ₹299 per sq ft.'
s=re.sub(r'<title>.*?</title>',f'<title>{T}</title>',s,count=1)
s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{D}">',s,count=1)
s=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{T}">',s,count=1)
s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{D}">',s,count=1)
s=re.sub(r'<meta name="twitter:title" content="[^"]*">',f'<meta name="twitter:title" content="{T}">',s,count=1)
s=R(s,'<h1>Arogya Vana</h1><p class="l">Live naturally. Grow together.</p><p class="by">An Arogya Vana project by Saptha Ventures · Premium managed farmland near the Karnataka – Andhra strategic border</p>',
      '<h1>Your own farmland, about 2 hours from Bengaluru</h1><p class="l">Live naturally. Grow together.</p><p class="by">Arogya Vana by Saptha Ventures · A weekend escape from the work week, with a clear, step-by-step buying process</p>')
s=R(s,'<a class="btn gh" href="#visit">Book Site Visit</a>','<a class="btn gh" href="#visit">Book a Saturday Site Visit</a>')
s=R(s,'<li><a href="#visit">Site Visit</a></li>','<li><a href="#visit">Book a Saturday Site Visit</a></li>')
HSTEPS=('<section class="sec off" id="buying-steps"><div class="wrap hsteps"><div class="hd c"><span class="kick">How buying works</span><h2>Buying in 5 steps</h2>'
 '<p>A clear process, explained by our team at every step.</p></div><ol class="steps5">'
 '<li><b>Enquire.</b> Call <a href="tel:+917090905031">+91 70909 05031</a> or send an enquiry.</li>'
 '<li><b>Take a Saturday site visit.</b> See the land, about 2 hours from Bengaluru.</li>'
 '<li><b>Review the documents with your own lawyer.</b></li>'
 '<li><b>Book your plot.</b></li>'
 '<li><b>Registration and handover.</b></li></ol>'
 '<p class="c"><a class="btn" href="#visit">Book a Saturday site visit</a> <a class="btn ln" href="/how-to-buy/">How to buy</a></p></div></section>\n')
s=R(s,'<section class="sec" id="visit">',HSTEPS+'<section class="sec" id="visit">')
s=R(s,'</head>',CSS+'</head>')
open(f,'w',encoding='utf-8').write(s); LOG.append('index.html: title/meta/og, hero h1+by-line, hero+menu Saturday CTA, Buying in 5 steps before #visit')
# ---------- every English page with a breadcrumb ----------
for d_,_,fs in os.walk(B):
    for fn in fs:
        if not fn.endswith('.html'): continue
        p=os.path.join(d_,fn); rel=os.path.relpath(p,B)
        if rel.startswith(('kn/','te/')) or rel in ('index.html',): continue
        s=open(p,encoding='utf-8').read()
        if '<nav class="crumb"' not in s: continue
        s=re.sub(r'(<nav class="crumb".*?</nav>)',lambda m:m.group(1)+'\n'+SATBAR,s,count=1,flags=re.S)
        if '<section class="cta"' in s:
            s=s.replace('>Book a Site Visit</a>','>Book a Saturday Site Visit</a>')
        else:
            s=R(s,'</main>','<section class="cta" aria-labelledby="cta-h"><h2 id="cta-h">See the land in person</h2><p>About 2 hours from Bengaluru. Book a Saturday site visit, or call us.</p><div class="row"><a class="btn" href="/#visit">Book a Saturday Site Visit</a><a class="btn ln" href="tel:+917090905031">Call +91 70909 05031</a></div></section>\n</main>')
        s=s.replace('<li><a href="/#visit">Site Visit</a></li>','<li><a href="/#visit">Book a Saturday Site Visit</a></li>')
        s=R(s,'</head>',CSS+'</head>')
        open(p,'w',encoding='utf-8').write(s); LOG.append(rel+': Saturday CTA top + end')
if __name__=='__main__':
    for x in LOG: print(x)
