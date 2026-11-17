import sys; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from common import *
B='/workspace/arogyavana-site/new/'
s=open(B+'thank-you.html').read()
s=R(s,'<a class="btn" id="wa" target="_blank" rel="noopener" href="https://wa.me/919886670006">Chat on WhatsApp</a>',f'<a class="btn" id="wa" href="{NEWTEL}">Call {NEWNUM}</a>',tag='thank-you WhatsApp button -> call')
s=phones(s); open(B+'thank-you.html','w').write(s)
j=open(B+'ty.js').read()
j=R(j,"wa:'Chat on WhatsApp'",f"wa:'Call {NEWNUM}'",tag='ty.js en')
j=R(j,"wa:'ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಚಾಟ್ ಮಾಡಿ'",f"wa:'ಕರೆ ಮಾಡಿ {NEWNUM}'",tag='ty.js kn')
j=R(j,"wa:'వాట్సాప్‌లో చాట్ చేయండి'",f"wa:'కాల్ చేయండి {NEWNUM}'",tag='ty.js te')
j=R(j,"$('wa').href='https://wa.me/919886670006?text='+encodeURIComponent(msg);",f"$('wa').href='{NEWTEL}';",tag='ty.js button href -> tel')
open(B+'ty.js','w').write(j)
for t in LOG: print(t[0],'|',t[3])
