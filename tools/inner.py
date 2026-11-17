import sys; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from common import *
import os
B='/workspace/arogyavana-site/new/'
S2="Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft. Phase 1 is sold out. Phase 3 is now launching; the Phase 3 price will be shared once it's announced."
SHARED_OLD='<p>The Phase 3 plan is ₹25 lakh per 4,400 sq.ft plot: ₹15 lakh for the land plus ₹10 lakh as a managed investment, with returns as per agreement (terms apply). <a href="/#plan">See the plan</a>.</p>'
SHARED_NEW=f'<p>{S2} <a href="/#visit">Book a visit</a> to see the land, the plantation and the clubhouse.</p>'
NOTE_OLD='General information, not financial or legal advice. Returns and appreciation are not guaranteed; review all project documents before investing.'
NOTE_NEW='General information, not financial or legal advice. Review all project documents before you decide.'
def common_inner(s,tag):
    s=R(s,'<a href="/#plan">Investment Plan</a>','<a href="/#plan">Plots</a>',must=False,tag=tag+' nav "Investment Plan" -> "Plots"')
    s=R(s,'<a class="btn ln" href="https://wa.me/919886670006" target="_blank" rel="noopener">WhatsApp</a>',f'<a class="btn ln" href="{NEWTEL}">Call {NEWNUM}</a>',must=False,tag=tag+' CTA WhatsApp -> call')
    s=R(s,'<a class="btn" href="https://wa.me/919886670006?text=Hello%2C%20I%20am%20interested%20in%20Arogya%20Vana%20Phase%203" target="_blank" rel="noopener">WhatsApp us</a>',f'<a class="btn" href="{NEWTEL}">Call {NEWNUM}</a>',must=False,tag=tag+' CTA WhatsApp -> call')
    s=R(s,NOTE_OLD,NOTE_NEW,must=False,tag=tag+' legal note')
    s=R(s,'<span class="fmotto">Invest in nature. Invest for future. · Own land. We manage. You enjoy.</span>','<span class="fmotto">We manage. You enjoy.</span>',must=False,tag=tag+' footer motto')
    s=R(s,SHARED_OLD,SHARED_NEW,must=False,tag=tag+' shared ₹25L plan CTA -> Phase 2 rate card')
    if 'class="wa"' in s: s=wa_button(s,'Call us on '+NEWNUM)
    s=phones(s)
    return s
def set_head(s,title=None,desc=None,tag=''):
    if title:
        old=re.search(r'<title>(.*?)</title>',s).group(1)
        s=R(s,f'<title>{old}</title>',f'<title>{title}</title>',tag=tag+' <title>')
        s=R(s,f'content="{old}"',f'content="{title}"',must=False,tag=tag+' og/twitter title')
    if desc:
        old=re.search(r'<meta name="description" content="(.*?)"',s).group(1)
        s=R(s,f'content="{old}"',f'content="{desc}"',tag=tag+' meta/og description')
    return s
def unesc(x): return x.replace('&amp;','&')
def ld_page(name=None,desc=None,crumb=None,faq=None,headline=None):
    def f(o):
        for n in o['@graph']:
            t=n.get('@type')
            if t in('WebPage','Article'):
                if name and t=='WebPage': n['name']=unesc(name)
                if headline and t=='Article': n['headline']=headline
                if desc: n['description']=unesc(desc)
            if t=='FAQPage' and faq is not None:
                n['mainEntity']=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]
            if t=='BreadcrumbList' and crumb:
                n['itemListElement'][-1]['name']=crumb
        return o
    return f
def faq_html(faq):
    return '<div class="faq">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)+'</div>'
def set_faq(s,faq,tag):
    return RX(s,r'<div class="faq">.*?</div>(?=</div>)',faq_html(faq).replace('\\','\\\\'),tag=tag+' visible FAQ')
def get_faq(s):
    o=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',s,re.S).group(1))
    for n in o['@graph']:
        if n['@type']=='FAQPage': return [(q['name'],q['acceptedAnswer']['text']) for q in n['mainEntity']]
def edit(p,fn):
    path=B+p; s=open(path).read(); s=fn(s,p); s=common_inner(s,p); open(path,'w').write(s)

