# New pages and site-wide additions, 15 Nov 2026 (approved by Karthick in chat: "fix all make it live").
# Runs after home.py, inner.py (incl. slug moves), blog.py, ty.py, hl.py.
# Built from the drafts in /workspace/arogyavana-site/drafts/. Every [CONFIRM]/[REVIEW] item was left out or rewritten neutrally.
import sys,re,json,os; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from common import *
B='/workspace/arogyavana-site/new/'
SITE='https://arogyavana.com'
TPL=open(B+'farmland-near-bagepalli/index.html',encoding='utf-8').read()
ORG={"@type":"Organization","name":"Arogya Vana by Saptha Ventures","url":SITE+"/","logo":{"@type":"ImageObject","url":SITE+"/img/arogyavana-logo.webp"}}
EXTRA_CSS='<style>.links{list-style:none;margin:0 0 1.4em;padding:0;display:grid;gap:0;border-top:1px solid #e4e2dc}.links li{border-bottom:1px solid #e4e2dc}.links a{display:flex;align-items:center;min-height:52px;font-weight:600}.facts{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 1.2em;padding:0;list-style:none}.facts li{background:#fff;border:1px solid #e4e2dc;border-radius:10px;padding:10px 14px;font-weight:600}.prose .small{font-size:.88rem;color:#4b5a50}</style>'
CALL='<a href="tel:+917090905031">+91 70909 05031</a>'
CTA_ROW='<div class="row"><a class="btn" href="/#visit">Book a Site Visit</a><a class="btn" href="/brochure.pdf">Download Brochure</a><a class="btn ln" href="tel:+917090905031">Call +91 70909 05031</a></div>'
NOTE='<p class="note">General information, not legal advice. Review all project documents before you decide. Arogya Vana is a project of Saptha Ventures.</p>'

def esc_attr(x): return x.replace('&','&amp;').replace('"','&quot;')
def build(path,title,desc,crumb,body,graph,og_img='/img/highway.webp',robots='index,follow',cta=('Visit Arogya Vana','See the land in person before you decide.'),canonical=True):
    url=f'{SITE}/{path}'
    s=TPL
    head_start=s.index('<title>'); head_end=s.index('<style>')
    t=esc_attr(title); d=esc_attr(desc)
    head=(f'<title>{t}</title><meta name="description" content="{d}">'
          +(f'<link rel="canonical" href="{url}">' if canonical else '')
          +f'<meta name="robots" content="{robots}"><meta name="theme-color" content="#14321f">\n'
          +'<meta property="og:type" content="website"><meta property="og:site_name" content="Arogya Vana">'
          +(f'<meta property="og:url" content="{url}">' if canonical else '')
          +f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:image" content="{SITE}{og_img}"><meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:image" content="{SITE}{og_img}">\n'
          +'<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
          +'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&display=swap">\n')
        
    if graph is not None:
        ld=json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False); assert '</' not in ld
        head+=f'<script type="application/ld+json">{ld}</script>\n'
    s=s[:head_start]+head+s[head_end:]
    s=s.replace('</head>',EXTRA_CSS+'</head>',1)
    s=s.replace('<li><a href="/blog/" aria-current="page">Blog</a></li>','<li><a href="/blog/">Blog</a></li>')
    lng_href='/'+path if path else '/'
    s=s.replace('<a href="/blog/" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a>',f'<a href="{lng_href}" hreflang="en" lang="en" aria-current="true" aria-label="English">EN</a>')
    i=s.index('<main id="main">'); j=s.index('</main>')+len('</main>')
    main=(f'<main id="main"><article class="art"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <span aria-current="page">{crumb}</span></nav>\n'
          +body
          +f'\n<section class="cta" aria-labelledby="cta-h"><h2 id="cta-h">{cta[0]}</h2><p>{cta[1]}</p>{CTA_ROW}</section>\n{NOTE}\n</article></main>')
    s=s[:i]+main+s[j:]
    out=B+(path+'index.html' if path.endswith('/') else path)
    os.makedirs(os.path.dirname(out),exist_ok=True); open(out,'w',encoding='utf-8').write(s)
    LOG.append((f'new page /{path}','','',1))

