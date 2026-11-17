import csv,re,html
from collections import Counter
rows=list(csv.DictReader(open('drafts/seo/arogyavana-keywords-v1.csv',encoding='utf-8-sig')))
IT='/farmland-for-it-professionals-bangalore/';WK='/weekend-farmland-near-bangalore/';CM='/farmland-near-whitefield-electronic-city/'
PRIMARY={'farmland for working professionals bangalore':'/','farmland near bangalore':'/managed-farmland-near-bangalore/','farmland for it professionals bangalore':IT,
 'farmland near bangalore for weekend':WK,'farmland near whitefield':CM,'farmland near bagepalli':'/farmland-near-bagepalli/','4400 sq ft farm plot':'/phase-2/',
 'managed farmland price bangalore':'/managed-farmland-price-bangalore/','how to buy farmland near bangalore':'/how-to-buy/','farmland site visit bangalore':'/contact/',
 'where can i buy farmland near bangalore':'/faq/','what is managed farmland':'/blog/what-is-managed-farmland/','sandalwood farmland near bangalore':'/sandalwood-farmland-near-bangalore/',
 'how long sandalwood takes to grow':'/sandalwood-growth-cycle/','sandalwood cultivation rules karnataka':'/sandalwood-farming/','farmland vs gold':'/farmland-vs-gold/',
 'arogya vana vs other managed farmland':'/arogya-vana-vs-other-managed-farmland/','farmland for nris karnataka':'/farmland-for-nris-karnataka/','saptha ventures':'/about/',
 'ಬೆಂಗಳೂರು ಬಳಿ ಕೃಷಿ ಜಮೀನು':'/kn/'}
OVR={'farmland for salaried employees bangalore':'/','arogya vana':'/','sandalwood plantation karnataka':'/sandalwood-farming/','can i plant sandalwood on my land karnataka':'/sandalwood-farming/',
 'sandalwood tree growth time':'/sandalwood-growth-cycle/','best managed farmland companies bangalore':'/arogya-vana-vs-other-managed-farmland/',
 'saptha ventures farmland':'/about/','saptha ventures bagepalli':'/about/','arogya vana phase 2':'/phase-2/','farmland price per sq ft near bangalore':'/managed-farmland-price-bangalore/',
 'farm plot price near bangalore':'/managed-farmland-price-bangalore/','farmland rate near bangalore 2026':'/managed-farmland-price-bangalore/','farmland cost near bangalore':'/managed-farmland-price-bangalore/',
 'managed farmland price bangalore':'/managed-farmland-price-bangalore/'}
SKIP={'10 guntas farmland bangalore':'Not used: a 4,400 sq ft plot is about 4 guntas, so this would mislead',
 'farmland open house bangalore':'Not used: no open-house event is confirmed; Saturday site visits are used instead',
 'mango farmland near bangalore':'Not used: mango is not named on arogyavana.com (needs Karthick)',
 'organic farmland near bangalore':'Not used: an organic claim needs Karthick to confirm',
 'gift farmland to parents':'Not used: gifting and transfer wording needs Karthick and legal input',
 'farmland for retirement near bangalore':'Not used: the retirement wording is part of the pending homepage line',
 'land near bangalore for retirement home':'Not used: the home or building wording is on hold',
 'arogya vana reviews':'Not used: arogyavana.com publishes no reviews; never invent them',
 'new farmland launch near bangalore':'Not targeted: launch wording is tied to the pending Phase 3 decision'}
LIGHT={'cheap farm plots near bangalore':'Light: "cheap" is not in the copy; covered by "affordable small farm plot"'}
CL={'Weekend & lifestyle':WK,'Family & life goals':WK,'Corporate professionals':IT,'Tech corridors / commute':CM,'Location – route & region':'/farmland-near-bagepalli/',
 'Plot size & price':'/phase-2/','How to buy / process':'/how-to-buy/','Site visit':'/contact/','Managed farmland – how it works':'/faq/','Sandalwood & plantation':'/sandalwood-farmland-near-bangalore/',
 'Comparisons':'/farmland-vs-gold/','NRI (secondary)':'/farmland-for-nris-karnataka/','Brand':'/','Question / voice (AEO)':'/faq/','Kannada':'/kn/','Core – farmland near Bangalore':'/managed-farmland-near-bangalore/'}
def where(page,kw):
    s=open('new'+page+'index.html',encoding='utf-8').read(); low=html.unescape(s).lower()
    t=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S).group(1)).lower()
    h=' '.join(html.unescape(re.sub('<[^>]+>','',x)).lower() for x in re.findall(r'<h[12][^>]*>(.*?)</h[12]>',s,re.S))
    toks=[x for x in re.split(r'\W+',kw.lower()) if len(x)>3]
    w=[]
    if kw.lower() in low: w.append('exact phrase in copy')
    if toks and all(x in t for x in toks): w.append('title')
    if toks and all(x in h for x in toks): w.append('H1/H2')
    return ', '.join(w) or 'topic covered in copy'
out=[]
for r in rows:
    k=r['Keyword']; pr=r['Priority']
    if pr=='Hold': out.append([k,r['Cluster'],pr,'On hold (not targeted)',r['Target page'],'',r['Note']]); continue
    if pr=='Ads only': out.append([k,r['Cluster'],pr,'Ad negative (never on site)','','','Exclude in ads']); continue
    if k in SKIP: out.append([k,r['Cluster'],pr,'Skipped',OVR.get(k) or CL[r['Cluster']],'',SKIP[k]]); continue
    page=PRIMARY.get(k) or OVR.get(k) or CL[r['Cluster']]
    role='Primary' if k in PRIMARY else 'Secondary'
    note=LIGHT.get(k,'') or ('kn meta description and alt text' if page=='/kn/' else where(page,k))
    out.append([k,r['Cluster'],pr,'Targeted',page,role,note])
w=csv.writer(open('drafts/seo/keyword-page-map-v2.csv','w',encoding='utf-8',newline=''))
w.writerow(['Keyword','Cluster','Priority','Status','Page','Role','How used / note']); w.writerows(out)
print(Counter(x[3] for x in out)); print(sorted(Counter(x[4] for x in out if x[3]=='Targeted').items()))
prim=Counter(x[4] for x in out if x[5]=='Primary'); print('pages with >1 primary',[p for p,c in prim.items() if c>1])
print('targeted with only topic coverage',sum(1 for x in out if x[3]=='Targeted' and x[6]=='topic covered in copy'))
