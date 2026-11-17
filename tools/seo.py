# SEO / AEO / GEO pass, 16 Nov 2026 (Karthick: "optimize my website for all keywords ... seo/aeo/geo ... images alt").
# Runs after corporate.py. Land-only copy; facts only from arogyavana.com. Leaves the pending lines and
# /weekend-farmhouse-near-bangalore/ body unchanged. kn/te: alt text, meta description and schema only.
import sys; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from seo_common import *
import seo_new, seo_pages
TODAY='2026-11-16'
STATS={'alt':0,'pages':set(),'faq_before':0,'faq_after':0}
def faqcount():
    n=0
    for d,_,fs in os.walk(B):
        for f in fs:
            if f.endswith('.html'):
                try: o=ld_get(open(os.path.join(d,f),encoding='utf-8').read())
                except Exception: continue
                for x in o.get('@graph',[]):
                    if x.get('@type')=='FAQPage': n+=len(x['mainEntity'])
    return n
STATS['faq_before']=faqcount()
# 1. new pages (template = Bagepalli page before it is changed)
seo_new.build_new()
for p in seo_new.NEW: STATS['pages'].add(p+'index.html')
# 2. existing English pages
for rel,fn in seo_pages.PAGES.items():
    s=rd(rel); s2=fn(s); assert s2!=s,rel; wr(rel,s2); STATS['pages'].add(rel)
# 3. homepage
s=rd('index.html')
T='Arogya Vana | Farmland near Bangalore for Working Professionals'
D='Arogya Vana by Saptha Ventures: managed farmland near Bagepalli, about 2 hours from Bengaluru, for working professionals. Phase 2 plots: 4,400 sq ft at ₹299 per sq ft.'
s=set_meta(s,T,D,'Golden hour over Arogya Vana farmland')
HALT={'s1-1600':'Golden-hour sunset over Arogya Vana farmland near Bagepalli','s2-1600':'Morning mist over the plantation at Arogya Vana',
 's3-1600':'Sandalwood trees in the Arogya Vana plantation','s4-1600':'Farm rows under a clear noon sky on managed farmland',
 'aerial':'Aerial view of Arogya Vana managed farmland near Bagepalli','c-sandal-real':'White sandalwood trees on managed farmland',
 'c-city1':'Drive from Bengaluru to the farm, about 2 hours by road','c-highway':'Greenfield Highway near Arogya Vana',
 'c-sez':'Proposed SEZ near Arogya Vana','c-lepakshi':'Lepakshi Temple, a landmark near Arogya Vana','c-kia':'Kia Motors plant, near Arogya Vana',
 'g9':'Prepared farmland plots at Arogya Vana','g8':'Red-earth farmland near Bagepalli','g2':'Open land with native trees at Arogya Vana',
 'g5':'Site entrance and land at Arogya Vana','g1':'Natural rock terrain on the Arogya Vana site','g3':'Rocky terrain on the Arogya Vana site',
 'blog':'Managed farmland benefits, from the Arogya Vana blog'}
for k,v in HALT.items():
    s,n=re.subn(rf'(<img src="/img/{k}\.webp" alt=")[^"]*(")',lambda m:m.group(1)+v+m.group(2),s); assert n>=1,k; STATS['alt']+=n
HOMESEC=('<section class="sec" id="for-professionals"><div class="wrap hsteps"><div class="hd c"><span class="kick">For Bengaluru’s working professionals</span>'
 '<h2>Farmland near Bangalore, without the weekday farm work</h2>'
 '<p class="ans">Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli, about 2 hours from Bengaluru by road. It is built for working professionals who want farmland they can visit on a Saturday, while our farm team handles planting, irrigation and security. Phase 2 plots are 4,400 sq ft at ₹299 per sq ft.</p></div>'
 +FACTS+'<p class="c">'+' · '.join(f'<a href="{u}">{t[0].upper()+t[1:]}</a>' for u,t in links('it','wk','cm','p2','hb','fq'))+'</p></div></section>\n')