# ---------- page-specific ----------
def price(s,p):
    t='Managed Farmland Price near Bangalore | Arogya Vana Phase 2'
    d="Phase 2 plots at Arogya Vana are 4,400 sq.ft at ₹299 per sq ft. Phase 1 is sold out. Phase 3 is now launching; the Phase 3 price will be shared once it's announced."
    s=set_head(s,t,d,p)
    s=R(s,'<h1>What a Managed Farm Plot Costs</h1>','<h1>Managed Farmland Price near Bangalore</h1>',tag=p+' H1')
    s=R(s,'Here is exactly what an Arogya Vana Phase 3 plot costs and what you get for it.','Here is the current price at Arogya Vana and what is included.',tag=p)
    s=R(s,'<h2>The Phase 3 price</h2><table><tr><th>Item</th><th>Amount</th></tr><tr><td>Land (4,400 sq.ft)</td><td>₹15 lakh</td></tr><tr><td>Managed investment</td><td>₹10 lakh</td></tr><tr><td><b>Total plan</b></td><td><b>₹25 lakh</b></td></tr></table>',
          '<h2>Current price</h2><table><tr><th>Phase</th><th>Price</th></tr><tr><td>Phase 1</td><td>Sold out</td></tr><tr><td>Phase 2 (4,400 sq.ft plots)</td><td><b>₹299 per sq ft</b></td></tr><tr><td>Phase 3</td><td>Now launching; price to be shared once announced</td></tr></table>',tag=p+' price table')
    s=R(s,'<p>Returns on the investment part are as per agreement; terms apply. Registration and stamp duty are extra as per government rates.</p>','<p>Registration and stamp duty are extra as per government rates.</p>',tag=p)
    s=R(s,'<li>70% of sandalwood profit and 100% of fruit and vegetable income to the owner (subject to terms)</li>','',tag=p+' profit-share bullet')
    s=R(s,'<p><a href="/#plan">Try the plan calculator</a>.</p>','',tag=p+' calculator link')
    faq=get_faq(s); faq[0]=('What is the price of a plot?',S2)
    s=set_faq(s,faq,p); s=jsonld(s,ld_page(name=t,desc=d,faq=faq),p+' JSON-LD')
    return s
def returns(s,p):
    t='Sandalwood Farming Over Time | A Long-Cycle Crop – Arogya Vana'
    d='How sandalwood grows over time as a long-cycle crop, what is grown alongside it, and how the farm team at Arogya Vana looks after the plantation.'
    s=set_head(s,t,d,p)
    s=R(s,'<span aria-current="page">Sandalwood farming returns</span>','<span aria-current="page">Sandalwood farming over time</span>',tag=p+' breadcrumb')
    s=R(s,'<h1>How Sandalwood Farming Pays Over Time</h1>','<h1>How Sandalwood Grows Over Time</h1>',tag=p+' H1')
    s=R(s,'alt="Sandalwood farming returns at Arogya Vana"','alt="Sandalwood plantation at Arogya Vana"',tag=p)
    s=R(s,'Its value comes at harvest, many years after planting, which is why managed sandalwood farms usually pair it with crops that earn sooner.','It is harvested many years after planting, which is why managed sandalwood farms usually grow it alongside seasonal crops.',tag=p)
    s=R(s,'<h2>Two kinds of income</h2><ul><li><b>Long term:</b>','<h2>What is grown</h2><ul><li><b>Long cycle:</b>',tag=p)
    s=R(s,'<li><b>Regular:</b> seasonal fruits and vegetables grown between the trees</li>','<li><b>Seasonal:</b> fruits and vegetables grown between the trees</li>',tag=p)
    s=R(s,'<h2>How Arogya Vana shares it</h2><ul><li>70% of sandalwood profit goes to the plot owner</li><li>100% of fruit and vegetable income goes to the owner</li><li>All subject to the terms in your agreement</li></ul>\n','',tag=p+' profit-share section')
    s=R(s,'<h2>What affects returns</h2><ul><li>Survival and growth of the trees, which depends on care, water and protection</li><li>Market price of sandalwood at harvest</li><li>Land value growth in the area</li></ul>\n<p>We don\'t quote per-tree or per-acre profit figures, because they depend on all of the above. Returns are not guaranteed.</p>',
          '<h2>What helps the trees grow</h2><ul><li>Steady care through the early years</li><li>Water, with drip irrigation to keep moisture even</li><li>Protection: at Arogya Vana, 24/7 security, CCTV and solar fencing</li></ul>',tag=p+' "what affects returns" -> growing')
    s=R(s,'Read our full <a href="/sandalwood-farming/">sandalwood farming guide</a>: how it grows, soil and water, planting, protection and legal sale.','Read our full <a href="/sandalwood-farming/">sandalwood farming guide</a>: how it grows, soil and water, planting, protection and legal harvest.',tag=p)
    faq=[('When is sandalwood harvested?','It is a long-cycle crop; the timeline is set out in your agreement.'),('What is grown alongside the sandalwood?','Seasonal fruits and vegetables are grown between the trees, with casuarina as a host plant.')]
    s=set_faq(s,faq,p); s=jsonld(s,ld_page(name=t,desc=d,crumb='Sandalwood farming over time',faq=faq),p+' JSON-LD')
    return s
