# arogyavana.com UI/UX pass, 2 Nov 2026
Lighthouse (before → after): mobile Perf 98→97, A11y 89→100, BP 100→100, SEO 100→100 | desktop Perf 98→100, A11y 89→100
Mobile LCP 1.8s→1.2s; desktop LCP 1.1s→0.8s; CLS ≤0.042 throughout.
Fixed: contrast (gold eyebrows/buttons/#777 text), nav crowding at 1024 + no hamburger, tap targets <44px (nav, FAQ, footer, contact links),
form labels/inline errors/aria-live/autocomplete/focus rings, select without name, logo aria-label mismatch, no <main>/skip link,
unsized images, 1MB oversized images (6.5MB→3.9MB), render-blocking fonts, short img cache, mobile hero wrapping/readability,
mobile sticky CTA + WhatsApp offset, contact phones wrapping, long mobile page (day carousel, 2-col gallery), section padding, reduced motion.
