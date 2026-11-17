import sys,json
from playwright.sync_api import sync_playwright
P=sys.argv[1]
JS="""()=>{const out={sw:document.documentElement.scrollWidth,small:[],navlinks:getComputedStyle(document.querySelector('nav ul')).display,burger:!!document.querySelector('.burger'),broken:[...document.images].filter(i=>i.complete&&!i.naturalWidth).length};
document.querySelectorAll('a,button,input,select,textarea,summary').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.height&&getComputedStyle(e).visibility!='hidden'&&r.left>-100&&(r.height<44||r.width<44))out.small.push((e.tagName+' '+(e.textContent||e.name||'').trim().slice(0,25)+' '+Math.round(r.width)+'x'+Math.round(r.height)))});
out.small=[...new Set(out.small)].slice(0,40);return out}"""
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
  for w in [1440,1024,768,390,360]:
    pg=b.new_page(viewport={'width':w,'height':900 if w>=768 else 780})
    pg.add_init_script("new PerformanceObserver(l=>{for(const e of l.getEntries())if(!e.hadRecentInput)window.__cls=(window.__cls||0)+e.value}).observe({type:'layout-shift',buffered:true})")
    pg.goto((sys.argv[2] if len(sys.argv)>2 else 'https://arogyavana.com/')+'?v=%s'%P,wait_until='networkidle');pg.wait_for_timeout(800)
    pg.screenshot(path=f'shots/shot6-{P}-{w}-top.png')
    m=pg.evaluate(JS)
    pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager');document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))")
    for sec in ['plan','contact']:
      pg.evaluate(f"document.getElementById('{sec}').scrollIntoView({{behavior:'instant'}})");pg.wait_for_timeout(700)
      pg.screenshot(path=f'shots/shot6-{P}-{w}-scrolled-{sec}.png')
    pg.evaluate("scrollTo(0,0)");pg.wait_for_timeout(1500)
    pg.screenshot(path=f'shots/shot6-{P}-{w}-full.png',full_page=True)
    m['cls']=pg.evaluate("window.__cls||0")
    print(w,json.dumps(m))
  b.close()
