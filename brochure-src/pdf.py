from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']);pg=b.new_page()
  pg.goto('file:///workspace/arogyavana-site/brochure-src/b.html');pg.wait_for_timeout(800)
  pg.pdf(path='/workspace/arogyavana-site/new/brochure.pdf',format='A4',print_background=True,prefer_css_page_size=True)
