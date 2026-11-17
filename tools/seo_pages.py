from seo_common import *
PAGES={}
def page(rel):
    def d(fn): PAGES[rel]=fn; return fn
    return d

@page('managed-farmland-near-bangalore/index.html')
def core(s):
    s=set_meta(s,'Farmland near Bangalore for Sale | Managed Farm Plots – Arogya Vana',
      'Farmland for sale near Bangalore: managed farm plots at Arogya Vana near Bagepalli, about 2 hours from Bengaluru. Phase 2: 4,400 sq ft at ₹299 per sq ft.',
      'Aerial view of Arogya Vana managed farmland near Bagepalli')
    s=h1(s,'Farmland near Bangalore, Managed for You')
    s=hero_alt(s,'Aerial view of Arogya Vana managed farmland near Bagepalli, about 2 hours from Bengaluru')
    s=prose_start(s,'<p class="ans">Looking for farmland near Bangalore? Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli in Chikkaballapur district, about 2 hours from Bengaluru by road. Phase 2 farm plots are 4,400 sq ft at ₹299 per sq ft, with a farm team looking after the plantation.</p>'+FACTS)
    add=(qa('Is there farmland for sale near Bangalore?',
      'Yes. Arogya Vana has Phase 2 farmland plots for sale near Bagepalli, about 2 hours from Bengaluru by road. Each plot is 4,400 sq ft at ₹299 per sq ft. Phase 1 is sold out. Registration and stamp duty are extra, and our team shares the full cost in writing before you pay.')
     +'<h2>Farm plots and agricultural land for sale near Bangalore: what you are buying</h2><p>At Arogya Vana you buy a farmland plot in a managed farmland community. The land is planted with white sandalwood, casuarina and seasonal fruits and vegetables, and our farm team handles planting, drip irrigation and upkeep. You do not need to run the farm yourself.</p>'
     +F('g9','Prepared farmland plots at Arogya Vana near Bagepalli','Prepared land at Arogya Vana.')
     +'<h2>How to judge a farmland project near Bengaluru</h2><p>Every buyer’s “best farmland near Bangalore” is different. Use the same checklist for every project you look at:</p><ul><li><b>Location and drive:</b> how long it takes to reach the land from your home. Arogya Vana is about 2 hours from Bengaluru.</li><li><b>Documents:</b> have your own lawyer check the title and land records.</li><li><b>Who manages it:</b> who plants, waters and secures the land, and on what written terms.</li><li><b>Full cost:</b> the rate per sq ft, plus registration, stamp duty and any other charges in writing.</li><li><b>A site visit:</b> walk the land before you decide.</li></ul><p>See our '+a('hb','farmland buying guide')+' and '+a('cmp','how Arogya Vana compares with other managed farmland projects')+'.</p>'
     +'<h2>Gated, managed farmland with a farm team on site</h2><p>Arogya Vana is a gated farmland community near Bangalore, developed and managed by Saptha Ventures. The farm has 24/7 security, CCTV and solar fencing, and agronomists plan the plantation and care for it through the seasons. For details of plot size and rate, see '+a('p2')+'; for the cost breakdown, see '+a('pr')+'.</p>'
     +'<h2>Who Arogya Vana is for</h2><p>Arogya Vana is built for Bengaluru’s working professionals who want farmland they can visit without weekday farm work. Read '+a('it')+', plan '+a('wk')+', or check the drive in '+a('cm')+'.</p>')
    s=ins_before_first(s,['<h2>Frequently asked questions</h2>'],add)
    s=related(s,links('bg','p2','pr','hb','it','wk','fq'))
    s=faq_add(s,[('Who is the developer of Arogya Vana?','Saptha Ventures. Arogya Vana is a project of Saptha Ventures, with a sales office at First Floor, 36, NTI Layout 1st phase, Bengaluru 560092.'),
                 ('Are farm plots near Bangalore sold with management?','At Arogya Vana, yes. The farm team plants, irrigates and looks after the plantation, and the land has 24/7 security, CCTV and solar fencing.')])
    return s