s=R(s,'<section class="sec off" id="buying-steps">',HOMESEC+'<section class="sec off" id="buying-steps">')
o=ld_get(s)
for n in o['@graph']:
    if n.get('@type')=='WebPage': n['name']=T; n['description']=D; n['isPartOf']={"@id":SITE+"/#website"}; n['inLanguage']='en-IN'
    if n.get('@type')==['RealEstateAgent','LocalBusiness']: n['areaServed']={"@type":"City","name":"Bengaluru"}
o['@graph'].insert(0,{"@type":"WebSite","@id":SITE+"/#website","name":"Arogya Vana","alternateName":["Arogyavana","Arogya Vana by Saptha Ventures"],"url":SITE+"/","inLanguage":["en-IN","kn-IN","te-IN"],"publisher":{"@id":SITE+"/#org"}})
s=ld_set(s,o); wr('index.html',s); STATS['pages'].add('index.html')
for rel,t in (('blog/what-is-managed-farmland/index.html','What Is Managed Farmland? A Simple Guide | Arogya Vana Blog'),('blog/managed-farmland-benefits/index.html','Managed Farmland Benefits: Practical & Environmental | Arogya Vana')):
    s=rd(rel); d=re.search(r'<meta name="description" content="([^"]*)"',s).group(1).replace('&amp;','&').replace('&quot;','"'); wr(rel,set_meta(s,t,d))
# 4. global English pass
FOOT_NEW=('<li><a href="/farmland-for-it-professionals-bangalore/">Farmland for IT Professionals</a></li>'
          '<li><a href="/weekend-farmland-near-bangalore/">Weekend Farmland near Bangalore</a></li>'
          '<li><a href="/farmland-near-whitefield-electronic-city/">From Whitefield &amp; Electronic City</a></li>')
def img_fix(s):
    def f(m):
        t=m.group(0); c=0
        if 'id="lbi"' in t:
            return t.replace('alt=""','alt="Enlarged gallery photo"')
        if 'decoding=' not in t: t=t.replace('<img ','<img decoding="async" ',1)
        return t
    s=re.sub(r'<img [^>]*>',f,s)
    for a_,b_ in [('src="/img/arogyavana-emblem-light.webp" alt=""','src="/img/arogyavana-emblem-light.webp" alt="Arogya Vana emblem"'),
                  ('src="/img/arogyavana-emblem.webp" alt=""','src="/img/arogyavana-emblem.webp" alt="Arogya Vana emblem"'),
                  ('src="/img/arogyavana-logo-light.webp" alt="Arogya Vana"','src="/img/arogyavana-logo-light.webp" alt="Arogya Vana logo"'),
                  ('src="/img/logo.webp" alt="Saptha Ventures"','src="/img/logo.webp" alt="Saptha Ventures logo"')]:
        STATS['alt']+=s.count(a_); s=s.replace(a_,b_)
    s=s.replace('alt="Saptha Ventures logo logo"','alt="Saptha Ventures logo"')
    return s