def gold(s,p):
    t='Farmland vs Gold: How They Compare | Arogya Vana'
    d='Farmland vs gold and fixed deposits in India: what you own, liquidity, use and risk compared, and where managed farmland fits.'
    s=set_head(s,t,d,p)
    s=R(s,'<h1>Farmland vs Gold: Which Builds Wealth?</h1>','<h1>Farmland vs Gold: How They Compare</h1>',tag=p+' H1')
    s=R(s,'<td>Registered land</td>','<td>Land</td>',tag=p+' table: what you own')
    s=R(s,'<tr><td>Regular income</td><td>None</td><td>Interest</td><td>Crop income, subject to terms</td></tr>','',tag=p+' table: income row removed')
    s=R(s,"<p>Farmland suits money you won't need for many years. It is a real asset you can visit, and managed farmland removes the work of running it. It shouldn't replace your emergency savings.</p>",
          "<p>Farmland is a long-term purchase: it takes time to sell, so it suits buyers who plan to hold it for many years. It is real land you can visit and use, and managed farmland removes the work of running it. It shouldn't replace your emergency savings.</p>",tag=p)
    faq=[('Is farmland better than gold?','Neither is better for everyone. Gold is easy to sell; farmland is land you can visit and use, and it takes longer to sell.'),('Is farmland easy to sell?','Not as quickly as gold or an FD. Plan to hold it long term.')]
    s=set_faq(s,faq,p); s=jsonld(s,ld_page(name=t,desc=d,faq=faq),p+' JSON-LD')
    return s
def sandal_blr(s,p):
    d="Managed white sandalwood farmland near Bagepalli, 2 hours from Bengaluru. Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft. Phase 3 now launching."
    s=set_head(s,None,d,p)
    s=R(s,'so the land gives regular produce income while the sandalwood matures.','so the land is productive while the sandalwood matures.',tag=p)
    s=R(s,'<li>Seasonal fruits and vegetables for regular income</li>','<li>Seasonal fruits and vegetables</li>',tag=p)
    s=R(s,'<h2>How sandalwood returns are shared</h2><ul><li>70% of sandalwood profit goes to the owner, plus 100% of fruit and vegetable income (subject to terms)</li><li>Plantation, pruning, irrigation, protection and harvest planning are handled by agronomists</li></ul>',
          '<h2>Who looks after the plantation</h2><ul><li>Plantation, pruning, irrigation, protection and harvest planning are handled by agronomists</li></ul>',tag=p+' profit-share section')
    s=R(s,'<h2>Why sandalwood farmland suits long-term wealth</h2><p>You hold land in a growing corridor near the proposed SEZ and Greenfield Highway, plus a long-cycle crop on it. Values are not guaranteed.</p>',
          '<h2>Why sandalwood farmland</h2><p>You hold land in a growing corridor near the proposed SEZ and Greenfield Highway, with a long-cycle sandalwood plantation on it.</p>',tag=p)
    s=R(s,'<h2>The Phase 3 plan</h2><p>₹15 lakh land + ₹10 lakh investment = ₹25 lakh per 4,400 sq.ft plot; returns as per agreement, terms apply. <a href="/#plan">See the full plan</a>.</p>',
          f'<h2>Plots and price</h2>{SHARED_NEW}',tag=p+' plan block -> Phase 2 rate card')
    faq=[x for x in get_faq(s) if x[0]!='Who gets the sandalwood income?']
    s=set_faq(s,faq,p); s=jsonld(s,ld_page(desc=d,faq=faq),p+' JSON-LD')
    return s
def mf_blr(s,p):
    t='Managed Farmland near Bangalore | Arogya Vana Phase 3'
    s=set_head(s,t,None,p)
    s=R(s,'<li><b>Clear entry plan:</b> a 4,400 sq.ft plot on the ₹25 lakh plan (₹15 lakh land + ₹10 lakh managed investment; returns as per agreement, terms apply). <a href="/#plan">See the plan</a>.</li><li>70% of sandalwood profit and 100% of seasonal fruit and vegetable income go to the owner (subject to terms).</li>',
          f'<li><b>Clear pricing:</b> Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft. Phase 3 is now launching; the Phase 3 price will be shared once it\'s announced.</li>',tag=p+' plan + profit-share bullets')
    faq=get_faq(s); faq=[(q,("Phase 2 plots are 4,400 sq.ft." if q=='What is the smallest plot?' else a)) for q,a in faq]
    s=set_faq(s,[(q,a.replace("'","&#x27;")) for q,a in faq],p); s=jsonld(s,ld_page(name=t,faq=faq),p+' JSON-LD')
    return s
def nri(s,p):
    t='Farmland for NRIs near Bengaluru | Rules &amp; Options – Arogya Vana'
    s=set_head(s,t,None,p); s=jsonld(s,ld_page(name=t),p+' JSON-LD'); return s