@page('farmland-near-bagepalli/index.html')
def bag(s):
    s=set_meta(s,'Farmland near Bagepalli, Chikkaballapur | Arogya Vana',
      'Farmland near Bagepalli, Chikkaballapur district: about 2 hours from Bengaluru, 15 minutes from NH44 (Bangalore–Hyderabad highway). Phase 2: 4,400 sq ft at ₹299 per sq ft.',
      'Highway towards Bagepalli and Arogya Vana farmland')
    s=h1(s,'Farmland near Bagepalli, Chikkaballapur District')
    s=hero_alt(s,'Highway drive from Bengaluru towards farmland near Bagepalli')
    s=prose_start(s,'<p class="ans">Arogya Vana is a Saptha Ventures managed farmland project near Bagepalli, in Chikkaballapur district on the Karnataka–Andhra Pradesh border. It is about 2 hours from Bengaluru by road and about 15 minutes from NH44, the Bangalore–Hyderabad highway. Phase 2 farm plots are 4,400 sq ft at ₹299 per sq ft.</p>'+FACTS)
    add=(qa('How far is Bagepalli from Bangalore?',
      'Arogya Vana, near Bagepalli, is about 2 hours from Bengaluru by road. The drive is along NH44, the Bangalore–Hyderabad highway, and the farm is about 15 minutes from NH44. Traffic and your starting point in the city change the time, so plan a Saturday visit with an early start.')
     +qa('Is Bagepalli good for farmland?',
      'Bagepalli has red soil and open land suited to sandalwood and fruit crops, with direct road access from Bengaluru via NH44. It is close to the Greenfield Highway and the proposed SEZ. Whether it suits you depends on your plans, so visit the land and review the documents before you decide.')
     +F('g8','Red-soil farmland near Bagepalli at Arogya Vana','Red soil on the land at Arogya Vana, near Bagepalli.')
     +'<h2>Farm plots and agricultural land near Bagepalli, Chikkaballapur district</h2><p>Bagepalli is in the north of Chikkaballapur district. People searching for farm plots in Chikkaballapur district, or for farmland near Chikkaballapur, Nandi Hills, Gudibande or Gauribidanur, are looking at the same stretch of country north of Bengaluru. Arogya Vana itself is near Bagepalli, on the Karnataka–Andhra Pradesh border.</p>'
     +'<h2>Farmland on the Bangalore–Hyderabad highway (NH44)</h2><p>From Bengaluru, the route north follows NH44, the Bangalore–Hyderabad highway. Arogya Vana is about 15 minutes from NH44. If you are coming from North Bangalore, you are already on this side of the city; from Whitefield or Electronic City, see '+a('cm')+'.</p>'
     +'<h2>Farmland about 2 hours from Bangalore</h2><p>Many people search by distance, such as farmland 100 km from Bangalore or within 150 km. We give the drive time instead, because traffic decides the trip: about 2 hours from Bengaluru by road. That keeps it within reach for a Saturday visit.</p>'
     +F('g2','Open land with native trees near Bagepalli','Open land and native trees at Arogya Vana.')
     +'<h2>Nearby landmarks</h2><p>The farm is near Lepakshi Temple and the Kia Motors plant across the border in Andhra Pradesh, and close to the Greenfield Highway and the proposed SEZ.</p>'
     +F('lepakshi','Lepakshi Temple, a landmark near Arogya Vana','Lepakshi Temple, one of the nearby landmarks.'))
    s=R(s,'<p>Arogya Vana is a managed farmland community near Bagepalli in Chikkaballapur district, on the Karnataka–Andhra Pradesh border. It is about 2 hours from Bengaluru and 15 minutes from NH44.</p>','')
    s=ins_before_first(s,['<p><a href="/#location">See the map and directions</a>.</p>'],add)
    s=related(s,links('core','p2','cm','wk','ct','fq'))
    s=faq_add(s,[('Is Arogya Vana on the Bangalore–Hyderabad highway?','The farm is about 15 minutes from NH44, the Bangalore–Hyderabad highway, near Bagepalli.'),
                 ('Which district is Bagepalli in?','Bagepalli is in Chikkaballapur district, on the Karnataka–Andhra Pradesh border.')])
    o=ld_get(s); o['@graph'].append({"@type":"Place","@id":SITE+"/farmland-near-bagepalli/#place","name":"Arogya Vana","description":"Managed farmland by Saptha Ventures near Bagepalli, Chikkaballapur district, on the Karnataka–Andhra Pradesh border. About 2 hours from Bengaluru by road and about 15 minutes from NH44.","address":{"@type":"PostalAddress","addressLocality":"near Bagepalli","addressRegion":"Chikkaballapur district, Karnataka–Andhra Pradesh border","addressCountry":"IN"}})
    return ld_set(s,o)