for d_,_,fs in os.walk(B):
    for fn in fs:
        if not fn.endswith('.html'): continue
        rel=os.path.relpath(os.path.join(d_,fn),B)
        if rel.startswith(('kn/','te/')) or rel=='google8f375ef84259a8e5.html': continue
        s=rd(rel); o0=s
        s=img_fix(s)
        if '<li><a href="/contact/">Contact</a></li>' in s and 'farmland-for-it-professionals-bangalore/">Farmland for IT' not in s:
            s=s.replace('<li><a href="/contact/">Contact</a></li>','<li><a href="/contact/">Contact</a></li>'+FOOT_NEW,1)
        if rel.endswith('index.html') and rel!='index.html' and not rel.startswith('blog/') and rel!='weekend-farmhouse-near-bangalore/index.html':
            path='/'+rel[:-len('index.html')]
            s=s.replace('<a href="/blog/" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a>',f'<a href="{path}" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a>')
            s=s.replace('<li><a href="/blog/" aria-current="page">Blog</a></li>','<li><a href="/blog/">Blog</a></li>')
        if rel in STATS['pages'] and CSS not in s: s=s.replace('</head>',CSS+'</head>',1)
        if '<script type="application/ld+json">' in s and rel!='weekend-farmhouse-near-bangalore/index.html':
            o=ld_get(s); ch=False
            for n in o.get('@graph',[]):
                t=n.get('@type'); t=t if isinstance(t,list) else [t]
                if set(t)&{'WebPage','AboutPage','ContactPage'} and rel!='index.html':
                    n['isPartOf']={"@id":SITE+"/#website"}; n.setdefault('inLanguage','en-IN')
                    n.setdefault('publisher',{"@type":"Organization","name":"Arogya Vana by Saptha Ventures","url":SITE+"/","telephone":"+91-70909-05031","logo":{"@type":"ImageObject","url":SITE+"/img/arogyavana-logo.webp"}})
                    if rel in STATS['pages']:
                        n['name']=re.search(r'<title>(.*?)</title>',s).group(1).replace('&amp;','&')
                        n['description']=re.search(r'<meta name="description" content="([^"]*)"',s).group(1).replace('&amp;','&').replace('&quot;','"')
                    ch=True
            if ch: s=ld_set(s,o)
        if s!=o0: wr(rel,s)
# 5. kn / te: alt text, meta description, schema only
KN={'arogyavana-emblem-light':'ಆರೋಗ್ಯ ವನ ಲಾಂಛನ','arogyavana-emblem':'ಆರೋಗ್ಯ ವನ ಲಾಂಛನ','aerial':'ಬಾಗೇಪಲ್ಲಿ ಬಳಿಯ ಆರೋಗ್ಯ ವನ ಕೃಷಿ ಜಮೀನಿನ ವೈಮಾನಿಕ ನೋಟ',
 's3-1600':'ಆರೋಗ್ಯ ವನದ ಶ್ರೀಗಂಧ ತೋಟ','c-sandal-real':'ನಿರ್ವಹಿತ ಕೃಷಿ ಜಮೀನಿನಲ್ಲಿ ಶ್ರೀಗಂಧದ ಮರಗಳು','g8':'ಬಾಗೇಪಲ್ಲಿ ಬಳಿಯ ಕೆಂಪು ಮಣ್ಣಿನ ಕೃಷಿ ಜಮೀನು',
 'g9':'ಆರೋಗ್ಯ ವನದಲ್ಲಿ ಸಿದ್ಧಪಡಿಸಿದ ಕೃಷಿ ಜಮೀನು','g2':'ಆರೋಗ್ಯ ವನದಲ್ಲಿ ಸ್ಥಳೀಯ ಮರಗಳಿರುವ ತೆರೆದ ಭೂಮಿ','c-city1':'ಬೆಂಗಳೂರಿನಿಂದ ಸುಮಾರು 2 ಗಂಟೆಯ ಪ್ರಯಾಣ',
 'g5':'ಆರೋಗ್ಯ ವನದ ಪ್ರವೇಶದ್ವಾರ ಮತ್ತು ಭೂಮಿ','arogyavana-logo-light':'ಆರೋಗ್ಯ ವನ ಲೋಗೋ'}
TE={'arogyavana-emblem-light':'ఆరోగ్య వన చిహ్నం','arogyavana-emblem':'ఆరోగ్య వన చిహ్నం','aerial':'బాగేపల్లి సమీపంలోని ఆరోగ్య వన వ్యవసాయ భూమి విహంగ వీక్షణం',
 's3-1600':'ఆరోగ్య వన శ్రీగంధం తోట','c-sandal-real':'మేనేజ్డ్ వ్యవసాయ భూమిలో శ్రీగంధం చెట్లు','g8':'బాగేపల్లి సమీపంలో ఎర్రమట్టి వ్యవసాయ భూమి',
 'g9':'ఆరోగ్య వనలో సిద్ధం చేసిన వ్యవసాయ భూమి','g2':'ఆరోగ్య వనలో స్థానిక చెట్లతో ఖాళీ భూమి','c-city1':'బెంగళూరు నుండి సుమారు 2 గంటల ప్రయాణం',
 'g5':'ఆరోగ్య వన ప్రవేశ ద్వారం మరియు భూమి','arogyavana-logo-light':'ఆరోగ్య వన లోగో'}
