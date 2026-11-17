import re,html,json,math
src=open('/tmp/art.html',errors='ignore').read()
i=src.find('</h3>',src.find('16 oct'))+5;j=src.find('</p>',src.find('Review all relevant documents before investing.'))+4
body=src[i:j]
body=re.sub(r'<h4>(\d+\. [^<]*)</h4>',r'<h3>\1</h3>',body)
body=re.sub(r'<h4>([^<]*)</h4>',lambda m:'<h2 id="%s">%s</h2>'%(re.sub(r'[^a-z]+','-',m.group(1).lower()).strip('-'),m.group(1)),body)
body=body.replace("&","&amp;").replace("&amp;amp;","&amp;")
# light edits
EDITS=[("At Saptha Ventures, we recognise","At Arogya Vana by Saptha Ventures, we recognise"),
("How Saptha Ventures Approaches Managed Farmland","How Arogya Vana by Saptha Ventures Approaches Managed Farmland"),
("At Saptha Ventures, managed farmland can be explored","At Arogya Vana by Saptha Ventures, managed farmland can be explored"),
("For details about available projects, land specifications, and management services, contact Saptha Ventures directly and review the relevant documentation before making an investment decision.","For details about Arogya Vana Phase 3, land specifications, and management services, contact our team directly and review the relevant documentation before making an investment decision."),
("At Saptha Ventures, informed decision-making","At Arogya Vana by Saptha Ventures, informed decision-making"),
("How can I learn more about managed farmland from Saptha Ventures?","How can I learn more about managed farmland at Arogya Vana?"),
("Contact Saptha Ventures for project-specific information","Contact the Arogya Vana team on +91 98866 70006 or <a href=\"/#visit\">book a site visit</a> for project-specific information")]
for a,b in EDITS:
  assert a in body,a;body=body.replace(a,b)
body=re.sub(r'\n\s*\n+','\n',body).strip()
# insert our photos
body=body.replace('<h2 id="environmental-benefits-of-managed-farmland"','<figure><img src="/img/sandal-real.webp" alt="Sandalwood plantation at Arogya Vana" width="1100" height="728" loading="lazy" decoding="async"><figcaption>Sandalwood plantation at Arogya Vana.</figcaption></figure>\n<h2 id="environmental-benefits-of-managed-farmland"',1)
words=len(re.sub(r'<[^>]+>',' ',body).split());mins=math.ceil(words/220)
faq=re.findall(r'<h3>\d+\. ([^<]*\?)</h3>\s*<p>(.*?)</p>',body.split('Frequently Asked')[1],re.S)
open('/workspace/arogyavana-site/blog/body.html','w').write(body)
json.dump({'words':words,'mins':mins,'faq':faq},open('/workspace/arogyavana-site/blog/meta.json','w'))
print(words,mins,len(faq),body.count('<h2'),re.findall(r'<h2 id="[^"]*"',body))