@page('phase-2/index.html')
def p2(s):
    s=set_meta(s,'4,400 sq ft Farm Plots near Bangalore | Arogya Vana Phase 2',
      'Arogya Vana Phase 2: 4,400 sq ft farm plots at ₹299 per sq ft near Bagepalli, about 2 hours from Bengaluru. A small managed farm plot for working professionals.',
      'Road to Arogya Vana Phase 2 near Bagepalli')
    s=hero_alt(s,'Road to Arogya Vana Phase 2 farm plots near Bagepalli')
    s=prose_start(s,'<p class="ans">Arogya Vana Phase 2 is the phase on sale now: 4,400 sq ft farm plots at ₹299 per sq ft, near Bagepalli and about 2 hours from Bengaluru. Phase 1 is sold out, and no Phase 3 price has been announced. Registration and stamp duty are extra, as per government rates.</p>')
    add=(qa('How big is a 4,400 sq ft farm plot?',
      'A 4,400 sq ft plot is about one-tenth of an acre, or about 4 guntas (one gunta is 1,089 sq ft). That makes it a small farm plot near Bangalore: big enough for a planted plot looked after by our farm team, and simple to visit and understand on a single Saturday trip.')
     +'<h2>A small, managed farm plot near Bangalore</h2><p>If you are looking for an affordable small farm plot near Bangalore without the work of running a farm, Phase 2 is a single, clearly priced size: 4,400 sq ft at ₹299 per sq ft. Phase 2 covers 13 acres, with 5,000+ trees planned. Our team gives you the full cost and payment steps in writing before you pay.</p>'
     +F('g9','Prepared Phase 2 farmland at Arogya Vana','Prepared farmland at Arogya Vana.'))
    s=ins_before_first(s,['<h2>The land</h2>'],add)
    s=s.replace('<h2>The land</h2>','<h2>The land</h2>'+F('aerial','Aerial view of the Arogya Vana farmland near Bagepalli','Aerial view of Arogya Vana.'),1)
    s=faq_add(s,[('How many guntas is a 4,400 sq ft plot?','About 4 guntas. One gunta is 1,089 sq ft, so 4,400 sq ft is just over 4 guntas, or about one-tenth of an acre.'),
                 ('Who are Phase 2 plots for?','Bengaluru working professionals and families who want a managed farmland plot they can visit, about 2 hours from the city.')])
    s=ins_before_first(s,['<h2>Frequently asked questions</h2>'],'<p class="rel"><b>Related guides:</b> '+' · '.join(f'<a href="{u}">{t}</a>' for u,t in links('pr','hb','ct','it','wk','bg'))+'</p>')
    return s

@page('managed-farmland-price-bangalore/index.html')
def price(s):
    s=set_meta(s,'Farmland Price near Bangalore 2026 | ₹299 per sq ft – Arogya Vana',
      'Managed farmland price near Bangalore, 2026: Arogya Vana Phase 2 plots are 4,400 sq ft at ₹299 per sq ft. What is included, extra costs and the full cost in writing.',
      'Aerial view of Arogya Vana managed farmland')
    s=h1(s,'Managed Farmland Price near Bangalore (2026)')
    s=hero_alt(s,'Aerial view of Arogya Vana managed farmland near Bagepalli')
    s=prose_start(s,'<p class="ans">The farmland price at Arogya Vana is ₹299 per sq ft for Phase 2 plots of 4,400 sq ft, near Bagepalli and about 2 hours from Bengaluru. Registration and stamp duty are paid separately at government rates. Phase 1 is sold out. Our team shares the full cost in writing before you pay.</p>')
    add=(qa('How much does a farm plot cost near Bangalore?',
      'It depends on the location, plot size and what is included. At Arogya Vana, Phase 2 farm plots are 4,400 sq ft at ₹299 per sq ft, with registration and stamp duty extra at government rates. Ask our team for the full cost and payment schedule in writing before you decide.')
     +'<h2>What affects farmland cost near Bengaluru</h2><ul><li><b>Location and drive time</b> from the city.</li><li><b>Plot size</b> and how the rate is quoted (per sq ft, per gunta or per acre).</li><li><b>What is planted and who maintains it</b>, and for how long.</li><li><b>Government charges</b>: registration and stamp duty.</li><li><b>Other charges</b>, which should be given to you in writing.</li></ul>'
     +'<h2>Farmland rate per sq ft: comparing like with like</h2><p>When you compare a farmland rate near Bangalore in 2026, compare the rate per sq ft on the same basis, then add what each project includes. See '+a('cmp')+' for public prices from other projects, and '+a('hb')+' for the buying steps.</p>'
     +F('g8','Red-soil farmland at Arogya Vana near Bagepalli','The land at Arogya Vana.'))
    s=ins_before_first(s,['<p class="rel">','<p>Related: '],add)
    s=related(s,links('p2','hb','cmp','core','ct','fq'))
    s=faq_add(s,[('Is the price per sq ft or per plot?','The published Phase 2 rate is ₹299 per sq ft, on 4,400 sq ft plots. Our team gives you the full cost in writing.'),
                 ('Is there a booking amount?','Our team gives you the booking amount and payment schedule in writing before you pay anything.')])
    return s

HB_CHECK=('<h2>Farmland buying checklist: what to check before buying farmland</h2><p>Use this farmland due diligence checklist for any farmland near Bangalore. Have an independent lawyer check each item.</p><ol>'
 '<li><b>Title:</b> who owns the land now, and the chain of past owners.</li>'
 '<li><b>Land records (RTC):</b> that the owner, survey number and extent match the sale documents.</li>'
 '<li><b>Mutation records:</b> that past transfers were recorded.</li>'
 '<li><b>Encumbrance certificate (EC):</b> that the land is free of loans and claims.</li>'
 '<li><b>Survey and boundaries:</b> that the plot on the ground matches the plot in the papers.</li>'
 '<li><b>Land classification:</b> whether the land is agricultural or converted, and what that means for its use.</li>'
 '<li><b>Access and water:</b> road access to the plot and how it is irrigated.</li>'
 '<li><b>Management agreement:</b> what is done on your plot, by whom, for how long, and at what cost.</li>'
 '<li><b>Full cost in writing:</b> rate, registration, stamp duty and any other charges.</li></ol>')