def webpage(path,title,desc,typ='WebPage'):
    return {"@type":typ,"name":title,"description":desc,"url":f'{SITE}/{path}',"inLanguage":"en-IN","publisher":ORG}
def crumbs(path,name):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":name,"item":f'{SITE}/{path}'}]}
def strip_tags(x): return re.sub(r'<[^>]+>','',x)
def faqld(faq): return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip_tags(a)}} for q,a in faq]}
def faqhtml(faq): return '<h2>Frequently asked questions</h2><div class="faq">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)+'</div>'

# ---------------- /about/ ----------------
p='about/'; t='About Arogya Vana | Managed Farmland by Saptha Ventures'
d='Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli, about 2 hours from Bengaluru. Learn who we are and how we work.'
body=('<h1>About Arogya Vana</h1><figure><img src="/img/c-hero-real.webp" alt="Golden hour over the farmland at Arogya Vana" width="1100" height="619" fetchpriority="high" decoding="async"></figure>\n<div class="prose">'
 '<p>Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli, about 2 hours from Bengaluru. The land is planted with white sandalwood, casuarina and seasonal fruits and vegetables.</p>'
 '<p>Arogya Vana currently sells farmland plots. Phase 2 plots are 4,400 sq ft at ₹299 per sq ft.</p>'
 '<h2>Who we are</h2><p>Arogya Vana is a project of Saptha Ventures, a Bengaluru real-estate company with an office at First Floor, 36, NTI Layout 1st phase, Bengaluru 560092.</p>'
 '<h2>What we believe</h2><ul>'
 '<li><b>The land comes first.</b> You are buying land with a living plantation. We talk about the plot, the trees and the care of the land.</li>'
 '<li><b>Clear about everything.</b> One published rate, plain documents and answers in writing. If we don\'t know something yet, we say so.</li>'
 '<li><b>Season after season.</b> Agronomists and a farm team work on the land through the year.</li>'
 '<li><b>A community, not a transaction.</b> Owners meet, visit and grow together.</li></ul>'
 '<h2>The teams behind the land</h2><table><tr><th>Team</th><th>What they do</th></tr>'
 '<tr><td>Agronomy &amp; Farm Science</td><td>Agronomists plan the tree mix, monitor soil health and manage irrigation and plantation care through the seasons.</td></tr>'
 '<tr><td>Co-Farmer Relations</td><td>One point of contact for farm queries and visit planning.</td></tr>'
 '<tr><td>Legal &amp; Documentation</td><td>Helps buyers through the paperwork. Our team explains the documents and steps in writing before you pay.</td></tr></table>'
 '<h2>Our phases</h2><ul><li><b>Phase 1:</b> sold out.</li><li><b>Phase 2:</b> plots available, 4,400 sq ft at ₹299 per sq ft.</li><li><b>Phase 3:</b> no price has been announced.</li></ul>'
 '<p><a href="/phase-2/">See Phase 2 plots</a> · <a href="/how-to-buy/">How to buy</a> · <a href="/contact/">Contact us</a></p>'
 '<h2>Visit us</h2><p>Come and walk the land. We are open Wednesday to Monday, 9 am to 6 pm (closed Tuesday). Call '+CALL+' or <a href="/#visit">book a site visit</a>.</p></div>')
build(p,t,d,'About',body,[webpage(p,t,d,'AboutPage'),crumbs(p,'About')],og_img='/img/c-hero-real.webp',cta=('Come and see the land','Book a site visit, or call us with any question.'))

