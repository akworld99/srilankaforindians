# srilankaforindians.com

India's guide to Sri Lanka: weddings, real estate, business (Port City), logistics, second home and travel. Static site, no build dependencies, deploys on GitHub Pages.

## Structure

Run `python3 build.py` after any edit. It regenerates every page.

- `sitekit.py`: shared header, footer, tax ribbon, WhatsApp number, video cards, schema helpers
- `media.py`: every YouTube video and Instagram reel used on the site, with verified upload dates and views. Add new ones here
- `home.py`: homepage
- `build.py`: pillar pages (weddings, real estate, business, logistics, second home, travel) and the build entrypoint
- `pages_extra.py`: Port City tax page with salary calculator, Watch page
- `sectors.py`: 16 "Why Sri Lanka for X" pages under `why/`
- `guides.py`: 8 guides under `guides/`
- `cities.py`: 25 city pages under `from/` (Tier 1 and Tier 2)
- `hindi.py`: Hindi pages under `hi/` with hreflang pairs
- `assets/css/style.css`, `assets/js/site.js` (lite YouTube, tax calculator), `assets/js/calculator.js` (wedding)
- `llms.txt`: summary for AI assistants; `sitemap.xml`, `robots.txt` are generated

Deploys automatically on push via `.github/workflows/pages.yml`. Bump `ASSET_V` in sitekit.py when CSS/JS changes.

## Before launch

1. WhatsApp: set in `sitekit.py` (`WA_NUM`, `WA_DISPLAY`). Currently +94 71 614 7945.
2. Email `hello@srilankaforindians.com`: create the mailbox or change it in sitekit.py.
3. Wedding calculator rates in `assets/js/calculator.js` are placeholders; replace with partner rate cards.
4. Google Search Console: verify the domain, submit sitemap.xml.

## Facts used (verify before big campaigns)

- 431,162 Indian arrivals Jan–Sep 2026, India No.1 source market — SLTDA
- Port City incentives per Regulation 01 of 2025: 8–15 yr corporate tax holidays (primary BSI), 7.5% for 4 yrs (secondary), 0% personal income tax — CPCEC framework; always confirm current terms
- Condo ownership + USD 100k investor visa — 2026 practice under Land (Restrictions on Alienation) Act
- Colombo port 8.29M TEU in 2025 — SLPA reporting

## Deploy

GitHub Pages from `main` branch, root folder. No build step needed; commit the generated HTML.