@page('how-to-buy/index.html')
def hb(s):
    s=set_meta(s,'How to Buy Farmland near Bangalore | Step-by-Step Guide – Arogya Vana',
      'How to buy farmland near Bangalore: the steps, documents to check (RTC, EC, title), registration and a buying checklist. Phase 2: 4,400 sq ft at ₹299 per sq ft.')
    s=h1(s,'How to Buy Farmland near Bangalore: Step by Step')
    s=prose_start(s,'<p class="ans">To buy farmland near Bangalore at Arogya Vana: enquire, take a Saturday site visit, choose a Phase 2 plot (4,400 sq ft at ₹299 per sq ft), have your own lawyer review the documents, book, then register at the sub-registrar’s office. Every cost and step is given in writing before you pay.</p>')
    add=(HB_CHECK
     +qa('Can non-farmers buy agricultural land in Karnataka?',
      'Who can buy agricultural land in Karnataka is governed by the Karnataka Land Reforms Act, which has been amended over the years. The rules depend on the land and on your own situation, so check the current position with an independent lawyer before you book. Our team explains our process and documents in writing.')
     +qa('What documents are needed to buy farmland in Karnataka?',
      'Your lawyer will usually look at the title documents, the land records (RTC), mutation records, the encumbrance certificate and the survey sketch, along with the draft sale deed. For the buyer, identity and address proof are needed at registration. Our team tells you which project documents are shared with buyers.')
     +'<h2>Land records explained: RTC, e-khata and DC conversion</h2><ul>'
      '<li><b>RTC (Record of Rights, Tenancy and Crops):</b> the Karnataka land record for agricultural land, also called the pahani. It shows the owner, survey number, extent and crops.</li>'
      '<li><b>E-khata:</b> a property record kept by local bodies, used mainly for non-agricultural property. It is not the same as an RTC.</li>'
      '<li><b>DC conversion:</b> an order converting agricultural land to non-agricultural use. Agricultural land without conversion stays agricultural land.</li></ul>'
      '<p>This is general information, not legal advice. Ask your lawyer which records apply to the plot you choose.</p>'
     +qa('How does farmland registration work in Karnataka?',
      'The sale deed is registered at the sub-registrar’s office, where buyer and seller sign and stamp duty and registration fees are paid at government rates. After registration, the land records are updated in the buyer’s favour. Your lawyer and our team explain each step before the registration date.')
     +'<h2>First-time farmland buyer guide</h2><p>Buying farmland for the first time? Go slowly: visit the land, read the management agreement, ask for the full cost in writing, and have your own lawyer check the documents. Never pay before you understand what you are buying. Working in tech or a corporate job? See '+a('it')+'.</p>')
    s=ins_before_first(s,['<h2>Costs at a glance</h2>'],add)
    s=ins_before_first(s,['<h2>Frequently asked questions</h2>'],'<p class="rel"><b>Related guides:</b> '+' · '.join(f'<a href="{u}">{t}</a>' for u,t in links('p2','pr','ct','fq','nri','wmf'))+'</p>')
    s=faq_add(s,[('What should I check before buying farmland?','Title, land records (RTC), mutation records, the encumbrance certificate, survey and boundaries, land classification, access and water, the management agreement and the full cost in writing. Have your own lawyer check them.'),
                 ('What is an RTC in Karnataka?','RTC stands for Record of Rights, Tenancy and Crops, also called the pahani. It is the land record for agricultural land and shows the owner, survey number, extent and crops.'),
                 ('Is DC-converted land the same as agricultural land?','No. DC conversion is an order converting agricultural land to non-agricultural use. Agricultural land without conversion stays agricultural land.')])
    return s