# ---------------- /contact/ ----------------
p='contact/'; t='Contact Arogya Vana | Book a Saturday Site Visit from Bengaluru'
d='Working in Bengaluru? Book a Saturday visit to Arogya Vana farmland near Bagepalli, about 2 hours from the city. Call +91 70909 05031 or email info@arogyavana.com.'
body=('<h1>Plan a Saturday visit from Bengaluru</h1>\n<div class="prose">'
 '<p>Busy work week? A Saturday visit is the easiest way to see the land for yourself. The farm is about 2 hours from Bengaluru, and our team takes you through the buying process step by step.</p>'
 '<p>The quickest way to reach us is a call. We are happy to answer questions, send the brochure or plan your visit to the farm.</p>'
 '<h2>Call</h2><p><b>'+CALL+'</b><br>Wednesday to Monday, 9 am to 6 pm. Closed Tuesday.</p>'
 '<h2>Languages</h2><p>We can speak with you in English and Kannada.</p>'
 '<h2>Brochure</h2><p><a class="btn" href="/brochure.pdf">Download the brochure (PDF)</a></p><p>We can also email it to you. Just ask when you call.</p>'
 '<h2>Email</h2><p><a href="mailto:info@arogyavana.com">info@arogyavana.com</a></p>'
 '<h2>Sales office</h2><p>First Floor, 36, NTI Layout 1st phase, Bengaluru, Karnataka 560092<br><span class="small">This is our sales office, not the farm.</span></p>'
 '<h2>Opening hours</h2><p>Wednesday to Monday, 9 am to 6 pm. Closed Tuesday.</p>'
 '<h2>The farm</h2><p>The farm is near Bagepalli, about 2 hours from Bengaluru. Directions are shared when we confirm your visit.</p>'
 '<h2>Book a site visit</h2><p>Pick a date and time on our <a href="/#visit">site-visit form</a>. Weekend visits, including Saturdays, are available. Our team will call you to confirm the visit and share directions.</p>'
 '<h2>Send an enquiry</h2><p>Use the <a href="/#enquire">enquiry form</a> and our team will call you back. See our <a href="/privacy-policy/">Privacy Policy</a> for how we use your details.</p>'
 '<h2>Follow us</h2><p><a href="https://www.instagram.com/arogyavanablr/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.youtube.com/@Arogyavana-q2z" target="_blank" rel="noopener">YouTube</a> · <a href="https://x.com/arogyavana" target="_blank" rel="noopener">X</a> · <a href="https://www.facebook.com/profile.php?id=61596195088770" target="_blank" rel="noopener">Facebook</a></p></div>')
org=dict(ORG); org["telephone"]="+91-70909-05031"; org["email"]="info@arogyavana.com"
org["contactPoint"]={"@type":"ContactPoint","telephone":"+91-70909-05031","contactType":"sales","areaServed":"IN","availableLanguage":["English","Kannada"]}
org["address"]={"@type":"PostalAddress","streetAddress":"First Floor, 36, NTI Layout 1st phase","addressLocality":"Bengaluru","addressRegion":"Karnataka","postalCode":"560092","addressCountry":"IN"}
build(p,t,d,'Contact',body,[webpage(p,t,d,'ContactPage'),org,crumbs(p,'Contact')],cta=('Book your visit','Weekend slots are available. We are closed on Tuesdays.'))

# ---------------- /phase-2/ ----------------
p='phase-2/'; t='Phase 2 Farm Plots near Bangalore for Weekend Visits | Arogya Vana'
d='Weekend farmland near Bangalore for working professionals: Phase 2 plots of 4,400 sq ft at ₹299 per sq ft near Bagepalli, about 2 hours from Bengaluru. Book a Saturday site visit.'
faq=[('How far is it from Bengaluru?','About 2 hours by road. The farm is near Bagepalli.'),
 ('What is planted?','White sandalwood, casuarina and seasonal fruits and vegetables.'),
 ('What does a Phase 2 plot cost per sq ft?','Phase 2 plots are 4,400 sq ft at ₹299 per sq ft. Registration and stamp duty are extra as per government rates.'),
 ('Is Phase 1 available?','No. Phase 1 is sold out. Plots are currently available in Phase 2.'),
 ('Has a Phase 3 price been announced?','No. No Phase 3 price has been announced.'),
 ('Can I visit before buying?','Yes. Site visits run every day except Tuesday, 9 am to 6 pm. Book online or call +91 70909 05031.')]
