import os,sys,json,base64,blake3
def mk(root):
  m={}
  for d,_,fs in os.walk(root):
    for f in fs:
      p=os.path.join(d,f); b=open(p,'rb').read()
      ext=os.path.splitext(f)[1][1:]
      h=blake3.blake3((base64.b64encode(b).decode()+ext).encode()).hexdigest()[:32]
      m['/'+os.path.relpath(p,root)]={'hash':h,'size':len(b)}
  return m
if __name__=='__main__':
  m=mk(sys.argv[1]); json.dump(m,open(sys.argv[2],'w'),sort_keys=True); print(len(m))