@page('contact/index.html')
def ct(s):
    s=set_meta(s,'Book a Farmland Site Visit from Bangalore | Contact Arogya Vana',
      'Book a farmland site visit near Bangalore: see Arogya Vana near Bagepalli, about 2 hours from Bengaluru. Saturday visits available. Call +91 70909 05031.')
    s=h1(s,'Book a Farmland Site Visit from Bangalore')
    s=prose_start(s,'<p class="ans">To visit Arogya Vana, book a site visit on our website or call +91 70909 05031. Saturday visits are available. The farm is near Bagepalli, about 2 hours from Bengaluru, and our team confirms your visit and shares directions by phone.</p>')
    add=(qa('What happens on a farmland tour near Bangalore?',
      'On a site visit you walk the land, see the plots, the plantation and the clubhouse, and ask our team anything about the buying steps and documents. It is the simplest way to judge farmland near Bangalore for yourself, and to ask about anything you are unsure of.')
     +'<h2>Questions to ask on your site visit</h2><ul><li>Which Phase 2 plots are available, and where are they?</li><li>What is planted on the plot, and who looks after it?</li><li>What does maintenance cover, and what does it cost after the free period?</li><li>Which documents will my lawyer receive?</li><li>What is the full cost, in writing?</li></ul>'
     +F('g5','Site entrance at Arogya Vana near Bagepalli','The site entrance at Arogya Vana.'))
    s=ins_before_first(s,['<h2>Send an enquiry</h2>'],add)
    s=ins_before_first(s,['<h2>Follow us</h2>'],'<p class="rel"><b>Before you visit:</b> '+' · '.join(f'<a href="{u}">{t}</a>' for u,t in links('cm','bg','p2','hb','fq'))+'</p>')
    o=ld_get(s); o['@graph'].append({"@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"How do I book a farmland site visit?","acceptedAnswer":{"@type":"Answer","text":"Book a site visit on arogyavana.com or call +91 70909 05031. Saturday visits are available. Our team confirms the visit and shares directions."}},
        {"@type":"Question","name":"What happens on a farmland tour near Bangalore?","acceptedAnswer":{"@type":"Answer","text":strip(add.split('<p class="ans">')[1].split('</p>')[0])}}]})
    return ld_set(s,o)

FAQ_SECTIONS=[
 ('Farmland near Bangalore',[
  ('Where can I buy farmland near Bangalore?','Arogya Vana sells managed farmland plots near Bagepalli, in Chikkaballapur district on the Karnataka–Andhra Pradesh border, about 2 hours from Bengaluru by road. Phase 2 plots are 4,400 sq ft at ₹299 per sq ft. Call +91 70909 05031 or book a Saturday site visit to see the land.'),
  ('Which is the best farmland near Bangalore for weekends?','The best choice depends on drive time, documents and who looks after the land. Arogya Vana is about 2 hours from Bengaluru, near Bagepalli, with a farm team managing the plantation. Compare any project on the same checklist, and visit the land yourself before you decide.'),
  ('Is there farmland near me in Bangalore?','If you live in Bengaluru, Arogya Vana is about 2 hours away by road, near Bagepalli and about 15 minutes from NH44. North Bangalore is on the highway side of the city; from Whitefield or Electronic City, allow extra time to cross the city. Book a Saturday site visit to see it.'),
  ('How far is Bagepalli from Bangalore?','Arogya Vana, near Bagepalli, is about 2 hours from Bengaluru by road, along NH44, the Bangalore–Hyderabad highway. The farm is about 15 minutes from NH44. Your actual time depends on where you start and on traffic, so plan an early start for a Saturday site visit.'),
  ('Is Bagepalli good for farmland?','Bagepalli has red soil and open land suited to sandalwood and fruit crops, and direct road access from Bengaluru via NH44. It is near the Greenfield Highway and the proposed SEZ. Whether it suits you depends on your own plans, so walk the land and check the documents first.')]),
 ('Plots, price and buying',[
  ('How much does a farm plot cost near Bangalore?','At Arogya Vana, Phase 2 farm plots are 4,400 sq ft at ₹299 per sq ft. Registration and stamp duty are extra, at government rates. Phase 1 is sold out and no Phase 3 price has been announced. Our team shares the full cost and payment schedule in writing before you pay.'),
  ('What is the minimum land size to buy at Arogya Vana?','Phase 2 plots at Arogya Vana are 4,400 sq ft each, about 4 guntas or one-tenth of an acre. Legal rules on land sizes depend on the state and the land’s classification, so ask your own lawyer about the plot you choose before you book or pay anything.'),
  ('Can a salaried person buy agricultural land in Karnataka?','Eligibility to buy agricultural land in Karnataka depends on the state’s land laws and your own situation, not on your job. The Karnataka Land Reforms Act sets the rules and has been amended over time. Check your case with an independent lawyer before you book; our team explains our process in writing.'),
  ('Is it worth buying farmland near Bangalore?','It depends on why you want it. Farmland suits buyers who want land they can visit and a plantation looked after for them. It takes time to sell and shouldn’t replace emergency savings. We make no promises about future land prices, so visit, read the documents and decide for yourself.')]),
 ('Managed farmland: how it works',[
  ('How does managed farmland work?','You buy a farmland plot, and the developer’s farm team plants, irrigates, secures and maintains it under a written agreement. At Arogya Vana, the plantation is white sandalwood with casuarina and seasonal fruits and vegetables, and the land has 24/7 security, CCTV and solar fencing. You visit whenever you like.'),
  ('Managed farmland vs buying agricultural land yourself: what is the difference?','Buying agricultural land yourself means you arrange planting, water, fencing, labour and security. With managed farmland, a farm team does that work under an agreement, and you share the land’s upkeep with a community. Either way, check the title and land records with your own lawyer.'),
  ('What are the pros and cons of managed farmland?','Pros: someone else runs the farm, the land is secured, and you can visit a planted plot without weekday work. Cons: you depend on the manager’s terms, maintenance is charged after any free period, and land takes time to sell. Read the management agreement carefully before you sign.'),
  ('Is managed farmland safe?','Safety comes from clear documents and a reliable manager. Have your own lawyer check the title, land records and encumbrance certificate, and read the management agreement. On the ground, Arogya Vana has 24/7 security, CCTV and solar fencing. Visit the land before you decide, and get every cost in writing.'),
  ('Is managed farmland legal in Karnataka?','Buying farmland and appointing a company to manage it is a common arrangement. Whether a specific purchase is in order depends on the land’s records and the buyer’s eligibility under state law. Have an independent lawyer check the documents and your eligibility before you book or pay anything.'),
  ('What are managed farmland maintenance charges at Arogya Vana?','At Arogya Vana, maintenance is free for the first two years, and charges apply from the third year. Our team shares the current maintenance charges and what they cover in writing, so ask for them during your site visit before you book a plot.'),
  ('Who maintains managed farmland at Arogya Vana?','Saptha Ventures’ agronomy and farm team. Agronomists plan the tree mix, monitor soil health and manage irrigation, and the farm team handles planting, upkeep and security. One point of contact handles farm queries and visit planning for owners.')]),
]
@page('faq/index.html')
def faq(s):
    s=set_meta(s,'Farmland near Bangalore FAQs | Managed Farmland – Arogya Vana',
      'Answers about farmland near Bangalore and managed farmland: Bagepalli distance, plot size, ₹299 per sq ft price, buying rules, maintenance and site visits.',
      'Plantation rows at a managed farm')
    s=h1(s,'Farmland near Bangalore: Your Questions Answered')
    s=hero_alt(s,'Morning light over plantation rows on managed farmland')
    s=prose_start(s,'<p class="ans">Quick answers about Arogya Vana and managed farmland near Bangalore. '+FACT_SENTENCE+' Phase 1 is sold out. For anything else, call +91 70909 05031.</p>'+FACTS)
    html=''
    for h,items in FAQ_SECTIONS:
        html+=f'<h2>{h}</h2><div class="faq">'+faq_items_html(items)+'</div>'
    s=R(s,'<h2>Frequently asked questions</h2>',html+'<h2>More frequently asked questions</h2>')
    s=related(s,links('hb','p2','pr','bg','core','wmf','ct'))
    s=faq_sync(s)
    return s

