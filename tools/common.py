import re, json
NEWTEL='tel:+917090905031'; NEWNUM='+91 70909 05031'
PHONE_SVG='<svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>'
LOG=[]
def R(s,a,b,n=None,must=True,tag=''):
    c=s.count(a)
    if must: assert c>=1, f'NOT FOUND [{tag}]: {a[:120]}'
    if c: LOG.append((tag,a,b,c if n is None else min(n,c)))
    return s.replace(a,b) if n is None else s.replace(a,b,n)
def RX(s,pat,rep,must=True,tag='',flags=re.S):
    new,c=re.subn(pat,rep,s,flags=flags)
    if must: assert c>=1, f'REGEX NOT FOUND [{tag}]: {pat[:120]}'
    if c: LOG.append((tag,'re:'+pat,rep if isinstance(rep,str) else '<fn>',c))
    return new
def cut(s,start,end_marker,repl='',tag='',include_end=True):
    i=s.index(start); j=s.index(end_marker,i)+(len(end_marker) if include_end else 0)
    LOG.append((tag,s[i:j][:200]+'…',repl[:200],1))
    return s[:i]+repl+s[j:]
def jsonld(s,fn,tag='jsonld'):
    def rep(m):
        obj=json.loads(m.group(1)); old=json.dumps(obj,ensure_ascii=False)
        obj=fn(obj); new=json.dumps(obj,ensure_ascii=False)
        assert '</' not in new
        if new!=old: LOG.append((tag,'JSON-LD block','(rewritten)',1))
        return '<script type="application/ld+json">'+new+'</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>',rep,s,flags=re.S)
def walk(o,f):
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,f) for v in o]
    if isinstance(o,str): return f(o)
    return o
def wa_button(s,label):
    s=RX(s,r'<a class="wa" href="https://wa\.me/[^"]*" target="_blank" rel="noopener" aria-label="[^"]*">(?:<svg.*?</svg>)?</a>',
         f'<a class="wa" href="{NEWTEL}" aria-label="{label}">{PHONE_SVG}</a>',tag='floating WhatsApp button -> call button')
    s=RX(s,r'(\.wa\{[^}]*?)background:#25d366',r'\1background:var(--g)',must=False,tag='floating button colour (WhatsApp green -> brand green)')
    return s
def phones(s):
    # two-number contact blocks -> one
    s=R(s,'<a href="tel:+919886670006">+91 98866 70006</a><br><a href="tel:+919900092996">+91 99000 92996</a>',f'<a href="{NEWTEL}">{NEWNUM}</a>',must=False,tag='footer contact numbers')
    s=R(s,'<a class="big" href="tel:+919886670006">+91 98866 70006</a><a class="big" href="tel:+919900092996">+91 99000 92996</a>',f'<a class="big" href="{NEWTEL}">{NEWNUM}</a>',must=False,tag='contact section numbers')
    s=R(s,'<a href="tel:+919886670006">+91 98866 70006</a> · <a href="tel:+919900092996">+91 99000 92996</a>',f'<a href="{NEWTEL}">{NEWNUM}</a>',must=False,tag='thank-you numbers')
    s=R(s,'tel:+919886670006',NEWTEL,must=False,tag='tel: link')
    s=R(s,'+91 98866 70006',NEWNUM,must=False,tag='phone text')
    s=R(s,'"telephone": ["+91-98866-70006", "+91-99000-92996"]','"telephone": "+91-70909-05031"',must=False,tag='JSON-LD telephone')
    return s