def sguide(s,p):
    d='A practical guide to sandalwood farming in India: how sandalwood grows with host plants, soil and water, planting and care, protection and legal sale.'
    s=set_head(s,None,d,p)
    i=s.index('<h2>How sandalwood farming returns work</h2>'); j=s.index('<h2>Or let us farm it for you</h2>')
    LOG.append((p+' returns section removed',s[i:i+80],'',1))
    s=s[:i]+'<p>At Arogya Vana the farm team plants and looks after the sandalwood. <a href="/#visit">Book a visit</a> to see the plantation.</p>\n'+s[j:]
    faq=[x for x in get_faq(s) if x[0]!='Are sandalwood returns guaranteed?']
    s=set_faq(s,faq,p); s=jsonld(s,ld_page(desc=d,faq=faq),p+' JSON-LD')
    return s
def compare(s,p):
    s=R(s,'<tr><td><b>Arogya Vana Phase 3</b></td><td>Near Bagepalli</td><td>₹25 lakh per 4,400 sq.ft (₹15L land + ₹10L investment)</td></tr>','<tr><td><b>Arogya Vana Phase 2</b></td><td>Near Bagepalli</td><td>₹299 per sq ft on 4,400 sq.ft plots (Phase 1 sold out; Phase 3 price to be announced)</td></tr>',tag=p+' price row')
    s=R(s,'<li>A managed investment component alongside the land, with returns as per agreement (terms apply)</li><li>70% sandalwood profit share and 100% fruit and vegetable income to owners (subject to terms)</li>','<li>A managed white sandalwood plantation, with fruits and vegetables grown alongside</li>',tag=p+' investment/profit bullets')
    s=R(s,'<li>How are crop proceeds shared, in writing?</li>','',tag=p+' crop-proceeds bullet')
    return s
def faqpage(s,p):
    d='Answers to common questions about Arogya Vana managed farmland: price, location, ownership, maintenance, what is planted and site visits.'
    s=set_head(s,None,d,p)
    s=R(s,'<p>Cannot find your question? Call <a href="tel:+919886670006">+91 98866 70006</a> or <a href="https://wa.me/919886670006" target="_blank" rel="noopener">WhatsApp us</a>.</p>',f'<p>Cannot find your question? Call <a href="{NEWTEL}">{NEWNUM}</a> or <a href="/#visit">book a site visit</a>.</p>',tag=p)
    faq=get_faq(s); out=[]
    for q,a in faq:
        if q=='Who gets the crop income?': continue
        if q=='What does a plot cost?': a=S2
        out.append((q,a))
    s=set_faq(s,out,p); s=jsonld(s,ld_page(desc=d,faq=out),p+' JSON-LD')
    return s
def light(s,p): return s
pages={'managed-farmland-price-bangalore/index.html':price,'sandalwood-farming-returns/index.html':returns,'farmland-vs-gold-investment/index.html':gold,
 'sandalwood-farmland-near-bangalore/index.html':sandal_blr,'managed-farmland-near-bangalore/index.html':mf_blr,'nri-farmland-investment-karnataka/index.html':nri,
 'sandalwood-farming/index.html':sguide,'arogya-vana-vs-other-managed-farmland/index.html':compare,'faq/index.html':faqpage,
 'weekend-farmhouse-near-bangalore/index.html':light,'farmland-near-bagepalli/index.html':light}
# 15 Nov 2026 (approved by Karthick, "fix all make it live"): land-first slugs. The old paths 301 in w.js.
SLUG_MOVES={'sandalwood-farming-returns':'sandalwood-growth-cycle','farmland-vs-gold-investment':'farmland-vs-gold','nri-farmland-investment-karnataka':'farmland-for-nris-karnataka'}
def move_slugs():
    import shutil
    for o,n in SLUG_MOVES.items():
        if os.path.isdir(B+o):
            if os.path.isdir(B+n): shutil.rmtree(B+n)
            os.rename(B+o,B+n); LOG.append((f'folder {o}/ -> {n}/','','',1))
    for d,_,fs in os.walk(B):
        for f in fs:
            if not f.endswith(('.html','.xml','.txt')): continue
            path=os.path.join(d,f); s=open(path,encoding='utf-8').read(); t=s
            for o,n in SLUG_MOVES.items(): t=t.replace(f'/{o}/',f'/{n}/')
            if t!=s: open(path,'w',encoding='utf-8').write(t); LOG.append((os.path.relpath(path,B)+' old slug URLs -> new','','',1))
if __name__=='__main__':
    for p,fn in pages.items(): edit(p,fn)
    move_slugs()
    for t in LOG: print(t[0],'|',t[3])