@page('sandalwood-farmland-near-bangalore/index.html')
def sw(s):
    s=set_meta(s,'Sandalwood Farmland near Bangalore | Plantation Plots – Arogya Vana',
      'Sandalwood farmland near Bangalore: 4,400 sq ft plots planted with white sandalwood, casuarina and seasonal fruits and vegetables near Bagepalli. Phase 2 at ₹299 per sq ft.',
      'Sandalwood trees in a plantation')
    s=hero_alt(s,'White sandalwood trees in a managed sandalwood plantation')
    s=R(s,'White sandalwood is one of the highest-value long-term timber crops.','White sandalwood is a long-cycle tree grown for its fragrant heartwood.')
    s=R(s,'You hold land in a growing corridor near the proposed SEZ and Greenfield Highway, with a long-cycle sandalwood plantation on it.','The land is near the proposed SEZ and the Greenfield Highway, with a long-cycle sandalwood plantation on it that our farm team looks after.')
    s=prose_start(s,'<p class="ans">Arogya Vana offers sandalwood farmland near Bangalore: managed plantation plots near Bagepalli, about 2 hours from Bengaluru. Each 4,400 sq ft Phase 2 plot (₹299 per sq ft) is planted with white sandalwood, casuarina and seasonal fruits and vegetables, cared for by our farm team.</p>')
    add=(qa('Can I own a sandalwood plantation plot near Bangalore without farming it?',
      'Yes. At Arogya Vana you buy a 4,400 sq ft farmland plot, and our farm team plants, irrigates and protects the sandalwood with casuarina as a host plant and seasonal fruits and vegetables alongside. You can visit whenever you like. Harvest follows the forest department’s procedures, and harvest planning is handled centrally.')
     +'<h2>White sandalwood, not red sandalwood</h2><p>Arogya Vana plants white sandalwood (<i>Santalum album</i>), the fragrant sandalwood traditionally grown in Karnataka. Red sandalwood (red sanders) is a different tree, and it is not what we plant.</p>'
     +'<h2>A mixed plantation: sandalwood with fruit trees and crops</h2><p>Sandalwood needs host plants, so a sandalwood plot is always a mixed plantation, a form of agroforestry. At Arogya Vana, casuarina is the host plant, with seasonal fruits and vegetables grown between the trees. Read '+a('sg')+' and the full '+a('sf')+'.</p>'
     +F('morning','Plantation rows in the morning on managed farmland','A managed plantation in the morning.'))
    s=ins_before_first(s,['<h2>Plots and price</h2>'],add)
    s=related(s,links('sf','sg','p2','bg','core','fq'))
    s=faq_add(s,[('Is it red sandalwood or white sandalwood?','White sandalwood (Santalum album). Red sandalwood is a different tree and is not planted at Arogya Vana.'),
                 ('What is grown with the sandalwood?','Casuarina as the host plant, with seasonal fruits and vegetables grown between the trees.')])
    return s

