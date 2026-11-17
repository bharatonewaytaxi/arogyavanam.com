import re,html,json,sys
sys.path.insert(0,'/workspace/arogyavana-site');sys.path.insert(0,'/workspace/arogyavana-site/i18n')
from apply import apply
from tr import TR,OPTS
S=[l.split('\t',1)[1] for l in open('/workspace/strings.txt').read().split('\n')]
SVT={
'kn':dict(kick='ಸ್ಥಳ ಭೇಟಿ',h='ಸ್ಥಳ ಭೇಟಿ ಬುಕ್ ಮಾಡಿ',p='ಆರೋಗ್ಯ ವನವನ್ನು ಖುದ್ದಾಗಿ ನೋಡಲು ದಿನಾಂಕ ಮತ್ತು ಸಮಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ. ನಾವು ಬುಧವಾರದಿಂದ ಸೋಮವಾರದವರೆಗೆ, ಬೆಳಗ್ಗೆ 9 – ಸಂಜೆ 6 ರವರೆಗೆ ತೆರೆದಿರುತ್ತೇವೆ (ಮಂಗಳವಾರ ರಜೆ).',l1='1. ದಿನಾಂಕ ಆಯ್ಕೆಮಾಡಿ',l2='2. ಸಮಯ ಆಯ್ಕೆಮಾಡಿ',l3='3. ನಿಮ್ಮ ವಿವರಗಳು',wk='ವಾರಾಂತ್ಯ',cl='ರಜೆ (ಮಂಗಳವಾರ)',name='ನಿಮ್ಮ ಹೆಸರು *',phone='ಫೋನ್ ಸಂಖ್ಯೆ *',ph1='ನಿಮ್ಮ ಹೆಸರು',ph2='ಫೋನ್ ಸಂಖ್ಯೆ',submit='ಸ್ಥಳ ಭೇಟಿ ಬುಕ್ ಮಾಡಿ',note='ಭೇಟಿಯನ್ನು ದೃಢೀಕರಿಸಲು ಮತ್ತು ದಾರಿ ತಿಳಿಸಲು ನಮ್ಮ ತಂಡ ನಿಮಗೆ ಕರೆ ಮಾಡುತ್ತದೆ.',closed='ರಜೆ',closedS='ರಜೆ',weekend='ವಾರಾಂತ್ಯ',eName='ದಯವಿಟ್ಟು ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.',ePhone='ದಯವಿಟ್ಟು ನಿಮ್ಮ ಫೋನ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.',ePhone2='ದಯವಿಟ್ಟು ಮಾನ್ಯ ಫೋನ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ (ಕನಿಷ್ಠ 10 ಅಂಕಿಗಳು).',eDate='ದಯವಿಟ್ಟು ದಿನಾಂಕ ಆಯ್ಕೆಮಾಡಿ.',eSlot='ದಯವಿಟ್ಟು ಸಮಯ ಆಯ್ಕೆಮಾಡಿ.',sending='ಬುಕ್ ಮಾಡಲಾಗುತ್ತಿದೆ…',fail='ಭೇಟಿ ಬುಕ್ ಮಾಡಲು +91 98866 70006 ಗೆ ಕರೆ ಮಾಡಿ.'),
'te':dict(kick='సైట్ విజిట్',h='సైట్ విజిట్ బుక్ చేయండి',p='ఆరోగ్య వనను స్వయంగా చూడటానికి తేదీ మరియు సమయం ఎంచుకోండి. మేము బుధవారం నుండి సోమవారం వరకు, ఉదయం 9 – సాయంత్రం 6 వరకు తెరిచి ఉంటాం (మంగళవారం సెలవు).',l1='1. తేదీ ఎంచుకోండి',l2='2. సమయం ఎంచుకోండి',l3='3. మీ వివరాలు',wk='వారాంతం',cl='సెలవు (మంగళవారం)',name='మీ పేరు *',phone='ఫోన్ నంబర్ *',ph1='మీ పేరు',ph2='ఫోన్ నంబర్',submit='సైట్ విజిట్ బుక్ చేయండి',note='విజిట్‌ను నిర్ధారించడానికి మరియు దారి వివరాలు తెలియజేయడానికి మా బృందం మీకు కాల్ చేస్తుంది.',closed='సెలవు',closedS='సెలవు',weekend='వారాంతం',eName='దయచేసి మీ పేరు నమోదు చేయండి.',ePhone='దయచేసి మీ ఫోన్ నంబర్ నమోదు చేయండి.',ePhone2='దయచేసి సరైన ఫోన్ నంబర్ నమోదు చేయండి (కనీసం 10 అంకెలు).',eDate='దయచేసి తేదీ ఎంచుకోండి.',eSlot='దయచేసి సమయం ఎంచుకోండి.',sending='బుక్ చేస్తోంది…',fail='విజిట్ బుక్ చేయడానికి +91 98866 70006కు కాల్ చేయండి.')}
L={'kn':dict(langlabel='ಭಾಷೆ',svnav='ಸ್ಥಳ ಭೇಟಿ',svcta='ಸ್ಥಳ ಭೇಟಿ ಬುಕ್ ಮಾಡಿ',svmob='ಭೇಟಿ ಬುಕ್'),'te':dict(langlabel='భాష',svnav='సైట్ విజిట్',svcta='సైట్ విజిట్ బుక్ చేయండి',svmob='విజిట్ బుక్')}
META={'kn':dict(title='ಆರೋಗ್ಯ ವನ | ಹಂತ 3 ಈಗ ಆರಂಭ – ಬೆಂಗಳೂರಿನ ಬಳಿ ನಿರ್ವಹಿತ ಶ್ರೀಗಂಧ ಕೃಷಿಭೂಮಿ – ಸಪ್ತ ವೆಂಚರ್ಸ್',desc='ಆರೋಗ್ಯ ವನ ಹಂತ 3 – ಸಪ್ತ ವೆಂಚರ್ಸ್‌ನ ಹೊಸ ಯೋಜನೆ. ಕರ್ನಾಟಕ–ಆಂಧ್ರಪ್ರದೇಶ ಗಡಿಯಲ್ಲಿ, ಬೆಂಗಳೂರಿನಿಂದ ಸುಮಾರು 2 ಗಂಟೆ ದೂರದ ನಿರ್ವಹಿತ ಶ್ರೀಗಂಧ ಕೃಷಿಭೂಮಿ. ಹಂತ 1 ಸಂಪೂರ್ಣ ಮಾರಾಟ, ಹಂತ 2 75% ಮಾರಾಟ. 4400 sq.ft ನಿವೇಶನ – ₹25 ಲಕ್ಷ ಯೋಜನೆ (₹15L ಭೂಮಿ + ₹10L ಹೂಡಿಕೆ).',loc='kn_IN'),
'te':dict(title='ఆరోగ్య వన | ఫేజ్ 3 ఇప్పుడు ప్రారంభం – బెంగళూరు సమీపంలో మేనేజ్డ్ శ్రీగంధం వ్యవసాయ భూమి – సప్త వెంచర్స్',desc='ఆరోగ్య వన ఫేజ్ 3 – సప్త వెంచర్స్ కొత్త లాంచ్. కర్ణాటక–ఆంధ్రప్రదేశ్ సరిహద్దులో, బెంగళూరు నుండి సుమారు 2 గంటల దూరంలో మేనేజ్డ్ శ్రీగంధం వ్యవసాయ భూమి. ఫేజ్ 1 పూర్తిగా అమ్ముడైంది, ఫేజ్ 2 75% అమ్ముడైంది. 4400 sq.ft ప్లాట్లు – ₹25 లక్షల ప్లాన్ (₹15L భూమి + ₹10L పెట్టుబడి).',loc='te_IN')}
JS={'kn':[("'Sending…'","'ಕಳುಹಿಸಲಾಗುತ್ತಿದೆ…'"),("b.textContent='Register Interest'","b.textContent='ಆಸಕ್ತಿ ನೋಂದಾಯಿಸಿ'"),("'Please enter your name.'","'ದಯವಿಟ್ಟು ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.'"),("'Please enter your phone number.'","'ದಯವಿಟ್ಟು ನಿಮ್ಮ ಫೋನ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.'"),("'Please enter a valid phone number (at least 10 digits).'","'ದಯವಿಟ್ಟು ಮಾನ್ಯ ಫೋನ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ (ಕನಿಷ್ಠ 10 ಅಂಕಿಗಳು).'"),("'Please enter a valid email address.'","'ದಯವಿಟ್ಟು ಮಾನ್ಯ ಇಮೇಲ್ ವಿಳಾಸವನ್ನು ನಮೂದಿಸಿ.'"),("'Request the Brochure'","'ಬ್ರೋಷರ್ ವಿನಂತಿಸಿ'"),("'Could not send'","'ಕಳುಹಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ'"),("'. You can also <a","'. ನೀವು <a"),("WhatsApp us</a> or call +91 98866 70006.","ವಾಟ್ಸಾಪ್ ಮಾಡಬಹುದು</a> ಅಥವಾ +91 98866 70006 ಗೆ ಕರೆ ಮಾಡಬಹುದು."),("' / month'","' /ತಿಂ'") ,("' /mo'","' /ತಿಂ'"),("'Close menu':'Open menu'","'ಮೆನು ಮುಚ್ಚಿ':'ಮೆನು ತೆರೆಯಿರಿ'")],
'te':[("'Sending…'","'పంపుతోంది…'"),("b.textContent='Register Interest'","b.textContent='ఆసక్తి నమోదు చేయండి'"),("'Please enter your name.'","'దయచేసి మీ పేరు నమోదు చేయండి.'"),("'Please enter your phone number.'","'దయచేసి మీ ఫోన్ నంబర్ నమోదు చేయండి.'"),("'Please enter a valid phone number (at least 10 digits).'","'దయచేసి సరైన ఫోన్ నంబర్ నమోదు చేయండి (కనీసం 10 అంకెలు).'"),("'Please enter a valid email address.'","'దయచేసి సరైన ఇమెయిల్ చిరునామా నమోదు చేయండి.'"),("'Request the Brochure'","'బ్రోచర్ కోసం అభ్యర్థించండి'"),("'Could not send'","'పంపడం సాధ్యం కాలేదు'"),("'. You can also <a","'. మీరు <a"),("WhatsApp us</a> or call +91 98866 70006.","వాట్సాప్ చేయవచ్చు</a> లేదా +91 98866 70006కు కాల్ చేయవచ్చు."),("' /mo'","' /నెల'"),("'Close menu':'Open menu'","'మెనూ మూసివేయండి':'మెనూ తెరవండి'")]}
FONT='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+{f}:wght@400;500;600;700&display=swap" media="print" onload="this.media=\'all\'">'
for lg,ix in (('kn',0),('te',1)):
  s=apply(open('/workspace/arogyavana-site/index-v10.html').read(),SVT[lg],lg,L[lg])
  head,body=s[:s.index('<body')],s[s.index('<body'):]
  pairs=[(S[i],v[ix]) for i,v in TR.items()]
  pairs.sort(key=lambda p:-len(p[0]))
  miss=[]
  for en,tr in pairs:
    if en.startswith('@'):
      e=html.escape(en[1:]);t=html.escape(tr[1:])
      n=0
      for a in('alt','aria-label','placeholder','title'):
        pat=f'{a}="{e}"'
        if pat in body:body=body.replace(pat,f'{a}="{t}"');n+=1
        pat2=f'{a}="{en[1:]}"'
        if pat2!=pat and pat2 in body:body=body.replace(pat2,f'{a}="{t}"');n+=1
      if not n:miss.append(en)
    else:
      cnt=0
      for e in {html.escape(en,quote=False),en}:
        rx=re.compile(r'>(\s*)'+re.escape(e)+r'(\s*)<')
        body,k=rx.subn(lambda m:'>'+m.group(1)+html.escape(tr,quote=False)+m.group(2)+'<',body);cnt+=k
      if not cnt:miss.append(en)
  for i,v in OPTS.items():
    e=html.escape(S[i],quote=False);body=body.replace(f'<option>{e}</option>',f'<option value="{html.escape(S[i])}">{html.escape(v[ix],quote=False)}</option>')
  for a,b in JS[lg]:
    if a in body:body=body.replace(a,b)
  # Telugu 'mo' handled; kn
  M=META[lg]
  head=re.sub(r'<html lang="en"',f'<html lang="{lg}"',head)
  head=re.sub(r'<title>.*?</title>',f'<title>{M["title"]}</title>',head)
  head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{M["desc"]}">',head)
  head=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{M["title"]}">',head)
  head=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{M["desc"]}">',head)
  head=re.sub(r'<meta name="twitter:title" content="[^"]*">',f'<meta name="twitter:title" content="{M["title"]}">',head)
  head=head.replace('<meta property="og:locale" content="en_IN">',f'<meta property="og:locale" content="{M["loc"]}">')
  head=head.replace('<link rel="canonical" href="https://arogyavana.com/">',f'<link rel="canonical" href="https://arogyavana.com/{lg}/">').replace('<meta property="og:url" content="https://arogyavana.com/">',f'<meta property="og:url" content="https://arogyavana.com/{lg}/">')
  head=head.replace('"url": "https://arogyavana.com/", "name": "Arogya Vana Phase 3 | Managed Farmland by Saptha Ventures (Now Launching)"',f'"url": "https://arogyavana.com/{lg}/", "inLanguage": "{lg}-IN", "name": "{M["title"]}"')
  if lg=='kn':head=head.replace('<noscript>',FONT.format(f='Kannada' if lg=='kn' else 'Telugu')+'<noscript>',1)
  fam='"Noto Sans Kannada"' if lg=='kn' else '"Noto Sans Telugu"'
  head=head.replace('font-family:Manrope,',f'font-family:Manrope,{fam},',1)
  head=head.replace('</style>',f'\nh1,h2,h3{{line-height:1.3}}.kick,.tag{{letter-spacing:.04em!important}}\n</style>',1)
  # fix page-level links that point to anchors: fine. skip-link etc.
  out=head+body
  out=out.replace('<a class="btn ln" href="https://www.sapthaventures.com/investing_in_managed_farmland_financial_environmental_benefits_by_saptha_ventures.php" target="_blank" rel="noopener">','<a class="btn ln" href="/blog/managed-farmland-benefits/">').replace('<li><a href="https://www.sapthaventures.com" target="_blank" rel="noopener">www.sapthaventures.com</a></li>','<li><a href="/blog/">'+{'kn':'ಬ್ಲಾಗ್','te':'బ్లాగ్'}[lg]+'</a></li>')
  import os;os.makedirs(f'/workspace/arogyavana-site/dist/{lg}',exist_ok=True)
  open(f'/workspace/arogyavana-site/dist/{lg}/index.html','w').write(out)
  print(lg,len(out),'missing:',miss)
