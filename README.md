# srilankaforindians.com

India's guide to Sri Lanka: weddings, real estate, business (Port City), logistics, second home and travel. Static site, no build dependencies, deploys on GitHub Pages.

## Structure

- `index.html` — homepage (hand edited)
- `weddings.html`, `real-estate.html`, `business.html`, `logistics.html`, `second-home.html`, `travel.html` — pillar pages
- `from/*.html` — 12 city landing pages for Indian metros (SEO)
- `assets/css/style.css` — all styling, design tokens at the top
- `assets/js/calculator.js` — wedding cost calculator (India vs Sri Lanka), rates at the top of the file
- `build.py` — generates every page except index.html. Edit content there, then run `python3 build.py`
- `sitemap.xml`, `robots.txt`, `404.html`

## Before launch — replace these placeholders

1. **WhatsApp number**: search and replace `94770000000` with the real number (appears in `index.html` and `build.py`, then rerun `python3 build.py`).
2. **Email**: `hello@srilankaforindians.com` — set up the mailbox or change the address.
3. **Video links**: the four video cards on `index.html` point to YouTube search results. Swap each `href` for the specific video URL (Think School x Sangakkara, a real wedding film, a Port City tour, a Hindi vlog). To embed instead of link, replace the card with a YouTube `<iframe>`.
4. **Calculator rates**: `assets/js/calculator.js` — replace indicative rates with partner rate cards as you sign venues.
5. **Domain**: buy `srilankaforindians.com`, add a `CNAME` file containing `srilankaforindians.com`, point DNS (A records to GitHub Pages IPs or CNAME to `<user>.github.io`), enable HTTPS in repo Settings → Pages.
6. **Analytics**: add GA4 / Meta Pixel snippet before `</head>` in `index.html` and in `head()` inside `build.py`.

## Facts used (verify before big campaigns)

- 431,162 Indian arrivals Jan–Sep 2026, India No.1 source market — SLTDA
- Port City incentives per Regulation 01 of 2025: 8–15 yr corporate tax holidays (primary BSI), 7.5% for 4 yrs (secondary), 0% personal income tax — CPCEC framework; always confirm current terms
- Condo ownership + USD 100k investor visa — 2026 practice under Land (Restrictions on Alienation) Act
- Colombo port 8.29M TEU in 2025 — SLPA reporting

## Deploy

GitHub Pages from `main` branch, root folder. No build step needed; commit the generated HTML.
