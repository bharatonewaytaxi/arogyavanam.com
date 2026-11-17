import sys,re; sys.path.insert(0,'/workspace/arogyavana-site/tools')
from common import *
B='/workspace/arogyavana-site/new/'
HOME='<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 20h18M5 20V9l7-5 7 5v11M9 20v-6h6v6"/></svg>'
TAG='<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12V4h8l10 10-8 8z"/><path d="M8 8h.01"/></svg>'
for f in ['index.html','kn/index.html','te/index.html']:
  s=open(B+f).read()
  m=re.search(r'<li><b>4,400 sq.ft</b><span>([^<]*)</span></li><li><b>₹299</b><span>([^<]*)</span></li>',s)
  size,rate=m.group(1),m.group(2)
  tiles=f'<div>{HOME}<b>4,400 sq.ft</b><span>{size}</span></div>\n<div>{TAG}<b>₹299</b><span>{rate}</span></div>\n'
  s=R(s,'<div class="hl rv">\n','<div class="hl rv">\n'+tiles,tag=f'{f}: highlights grid gets Phase 2 size + rate tiles (fills slots left by removed 70%/100% tiles)')
  open(B+f,'w').write(s)
for t in LOG: print(t[0],t[3])