@page('sandalwood-farming/index.html')
def sf(s):
    s=set_meta(s,'Sandalwood Farming Guide: Planting, Care & Rules | Arogya Vana',
      'A plain-language sandalwood farming guide: how white sandalwood grows, host plants, soil and water, protection, and the forest department rules on harvest in Karnataka.',
      'Sandalwood trees in a plantation')
    s=h1(s,'Sandalwood Farming Guide: Planting, Care and Rules')
    s=hero_alt(s,'Sandalwood trees growing with host plants in a plantation')
    add=(qa('Can I plant sandalwood on my land in Karnataka?',
      'Private landowners can grow sandalwood, but felling and sale are regulated, and growers generally need to register trees and follow the state forest department’s process at harvest. Rules change, so check the current position with the Karnataka Forest Department or a lawyer before you plant. Sandalwood also needs host plants and protection.')
     +F('sandal','Sandalwood trees in a plantation','Sandalwood is a long-cycle tree grown with host plants.'))
    s=ins_before_first(s,['<h2>Or let us farm it for you</h2>'],add)
    s=related(s,links('sw','sg','p2','core','fq'))
    return s

@page('sandalwood-growth-cycle/index.html')
def sg(s):
    s=set_meta(s,'How Long Does Sandalwood Take to Grow? | Growth Cycle – Arogya Vana',
      'How long sandalwood takes to grow: it is a long-cycle tree harvested many years after planting. The stages of growth, what helps the trees, and how Arogya Vana manages it.',
      'Sandalwood plantation')
    s=h1(s,'How Long Does Sandalwood Take to Grow?')
    s=hero_alt(s,'Sandalwood trees in a long-cycle plantation')
    s=prose_start(s,'<p class="ans">Sandalwood takes many years to grow. It is a long-cycle tree: the fragrant heartwood forms slowly inside the trunk, and the tree is harvested at maturity under forest department procedures. At Arogya Vana, the timeline for your plot is set out in your agreement, and seasonal crops grow alongside meanwhile.</p>')
    add=('<h2>The stages of sandalwood tree growth</h2><ol><li><b>Sapling and host plant:</b> each sapling is planted next to a host plant, because sandalwood draws water and nutrients from nearby roots.</li><li><b>Establishment years:</b> regular watering, weeding and mulching while the young tree settles.</li><li><b>Growing years:</b> pruning, host-plant care and protection as the canopy develops.</li><li><b>Heartwood formation:</b> the scented heartwood builds slowly inside the trunk.</li><li><b>Harvest:</b> at maturity, following the forest department’s procedures.</li></ol>'
     +F('managed','Fruit and vegetable plots on managed farmland','Seasonal fruits and vegetables are grown between the trees.'))
    s=ins_before_first(s,['<h2>What helps the trees grow</h2>'],add)
    s=related(s,links('sf','sw','p2','fq'))
    s=faq_add(s,[('How long does sandalwood take to grow?','Many years. It is a long-cycle tree harvested at maturity; at Arogya Vana, the timeline is set out in your agreement.')])
    return s

@page('farmland-vs-gold/index.html')
def vg(s):
    s=set_meta(s,'Farmland vs Gold, Apartment or Plot in Bangalore | Arogya Vana',
      'Farmland vs gold, farmland vs apartment and farmland vs plot in Bangalore: what you own, upkeep, how you use it and what to check, compared side by side.',
      'Managed farmland with fruit and vegetable plots')
    s=h1(s,'Farmland vs Gold, Apartments and Plots: How They Compare')
    s=hero_alt(s,'Managed farmland with fruit and vegetable plots')
    add=('<h2>Farmland vs apartment, plot or villa plot in Bangalore</h2><p>Each is a different kind of property, bought for a different use.</p><div class="tw"><table><thead><tr><th></th><th>Managed farmland</th><th>Apartment</th><th>Residential or villa plot</th></tr></thead><tbody>'
      '<tr><th>What you own</th><td>Agricultural land with a plantation</td><td>A flat and a share of the land</td><td>A plot of non-agricultural land</td></tr>'
      '<tr><th>Typical use</th><td>Green land you visit; crops grown for you</td><td>A home in the city</td><td>A future home site</td></tr>'
      '<tr><th>Upkeep</th><td>Farm team, under an agreement</td><td>Association and maintenance fees</td><td>Your own, until you use it</td></tr>'
      '<tr><th>Key records</th><td>Title, RTC, EC</td><td>Title, building approvals, khata</td><td>Title, conversion order, layout approval, khata</td></tr></tbody></table></div>'
     +qa('Managed farmland vs a DC-converted plot: what is the difference?',
      'A DC-converted plot is land converted from agricultural to non-agricultural use, usually bought as a home site. Managed farmland stays agricultural land, planted and looked after by a farm team. They suit different goals, carry different records, and your lawyer should check the right documents for whichever one you choose.')
     +F('g9','Prepared farmland at Arogya Vana','Agricultural land at Arogya Vana, near Bagepalli.'))
    s=ins_before_first(s,['<h2>Check before you buy</h2>'],add)
    s=related(s,links('cmp','core','pr','hb','fq'))
    s=faq_add(s,[('Is farmland better than an apartment in Bangalore?','They do different jobs. An apartment is a home in the city; farmland is green land you visit, with crops grown for you. Choose by how you plan to use it.')])
    return s