body=('<h1>Phase 2: your own farm plot, about 2 hours from Bengaluru</h1><figure><img src="/img/highway.webp" alt="Road to Arogya Vana Phase 2 near Bagepalli" width="1100" height="619" fetchpriority="high" decoding="async"></figure>\n<div class="prose">'
 '<p>For working professionals in Bengaluru: green farmland you can visit at the weekend, about 2 hours from the city, with a clear buying process explained in writing.</p>'
 '<p>Phase 2 is the phase on sale at Arogya Vana. The land is planted with white sandalwood, casuarina and seasonal fruits and vegetables.</p>'
 '<ul class="facts"><li>4,400 sq ft plots</li><li>₹299 per sq ft</li><li>About 2 hrs from Bengaluru</li></ul>'
 '<h2>Quick answers</h2><ul><li><b>What is the price?</b> ₹299 per sq ft on a 4,400 sq ft plot. Registration and stamp duty are extra as per government rates.</li><li><b>How does buying work?</b> Enquire, visit the farm, choose your plot and go through the documents with our team. See <a href="/how-to-buy/">how to buy</a>.</li><li><b>Can I buy?</b> Rules on who can buy agricultural land depend on your situation. Please take independent legal advice. See the <a href="/how-to-buy/#faq">How to buy FAQ</a>.</li></ul>'
 '<h2>The land</h2><p>The farm is near Bagepalli, about 2 hours from Bengaluru. <a href="/#location">See the location</a>, or <a href="/#visit">book a visit</a> to walk the plots.</p>'
 '<h2>What is grown</h2><ul><li>White sandalwood, a long-cycle tree</li><li>Casuarina</li><li>Seasonal fruits and vegetables</li><li>Drip irrigation for even moisture</li></ul><p>Ask our team what plantation care covers for your plot.</p>'
 '<h2>Price</h2><table><tr><th>Phase</th><th>Price</th></tr><tr><td>Phase 1</td><td>Sold out</td></tr><tr><td>Phase 2 (4,400 sq ft plots)</td><td><b>₹299 per sq ft</b></td></tr><tr><td>Phase 3</td><td>No price announced</td></tr></table>'
 '<p>Registration and stamp duty are extra as per government rates. Our team shares the full cost, booking steps and payment schedule in writing before you pay anything.</p>'
 '<h2>Documents</h2><p>Our team explains which documents you receive. We recommend that your own lawyer reviews them before you sign or pay.</p>'
 '<h2>Visit the farm</h2><p>Open Wednesday to Monday, 9 am to 6 pm (closed Tuesday). Weekend visits, including Saturdays, are available. <a href="/#visit">Book a site visit</a> or call '+CALL+'.</p>'
 +faqhtml(faq)+'</div>')
build(p,t,d,'Phase 2',body,[webpage(p,t,d),faqld(faq),crumbs(p,'Phase 2')],cta=('See Phase 2 in person','Book a weekend site visit, or call us.'))

# ---------------- /how-to-buy/ ----------------
STEPS5=('<h2 id="buying-steps">Buying in 5 steps</h2><ol class="steps5">'
 '<li><b>Enquire.</b> Call '+CALL+' or send an enquiry.</li>'
 '<li><b>Take a Saturday site visit.</b> See the land, about 2 hours from Bengaluru.</li>'
 '<li><b>Review the documents with your own lawyer.</b></li>'
 '<li><b>Book your plot.</b></li>'
 '<li><b>Registration and handover.</b></li></ol>'
 '<p><a class="btn" href="/#visit">Book a Saturday site visit</a></p>')
