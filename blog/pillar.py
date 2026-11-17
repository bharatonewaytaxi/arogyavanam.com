import re,json,html,os
src=open('blog/page.py').read()
exec(src[:src.index("U='https://arogyavana.com/blog/managed")])
exec(src[src.index('def head('):src.index('pub={')])
exec(src[src.index('pub={'):src.index('ld={')])
exec(src[src.index("JS='''"):src.index("art=f'''")])
CSS2='<style>.prose table{width:100%;border-collapse:collapse;margin:0 0 1.2em;font-size:.95rem}.prose th,.prose td{border:1px solid #d9d4c7;padding:8px 10px;text-align:left;vertical-align:top}.prose th{background:#14321f;color:#fff}.prose ol{margin:0 0 1.2em 1.2em}.faq details{background:#fff;border-radius:10px;padding:14px 18px;margin:10px 0}.faq summary{font-weight:700;cursor:pointer}.rel{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0}</style>'
P=[
dict(slug='managed-farmland-near-bangalore',crumb='Managed farmland near Bangalore',
 title='Managed Farmland near Bangalore | Arogya Vana Phase 3 from ₹25 Lakh',
 desc='Own a 4,400 sq.ft managed farmland plot about 2 hours from Bengaluru near Bagepalli. Sandalwood, fruits and full farm management by Saptha Ventures.',
 h1='Managed Farmland near Bangalore, Run for You',img='/img/aerial.webp',
 body='''<p>Managed farmland lets city families own agricultural land while a professional team plants, irrigates, secures and maintains it. Arogya Vana, by Saptha Ventures, is a managed farmland community near Bagepalli on the Karnataka–Andhra Pradesh border, about 2 hours from Bengaluru and 15 minutes from NH44.</p>
<h2>What managed farmland means at Arogya Vana</h2><ul><li>100% land ownership in your name</li><li>Agronomist-run plantation: white sandalwood, casuarina, seasonal fruits and vegetables</li><li>Drip irrigation, water management and rainwater harvesting</li><li>24/7 security, CCTV and solar fencing</li><li>Free maintenance for the first 2 years (charges apply from year 3)</li></ul>
<h2>Farm land near Bangalore that's managed for you</h2><ul><li><b>Proven demand:</b> Phase 1 (5 acres, 2,000+ trees) is sold out and Phase 2 (13 acres) is about 75% sold.</li><li><b>Clear entry plan:</b> a 4,400 sq.ft plot on the ₹25 lakh plan (₹15 lakh land + ₹10 lakh managed investment; returns as per agreement, terms apply). <a href="/#plan">See the plan</a>.</li><li>70% of sandalwood profit and 100% of seasonal fruit and vegetable income go to the owner (subject to terms).</li><li>Resort-style amenities: clubhouse and cottages, pool, yoga deck, gym, play area and jogging trail.</li><li>Legal work handled in-house: title verification, registration, EC, mutation and sale deed.</li><li>Backed by Saptha Ventures and its track record of plotted developments.</li></ul>
<h2>Location</h2><p>Arogya Vana sits near Bagepalli on the Karnataka–Andhra border, close to the Greenfield Highway, the proposed SEZ, Lepakshi Temple and Kia Motors. <a href="/#location">See the location map</a>.</p>
<h2>How to buy</h2><ol><li>Register interest or call <a href="tel:+919886670006">+91 98866 70006</a></li><li>Book a site visit</li><li>Choose your plot and review the documents</li><li>Register the plot, and we start plantation and management</li></ol>
<p>Prefer sandalwood specifically? Read about our <a href="/sandalwood-farmland-near-bangalore/">sandalwood farmland near Bangalore</a>.</p>''',
 faq=[('What is managed farmland?','Land you own outright, while the developer handles farming, upkeep and security.'),('How far is Arogya Vana from Bengaluru?','About 2 hours by road, and 15 minutes from NH44.'),('What is the smallest plot?','4,400 sq.ft.'),('Who maintains the farm?',"Saptha Ventures' agronomy and farm team, free for the first 2 years."),('Can I visit my farm?','Yes. Site visits run every day except Tuesday, 9 AM to 6 PM.')]),
dict(slug='sandalwood-farmland-near-bangalore',crumb='Sandalwood farmland near Bangalore',
 title='Sandalwood Farmland near Bangalore | Managed Plots – Arogya Vana',
 desc='Managed white sandalwood farmland near Bagepalli, 2 hours from Bengaluru. 4,400 sq.ft plots, 70% sandalwood profit share to owners. Phase 3 now launching.',
 h1='Managed Sandalwood Farmland near Bangalore',img='/img/sandal-real.webp',
 body='''<p>White sandalwood is one of the highest-value long-term timber crops. At Arogya Vana, each plot is planted with sandalwood alongside casuarina, fruits and vegetables, so the land gives regular produce income while the sandalwood matures.</p>
<h2>What is planted on your plot</h2><ul><li>About 100 plants per 4,400 sq.ft plot (illustrative)</li><li>White sandalwood as the long-term crop, with casuarina as timber</li><li>Seasonal fruits and vegetables for regular income</li></ul>
<h2>How sandalwood returns are shared</h2><ul><li>70% of sandalwood profit goes to the owner, plus 100% of fruit and vegetable income (subject to terms)</li><li>Plantation, pruning, irrigation, protection and harvest planning are handled by agronomists</li></ul>
<h2>How we protect the sandalwood</h2><p>24/7 security, CCTV and solar fencing, with harvesting managed centrally by the farm team.</p>
<h2>Why sandalwood farmland suits long-term wealth</h2><p>You hold land in a growing corridor near the proposed SEZ and Greenfield Highway, plus a long-cycle crop on it. Values are not guaranteed.</p>
<h2>The Phase 3 plan</h2><p>₹15 lakh land + ₹10 lakh investment = ₹25 lakh per 4,400 sq.ft plot; returns as per agreement, terms apply. <a href="/#plan">See the full plan</a>.</p>
<p>New to the idea? Start with <a href="/managed-farmland-near-bangalore/">managed farmland near Bangalore</a>.</p>''',
 faq=[('How long until sandalwood is harvested?','Sandalwood is a long-cycle crop; the exact timeline is set out in the agreement.'),('Who gets the sandalwood income?','70% goes to the owner, subject to terms.'),('Can I build a farmhouse?','Ask our team; it depends on local rules.')]),
]
exec(open('blog/pages2.py').read())
for p in P:
  U=f"https://arogyavana.com/{p['slug']}/"
  ld={"@context":"https://schema.org","@graph":[{"@type":"WebPage","name":p['title'],"description":p['desc'],"url":U,"inLanguage":"en-IN","publisher":pub},
   {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]},
   {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://arogyavana.com/"},{"@type":"ListItem","position":2,"name":p['crumb'],"item":U}]}]}
  fq=''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q,a in p['faq'])
  b=f'''<body class="pg"><a class="skip" href="#main">Skip to content</a>
{nav}<main id="main"><article class="art"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <span aria-current="page">{p['crumb']}</span></nav>
<h1>{html.escape(p['h1'])}</h1><figure><img src="{p['img']}" alt="{html.escape(p['crumb'])} at Arogya Vana" width="1100" height="619" fetchpriority="high" decoding="async"></figure>
<div class="prose">{p['body']}<h2>Frequently asked questions</h2><div class="faq">{fq}</div></div>
<section class="cta" aria-labelledby="cta-h"><h2 id="cta-h">Explore Arogya Vana Phase 3</h2><p>See the land in person before you decide.</p><div class="row"><a class="btn" href="/#visit">Book a Site Visit</a><a class="btn" href="/brochure.pdf">Download Brochure</a><a class="btn ln" href="https://wa.me/919886670006" target="_blank" rel="noopener">WhatsApp</a></div></section>
<p class="note">General information, not financial or legal advice. Returns and appreciation are not guaranteed; review all project documents before investing. Arogya Vana is a project of Saptha Ventures.</p>
</article></main>{foot}{MC}{wa}{JS}</body></html>'''
  os.makedirs(f"dist/{p['slug']}",exist_ok=True)
  open(f"dist/{p['slug']}/index.html",'w').write(head(p['title'],p['desc'],U,ld,img='https://arogyavana.com'+p['img'],typ='website').replace('</head>',CSS2+'</head>')+b)
print('ok')
