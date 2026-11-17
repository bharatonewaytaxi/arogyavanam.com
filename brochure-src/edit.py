import sys; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from common import *
s=open('b.orig.html').read()
pairs=[("Live naturally. Invest wisely. Grow together.","Live naturally. Grow together."),
("<div><b>4400 sq.ft</b><span>Plot sizes start from</span></div><div><b>₹25 Lakh</b><span>Total plan per plot</span></div>","<div><b>4,400 sq.ft</b><span>Phase 2 plot size</span></div><div><b>₹299</b><span>Per sq ft · Phase 2</span></div>"),
("<h2>Health, nature &amp; long-term wealth</h2>","<h2>Health &amp; nature</h2>"),
("designed for those who value health, nature, and long-term wealth. Own your land, we take care of everything – you enjoy the returns.","designed for those who value health and nature. We take care of everything – you enjoy the land."),
("Why invest in Arogya Vana?","Why Arogya Vana?"),
("<li>High appreciation potential due to proposed SEZ</li>","<li>Close to the proposed SEZ</li>"),
("<li>White Sandalwood Plantation with long-term high returns</li>","<li>Managed white sandalwood plantation</li>"),
("<li>Seasonal fruits and vegetables for additional income</li>","<li>Seasonal fruits and vegetables</li>"),
("<li>Ideal for weekend homes, retirement living, and future wealth</li>","<li>Ideal for weekend homes and retirement living</li>"),
('<span>Investment Plan</span></div>','<span>Plots</span></div>'),
("<h2 style=\"font-size:17pt;margin-top:1mm\">Call or WhatsApp us</h2><span class=\"ph2\">+91 98866 70006</span><span class=\"ph2\">+91 99000 92996</span>","<h2 style=\"font-size:17pt;margin-top:1mm\">Call us</h2><span class=\"ph2\">+91 70909 05031</span>"),
("*Terms apply. Returns are as per the agreement. Some amenity","*Terms apply. Some amenity"),
]
for a,b in pairs: s=R(s,a,b,tag='brochure')
newblock=('<span class="k">Plots</span><h2>Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft</h2><p class="mut">Phase 1 is sold out. Phase 3 is now launching; the Phase 3 price will be shared once it\'s announced. Our farm team manages the plantation. Visit to see the land, the plantation and the clubhouse.</p>\n'
 '<div style="margin-top:8mm"><div class="dist" style="grid-template-columns:repeat(3,1fr)"><div><b>4,400 sq.ft</b><span>Phase 2 plot size</span></div><div><b>₹299</b><span>Per sq ft · Phase 2</span></div><div><b>2 Yrs*</b><span>Free maintenance</span></div></div></div>\n')
i=s.index('<span class="k">Investment Plan</span>'); j=s.index('<div class="two" style="margin-top:2mm">',i)
s=s[:i]+newblock+s[j:]
open('b.html','w').write(s)
for t in LOG: print(t[0],t[3])