@page('arogya-vana-vs-other-managed-farmland/index.html')
def cmp(s):
    s=set_meta(s,'Best Managed Farmland Companies near Bangalore Compared | Arogya Vana',
      'Arogya Vana vs other managed farmland near Bangalore: public entry prices, locations and a checklist to compare any managed farmland company fairly.',
      'Farmland at golden hour')
    s=hero_alt(s,'Farmland at golden hour, comparing managed farmland near Bangalore')
    add=qa('How do I choose between managed farmland companies near Bangalore?',
      'Compare on the same basis: what you own and whose name it is in, the location and drive time, what is planted, who maintains it and on what written terms, the full cost including registration, and the documents your lawyer can check. Then visit each site before you decide.')
    s=ins_before_first(s,['<h2>How to compare any project</h2>'],add)
    s=related(s,links('core','pr','p2','hb','vg','fq'))
    return s

@page('about/index.html')
def ab(s):
    s=set_meta(s,'About Arogya Vana & Saptha Ventures | Managed Farmland near Bagepalli',
      'Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli, about 2 hours from Bengaluru. Who we are, how we work and how to reach us.',
      'Farmland at golden hour')
    s=hero_alt(s,'Farmland at golden hour, Arogya Vana by Saptha Ventures')
    s=prose_start(s,FACTS)
    s=s.replace('See Phase 2 plots · How to buy · Contact us','See Phase 2 plots · How to buy · Contact us',1)
    s=ins_before_first(s,['<h2>Visit us</h2>'],qa('Who is Saptha Ventures?',
      'Saptha Ventures is the Bengaluru company behind Arogya Vana, with a sales office at First Floor, 36, NTI Layout 1st phase, Bengaluru 560092. Arogya Vana is its managed farmland project near Bagepalli, about 2 hours from Bengaluru, where its agronomy and farm teams look after the land.'))
    s=related(s,links('p2','hb','core','bg','ct','fq'))
    o=ld_get(s)
    for n in o['@graph']:
        if n.get('@type')=='AboutPage': n['about']={"@type":"Organization","name":"Saptha Ventures","url":"https://www.sapthaventures.com/","telephone":"+91-70909-05031","email":"info@arogyavana.com"}
    return ld_set(s,o)

@page('farmland-for-nris-karnataka/index.html')
def nri(s):
    s=set_meta(s,'Farmland for NRIs near Bengaluru | Rules & Options – Arogya Vana',
      'Can NRIs buy farmland in Karnataka? What FEMA generally allows and how NRI families usually take part. Arogya Vana is near Bagepalli, about 2 hours from Bengaluru.',
      'Dawn mist over farmland')
    s=hero_alt(s,'Dawn mist over farmland near Bengaluru')
    s=R(s,'for family, retirement or a long-term asset','for family time and a place to reconnect with the land')
    s=related(s,links('hb','core','p2','fq'))
    return s

@page('blog/index.html')
def blog(s):
    s=s.replace('<img src="/img/managed.webp" alt=""','<img src="/img/managed.webp" alt="Managed farmland with fruit and vegetable plots"',1)
    s=s.replace('<img src="/img/blog.webp" alt=""','<img src="/img/blog.webp" alt="Managed farmland guide from the Arogya Vana blog"',1)
    o=ld_get(s)
    if not any(n.get('@type')=='BreadcrumbList' for n in o.get('@graph',[o])):
        if '@graph' not in o: o={"@context":"https://schema.org","@graph":[{k:v for k,v in o.items() if k!='@context'}]}
        o['@graph'].append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+'/'},{"@type":"ListItem","position":2,"name":"Blog","item":SITE+'/blog/'}]})
    s=ld_set(s,o)
    s=ins_before_first(s,['<section class="cta"'],'<p class="rel"><b>Guides:</b> '+' · '.join(f'<a href="{u}">{t}</a>' for u,t in links('hb','core','wk','it','sg','fq'))+'</p>\n')
    return s

for _rel in ('blog/what-is-managed-farmland/index.html','blog/managed-farmland-benefits/index.html'):
    def _b(s):
        return ins_before_first(s,['<section class="cta"'],'<p class="rel"><b>Next steps:</b> '+' · '.join(f'<a href="{u}">{t}</a>' for u,t in links('core','hb','p2','fq','ct'))+'</p>\n')
    PAGES[_rel]=_b