p='how-to-buy/'; t='How to Buy Managed Farmland at Arogya Vana | Step by Step'
d='How buying a Phase 2 farmland plot at Arogya Vana works: enquire, visit the farm, choose a 4,400 sq ft plot at ₹299 per sq ft, check the documents and register.'
faq=[('How do I buy a farmland plot at Arogya Vana?','Call +91 70909 05031 or send an enquiry on arogyavana.com. Our team will share plot details and book a free site visit. After you visit and choose a Phase 2 plot, our team explains the booking, documents and payment steps in writing before you pay anything.'),
 ('What does a plot cost?','Phase 2 plots are 4,400 sq ft at ₹299 per sq ft. Phase 1 is sold out, and no Phase 3 price has been announced. Registration charges and stamp duty are extra, at government rates. Call +91 70909 05031 for the full cost in writing.'),
 ('Is Phase 1 available?','No, Phase 1 is sold out. Plots are currently available in Phase 2, at 4,400 sq ft and ₹299 per sq ft.'),
 ('How much do I pay to book a plot?','Our team gives you the booking amount and payment schedule in writing before you pay anything.'),
 ('Can I visit the farm before buying?','Yes. Book a free site visit on arogyavana.com or call +91 70909 05031. Pick a date and time slot, and our team will call to confirm and share directions. Visits are closed on Tuesdays. The farm is about 2 hours from Bengaluru.'),
 ('What documents should I check before buying farmland?','Have an independent lawyer check the land documents and land records before you sign or pay. Our team will tell you which documents are shared with buyers.'),
 ('Who can buy agricultural land?','Rules on who can buy agricultural land depend on the state and on your situation, and they can change. Please take independent legal advice before buying.'),
 ('Can NRIs or OCI cardholders buy the plots?','Rules for NRIs and OCI cardholders buying agricultural land are restrictive. Please take legal advice on your own situation before enquiring. See our <a href="/farmland-for-nris-karnataka/">guide for NRIs</a>.'),
 ('Are there extra costs beyond the plot price?','Yes. Registration charges and stamp duty are paid separately at government rates. Our team shares the full cost in writing before you pay.'),
 ('What exactly am I buying?','A farmland plot. Arogya Vana currently sells farmland plots only.'),
 ('Who do I contact to buy?','Call +91 70909 05031, or send an enquiry or book a site visit on arogyavana.com.')]
body=('<h1>How buying your Arogya Vana plot works</h1>\n<div class="prose">'
 '<p>You visit the farm, choose your plot and go through each step with our team beside you. Arogya Vana currently sells farmland plots, and every step is explained in writing before you pay.</p>'
 +STEPS5+
 '<h2>Step 1: Call or enquire</h2><p>Call '+CALL+', or use the <a href="/#enquire">enquiry form</a>. We answer your questions and send the brochure.</p>'
 '<h2>Step 2: Visit the farm</h2><p>Open Wednesday to Monday, 9 am to 6 pm (closed Tuesday). Weekend visits, including Saturdays, are available. <a href="/#visit">Book online</a>. The farm is about 2 hours from Bengaluru.</p>'
 '<h2>Step 3: Choose your plot</h2><p>Phase 2 plots are 4,400 sq ft at ₹299 per sq ft. Phase 1 is sold out. <a href="/phase-2/">See Phase 2</a>.</p>'
 '<h2>Step 4: Book your plot</h2><p>Our team gives you the booking amount, how to pay and the payment schedule in writing before you pay anything.</p>'
 '<h2>Step 5: Check the documents</h2><p>Our team explains which documents are shared with buyers. We recommend that your own lawyer reviews them before you sign or pay.</p>'
 '<h2>Step 6: Pay and register</h2><p>Registration takes place at the sub-registrar\'s office. Registration and stamp duty are extra as per government rates.</p>'
 '<h2>Step 7: Stay in touch with your land</h2><p>Visit the farm any day except Tuesday, and call our team with any farm question.</p>'
 '<h2>Costs at a glance</h2><table><tr><th>Item</th><th>Amount</th></tr><tr><td>Land (Phase 2, 4,400 sq ft plot)</td><td>₹299 per sq ft</td></tr><tr><td>Registration and stamp duty</td><td>As per government rates</td></tr><tr><td>Any other charges</td><td>Shared in writing by our team before you pay</td></tr></table>'
 '<div id="faq"></div>'+faqhtml(faq)+'<p class="small">General information, not legal advice. Please review all documents with your lawyer before buying.</p></div>')
build(p,t,d,'How to buy',body,[webpage(p,t,d),faqld(faq),crumbs(p,'How to buy')],cta=('Start with a visit','Book a site visit, or call us to talk it through.'))

