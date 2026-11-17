from seo_lib import *
CALL='<a href="tel:+917090905031">+91 70909 05031</a>'
CSS=('<style>.kf{margin:0 0 1.4em;padding:16px 18px;border:1px solid #e4e2dc;border-left:4px solid #14321f;border-radius:10px;background:#f6f5f0}'
 '.kf .kf-h{font-weight:700;margin:0 0 .5em}.kf ul{margin:0;padding-left:1.1em}.kf li{margin:.2em 0}'
 '.prose .ans{font-size:1.02rem}.rel{font-size:.95rem}.prose figure{margin:1.2em 0}.prose figure img{width:100%;height:auto;border-radius:10px}'
 '.prose figcaption{font-size:.85rem;color:#4b5a50;margin-top:.4em}.prose table{width:100%;border-collapse:collapse;margin:0 0 1.2em}'
 '.prose th,.prose td{border:1px solid #e4e2dc;padding:8px 10px;text-align:left;vertical-align:top}.prose th{background:#f6f5f0}'
 '.tw{overflow-x:auto}.kf a,#for-professionals .c a{text-decoration:underline;text-underline-offset:3px;font-weight:600}</style>')
FACTS=('<aside class="kf" aria-label="Arogya Vana quick facts"><p class="kf-h">Arogya Vana: quick facts</p><ul>'
 '<li><b>What it is:</b> managed farmland plots, an Arogya Vana project by Saptha Ventures. Farmland plots only.</li>'
 '<li><b>Where:</b> near Bagepalli in Chikkaballapur district, on the Karnataka–Andhra Pradesh border, about 15 minutes from NH44.</li>'
 '<li><b>From Bengaluru:</b> about 2 hours by road.</li>'
 '<li><b>On sale now:</b> Phase 2 plots of 4,400 sq ft at ₹299 per sq ft. Phase 1 is sold out.</li>'
 '<li><b>Planted with:</b> white sandalwood, casuarina and seasonal fruits and vegetables, looked after by our farm team.</li>'
 '<li><b>Visit or call:</b> <a href="/#visit">book a Saturday site visit</a> or call '+CALL+'.</li></ul></aside>')
FACT_SENTENCE=('Arogya Vana is a managed farmland project by Saptha Ventures near Bagepalli in Chikkaballapur district, about 2 hours by road from Bengaluru. '
 'Phase 2 plots are 4,400 sq ft at ₹299 per sq ft.')
# link labels (descriptive anchors)
L={
 'core':('/managed-farmland-near-bangalore/','farmland near Bangalore'),
 'it':('/farmland-for-it-professionals-bangalore/','farmland for IT professionals'),
 'wk':('/weekend-farmland-near-bangalore/','weekend farmland near Bangalore'),
 'cm':('/farmland-near-whitefield-electronic-city/','farmland from Whitefield, Electronic City and North Bangalore'),
 'bg':('/farmland-near-bagepalli/','farmland near Bagepalli'),
 'p2':('/phase-2/','4,400 sq ft Phase 2 farm plots'),
 'pr':('/managed-farmland-price-bangalore/','farmland price near Bangalore'),
 'hb':('/how-to-buy/','how to buy farmland near Bangalore'),
 'ct':('/contact/','book a farmland site visit'),
 'fq':('/faq/','farmland FAQs'),
 'sw':('/sandalwood-farmland-near-bangalore/','sandalwood farmland near Bangalore'),
 'sf':('/sandalwood-farming/','sandalwood farming guide'),
 'sg':('/sandalwood-growth-cycle/','how long sandalwood takes to grow'),
 'vg':('/farmland-vs-gold/','farmland vs gold, apartments and plots'),
 'cmp':('/arogya-vana-vs-other-managed-farmland/','compare managed farmland projects'),
 'ab':('/about/','about Arogya Vana and Saptha Ventures'),
 'nri':('/farmland-for-nris-karnataka/','farmland rules for NRIs'),
 'wmf':('/blog/what-is-managed-farmland/','what is managed farmland'),
}
def links(*keys): return [L[k] for k in keys]
def a(k,text=None): u,t=L[k]; return f'<a href="{u}">{text or t}</a>'
# image library: only existing site images; alt describes what the picture shows
IMG={
 'aerial':('/img/aerial.webp',834,1100),'g8':('/img/g8.webp',1100,825),'g9':('/img/g9.webp',1100,618),
 'g2':('/img/g2.webp',825,1100),'g5':('/img/g5.webp',825,1100),'g1':('/img/g1.webp',825,1100),'g3':('/img/g3.webp',825,1100),
 'highway':('/img/highway.webp',1100,619),'city1':('/img/city1.webp',1100,619),'sandal':('/img/sandal-real.webp',1100,728),
 'managed':('/img/managed.webp',1100,550),'morning':('/img/morning.webp',1100,733),'dawn':('/img/dawn.webp',1100,733),
 'noon':('/img/noon.webp',1100,733),'lepakshi':('/img/lepakshi.webp',1100,613),'sez':('/img/sez.webp',1100,619),
 'kia':('/img/kia.webp',1100,459),'clubhouse':('/img/clubhouse.webp',1100,825),'hero':('/img/hero-real.webp',1536,1024),
}
def F(k,alt,cap=None):
    src,w,h=IMG[k]; return fig(src,alt,w,h,cap)
