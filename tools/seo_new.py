from seo_common import *
# Small set of distinct new pages; their intent is not repeated by the homepage or core land page.
NEW={}
IT_FAQ=[
 ('Can a salaried person buy agricultural land in Karnataka?',
  'Being salaried does not by itself answer the legal question. Eligibility depends on the land and the buyer’s circumstances. Ask an independent lawyer to check your position before signing or paying. At Arogya Vana, our team explains the plot documents and buying steps; your lawyer should assess eligibility.'),
 ('Is this farmland for working couples and corporate employees?',
  'Arogya Vana is aimed at Bengaluru working professionals, including working couples, IT employees and corporate employees who want farmland they can visit. Our farm team handles routine plantation care. A visit helps you understand the land, the travel from your neighbourhood and the written management terms before deciding.'),
 ('What should a first-time farmland buyer check?',
  'Start with the land itself, the documents, the full written cost and the management agreement. Visit, ask who looks after the plot, and have an independent lawyer review the papers before signing or paying. Phase 2 plots at Arogya Vana are 4,400 sq ft at ₹299 per sq ft.'),
]
body=('<p>Looking for a farm plot near Bangalore for IT employees or corporate working professionals? Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli in Chikkaballapur district, about 2 hours from Bengaluru. It is farmland you can visit, with routine plantation care handled by a farm team.</p>'
 +qa('How can working professionals own farmland without running a farm every day?',
 'Managed farmland separates the buyer’s land purchase from the day-to-day work of plantation care. At Arogya Vana, a farm team handles planting, irrigation, maintenance and security. Bengaluru professionals should still review the written scope, costs and responsibilities, and plan visits around their work week before choosing a plot.')
 +'<h2>For software engineers, techies and corporate employees</h2><p>A long work week leaves little time for irrigation, weeding or plantation checks. If you are comparing farmland for IT professionals in Bangalore, start with what the management agreement actually covers. Ask who your farm contact is and how to raise a question about the land.</p>'
 +'<p>Whether you are a young professional making a first land purchase, a working couple, or a salaried employee considering a second property, compare the written costs with your own household budget. The published Phase 2 rate is ₹299 per sq ft for a 4,400 sq ft plot; ask for the full cost before making a decision.</p>'
 +'<h2>A visit that fits around the work week</h2><p>Use a Saturday site visit to see the plots, ask about plantation care and understand the route from home. '+a('cm')+' explains how to plan your journey without assuming the same drive time from every tech corridor.</p>'
 +F('g9','Prepared farmland and planted rows at Arogya Vana near Bagepalli','Prepared land at Arogya Vana. Walk the land before you decide.')
 +'<h2>Questions to take from your desk to the farm</h2><ul><li>Which Phase 2 plot is available and how is it identified on the plan?</li><li>What is planted, who maintains it and what does the written scope cover?</li><li>What are the full charges and payment steps?</li><li>Which papers can your own lawyer review?</li><li>Who will help with farm queries after the purchase?</li></ul>'
 +'<p>Use our '+a('hb')+' guide for the process, and '+a('wk')+' for a land-only weekend perspective. To arrange a visit, call '+CALL+'.</p>')
NEW['farmland-for-it-professionals-bangalore/']={
 'title':'Farmland for IT Professionals in Bangalore | Arogya Vana',
 'desc':'Farm plots for Bengaluru IT and corporate professionals. Explore managed farmland near Bagepalli, Phase 2 plot details and a Saturday site visit.',
 'h1':'Farmland for IT and corporate professionals in Bangalore','crumb':'Farmland for IT professionals','body':body,'faq':IT_FAQ,
 'img':'g8','alt':'Red-earth farmland at Arogya Vana near Bagepalli','keys':('p2','cm','hb','fq')}