# ---------------- /privacy-policy/ ----------------
p='privacy-policy/'; t='Privacy Policy | Arogya Vana'
d='How arogyavana.com collects and uses the details you share when you send an enquiry or book a site visit, and how to ask us to change or delete them.'
body=('<h1>Privacy Policy</h1>\n<div class="prose"><p class="small">Last updated: 15 November 2026</p>'
 '<p>This policy explains what information arogyavana.com collects when you send an enquiry or book a site visit, why we collect it and how you can ask us to change or delete it.</p>'
 '<h2>Who we are</h2><p>arogyavana.com is run by Saptha Ventures, the company behind Arogya Vana. Phone: '+CALL+'.</p>'
 '<h2>What we collect</h2><p><b>Enquiry form</b></p><ul><li>Your name and phone number (required)</li><li>Your email address (optional)</li><li>The kind of plot you are interested in, and any message you write (optional)</li></ul>'
 '<p><b>Site-visit form</b></p><ul><li>Your name and phone number (required)</li><li>The date and time slot you pick, and the page language</li></ul>'
 '<p><b>Collected automatically when you submit a form</b></p><ul><li>The page you sent it from and the date and time</li><li>Your browser type (user agent) and your IP address. We use these to stop spam and limit repeated submissions.</li></ul>'
 '<p>We do not ask for payment details, ID documents or passwords on this website. This site does not use advertising or analytics cookies.</p>'
 '<h2>Why we use it</h2><ul><li>To call you back about your enquiry and share plot details</li><li>To confirm your site visit and share directions</li><li>To keep our records of enquiries and visits</li><li>To protect the site from spam and misuse</li></ul><p>We do not sell your information. You can ask us to stop contacting you at any time.</p>'
 '<h2>Who we share it with</h2><ul><li>Our own sales and site-visit team, to contact you</li><li>Service providers that host the site and deliver our emails: Cloudflare (website hosting, form storage and email delivery) and Google (our team\'s email inbox). They process data to provide these services.</li><li>Authorities, if the law requires it</li></ul>'
 '<h2>How long we keep it</h2><p>Short-term records used only to limit repeated submissions are cleared regularly. Enquiry and site-visit records are kept only as long as we need them for the purposes above, or as the law requires.</p>'
 '<h2>Your rights</h2><p>You can ask us to see the information we hold about you, correct it, delete it, or stop contacting you. Call '+CALL+'.</p>'
 '<h2>Security</h2><p>Forms are sent over HTTPS and stored in access-controlled systems. No method is fully secure, but we limit who on our team can see your details.</p>'
 '<h2>Children</h2><p>This site is meant for adults buying farmland. We do not knowingly collect information from anyone under 18.</p>'
 '<h2>Changes</h2><p>If we change this policy, we will update the date at the top of this page.</p></div>')
build(p,t,d,'Privacy Policy',body,[webpage(p,t,d),crumbs(p,'Privacy Policy')])