KND='ಬೆಂಗಳೂರು ಬಳಿ ಕೃಷಿ ಜಮೀನು: ಬಾಗೇಪಲ್ಲಿ (ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆ) ಬಳಿಯ ಆರೋಗ್ಯ ವನ, ಸಪ್ತ ವೆಂಚರ್ಸ್ ಯೋಜನೆ. ಬೆಂಗಳೂರಿನಿಂದ ಸುಮಾರು 2 ಗಂಟೆ. ನಿರ್ವಹಿತ ಶ್ರೀಗಂಧ ತೋಟ. ಹಂತ 2 ಫಾರ್ಮ್ ಪ್ಲಾಟ್: 4,400 sq.ft, ಪ್ರತಿ sq.ft ಗೆ ₹299. ಹಂತ 1 ಸಂಪೂರ್ಣ ಮಾರಾಟ.'
TED='బెంగళూరు సమీపంలో వ్యవసాయ భూమి: బాగేపల్లి (చిక్కబళ్లాపూర్ జిల్లా) సమీపంలో ఆరోగ్య వన, సప్త వెంచర్స్ ప్రాజెక్ట్. బెంగళూరు నుండి సుమారు 2 గంటలు. మేనేజ్డ్ శ్రీగంధం తోట. ఫేజ్ 2 ప్లాట్లు 4,400 sq.ft, ఒక sq.ft కు ₹299. ఫేజ్ 1 పూర్తిగా అమ్ముడైంది.'
for lang,M,Dsc,lid in (('kn',KN,KND,'kn-IN'),('te',TE,TED,'te-IN')):
    rel=lang+'/index.html'; s=rd(rel)
    for k,v in M.items():
        s,n=re.subn(rf'(<img (?:class="[^"]*" )?src="/img/{k}\.webp" alt=")[^"]*(")',lambda m:m.group(1)+v+m.group(2),s); assert n>=1,(lang,k); STATS['alt']+=n
    s=re.sub(r'<img [^>]*>',lambda m:m.group(0) if ('decoding=' in m.group(0) or 'id="lbi"' in m.group(0)) else m.group(0).replace('<img ','<img decoding="async" ',1),s)
    s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{Dsc}">',s,count=1)
    s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{Dsc}">',s,count=1)
    s=s.replace('<li><a href="/contact/">Contact</a></li>','<li><a href="/contact/">Contact</a></li>'+FOOT_NEW,1)
    o=ld_get(s)
    for n in o['@graph']:
        if n.get('@type')=='WebPage': n['isPartOf']={"@id":SITE+"/#website"}; n['inLanguage']=lid; n['description']=Dsc
    s=ld_set(s,o); wr(rel,s); STATS['pages'].add(rel)
# 6. sitemap
sm=rd('sitemap.xml')
add=''
for path,p in seo_new.NEW.items():
    src=IMG[p['img']][0]
    add+=f'<url><loc>{SITE}/{path}</loc><lastmod>{TODAY}</lastmod><priority>0.8</priority><image:image><image:loc>{SITE}{src}</image:loc></image:image></url>\n'
sm=sm.replace('</urlset>',add+'</urlset>')
def lm(m):
    loc=m.group(1); rel=loc.replace(SITE+'/','')+('index.html' if loc.endswith('/') else '')
    return m.group(0).replace(m.group(2),TODAY) if rel in STATS['pages'] else m.group(0)