WK_FAQ=[
 ('Which is the best farmland near Bangalore for weekends?',
  'There is no single best choice for every buyer. Compare the route from your home, the land you can inspect, the written management terms and your own priorities. Arogya Vana is near Bagepalli, about 2 hours from Bengaluru; visit and review the documents before deciding whether it suits you.'),
 ('Can a family visit the farmland before buying?',
  'Yes. A site visit lets you see the land and ask about the plantation before deciding. Book through arogyavana.com or call +91 70909 05031. The team confirms the visit and directions. Phase 2 plots are 4,400 sq ft at ₹299 per sq ft, and Phase 1 is sold out.'),
 ('What should I ask about weekend gardening?',
  'Ask the farm team what is already planted, how routine care works and whether any personal gardening activity fits the plot’s management plan. Do not assume that every activity is included. A site visit is a useful time to discuss the land, the trees and the written care arrangements.'),
]
body=('<p>Weekend farmland near Bangalore is about having a connection to land beyond the work week. Arogya Vana is a Saptha Ventures managed farmland project near Bagepalli in Chikkaballapur district, about 2 hours from Bengaluru. The offer is farmland plots only, with white sandalwood, casuarina and seasonal fruits and vegetables.</p>'
 +qa('What makes a farm plot useful for weekend visits?',
 'A useful weekend farm plot starts with a route you can plan, land you can inspect and a clear arrangement for care while you are in the city. At Arogya Vana, the farm team looks after the plantation. Visit first and review the written terms rather than choosing only from photographs.')
 +'<h2>A green break from the city</h2><p>If you are searching for a weekend farm near Bangalore, a country-side plot or a slower connection to nature, look at the actual land. Notice the terrain, planted areas and access. Ask how the farm is cared for between your visits and how you can keep in touch with the team.</p>'
 +'<p>Whether you think of it as a weekend getaway, slow living or an escape from city life, owning a farm near Bangalore for weekends starts with the land itself.</p><p>A farm plot for weekend visits is different from a short trip to a tourist destination: you are considering a land purchase. Take time to understand the documents and full charges as well as the setting. The '+a('hb')+' guide explains the steps.</p>'
 +F('g2','Open land and native trees at Arogya Vana near Bagepalli','Open land and native trees at Arogya Vana.')
 +'<h2>Weekend farmland for family time and nature</h2><p>For working parents and couples, a site visit is a chance to look beyond the screen and see the land together. If children or parents are joining, discuss your needs with the team before travelling. Check the terrain in person rather than assuming it suits every age or mobility requirement.</p>'
 +'<p>Farmland for kids’ nature experience starts with observing trees, soil and the changing plantation. If weekend gardening matters to you, ask how it fits the existing plantation and management plan. Seasonal fruits and vegetables are part of the plantation; ask what that means for your plot.</p>'
 +'<h2>Plan a Saturday site visit</h2><p>Start with '+a('ct')+', then review '+a('p2')+'. If you work in a tech corridor, see '+a('cm')+' before travelling. Call '+CALL+' to ask questions and arrange your visit.</p>')
NEW['weekend-farmland-near-bangalore/']={
 'title':'Weekend Farmland near Bangalore | Arogya Vana',
 'desc':'Explore weekend farmland near Bangalore: managed plots near Bagepalli, about 2 hours from Bengaluru. Plan a family site visit and check Phase 2 details.',
 'h1':'Weekend farmland near Bangalore, for a connection to nature','crumb':'Weekend farmland near Bangalore','body':body,'faq':WK_FAQ,
 'img':'g9','alt':'Prepared farmland at Arogya Vana for buyers to inspect','keys':('it','p2','cm','hb')}
CM_FAQ=[
 ('Is Arogya Vana in Whitefield or Electronic City?',
  'No. Arogya Vana is near Bagepalli in Chikkaballapur district, on the Karnataka–Andhra Pradesh border. Whitefield and Electronic City are starting points for Bengaluru buyers planning a visit, not the farm’s address. Ask the team for directions and check the route from your own location before travelling.'),
 ('How long is the drive from Manyata, Hebbal or the airport?',
  'Arogya Vana is about 2 hours from Bengaluru by road and about 15 minutes from NH44. We don’t publish separate journey times from Manyata Tech Park, Hebbal or Kempegowda airport. Check a live map from your actual starting point and allow for traffic on the day.'),
 ('Can I book a Saturday farmland visit from North Bangalore?',
  'Yes. Use the site-visit form or call +91 70909 05031 to arrange a Saturday visit. The team confirms the visit and shares directions. Confirm travel arrangements directly rather than assuming transport is included, and review the route from your own neighbourhood before you leave for Bagepalli.'),
]
body=('<p>Searching for farmland near Whitefield, Electronic City or Manyata Tech Park? Treat your Bengaluru neighbourhood as the starting point, not the property location. Arogya Vana is managed farmland near Bagepalli in Chikkaballapur district, on the Karnataka–Andhra Pradesh border. The farm is about 2 hours from Bengaluru by road.</p>'
 +qa('Where is the farm relative to Bengaluru’s tech corridors?',
 'Arogya Vana is near Bagepalli, not inside Whitefield, Electronic City or the airport neighbourhood. Bengaluru professionals can plan a site visit from their own home or office. Access is via NH44, and the farm is about 15 minutes from it; your travel time depends on where you start.')
 +'<h2>From Whitefield, KR Puram and Marathahalli</h2><p>If your search starts with “farmland near Whitefield”, first compare the farm’s actual location with your planned route. For buyers from KR Puram, Marathahalli, Bellandur and the Outer Ring Road corridor, ask for the destination directions before travelling. We don’t give a separate drive time for each neighbourhood.</p>'
 +'<h2>From Electronic City, HSR Layout and Sarjapur Road</h2><p>Farmland near Electronic City is a broad search, not a promise that the land is close to your office. The same applies to Sarjapur Road, HSR Layout and Koramangala. Plan from your actual start point, account for Bengaluru traffic and confirm the visit before leaving. The property itself is near Bagepalli.</p>'
 +'<h2>From Manyata Tech Park, Hebbal and Yelahanka</h2><p>For searches around farmland near Manyata Tech Park, Hebbal or Yelahanka, use the NH44 route as a starting point for planning. North Bangalore and North Bengaluru farm-plot searches cover a wide area. Check the destination and access rather than treating all north-side locations as interchangeable.</p>'
 +F('g5','Site entrance and open land at Arogya Vana near Bagepalli','The site entrance at Arogya Vana. Ask for directions before you travel.')
 +'<h2>From Kempegowda airport and Devanahalli</h2><p>A search for farmland near Kempegowda airport or Devanahalli may lead to projects in very different places. Arogya Vana is near Bagepalli. Ask for the farm directions, review the onward journey from the airport area and avoid assuming that “near Bengaluru” means beside the airport.</p>'
 +'<h2>NH44 and the Bangalore–Hyderabad highway route</h2><p>Access from Bengaluru is via NH44, and the farm is about 15 minutes from the highway. See '+a('bg')+' for the property’s location context and request the current directions when you '+a('ct')+'.</p>'
 +'<h2>A simple travel checklist for your visit</h2><ol><li>Book the visit and wait for the team’s confirmation.</li><li>Ask for the exact destination and access directions.</li><li>Check a live map from your own home or office.</li><li>Confirm who is joining and any travel needs directly.</li><li>Take your land and document questions with you.</li></ol><p>Call '+CALL+' or use the '+a('ct','site-visit booking page')+'.</p>')
