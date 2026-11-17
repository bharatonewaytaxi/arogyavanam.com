import sys; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from common import *
PLACE_OLD="Plots of 4400 sq.ft at ₹25 lakh per plot (₹15 lakh land + ₹10 lakh investment; returns as per agreement, terms apply)."
PLACE_NEW="Phase 1 is sold out. Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft. The Phase 3 price will be shared once it's announced."
def plan_section(kick,h2,p,btn):
    return (f'<section class="sec" id="plan"><div class="wrap"><div class="hd c"><span class="kick">{kick}</span><h2>{h2}</h2><p>{p}</p>'
            f'<p style="margin-top:24px"><a class="btn" href="#visit">{btn}</a></p></div></div></section>')
L={
'en':dict(
 pairs=[
  ("4400 sq.ft plots – ₹25 lakh plan (₹15L land + ₹10L investment).","Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft; the Phase 3 price will be shared once it's announced."),
  ("Phase 3 now launching – ₹25 lakh per 4400 sq.ft plot.","Phase 3 now launching. Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft."),
  ('<a href="#plan">Investment Plan</a>','<a href="#plan">Plots</a>'),
  ("Live naturally. Invest wisely. Grow together.","Live naturally. Grow together."),
  ("<li><b>₹25 Lakh</b><span>Total plan per plot</span></li>","<li><b>₹299</b><span>Per sq ft · Phase 2</span></li>"),
  ("<b>4400 sq.ft</b><span>Plot sizes start from</span>","<b>4,400 sq.ft</b><span>Phase 2 plot size</span>"),
  ("<h2>Health, nature &amp; long-term wealth</h2>","<h2>Health &amp; nature</h2>"),
  ("designed for those who value health, nature, and long-term wealth. Own your land, we take care of everything – you enjoy the returns.","designed for those who value health and nature. We take care of everything – you enjoy the land."),
  ("Why Invest in Arogya Vana?","Why Arogya Vana?"),
  ("<li>High appreciation potential due to proposed SEZ</li>","<li>Close to the proposed SEZ</li>"),
  ("<li>White Sandalwood Plantation with Long term High Returns</li>","<li>Managed White Sandalwood Plantation</li>"),
  ("<li>Seasonal Fruits and Vegetables for additional income</li>","<li>Seasonal Fruits and Vegetables</li>"),
  ("<li>Ideal for weekend homes, retirement living, and future wealth</li>","<li>Ideal for weekend homes and retirement living</li>"),
  ('<span class="kick">Plantation &amp; Returns</span><h2>Your land, growing value</h2>','<span class="kick">Plantation</span><h2>Your land, growing green</h2>'),
  ("Sandalwood offers high-value returns in the long run. Add fruits &amp; vegetables for regular income. We take care","White sandalwood is planted with fruits &amp; vegetables grown alongside. We take care"),
  (" Profit share and produce income subject to terms.</p>","</p>"),
  ("and optimise yield each season.","and care for the plantation each season."),
  ("<h3>Long Term High Returns</h3><p>Sandalwood offers high-value returns in the long run. Add fruits &amp; vegetables for regular income.</p>","<h3>A Managed Plantation</h3><p>White sandalwood, with fruits &amp; vegetables grown alongside.</p>"),
  ("<h3>Safe &amp; Secure Investment</h3>","<h3>Safe &amp; Secure</h3>"),
  ("High Returns from Sandalwood &amp; Other Crops","White Sandalwood &amp; Other Crops"),
  ("<span>Long Term Appreciation</span><span>Passive Income</span>",""),
  ('alt="Investing in Managed Farmland – Saptha Ventures blog"','alt="Managed farmland – Saptha Ventures blog"'),
  ("<h3>Investing in Managed Farmland: Financial &amp; Environmental Benefits</h3><p>Discover the financial and environmental benefits of investing in managed farmland with Saptha Ventures.</p>","<h3>Managed Farmland: Practical &amp; Environmental Benefits</h3><p>What managed farmland involves, its practical and environmental benefits, and what to check before you buy.</p>"),
  ("<p>Call or WhatsApp us, or ","<p>Call us, or "),
  ("<option>5000 sq.ft plot</option>",""),
  ("<option>Farmland investment</option>","<option>Farmland plot</option>"),
  ("<option>Plantation and profit sharing</option>","<option>Plantation</option>"),
  ('<span class="fmotto">Invest in nature. Invest for future. · Own land. We manage. You enjoy.</span>','<span class="fmotto">We manage. You enjoy.</span>'),
 ],
 future_li="Future-Ready Investment",
 plan=plan_section("Plots","Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft","Phase 1 is sold out. Phase 3 is now launching; the Phase 3 price will be shared once it's announced. Our farm team manages the plantation. Visit to see the land, the plantation and the clubhouse.","Book Site Visit"),
 call="Call us on +91 70909 05031", err_also="You can also "),
'kn':dict(
 pairs=[
  ("4400 sq.ft ನಿವೇಶನ – ₹25 ಲಕ್ಷ ಯೋಜನೆ (₹15L ಭೂಮಿ + ₹10L ಹೂಡಿಕೆ).","ಹಂತ 2 ನಿವೇಶನಗಳು 4,400 sq.ft, ಪ್ರತಿ sq.ft ಗೆ ₹299; ಹಂತ 3 ಬೆಲೆ ಘೋಷಣೆಯಾದ ನಂತರ ತಿಳಿಸಲಾಗುತ್ತದೆ."),
  ('<a href="#plan">ಹೂಡಿಕೆ ಯೋಜನೆ</a>','<a href="#plan">ನಿವೇಶನಗಳು</a>'),
  ("ಸಹಜವಾಗಿ ಬದುಕಿ. ಜಾಣ್ಮೆಯಿಂದ ಹೂಡಿಕೆ ಮಾಡಿ. ಒಟ್ಟಿಗೆ ಬೆಳೆಯಿರಿ.","ಸಹಜವಾಗಿ ಬದುಕಿ. ಒಟ್ಟಿಗೆ ಬೆಳೆಯಿರಿ."),
  ("<li><b>₹25 ಲಕ್ಷ</b><span>ಪ್ರತಿ ನಿವೇಶನಕ್ಕೆ ಒಟ್ಟು ಯೋಜನೆ</span></li>","<li><b>₹299</b><span>ಪ್ರತಿ sq.ft · ಹಂತ 2</span></li>"),
  ("<b>4400 sq.ft</b><span>ನಿವೇಶನದ ಗಾತ್ರ ಇಲ್ಲಿಂದ ಆರಂಭ</span>","<b>4,400 sq.ft</b><span>ಹಂತ 2 ನಿವೇಶನದ ಗಾತ್ರ</span>"),
  ("<h2>ಆರೋಗ್ಯ, ಪ್ರಕೃತಿ ಮತ್ತು ದೀರ್ಘಕಾಲೀನ ಸಂಪತ್ತು</h2>","<h2>ಆರೋಗ್ಯ ಮತ್ತು ಪ್ರಕೃತಿ</h2>"),
  ("ಆರೋಗ್ಯ, ಪ್ರಕೃತಿ ಮತ್ತು ದೀರ್ಘಕಾಲೀನ ಸಂಪತ್ತನ್ನು ಮೌಲ್ಯೀಕರಿಸುವವರಿಗಾಗಿ","ಆರೋಗ್ಯ ಮತ್ತು ಪ್ರಕೃತಿಯನ್ನು ಮೌಲ್ಯೀಕರಿಸುವವರಿಗಾಗಿ"),
  ("ಭೂಮಿ ನಿಮ್ಮದು, ಎಲ್ಲವನ್ನೂ ನಾವು ನೋಡಿಕೊಳ್ಳುತ್ತೇವೆ – ಲಾಭ ನೀವು ಆನಂದಿಸಿ.","ಎಲ್ಲವನ್ನೂ ನಾವು ನೋಡಿಕೊಳ್ಳುತ್ತೇವೆ – ಭೂಮಿಯನ್ನು ನೀವು ಆನಂದಿಸಿ."),
  ("ಆರೋಗ್ಯ ವನದಲ್ಲಿ ಏಕೆ ಹೂಡಿಕೆ ಮಾಡಬೇಕು?","ಆರೋಗ್ಯ ವನ ಏಕೆ?"),
  ("<li>ಪ್ರಸ್ತಾವಿತ SEZ ಕಾರಣ ಹೆಚ್ಚಿನ ಮೌಲ್ಯವೃದ್ಧಿ ಸಾಧ್ಯತೆ</li>","<li>ಪ್ರಸ್ತಾವಿತ SEZ ಸಮೀಪ</li>"),
  ("<li>ದೀರ್ಘಕಾಲೀನ ಹೆಚ್ಚಿನ ಲಾಭದೊಂದಿಗೆ ಬಿಳಿ ಶ್ರೀಗಂಧ ತೋಟ</li>","<li>ನಿರ್ವಹಿತ ಬಿಳಿ ಶ್ರೀಗಂಧ ತೋಟ</li>"),
  ("<li>ಹೆಚ್ಚುವರಿ ಆದಾಯಕ್ಕಾಗಿ ಕಾಲೋಚಿತ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳು</li>","<li>ಕಾಲೋಚಿತ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳು</li>"),
  ('<span class="kick">ತೋಟ ಮತ್ತು ಆದಾಯ</span><h2>ನಿಮ್ಮ ಭೂಮಿ, ಬೆಳೆಯುತ್ತಿರುವ ಮೌಲ್ಯ</h2>','<span class="kick">ತೋಟ</span><h2>ನಿಮ್ಮ ಭೂಮಿ, ಬೆಳೆಯುತ್ತಿರುವ ಹಸಿರು</h2>'),
  ("ಶ್ರೀಗಂಧವು ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಹೆಚ್ಚಿನ ಮೌಲ್ಯದ ಆದಾಯ ನೀಡುತ್ತದೆ. ನಿಯಮಿತ ಆದಾಯಕ್ಕಾಗಿ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳನ್ನು ಸೇರಿಸಿ. ತೋಟ,","ತೋಟದಲ್ಲಿ ಬಿಳಿ ಶ್ರೀಗಂಧ, ಜೊತೆಗೆ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳನ್ನು ನೆಡಲಾಗುತ್ತದೆ. ತೋಟ,"),
  (" ಲಾಭದ ಪಾಲು ಮತ್ತು ಉತ್ಪನ್ನ ಆದಾಯ ನಿಯಮಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ.</p>","</p>"),
  ("ಮತ್ತು ಪ್ರತಿ ಋತುವಿನಲ್ಲಿ ಇಳುವರಿ ಉತ್ತಮಗೊಳಿಸುತ್ತಾರೆ.","ಮತ್ತು ಪ್ರತಿ ಋತುವಿನಲ್ಲಿ ತೋಟವನ್ನು ಆರೈಕೆ ಮಾಡುತ್ತಾರೆ."),
  ("<h3>ದೀರ್ಘಕಾಲೀನ ಹೆಚ್ಚಿನ ಆದಾಯ</h3><p>ಶ್ರೀಗಂಧವು ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಹೆಚ್ಚಿನ ಮೌಲ್ಯದ ಆದಾಯ ನೀಡುತ್ತದೆ. ನಿಯಮಿತ ಆದಾಯಕ್ಕಾಗಿ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳನ್ನು ಸೇರಿಸಿ.</p>","<h3>ನಿರ್ವಹಿತ ತೋಟ</h3><p>ಬಿಳಿ ಶ್ರೀಗಂಧ, ಜೊತೆಗೆ ಹಣ್ಣು ಮತ್ತು ತರಕಾರಿಗಳು.</p>"),
  ("<h3>ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ</h3>","<h3>ಸುರಕ್ಷಿತ ಮತ್ತು ಭದ್ರ</h3>"),
  ("ಶ್ರೀಗಂಧ ಮತ್ತು ಇತರ ಬೆಳೆಗಳಿಂದ ಹೆಚ್ಚಿನ ಆದಾಯ","ಬಿಳಿ ಶ್ರೀಗಂಧ ಮತ್ತು ಇತರ ಬೆಳೆಗಳು"),
  ("<span>ದೀರ್ಘಕಾಲೀನ ಮೌಲ್ಯವೃದ್ಧಿ</span><span>ನಿಷ್ಕ್ರಿಯ ಆದಾಯ</span>",""),
  ('alt="ನಿರ್ವಹಿತ ಕೃಷಿಭೂಮಿಯಲ್ಲಿ ಹೂಡಿಕೆ – ಸಪ್ತ ವೆಂಚರ್ಸ್ ಬ್ಲಾಗ್"','alt="ನಿರ್ವಹಿತ ಕೃಷಿಭೂಮಿ – ಸಪ್ತ ವೆಂಚರ್ಸ್ ಬ್ಲಾಗ್"'),
  ("<h3>ನಿರ್ವಹಿತ ಕೃಷಿಭೂಮಿಯಲ್ಲಿ ಹೂಡಿಕೆ: ಆರ್ಥಿಕ ಮತ್ತು ಪರಿಸರ ಪ್ರಯೋಜನಗಳು (ಲೇಖನ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿದೆ)</h3><p>ಸಪ್ತ ವೆಂಚರ್ಸ್‌ನೊಂದಿಗೆ ನಿರ್ವಹಿತ ಕೃಷಿಭೂಮಿಯಲ್ಲಿ ಹೂಡಿಕೆಯ ಆರ್ಥಿಕ ಮತ್ತು ಪರಿಸರ ಪ್ರಯೋಜನಗಳನ್ನು ತಿಳಿಯಿರಿ.</p>","<h3>ನಿರ್ವಹಿತ ಕೃಷಿಭೂಮಿ: ಪ್ರಾಯೋಗಿಕ ಮತ್ತು ಪರಿಸರ ಪ್ರಯೋಜನಗಳು (ಲೇಖನ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿದೆ)</h3><p>ನಿರ್ವಹಿತ ಕೃಷಿಭೂಮಿಯ ಪ್ರಾಯೋಗಿಕ ಮತ್ತು ಪರಿಸರ ಪ್ರಯೋಜನಗಳು, ಮತ್ತು ಖರೀದಿಸುವ ಮೊದಲು ಏನು ಪರಿಶೀಲಿಸಬೇಕು ಎಂದು ತಿಳಿಯಿರಿ.</p>"),
  ("<p>ಕರೆ ಅಥವಾ ವಾಟ್ಸಾಪ್ ಮಾಡಿ, ಅಥವಾ ","<p>ಕರೆ ಮಾಡಿ, ಅಥವಾ "),
  ('<option value="5000 sq.ft plot">5000 sq.ft ನಿವೇಶನ</option>',""),
  ('<option value="Farmland investment">ಕೃಷಿಭೂಮಿ ಹೂಡಿಕೆ</option>','<option value="Farmland plot">ಕೃಷಿಭೂಮಿ ನಿವೇಶನ</option>'),
  ('<option value="Plantation and profit sharing">ತೋಟ ಮತ್ತು ಲಾಭ ಹಂಚಿಕೆ</option>','<option value="Plantation">ತೋಟ</option>'),
  ('<span class="fmotto">ಪ್ರಕೃತಿಯಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡಿ. ಭವಿಷ್ಯಕ್ಕಾಗಿ ಹೂಡಿಕೆ ಮಾಡಿ. · ಭೂಮಿ ನಿಮ್ಮದು. ನಿರ್ವಹಣೆ ನಮ್ಮದು. ಆನಂದ ನಿಮ್ಮದು.</span>','<span class="fmotto">ನಿರ್ವಹಣೆ ನಮ್ಮದು. ಆನಂದ ನಿಮ್ಮದು.</span>'),
 ],
 future_li="ಭವಿಷ್ಯಕ್ಕೆ ಸಿದ್ಧ ಹೂಡಿಕೆ",
 plan=plan_section("ನಿವೇಶನಗಳು","ಹಂತ 2 ನಿವೇಶನಗಳು 4,400 sq.ft, ಪ್ರತಿ sq.ft ಗೆ ₹299","ಹಂತ 1 ಸಂಪೂರ್ಣ ಮಾರಾಟವಾಗಿದೆ. ಹಂತ 3 ಈಗ ಆರಂಭ; ಹಂತ 3 ಬೆಲೆ ಘೋಷಣೆಯಾದ ನಂತರ ತಿಳಿಸಲಾಗುತ್ತದೆ. ತೋಟವನ್ನು ನಮ್ಮ ತಂಡ ನೋಡಿಕೊಳ್ಳುತ್ತದೆ. ಭೂಮಿ, ತೋಟ ಮತ್ತು ಕ್ಲಬ್‌ಹೌಸ್ ನೋಡಲು ಭೇಟಿ ಬುಕ್ ಮಾಡಿ.","ಸ್ಥಳ ಭೇಟಿ ಬುಕ್ ಮಾಡಿ"),
 call="+91 70909 05031 ಗೆ ಕರೆ ಮಾಡಿ"),
'te':dict(
 pairs=[
  ("4400 sq.ft ప్లాట్లు – ₹25 లక్షల ప్లాన్ (₹15L భూమి + ₹10L పెట్టుబడి).","ఫేజ్ 2 ప్లాట్లు 4,400 sq.ft, ఒక sq.ft కు ₹299; ఫేజ్ 3 ధర ప్రకటన అయిన తర్వాత తెలియజేస్తాం."),
  ('<a href="#plan">పెట్టుబడి ప్రణాళిక</a>','<a href="#plan">ప్లాట్లు</a>'),
  ("సహజంగా జీవించండి. తెలివిగా పెట్టుబడి పెట్టండి. కలిసి ఎదగండి.","సహజంగా జీవించండి. కలిసి ఎదగండి."),
  ("<li><b>₹25 లక్షలు</b><span>ప్రతి ప్లాట్‌కు మొత్తం ప్లాన్</span></li>","<li><b>₹299</b><span>ఒక sq.ft కు · ఫేజ్ 2</span></li>"),
  ("<b>4400 sq.ft</b><span>ప్లాట్ పరిమాణం ఇక్కడి నుండి ప్రారంభం</span>","<b>4,400 sq.ft</b><span>ఫేజ్ 2 ప్లాట్ పరిమాణం</span>"),
  ("<h2>ఆరోగ్యం, ప్రకృతి &amp; దీర్ఘకాలిక సంపద</h2>","<h2>ఆరోగ్యం &amp; ప్రకృతి</h2>"),
  ("ఆరోగ్యం, ప్రకృతి మరియు దీర్ఘకాలిక సంపదకు విలువ ఇచ్చేవారి కోసం","ఆరోగ్యం మరియు ప్రకృతికి విలువ ఇచ్చేవారి కోసం"),
  ("భూమి మీది, అన్నీ మేము చూసుకుంటాం – రాబడిని మీరు ఆస్వాదించండి.","అన్నీ మేము చూసుకుంటాం – భూమిని మీరు ఆస్వాదించండి."),
  ("ఆరోగ్య వనలో ఎందుకు పెట్టుబడి పెట్టాలి?","ఆరోగ్య వన ఎందుకు?"),
  ("<li>ప్రతిపాదిత SEZ కారణంగా అధిక విలువ పెరుగుదల అవకాశం</li>","<li>ప్రతిపాదిత SEZ సమీపంలో</li>"),
  ("<li>దీర్ఘకాలిక అధిక రాబడితో తెల్ల శ్రీగంధం తోట</li>","<li>మేనేజ్డ్ తెల్ల శ్రీగంధం తోట</li>"),
  ("<li>అదనపు ఆదాయం కోసం సీజనల్ పండ్లు మరియు కూరగాయలు</li>","<li>సీజనల్ పండ్లు మరియు కూరగాయలు</li>"),
  ("<li>వారాంతపు ఇళ్లు, రిటైర్మెంట్ జీవితం మరియు భవిష్యత్ సంపదకు అనువైనది</li>","<li>వారాంతపు ఇళ్లు మరియు రిటైర్మెంట్ జీవితానికి అనువైనది</li>"),
  ('<span class="kick">తోట &amp; రాబడి</span><h2>మీ భూమి, పెరుగుతున్న విలువ</h2>','<span class="kick">తోట</span><h2>మీ భూమి, పెరుగుతున్న పచ్చదనం</h2>'),
  ("శ్రీగంధం దీర్ఘకాలంలో అధిక విలువైన రాబడి ఇస్తుంది. క్రమమైన ఆదాయం కోసం పండ్లు &amp; కూరగాయలు జోడించండి. తోట పెంపకం,","తోటలో తెల్ల శ్రీగంధంతో పాటు పండ్లు &amp; కూరగాయలు నాటుతాం. తోట పెంపకం,"),
  (" లాభ వాటా మరియు పంట ఆదాయం నిబంధనలకు లోబడి ఉంటాయి.</p>","</p>"),
  ("మరియు ప్రతి సీజన్‌లో దిగుబడిని మెరుగుపరుస్తారు.","మరియు ప్రతి సీజన్‌లో తోటను సంరక్షిస్తారు."),
  ("<h3>దీర్ఘకాలిక అధిక రాబడి</h3><p>శ్రీగంధం దీర్ఘకాలంలో అధిక విలువైన రాబడి ఇస్తుంది. క్రమమైన ఆదాయం కోసం పండ్లు &amp; కూరగాయలు జోడించండి.</p>","<h3>మేనేజ్డ్ తోట</h3><p>తెల్ల శ్రీగంధం, దానితో పాటు పండ్లు &amp; కూరగాయలు.</p>"),
  ("<h3>సురక్షితమైన పెట్టుబడి</h3>","<h3>సురక్షితం &amp; భద్రం</h3>"),
  ("శ్రీగంధం &amp; ఇతర పంటల నుండి అధిక రాబడి","తెల్ల శ్రీగంధం &amp; ఇతర పంటలు"),
  ("<span>దీర్ఘకాలిక విలువ పెరుగుదల</span><span>పాసివ్ ఆదాయం</span>",""),
  ('alt="మేనేజ్డ్ వ్యవసాయ భూమిలో పెట్టుబడి – సప్త వెంచర్స్ బ్లాగ్"','alt="మేనేజ్డ్ వ్యవసాయ భూమి – సప్త వెంచర్స్ బ్లాగ్"'),
  ("<h3>మేనేజ్డ్ వ్యవసాయ భూమిలో పెట్టుబడి: ఆర్థిక &amp; పర్యావరణ ప్రయోజనాలు (వ్యాసం ఆంగ్లంలో ఉంది)</h3><p>సప్త వెంచర్స్‌తో మేనేజ్డ్ వ్యవసాయ భూమిలో పెట్టుబడి వల్ల కలిగే ఆర్థిక మరియు పర్యావరణ ప్రయోజనాలను తెలుసుకోండి.</p>","<h3>మేనేజ్డ్ వ్యవసాయ భూమి: ఆచరణాత్మక &amp; పర్యావరణ ప్రయోజనాలు (వ్యాసం ఆంగ్లంలో ఉంది)</h3><p>మేనేజ్డ్ వ్యవసాయ భూమి ఆచరణాత్మక మరియు పర్యావరణ ప్రయోజనాలు, కొనుగోలుకు ముందు ఏమి చూడాలో తెలుసుకోండి.</p>"),
  ("<p>కాల్ లేదా వాట్సాప్ చేయండి, లేదా ","<p>కాల్ చేయండి, లేదా "),
  ('<option value="5000 sq.ft plot">5000 sq.ft ప్లాట్</option>',""),
  ('<option value="Farmland investment">వ్యవసాయ భూమి పెట్టుబడి</option>','<option value="Farmland plot">వ్యవసాయ భూమి ప్లాట్</option>'),
  ('<option value="Plantation and profit sharing">తోట &amp; లాభ వాటా</option>','<option value="Plantation">తోట</option>'),
  ('<span class="fmotto">ప్రకృతిలో పెట్టుబడి పెట్టండి. భవిష్యత్తు కోసం పెట్టుబడి పెట్టండి. · భూమి మీది. నిర్వహణ మాది. ఆనందం మీది.</span>','<span class="fmotto">నిర్వహణ మాది. ఆనందం మీది.</span>'),
 ],
 future_li="భవిష్యత్తుకు సిద్ధమైన పెట్టుబడి",
 plan=plan_section("ప్లాట్లు","ఫేజ్ 2 ప్లాట్లు 4,400 sq.ft, ఒక sq.ft కు ₹299","ఫేజ్ 1 పూర్తిగా అమ్ముడైంది. ఫేజ్ 3 ఇప్పుడు ప్రారంభం; ఫేజ్ 3 ధర ప్రకటన అయిన తర్వాత తెలియజేస్తాం. తోటను మా బృందం చూసుకుంటుంది. భూమి, తోట మరియు క్లబ్‌హౌస్ చూడడానికి విజిట్ బుక్ చేయండి.","సైట్ విజిట్ బుక్ చేయండి"),
 call="+91 70909 05031కు కాల్ చేయండి"),
}
def edit_home(path,lang):
    s=open(path).read(); d=L[lang]
    for a,b in d['pairs']: s=R(s,a,b,tag=f'{lang} copy')
    s=R(s,PLACE_OLD,PLACE_NEW,tag=f'{lang} JSON-LD Place description')
    # 70% / 100% profit-share stat tiles (highlights + plantation strip)
    s=RX(s,r'<div>(?:<svg class="ic"[^>]*>.*?</svg>)?<b>(?:70|100)<sup>%</sup></b><span>[^<]*</span></div>\n?','',tag=f'{lang} 70%/100% profit-share tiles')
    s=RX(s,r'<li><svg class="ic"(?:(?!<li>).)*?</svg>'+re.escape(d['future_li'])+'</li>','',tag=f'{lang} "future-ready investment" list item')
    # plan section + calculator
    s=cut(s,'<section class="sec" id="plan">','</section>',d['plan'],tag=f'{lang} #plan investment plan + returns calculator -> Phase 2 rate card')
    # calculator JS
    i=s.index("(function(){var n=document.getElementById('cn')"); j=s.index("})})();",i)+len("})})();")
    LOG.append((f'{lang} calculator JS removed',s[i:i+80],'',1)); s=s[:i]+s[j:]
    # wa() helper + error message
    i=s.index("function wa(f){return 'https://wa.me/"); j=s.index("}\n",i)+2
    s=s[:i]+"function wa(f){return '"+NEWTEL+"'}\n"+s[j:]; LOG.append((f'{lang} wa() helper -> tel','function wa','tel',1))
    s=RX(s,r"""<a style="text-decoration:underline" target="_blank" href="'\+wa\(F\)\+'">[^<]*</a> (?:or |ಅಥವಾ |లేదా )""",'',tag=f'{lang} form error WhatsApp link removed')
    s=wa_button(s,d['call'])
    s=phones(s)
    open(path,'w').write(s)
if __name__=='__main__':
    base='/workspace/arogyavana-site/new/'
    edit_home(base+'index.html','en'); edit_home(base+'kn/index.html','kn'); edit_home(base+'te/index.html','te')
    for t in LOG: print(t[0],'|',t[3])