# ---------------- /terms/ ----------------
p='terms/'; t='Terms of Use | Arogya Vana'
d='The terms that apply when you use arogyavana.com: information only, prices, images, enquiries and site visits.'
body=('<h1>Terms of Use</h1>\n<div class="prose"><p class="small">Last updated: 15 November 2026</p>'
 '<p>These terms apply when you use arogyavana.com. By using the site, you agree to them.</p>'
 '<h2>1. About this website</h2><p>arogyavana.com gives information about Arogya Vana, a managed farmland project by Saptha Ventures.</p>'
 '<h2>2. Information only, not an offer</h2><p>Everything on this site, including plot sizes, rates, layouts, photos and plantation details, is general information. It is not an offer, a contract or a promise. A purchase is governed only by the signed sale documents.</p>'
 '<h2>3. Prices</h2><p>Rates shown are per sq ft for the phase named and may change without notice. Registration charges, stamp duty and other government fees are extra, at government rates. Always confirm the current rate and total cost in writing with our team before paying anything.</p>'
 '<h2>4. Land only</h2><p>Arogya Vana currently sells farmland plots. Nothing on this site is a promise of income or of a rise in land value.</p>'
 '<h2>5. Images and illustrations</h2><p>Some images and layouts are illustrative or artist\'s impressions and may differ from the actual site.</p>'
 '<h2>6. Enquiries and site visits</h2><ul><li>When you submit a form, our team may call or email you about your enquiry or visit (see our <a href="/privacy-policy/">Privacy Policy</a>).</li><li>Site-visit slots are requests until our team calls to confirm them. We may need to reschedule because of weather, safety or availability. Visits are closed on Tuesdays.</li><li>Please follow our team\'s safety instructions at the farm.</li></ul>'
 '<h2>7. Your responsibilities</h2><p>Please give accurate details in our forms, don\'t misuse the site, and don\'t try to access systems or data you\'re not allowed to.</p>'
 '<h2>8. Intellectual property</h2><p>The text, photos, logo and design of this site belong to Saptha Ventures or are used with permission. Don\'t copy them for commercial use without written permission.</p>'
 '<h2>9. Links to other sites</h2><p>Links to other websites are for convenience. We are not responsible for their content.</p>'
 '<h2>10. Check before you rely on it</h2><p>Please confirm any information on this site in writing with our team before you rely on it.</p>'
 '<h2>11. Governing law</h2><p>These terms are governed by the laws of India.</p>'
 '<h2>12. Contact</h2><p>Phone: '+CALL+'. See our <a href="/contact/">Contact page</a>.</p></div>')
build(p,t,d,'Terms of Use',body,[webpage(p,t,d),crumbs(p,'Terms of Use')])

# ---------------- /disclaimer/ ----------------
p='disclaimer/'; t='Disclaimer | Arogya Vana'
d='The information on arogyavana.com is general guidance only. Read what it does and does not cover before you decide.'
body=('<h1>Disclaimer</h1>\n<div class="prose"><p>The information on arogyavana.com is for general guidance only. It is not an offer, a contract, or legal, tax or financial advice.</p><ul>'
 '<li><b>Land only.</b> Arogya Vana currently sells farmland plots. No statement on this site should be read as a promise of income or of a rise in land value.</li>'
 '<li><b>Plantation.</b> Plantation timelines and outcomes, including sandalwood, depend on soil, weather, care and government rules on harvest and sale. They are not guaranteed.</li>'
 '<li><b>Prices and availability.</b> Rates and plot availability can change without notice. Confirm the current rate, total cost and government charges in writing before paying.</li>'
 '<li><b>Legal rules on buying farmland</b> depend on your situation and can change. Before you buy, check the land documents and your eligibility with an independent lawyer.</li>'
 '<li><b>Images</b> may be illustrative or artist\'s impressions.</li>'
 '<li><b>Third-party content</b> linked from this site is not controlled by us.</li></ul>'
 '<p>For any question, call '+CALL+'.</p></div>')
build(p,t,d,'Disclaimer',body,[webpage(p,t,d),crumbs(p,'Disclaimer')])

# ---------------- 404.html (served with HTTP 404 by w.js) ----------------
body=('<p class="kick">404</p><h1>Page not found</h1>\n<div class="prose">'
 '<p>This page is not available, or the link may have changed.</p>'
 '<p>You can return home, open one of our farmland pages, read the FAQs, or book a site visit. To speak with us, call '+CALL+'.</p></div>'
 '<ul class="links"><li><a href="/">Home</a></li><li><a href="/phase-2/">Phase 2 Plots</a></li><li><a href="/how-to-buy/">How to Buy</a></li><li><a href="/managed-farmland-near-bangalore/">Managed Farmland near Bangalore</a></li><li><a href="/sandalwood-farmland-near-bangalore/">Sandalwood Farmland</a></li><li><a href="/sandalwood-farming/">Sandalwood Farming Guide</a></li><li><a href="/farmland-near-bagepalli/">Farmland near Bagepalli</a></li><li><a href="/managed-farmland-price-bangalore/">Farmland Price</a></li><li><a href="/faq/">FAQs</a></li><li><a href="/contact/">Contact</a></li><li><a href="/#visit">Book a Site Visit</a></li></ul>')