NEW['farmland-near-whitefield-electronic-city/']={
 'title':'Farmland from Whitefield & Electronic City | Arogya Vana',
 'desc':'Plan a farmland visit from Whitefield, Electronic City, Manyata or North Bangalore. Arogya Vana is near Bagepalli; check directions from your starting point.',
 'h1':'Farmland visits from Whitefield, Electronic City and North Bangalore','crumb':'From Bengaluru tech corridors','body':body,'faq':CM_FAQ,
 'img':'g8','alt':'Red-earth farmland near Bagepalli at Arogya Vana','keys':('bg','ct','it','wk')}

def build_new():
    tpl=rd('farmland-near-bagepalli/index.html')
    for path,p in NEW.items():
        s=tpl
        url=SITE+'/'+path
        s=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="{url}">',s,count=1)
        s=re.sub(r'<meta property="og:url" content="[^"]*">',f'<meta property="og:url" content="{url}">',s,count=1)
        src,w,h=IMG[p['img']]
        s=re.sub(r'<meta property="og:image" content="[^"]*">',f'<meta property="og:image" content="{SITE}{src}">',s,count=1)
        s=re.sub(r'<meta name="twitter:image" content="[^"]*">',f'<meta name="twitter:image" content="{SITE}{src}">',s,count=1)
        s=set_meta(s,p['title'],p['desc'],p['alt'])
        body=(f'<main id="main"><article class="art"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <span aria-current="page">{p["crumb"]}</span></nav>'
              '<p class="satbar"><a href="/#visit">Book a Saturday site visit</a> · see the land for yourself, about 2 hours from Bengaluru.</p>'
              +f'<h1>{p["h1"]}</h1><figure><img src="{src}" alt="{ea(p["alt"])}" width="{w}" height="{h}" decoding="async" fetchpriority="high"></figure>'
              +'<div class="prose">'+p['body']+'<h2>Frequently asked questions</h2><div class="faq">'+faq_items_html(p['faq'])+'</div></div>'
              +'<section class="cta" aria-labelledby="cta-h"><h2 id="cta-h">See Arogya Vana before you decide</h2><p>Walk the land and ask your questions.</p><div class="row"><a class="btn" href="/#visit">Book a Saturday Site Visit</a><a class="btn ln" href="tel:+917090905031">Call +91 70909 05031</a></div></section>'
              +'<p class="note">General information, not legal advice. Review the documents with your own lawyer before signing or paying. Arogya Vana is a project of Saptha Ventures.</p></article></main>')
        i=s.index('<main'); j=s.index('</main>')+len('</main>'); s=s[:i]+body+s[j:]
        graph={"@context":"https://schema.org","@graph":[
          {"@type":"WebPage","@id":url+'#page',"name":p['title'],"description":p['desc'],"url":url,"inLanguage":"en-IN"},
          {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+'/'},{"@type":"ListItem","position":2,"name":p['crumb'],"item":url}]},
          {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in p['faq']]}]}
        s=ld_set(s,graph)
        s=related(s,links(*p['keys']))
        os.makedirs(B+path,exist_ok=True); wr(path+'index.html',s)
