# arogyavana.com: land-only update, 15 Nov 2026

**Live:** version 28 (5e47dca3-0e86-4aa0-b0c1-b362b774b294), deployment 49b1d832-3f1a-48c4-9afe-a4363ca7675d, serving 100% since 20:04 IST.
The worker script (w.js), its bindings (ASSETS, DB, MAIL), compatibility_date 2026-01-01 and run_worker_first are all unchanged. Only static assets changed.
**Backup:** /workspace/arogyavana-site/backup-20261115-1950 (live assets, asset-manifest.json, worker/w.js, worker/metadata.json). The previous version was 27 (83ebf6ae-1117-4bdf-90e5-fad90fad3272).
**Rollback:** POST /accounts/bfb07c769e147fd51d87a06c884a8dd7/workers/scripts/arogyavana/deployments with
{"strategy":"percentage","versions":[{"version_id":"83ebf6ae-1117-4bdf-90e5-fad90fad3272","percentage":100}]}
**Rebuild:** rm -rf new && cp -r /workspace/arogyavana-site/backup-20261115-1950/assets new && python3 tools/home.py && python3 tools/inner.py && python3 tools/blog.py && python3 tools/ty.py && python3 tools/hl.py && (cd brochure-src && python3 pdf.py)

## Changes on every page
- **Phone:** +91 98866 70006 and +91 99000 92996 (every format, tel:, JSON-LD telephone) are now +91 70909 05031 (tel:+917090905031). Where a page had two numbers, there is now one.
- **WhatsApp:** the floating wa.me button is now a call button (phone icon, tel link). "Call or WhatsApp us" is now "Call us". The CTA WhatsApp buttons are now "Call +91 70909 05031". The new number is never labelled WhatsApp.
- **Navigation and footer:** nav "Investment Plan" is now "Plots". Footer motto: "We manage. You enjoy."
- **Pricing:** the shared ₹25L plan sentence is now: "Phase 2 plots are 4,400 sq.ft at ₹299 per sq ft. Phase 1 is sold out. Phase 3 is now launching; the Phase 3 price will be shared once it's announced."
- **Legal note** now ends "Review all project documents before you decide."

## Pages
- **index.html, kn/index.html, te/index.html** (each kept in its own language)
  - Meta, OG and Place JSON-LD: only the price text changed.
  - Hero stat ₹25L is now ₹299 per sq ft (Phase 2).
  - Wealth, returns and appreciation copy reworded. The 70% profit and 100% fruit-income tiles removed; Phase 2 size and rate tiles added in their place.
  - The #plan section (₹15L + ₹10L, 3% × 30 months) and the returns calculator (HTML and JS) are replaced by a Phase 2 rate card with a Book Site Visit button.
  - Form: the 5000 sq.ft option was removed and options are now "Farmland plot" and "Plantation". The WhatsApp link in the form error message was removed.
  - The profit-share line was removed from the plantation footnote. The blog card was retitled.
- **managed-farmland-price-bangalore:** retitled "Managed Farmland Price near Bangalore | Arogya Vana Phase 2". New phase table (P1 sold out / P2 ₹299 per sq ft / P3 to be announced). Returns, 70% and calculator link removed. FAQ updated.
- **sandalwood-farming-returns** (URL kept): rewritten land-first.
  - Title: "Sandalwood Farming Over Time | A Long-Cycle Crop".
  - H1: "How Sandalwood Grows Over Time".
  - Two-question FAQ.
- **farmland-vs-gold-investment** (URL kept): now "How They Compare". The income row was removed, and the investment wording was removed from the FAQ.
- **sandalwood-farmland-near-bangalore:** 70% profit share removed from the meta, body and FAQ. The returns and wealth sections were reworded.
- **managed-farmland-near-bangalore:** ₹25 Lakh removed from the title. The plan and profit bullets are now Phase 2 pricing. The smallest-plot FAQ was updated.
- **nri-farmland-investment-karnataka** (URL kept): title is now "Farmland for NRIs near Bengaluru | Rules & Options". Investment wording removed.
- **sandalwood-farming:** the returns section was replaced with a farm-team line, and the returns FAQ was removed.
- **arogya-vana-vs-other-managed-farmland:** the Arogya Vana row is now Phase 2 at ₹299 per sq ft. Investment and profit bullets were reworded, and the crop-proceeds bullet was removed. Competitor prices are unchanged.
- **faq:** crop-income question removed; cost answer is now the Phase 2 sentence; the WhatsApp line now says call.
- **farmland-near-bagepalli, weekend-farmhouse-near-bangalore:** only the changes listed under "Changes on every page".
- **blog/managed-farmland-benefits:** fully rewritten.
  - Title: "Managed Farmland: Practical & Environmental Benefits".
  - The financial-returns sections were removed.
  - New FAQ, in both the page copy and the JSON-LD.