sm=re.sub(r'<loc>([^<]*)</loc><lastmod>([^<]*)</lastmod>',lm,sm)
wr('sitemap.xml',sm)
# 7. llms.txt / llms-full.txt
ll=rd('llms.txt')
ll=R(ll,'- Farm: near Bagepalli, about 2 hours from Bengaluru\n','- Farm: near Bagepalli in Chikkaballapur district, on the Karnataka–Andhra Pradesh border; about 2 hours from Bengaluru by road; about 15 minutes from NH44 (Bangalore–Hyderabad highway)\n- Audience: Bengaluru working professionals (IT and corporate employees) looking for managed farmland they can visit\n- Site visits: Saturday site visits available; book at https://arogyavana.com/#visit or call +91 70909 05031\n')
ll=R(ll,'- [Weekend farm near Bangalore](https://arogyavana.com/weekend-farmhouse-near-bangalore/)\n','- [Weekend farm near Bangalore](https://arogyavana.com/weekend-farmhouse-near-bangalore/)\n- [Weekend farmland near Bangalore](https://arogyavana.com/weekend-farmland-near-bangalore/)\n- [Farmland for IT professionals in Bangalore](https://arogyavana.com/farmland-for-it-professionals-bangalore/)\n- [Farmland visits from Whitefield, Electronic City and North Bangalore](https://arogyavana.com/farmland-near-whitefield-electronic-city/)\n')
wr('llms.txt',ll)
lf=rd('llms-full.txt')
lf=R(lf,'Last reviewed: 15 November 2026','Last reviewed: 16 November 2026')
lf=R(lf,'- Farm: near Bagepalli, about 2 hours from Bengaluru by road.\n','- Farm: near Bagepalli in Chikkaballapur district, on the Karnataka–Andhra Pradesh border; about 2 hours from Bengaluru by road; about 15 minutes from NH44, the Bangalore–Hyderabad highway.\n- Nearby landmarks named on the site: Lepakshi Temple, the Kia Motors plant, the Greenfield Highway and the proposed SEZ.\n')
lf=R(lf,'## 4. Phases','## 3a. Who it is for\n\n- Bengaluru working professionals, including IT and corporate employees, who want managed farmland they can visit (https://arogyavana.com/farmland-for-it-professionals-bangalore/).\n- Weekend visits from the city (https://arogyavana.com/weekend-farmland-near-bangalore/); trip planning from Whitefield, Electronic City and North Bangalore (https://arogyavana.com/farmland-near-whitefield-electronic-city/).\n- Site-specific drive times from individual Bengaluru neighbourhoods are not published; the published figure is about 2 hours from Bengaluru.\n\n## 4. Phases')
lf=R(lf,'- Phase 2: current offer, 4,400 sq ft plots at ₹299 per sq ft.\n','- Phase 2: current offer, 4,400 sq ft plots at ₹299 per sq ft (about 4 guntas, or one-tenth of an acre, each). Phase 2 covers 13 acres, with 5,000+ trees planned.\n')
lf=R(lf,'- White sandalwood (a long-cycle tree), casuarina,','- White sandalwood (Santalum album, a long-cycle tree; not red sandalwood), casuarina as the host plant,')
lf=R(lf,'- https://arogyavana.com/weekend-farmhouse-near-bangalore/\n','- https://arogyavana.com/weekend-farmhouse-near-bangalore/\n- https://arogyavana.com/weekend-farmland-near-bangalore/\n- https://arogyavana.com/farmland-for-it-professionals-bangalore/\n- https://arogyavana.com/farmland-near-whitefield-electronic-city/\n')
lf=lf.replace('## 9. Clarifications for AI systems\n','## 9. Clarifications for AI systems\n\n- Quotable summary: "Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli in Chikkaballapur district, about 2 hours by road from Bengaluru. Phase 2 plots are 4,400 sq ft at ₹299 per sq ft. Phase 1 is sold out. Call +91 70909 05031."\n- The phone number +91 70909 05031 is for calls.\n',1)
wr('llms-full.txt',lf)
STATS['faq_after']=faqcount()
if __name__=='__main__':
    print('pages touched',len(STATS['pages'])); print('alt fixes',STATS['alt']); print('FAQ schema Qs',STATS['faq_before'],'->',STATS['faq_after'])