build('404.html','Page not found | Arogya Vana','This page is not available. Visit the Arogya Vana home page, browse our farmland pages, read the FAQs, or book a site visit.','Page not found',body,None,og_img='/og.jpg',robots='noindex,follow',cta=('See the land in person','Book a site visit, or call us. We are happy to help you find the right page.'),canonical=False)
s=open(B+'404.html',encoding='utf-8').read()
s=s.replace('<a href="/404.html" hreflang="en"','<a href="/" hreflang="en"'); open(B+'404.html','w',encoding='utf-8').write(s)

# ---------------- footer links on every page ----------------
NEW_LI='<li><a href="/about/">About Us</a></li><li><a href="/phase-2/">Phase 2 Plots</a></li><li><a href="/how-to-buy/">How to Buy</a></li><li><a href="/contact/">Contact</a></li>'
LEGAL='<span class="flegal"><a href="/privacy-policy/">Privacy Policy</a> · <a href="/terms/">Terms</a> · <a href="/disclaimer/">Disclaimer</a></span>'
for d_,_,fs in os.walk(B):
    for f in fs:
        if not f.endswith('.html'): continue
        path=os.path.join(d_,f); s=open(path,encoding='utf-8').read(); o=s
        if '<h4>Company</h4>' in s:
            s=R(s,'<li><a href="/faq/">All FAQs</a></li>','<li><a href="/faq/">All FAQs</a></li>'+NEW_LI,tag=os.path.relpath(path,B)+' footer: new page links')
        elif '<h4>ಸಂಸ್ಥೆ</h4>' in s or '<h4>సంస్థ</h4>' in s:
            s=RX(s,r'(<h4>(?:ಸಂಸ್ಥೆ|సంస్థ)</h4><ul>.*?<li><a href="/blog/">[^<]*</a></li>)',lambda m:m.group(1)+NEW_LI,tag=os.path.relpath(path,B)+' footer: new page links (English labels)')
        if '<span class="fmotto">' in s:
            s=RX(s,r'(<span class="fmotto">[^<]*</span>)',lambda m:m.group(1)+LEGAL,tag=os.path.relpath(path,B)+' footer: legal links')
        if s!=o: open(path,'w',encoding='utf-8').write(s)

# ---------------- homepage anchor rename (no links point to it) ----------------
for f in ['index.html','kn/index.html','te/index.html']:
    s=open(B+f,encoding='utf-8').read(); s=R(s,'<section class="sec dk" id="profit">','<section class="sec dk" id="plantation">',tag=f+' section anchor #profit -> #plantation'); open(B+f,'w',encoding='utf-8').write(s)

# ---------------- sitemap ----------------
s=open('/workspace/arogyavana-site/drafts/seo/sitemap-after-redirects.xml',encoding='utf-8').read()
s=re.sub(r'<!--.*?-->\n?','',s,flags=re.S)
add=''.join(f'<url><loc>{SITE}/{u}</loc><lastmod>2026-11-15</lastmod><priority>{pr}</priority></url>\n' for u,pr in [('phase-2/','0.9'),('how-to-buy/','0.8'),('about/','0.6'),('contact/','0.6'),('privacy-policy/','0.3'),('terms/','0.3'),('disclaimer/','0.3')])
s=s.replace('</urlset>',add+'</urlset>'); open(B+'sitemap.xml','w',encoding='utf-8').write(s); LOG.append(('sitemap.xml: 17 URLs (new slugs) + 7 new pages, lastmod 2026-11-15','','',1))

# ---------------- llms.txt / llms-full.txt ----------------
for f in ['llms.txt','llms-full.txt']:
    src=open(f'/workspace/arogyavana-site/tools/{f}.src',encoding='utf-8').read()
    open(B+f,'w',encoding='utf-8').write(src); LOG.append((f'/{f}','','',1))
if __name__=='__main__':
    for x in LOG: print(x[0],'|',x[3])