- **blog/what-is-managed-farmland:** the income-share bullet, returns paragraph, ₹25L paragraph and returns FAQ were removed.
- **blog/index:** card and JSON-LD headline updated.
- **thank-you.html and ty.js:** the WhatsApp button is now "Call +91 70909 05031" (en/kn/te) pointing to tel:+917090905031. The two numbers became one. The dataLayer events are kept.
- **brochure.pdf:** re-exported from its source (/workspace/bro/b.html, edited copy in brochure-src/b.html).
  - Removed: the ₹25 Lakh plan, ₹15L / ₹10L, 3% / 30 months, profit sharing, returns and "Invest wisely".
  - Page 3 is now "Plots": Phase 2 at ₹299 per sq ft, Phase 1 sold out, Phase 3 price to be announced.
  - New number added; WhatsApp removed. Still 4 pages.

## Held, deliberately unchanged
- **Location wording:** no changes. The location word counts in the old and new HTML are identical.
- **Ownership claims** ("100% Land Ownership", "Land registered in your name", "Clear titles", FAQ "Is the land in my name?"): left as they were. Nothing new was added.
- **"2 Yrs free maintenance":** kept.
- **Pool / play-area amenity JSON-LD:** not removed (it isn't in the approved scope).

## Grep verification (live = new copy, byte-identical for all 99 files)
- **Required terms:** 0 hits, apart from these harmless ones:
  - URL slugs: /sandalwood-farming-returns/, /farmland-vs-gold-investment/, /nri-farmland-investment-karnataka/.
  - The JS keyword `return`, the `id="profit"` anchor, and `passive:true`.
  - Competitor prices on the compare page (₹27.99 lakh, ₹40 lakh, ₹55 lakh).
  - Blog "Share on WhatsApp" share links (these have no number).
- **Kannada and Telugu investment/returns terms, 13,15,600, ₹349, and the brochure text:** 0 hits.
- **JSON-LD:** all 17 blocks parse.

## Raw edit log (change | count)
```
blog/managed-farmland-benefits/index.html <title> | 1
blog/managed-farmland-benefits/index.html og/twitter title | 2
blog/managed-farmland-benefits/index.html meta/og description | 2
blog/managed-farmland-benefits/index.html H1 | 1
blog/managed-farmland-benefits/index.html | 1
blog/managed-farmland-benefits/index.html share links text | 2
blog/managed-farmland-benefits/index.html article body rewritten (land-first) | 1
blog/managed-farmland-benefits/index.html CTA | 1
blog/managed-farmland-benefits/index.html calculator CTA -> call | 1
blog/managed-farmland-benefits/index.html note | 1
blog/managed-farmland-benefits/index.html JSON-LD | 1
blog/managed-farmland-benefits/index.html nav "Investment Plan" -> "Plots" | 3
blog/managed-farmland-benefits/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
blog/what-is-managed-farmland/index.html | 1
blog/what-is-managed-farmland/index.html | 1
blog/what-is-managed-farmland/index.html profit-share bullet | 1
blog/what-is-managed-farmland/index.html returns paragraph | 1
blog/what-is-managed-farmland/index.html purchase price | 1
blog/what-is-managed-farmland/index.html | 1
blog/what-is-managed-farmland/index.html | 1
blog/what-is-managed-farmland/index.html | 1
blog/what-is-managed-farmland/index.html FAQ price | 1
blog/what-is-managed-farmland/index.html FAQ returns removed | 1
blog/what-is-managed-farmland/index.html | 1
blog/what-is-managed-farmland/index.html CTA | 1
blog/what-is-managed-farmland/index.html note | 1
blog/what-is-managed-farmland/index.html JSON-LD | 1
blog/what-is-managed-farmland/index.html nav "Investment Plan" -> "Plots" | 3
blog/what-is-managed-farmland/index.html CTA WhatsApp -> call | 1
blog/what-is-managed-farmland/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
blog/index.html JSON-LD | 1
blog/index.html card title | 2
blog/index.html card text | 1
blog/index.html nav "Investment Plan" -> "Plots" | 3
blog/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
index.html: highlights grid gets Phase 2 size + rate tiles (fills slots left by removed 70%/100% tiles) 1
kn/index.html: highlights grid gets Phase 2 size + rate tiles (fills slots left by removed 70%/100% tiles) 1
te/index.html: highlights grid gets Phase 2 size + rate tiles (fills slots left by removed 70%/100% tiles) 1
en copy | 1
en copy | 1
en copy | 3
en copy | 1
en copy | 1
en copy | 2
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en copy | 1
en JSON-LD Place description | 1
en 70%/100% profit-share tiles | 4
en "future-ready investment" list item | 1
en #plan investment plan + returns calculator -> Phase 2 rate card | 1
en calculator JS removed | 1
en wa() helper -> tel | 1
en form error WhatsApp link removed | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
contact section numbers | 1
tel: link | 3
phone text | 4
JSON-LD telephone | 1
kn copy | 2
kn copy | 3
kn copy | 1
kn copy | 1
kn copy | 2
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn copy | 1
kn JSON-LD Place description | 1
kn 70%/100% profit-share tiles | 4
kn "future-ready investment" list item | 1
kn #plan investment plan + returns calculator -> Phase 2 rate card | 1
kn calculator JS removed | 1
kn wa() helper -> tel | 1
kn form error WhatsApp link removed | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
contact section numbers | 1
tel: link | 3
phone text | 4
JSON-LD telephone | 1
te copy | 2
te copy | 3
te copy | 1
te copy | 1
te copy | 2
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te copy | 1
te JSON-LD Place description | 1
te 70%/100% profit-share tiles | 4
te "future-ready investment" list item | 1
te #plan investment plan + returns calculator -> Phase 2 rate card | 1
te calculator JS removed | 1
te wa() helper -> tel | 1
te form error WhatsApp link removed | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
contact section numbers | 1
tel: link | 3
phone text | 4
JSON-LD telephone | 1
managed-farmland-price-bangalore/index.html <title> | 1
managed-farmland-price-bangalore/index.html og/twitter title | 2
managed-farmland-price-bangalore/index.html meta/og description | 2
managed-farmland-price-bangalore/index.html H1 | 1
managed-farmland-price-bangalore/index.html | 1
managed-farmland-price-bangalore/index.html price table | 1
managed-farmland-price-bangalore/index.html | 1
managed-farmland-price-bangalore/index.html profit-share bullet | 1
managed-farmland-price-bangalore/index.html calculator link | 1
managed-farmland-price-bangalore/index.html visible FAQ | 1
managed-farmland-price-bangalore/index.html JSON-LD | 1
managed-farmland-price-bangalore/index.html nav "Investment Plan" -> "Plots" | 3
managed-farmland-price-bangalore/index.html CTA WhatsApp -> call | 1
managed-farmland-price-bangalore/index.html legal note | 1
managed-farmland-price-bangalore/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
sandalwood-farming-returns/index.html <title> | 1
sandalwood-farming-returns/index.html og/twitter title | 2
sandalwood-farming-returns/index.html meta/og description | 2
sandalwood-farming-returns/index.html breadcrumb | 1
sandalwood-farming-returns/index.html H1 | 1
sandalwood-farming-returns/index.html | 1
sandalwood-farming-returns/index.html | 1
sandalwood-farming-returns/index.html | 1
sandalwood-farming-returns/index.html | 1
sandalwood-farming-returns/index.html profit-share section | 1
sandalwood-farming-returns/index.html "what affects returns" -> growing | 1
sandalwood-farming-returns/index.html | 1
sandalwood-farming-returns/index.html visible FAQ | 1
sandalwood-farming-returns/index.html JSON-LD | 1
sandalwood-farming-returns/index.html nav "Investment Plan" -> "Plots" | 3
sandalwood-farming-returns/index.html CTA WhatsApp -> call | 1
sandalwood-farming-returns/index.html legal note | 1
sandalwood-farming-returns/index.html footer motto | 1
sandalwood-farming-returns/index.html shared ₹25L plan CTA -> Phase 2 rate card | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
farmland-vs-gold-investment/index.html <title> | 1
farmland-vs-gold-investment/index.html og/twitter title | 2
farmland-vs-gold-investment/index.html meta/og description | 2
farmland-vs-gold-investment/index.html H1 | 1
farmland-vs-gold-investment/index.html table: what you own | 1
farmland-vs-gold-investment/index.html table: income row removed | 1
farmland-vs-gold-investment/index.html | 1
farmland-vs-gold-investment/index.html visible FAQ | 1
farmland-vs-gold-investment/index.html JSON-LD | 1
farmland-vs-gold-investment/index.html nav "Investment Plan" -> "Plots" | 3
farmland-vs-gold-investment/index.html CTA WhatsApp -> call | 1
farmland-vs-gold-investment/index.html legal note | 1
farmland-vs-gold-investment/index.html footer motto | 1
farmland-vs-gold-investment/index.html shared ₹25L plan CTA -> Phase 2 rate card | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
sandalwood-farmland-near-bangalore/index.html meta/og description | 2
sandalwood-farmland-near-bangalore/index.html | 1
sandalwood-farmland-near-bangalore/index.html | 1
sandalwood-farmland-near-bangalore/index.html profit-share section | 1
sandalwood-farmland-near-bangalore/index.html | 1
sandalwood-farmland-near-bangalore/index.html plan block -> Phase 2 rate card | 1
sandalwood-farmland-near-bangalore/index.html visible FAQ | 1
sandalwood-farmland-near-bangalore/index.html JSON-LD | 1
sandalwood-farmland-near-bangalore/index.html nav "Investment Plan" -> "Plots" | 3
sandalwood-farmland-near-bangalore/index.html CTA WhatsApp -> call | 1
sandalwood-farmland-near-bangalore/index.html legal note | 1
sandalwood-farmland-near-bangalore/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
managed-farmland-near-bangalore/index.html <title> | 1
managed-farmland-near-bangalore/index.html og/twitter title | 2
managed-farmland-near-bangalore/index.html plan + profit-share bullets | 1
managed-farmland-near-bangalore/index.html visible FAQ | 1
managed-farmland-near-bangalore/index.html JSON-LD | 1
managed-farmland-near-bangalore/index.html nav "Investment Plan" -> "Plots" | 3
managed-farmland-near-bangalore/index.html CTA WhatsApp -> call | 1
managed-farmland-near-bangalore/index.html legal note | 1
managed-farmland-near-bangalore/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 3
phone text | 2
nri-farmland-investment-karnataka/index.html <title> | 1
nri-farmland-investment-karnataka/index.html og/twitter title | 2
nri-farmland-investment-karnataka/index.html JSON-LD | 1
nri-farmland-investment-karnataka/index.html nav "Investment Plan" -> "Plots" | 3
nri-farmland-investment-karnataka/index.html CTA WhatsApp -> call | 1
nri-farmland-investment-karnataka/index.html legal note | 1
nri-farmland-investment-karnataka/index.html footer motto | 1
nri-farmland-investment-karnataka/index.html shared ₹25L plan CTA -> Phase 2 rate card | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
sandalwood-farming/index.html meta/og description | 2
sandalwood-farming/index.html returns section removed | 1
sandalwood-farming/index.html visible FAQ | 1
sandalwood-farming/index.html JSON-LD | 1
sandalwood-farming/index.html nav "Investment Plan" -> "Plots" | 3
sandalwood-farming/index.html CTA WhatsApp -> call | 1
sandalwood-farming/index.html legal note | 1
sandalwood-farming/index.html footer motto | 1
sandalwood-farming/index.html shared ₹25L plan CTA -> Phase 2 rate card | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
arogya-vana-vs-other-managed-farmland/index.html price row | 1
arogya-vana-vs-other-managed-farmland/index.html investment/profit bullets | 1
arogya-vana-vs-other-managed-farmland/index.html crop-proceeds bullet | 1
arogya-vana-vs-other-managed-farmland/index.html nav "Investment Plan" -> "Plots" | 3
arogya-vana-vs-other-managed-farmland/index.html CTA WhatsApp -> call | 1
arogya-vana-vs-other-managed-farmland/index.html legal note | 1
arogya-vana-vs-other-managed-farmland/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
faq/index.html meta/og description | 2
faq/index.html | 1
faq/index.html visible FAQ | 1
faq/index.html JSON-LD | 1
faq/index.html nav "Investment Plan" -> "Plots" | 3
faq/index.html CTA WhatsApp -> call | 1
faq/index.html legal note | 1
faq/index.html footer motto | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
weekend-farmhouse-near-bangalore/index.html nav "Investment Plan" -> "Plots" | 3
weekend-farmhouse-near-bangalore/index.html CTA WhatsApp -> call | 1
weekend-farmhouse-near-bangalore/index.html legal note | 1
weekend-farmhouse-near-bangalore/index.html footer motto | 1
weekend-farmhouse-near-bangalore/index.html shared ₹25L plan CTA -> Phase 2 rate card | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
farmland-near-bagepalli/index.html nav "Investment Plan" -> "Plots" | 3
farmland-near-bagepalli/index.html CTA WhatsApp -> call | 1
farmland-near-bagepalli/index.html legal note | 1
farmland-near-bagepalli/index.html footer motto | 1
farmland-near-bagepalli/index.html shared ₹25L plan CTA -> Phase 2 rate card | 1
floating WhatsApp button -> call button | 1
floating button colour (WhatsApp green -> brand green) | 1
footer contact numbers | 1
tel: link | 2
phone text | 1
thank-you WhatsApp button -> call | 1
thank-you numbers | 1
ty.js en | 1
ty.js kn | 1
ty.js te | 1
ty.js button href -> tel | 1
```

---

# arogyavana.com: gap-fill pages, 404, 301s, sitemap, llms.txt — 15 Nov 2026 (approved by Karthick in chat: "fix all make it live")

**Live:** version 29 (c8de07f2-1e09-4a8d-a5e3-f57e7e8d4be2), deployment 744177cc-0442-4745-aa45-3b2de190e2b8, 100% since ~20:27 IST.
Bindings (ASSETS, DB, MAIL), compatibility_date 2026-01-01 and run_worker_first unchanged. w.js changed (redirects + 404 branch).
**Backup:** /workspace/arogyavana-site/backup-20261115-2020 (v28 assets verified byte-identical to live, asset-manifest.json, tools/, worker/w.js = v28, worker/version-v28.js, worker/metadata.json). w.js.v29 also saved there.
**Rollback to v28:** POST /accounts/bfb07c769e147fd51d87a06c884a8dd7/workers/scripts/arogyavana/deployments with
{"strategy":"percentage","versions":[{"version_id":"5e47dca3-0e86-4aa0-b0c1-b362b774b294","percentage":100}]}
**Rebuild:** rm -rf new && cp -r backup-20261115-1950/assets new && python3 tools/home.py && python3 tools/inner.py && python3 tools/blog.py && python3 tools/ty.py && python3 tools/hl.py && python3 tools/pages.py && (cd brochure-src && python3 pdf.py)  — then python3 tools/manifest.py new new-manifest.json. Deploy files: deploy/v29/ (session.js, upload.py, version.js).

## Added
- New pages (live header/footer/CSS from inner pages; tools/pages.py): /about/ (AboutPage), /contact/ (ContactPage + Organization contactPoint), /phase-2/ (FAQPage), /how-to-buy/ (outline + AEO FAQ merged, FAQPage, 11 Q&As), /privacy-policy/, /terms/, /disclaimer/.
- /404.html: branded, noindex; w.js serves it with HTTP 404 + x-robots-tag noindex + no-store for unknown GET paths (HTML or extension-less). Kannada block from the draft dropped (not live copy).
- /llms.txt, /llms-full.txt (tools/llms*.txt.src): GEO drafts with the 14-item reviewer header and every [CONFIRM] line removed.
- Footer on every page: About Us, Phase 2 Plots, How to Buy, Contact (Company list; English labels on kn/te), plus Privacy Policy · Terms · Disclaimer in the bottom bar.
- sitemap.xml = sitemap-after-redirects (17) + 7 new pages = 24 URLs, lastmod 2026-11-15.

## Moved (301 in w.js, www + old slug = one hop, query kept)
- /sandalwood-farming-returns(/) → /sandalwood-growth-cycle/
- /farmland-vs-gold-investment(/) → /farmland-vs-gold/
- /nri-farmland-investment-karnataka(/) → /farmland-for-nris-karnataka/
- tools/inner.py: SLUG_MOVES + move_slugs() renames the folders and rewrites canonical/og:url/JSON-LD/sitemap so rebuilds keep the new slugs.

## Other
- Homepage (en/kn/te) section anchor id="profit" → id="plantation" (no links pointed to it).
- No GA4/GTM installed. Privacy page says no advertising or analytics cookies. Note: Cloudflare Web Analytics (cookieless beacon) is injected at the edge on HTML responses — zone setting, not in the assets.

## Left out (await Karthick)
Planting/farm-management inclusion in the price; title/registration in buyer's name; RERA; maintenance term; Phase 3 launching; legal entity/CIN/GST/founders; company track record (projects, acres, years); booking amount and payment schedule; pickup from Bengaluru; map pin; reviews; privacy mailbox, retention period, grievance officer, response time; built amenities (clubhouse, pool, etc.); tree counts/acreage/Phase 2 % sold; WhatsApp; extra emails (sales@/info@sapthaventures.in) on new pages; Telugu/Tamil languages; specific legal statements (Karnataka land-reform rules, FEMA detail, document list, liability/jurisdiction clauses); Kannada 404 copy.
Existing live claims untouched: footer "We manage. You enjoy.", homepage RERA/ownership/"2 Yrs free maintenance", "Phase 3 now launching" lines, brochure download filename Arogya-Vana-Phase-3-Brochure.pdf.

## Verification (live, after deploy)
- 200: all 7 new pages, /llms.txt, /llms-full.txt, /sitemap.xml (24 locs), 3 new slugs, /, /faq/, /brochure.pdf, /robots.txt.
- 301: all 6 old-slug forms → new slashed URLs; ?utm kept; www + old slug → one hop.
- 404: /this-page-does-not-exist → 404, branded page, x-robots-tag noindex, follow, cache-control no-store.
- /api/enquiry still answers (validation error on empty POST).
- Live HTML/XML/TXT = built files byte-for-byte except the edge-injected Cloudflare beacon.
- Grep of live files: 0 hits for 98866, 99000 92996, 349, 13,15,600, returns, payout, yield, profit, [CONFIRM, [REVIEW, Sobha, Prestige.

---

# arogyavana.com: Bengaluru working-professionals refresh — 16 Nov 2026 (Karthick: "implement all", 5:33 AM IST)

**Live:** version 30 (48830974-8ad7-4479-a63c-bfe46267d341), deployment b196b093-335c-4af3-9792-f690c67d88a5, 100% since ~05:50 IST. w.js, bindings, compatibility_date, run_worker_first unchanged from v29.
**Backup:** /workspace/arogyavana-site/backup-20261116-0533 (v29 assets verified identical to live + manifest, tools/, worker/w.js = v29, deploy-v29/).
**Rollback to v29:** POST /accounts/bfb07c769e147fd51d87a06c884a8dd7/workers/scripts/arogyavana/deployments with
{"strategy":"percentage","versions":[{"version_id":"c8de07f2-1e09-4a8d-a5e3-f57e7e8d4be2","percentage":100}]}
**Rebuild:** same chain as v29, then `cp backup-20261116-0533/assets/brochure.pdf new/brochure.pdf && python3 tools/corporate.py` (pdf.py output differs byte-wise each run; keep the live brochure), then python3 tools/manifest.py new new-manifest.json. Deploy files: deploy/v30/.

## Changed
- tools/pages.py: /phase-2/ and /contact/ title, meta, H1, intro for Bengaluru working professionals; /how-to-buy/ "In short" line replaced by "Buying in 5 steps" (enquire, Saturday site visit, documents with your own lawyer, book, registration and handover) + Saturday CTA.
- tools/corporate.py (new, runs after pages.py): homepage title/meta/og/twitter, hero H1 + by-line, hero and mobile-menu "Book a Saturday Site Visit", "Buying in 5 steps" section (#buying-steps) before #visit; every English page with a breadcrumb gets a "Book a Saturday site visit" bar under the breadcrumb and the end CTA button relabelled (blog index gets a new end CTA). All link to the existing /#visit form; no form or script changes.
- kn/te homepages untouched. No "farmhouse"/overnight wording, no visit time slots in new copy.

## Before → after
- / title: "Arogya Vana | Phase 3 Now Launching – Managed Sandalwood Farmland near Bengaluru – A Saptha Ventures Project" → "Weekend Farmland near Bangalore for Working Professionals | Arogya Vana"; H1 "Arogya Vana" → "Your own farmland, about 2 hours from Bengaluru".
- /phase-2/ title: "Arogya Vana Phase 2 | 4,400 sq ft Managed Farmland Plots near Bengaluru" → "Phase 2 Farm Plots near Bangalore for Weekend Visits | Arogya Vana"; H1 "Phase 2: managed farmland plots, about 2 hours from Bengaluru" → "Phase 2: your own farm plot, about 2 hours from Bengaluru".
- /contact/ title: "Contact Arogya Vana | Call +91 70909 05031 | Book a Site Visit" → "Contact Arogya Vana | Book a Saturday Site Visit from Bengaluru"; H1 "Talk to us, or come and see the land" → "Plan a Saturday visit from Bengaluru".
- /how-to-buy/: title/H1 unchanged; 5-step section added.

## Left as is (await Karthick)
Hero tag "Phase 3 · New Launch · Now Registering Interest", Phase 3 badge/CTA headings, "We manage. You enjoy.", RERA/ownership/"2 Yrs free maintenance", brochure filename, "75% sold", existing /weekend-farmhouse-near-bangalore/ page and "weekend homes" bullet.

## Verification (live)
- 200 + byte-identical to build (minus CF beacon) for all 29 HTML/XML/TXT pages; /thank-you.html 307 → /thank-you 200 (CF html_handling, as before).
- 301s: 3 old slugs (slash/no-slash, ?utm kept), www + old slug one hop. 404 page: 404 + noindex.
- /api/enquiry: 400 validation on empty POST (responds). /brochure.pdf 200 same size.
- Grep live: 0 hits for 98866, 99000 92996, 349, 13,15,600, returns, payout, yield, profit, [CONFIRM, Sobha, Prestige.

---

# arogyavana.com: SEO / AEO / GEO pass, 16 Nov 2026 (Karthick: "optimize my website for all keywords ... seo/aeo/geo ... images alt", 5:39 AM IST)

**Live:** version 31 (cb45950b-a728-4ade-95b0-e4fdf776a9cc), deployment a37b497c-3a76-41c7-8f10-7d8352c98582, 100% since ~05:59 IST. w.js, bindings, compatibility_date and run_worker_first are unchanged from v30 (w.js verified identical).
**Backup:** /workspace/arogyavana-site/backup-20261116-0540 (v30 assets verified identical to live: all 30 HTML/XML/TXT files byte-for-byte, and the manifest matches deploy/v30; also asset-manifest.json, tools/, worker/w.js, deploy-v30/).
**Rollback to v30:** POST /accounts/bfb07c769e147fd51d87a06c884a8dd7/workers/scripts/arogyavana/deployments with
{"strategy":"percentage","versions":[{"version_id":"48830974-8ad7-4479-a63c-bfe46267d341","percentage":100}]}
(v29 c8de07f2-1e09-4a8d-a5e3-f57e7e8d4be2 is still available.)
**Rebuild:** use the v30 chain, then `python3 tools/seo.py`, `python3 tools/seo_check.py`, `python3 tools/kwmap.py` and `python3 tools/manifest.py new new-manifest.json`. A quick way to rebuild from the v30 output is `rm -rf new && cp -r backup-20261116-0540/assets new && python3 tools/seo.py`. The new tools are seo.py, seo_lib.py, seo_common.py, seo_pages.py, seo_new.py, seo_check.py and kwmap.py. The deploy files are in deploy/v31/.
**Keyword map:** drafts/seo/keyword-page-map-v2.csv. It has 194 rows: 164 targeted, 12 on hold, 9 skipped and 9 ad negatives. Each page has one primary keyword, and no two pages share one.

## New pages (in the sitemap, llms.txt, llms-full.txt and every footer)
- /farmland-for-it-professionals-bangalore/: the IT and corporate professionals cluster.
- /weekend-farmland-near-bangalore/: the weekend, lifestyle and family cluster. It is land only, with no stay or build wording. The weekend cluster's old target page is the frozen farmhouse page.
- /farmland-near-whitefield-electronic-city/: the tech-corridor and commute cluster (Whitefield, Electronic City, Manyata, Hebbal, Yelahanka, the airport, NH44). It states plainly that the farm is near Bagepalli, and it gives no drive time per neighbourhood.

## Changed (English)
- Every touched page has a keyword-led title, meta description, og/twitter description and og:image:alt, plus answer-first intros.
- **AEO:** question H2s with 40–60 word answers.
- **GEO:** a "quick facts" block on the homepage, /managed-farmland-near-bangalore/, /farmland-near-bagepalli/, /faq/ and /about/.
- Descriptive "Related guides" links and extra existing site photos, all lazy-loaded with width and height set.
- **Pages:**
  - **/ (homepage):** new title and meta, a "For Bengaluru's working professionals" section with the facts block and links, 18 alt texts updated, WebSite JSON-LD, the WebPage name brought in line with the title, and areaServed Bengaluru.
  - **/managed-farmland-near-bangalore/:** new H1 "Farmland near Bangalore, Managed for You", plus project checklist, gated community and audience sections.
  - **/farmland-near-bagepalli/:** new H1. Covers distance from Bangalore, whether Bagepalli suits farmland, Chikkaballapur district, NH44, "about 2 hours" (no km figures) and landmarks. Place JSON-LD added. The old intro sentence is now in the answer and the facts box.
  - **/phase-2/:** 4,400 sq ft is about 4 guntas, or about 0.1 acre, and the page explains this. It also describes a small managed plot and Phase 2's 13 acres with 5,000+ trees planned.
  - **/managed-farmland-price-bangalore/:** new H1 "(2026)". Covers what a farm plot costs, cost factors and how to compare rates per sq ft.
  - **/how-to-buy/:** new H1. Adds a buying checklist, who can buy (the Karnataka Land Reforms Act, with advice to see a lawyer), documents, what RTC, e-khata and DC conversion mean, the registration process and a first-time buyer guide.
  - **/contact/:** new H1 "Book a Farmland Site Visit from Bangalore", what happens on a site visit, a list of questions to ask, and FAQPage JSON-LD.
  - **/faq/:** new H1 and three sections with 16 new Q&As (location, price and buying, how managed farmland works). FAQPage now matches all the visible Q&As.
  - **Sandalwood pages:** "highest-value" and "growing corridor" are reworded. They now explain white vs red sandalwood and agroforestry, whether you can plant sandalwood in Karnataka, and how long sandalwood takes to grow, with growth stages.
  - **/farmland-vs-gold/:** a table comparing farmland, apartments and residential or villa plots, and a section on managed farmland vs DC-converted plots.
  - **/arogya-vana-vs-other-managed-farmland/:** how to choose a project.
  - **/about/:** facts box and "Who is Saptha Ventures?".
  - **/farmland-for-nris-karnataka/:** "long-term asset" wording removed.
  - **Blog pages:** titles shortened and next-step links added.
  - **/blog/:** alt text and BreadcrumbList.
- **Site-wide:** descriptive alt text on the emblem and logo images, decoding=async on every image, and the inner-page EN language link fixed (it pointed to /blog/). Every WebPage now has isPartOf → #website, plus a publisher. Three footer links added.
- **kn/te:** only alt text (11 images each), meta and og descriptions, and WebPage schema (isPartOf, inLanguage, description) changed. Body copy is untouched.
- **sitemap.xml:** 27 URLs, with lastmod 2026-11-16 on changed pages. robots.txt is unchanged (Allow /, Disallow /api/, Sitemap).
- **llms.txt and llms-full.txt:** location (Chikkaballapur district, NH44), audience, Saturday visits, the new pages, plot size in guntas, Phase 2 acreage, the white sandalwood note and a quotable summary.

## Left unchanged on purpose
- The /weekend-farmhouse-near-bangalore/ main content and head (only the footer links and emblem alt changed) and the "weekend homes and retirement living" bullet.
- The lines "Phase 3 · New Launch", "We manage. You enjoy.", RERA, ownership, "2 Yrs free maintenance" and "75% sold", plus the brochure filename. Their on-page counts are the same as in v30.
- Exception: rewriting the meta descriptions dropped some meta-only mentions:
  - Phase 3 is gone from the price page's meta and WebPage description.
  - Phase 3 and 75% are gone from the kn/te meta descriptions.

## Skipped (needs Karthick)
- **Keywords not used:**
  - "10 guntas": the plot is about 4 guntas.
  - "open house": no such event exists.
  - "mango" and "organic": neither is named or confirmed on the site.
  - "gift to parents" and "retirement": these depend on the pending line.
  - "arogya vana reviews": there are no reviews.
  - "new launch": tied to the Phase 3 decision.
  - The Hold rows: farmhouse/stay, under ₹15 lakh, and loans/EMI.
- **Facts that would strengthen the pages:**
  - Per-area drive times or distances in km.
  - Whether all plots are in Karnataka.
  - Owner activities and gardening.
  - A map pin and coordinates.
  - Reviews.
  - Which Saturday slots are available.

## Verification
- **Before deploy:**
  - Every JSON-LD block parses.
  - No broken internal links and no links to redirected slugs.
  - Every img has a non-empty alt, width and height, and decoding.
  - One H1 per page, with no skipped heading levels.
  - Titles and descriptions are unique.
  - Desktop (1366) and mobile (390) screenshots in shots/seo/ show no horizontal overflow and no broken images.
- **Banned-text scan:** 0 hits for 98866, 99000 92996, 349, 13,15,600, payout, yield, profit, ROI, buyback, [CONFIRM, Sobha, Prestige, invest or apprecia. The only matches left are harmless ones that were already there:
  - The JS keyword `return`.
  - "return home" on the 404 page.
  - The blog's share-on-WhatsApp links, which carry no number.
  - "not a promise of income" in the Terms and Disclaimer.
  - New copy has no farmhouse, stay, slot or pickup wording.
- **Live:**
  - All 33 HTML/XML/TXT files return 200 and are byte-identical to the build, apart from the CF beacon.
  - 301s: the 3 old slugs, with or without a trailing slash; ?utm is kept; www plus an old slug takes one hop.
  - An unknown URL returns 404 with noindex and no-store and shows the branded page.
  - An empty POST to /api/enquiry returns 400 "Please enter your name".
  - /brochure.pdf returns 200 at 1,629,060 bytes, the same as before.
  - /thank-you.html returns a 307, as before.
