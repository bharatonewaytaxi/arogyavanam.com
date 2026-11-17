import json
s=open('/workspace/deploy3.js').read();k='fd.append("w.js",new Blob(['
i=s.index(k)+len(k);_,e=json.JSONDecoder().raw_decode(s[i:])
open('/workspace/deploy3.js','w').write(s[:i]+json.dumps(open('/workspace/arogyavana-site/w.js').read())+s[i+e:])
