"""Shared building blocks for every page: head, header, footer, ribbons, video cards, schema."""
import html, re

SITE = "https://srilankaforindians.com"
WA_NUM = "94716147945"
WA = f"https://wa.me/{WA_NUM}"
WA_DISPLAY = "+94 71 614 7945"
ASSET_V = "8"
GA_ID = "G-EK1H1EL9KC"
HERO_ID = "NGoCQ3HyxQs"          # Scenic Relaxation: Sri Lanka 4K, no narration
FILM_ID = "dbM8AMmEdgY"          # Think School x Kumar Sangakkara on real estate
OG_IMAGE = f"https://i.ytimg.com/vi/{HERO_ID}/maxresdefault.jpg"

def esc(s): return html.escape(s, quote=True)

def wa_link(text):
    from urllib.parse import quote
    return f"{WA}?text={quote(text)}"

# ---------------------------------------------------------------- schema
def crumb_schema(trail):
    """trail: list of (name, path) after Home."""
    items = [{"name": "Home", "item": SITE + "/"}] + [{"name": n, "item": f"{SITE}/{p}"} for n, p in trail]
    parts = ",".join(
        f'{{"@type":"ListItem","position":{i+1},"name":{json_str(x["name"])},"item":"{x["item"]}"}}' for i, x in enumerate(items))
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{parts}]}}</script>'

def faq_schema(pairs):
    items = ",".join(
        f'{{"@type":"Question","name":{json_str(q)},"acceptedAnswer":{{"@type":"Answer","text":{json_str(a)}}}}}' for q, a in pairs)
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def json_str(s):
    import json
    return json.dumps(s, ensure_ascii=False)

def iso_dur(sec):
    sec = int(sec); h, r = divmod(sec, 3600); m, s = divmod(r, 60)
    return "PT" + (f"{h}H" if h else "") + (f"{m}M" if m else "") + f"{s}S"

def video_obj(v):
    return (f'{{"@type":"VideoObject","name":{json_str(v["title"])},'
            f'"description":{json_str(v["title"] + " by " + v["ch"] + ". Featured on Sri Lanka for Indians.")},'
            f'"thumbnailUrl":["https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg"],'
            f'"uploadDate":"{v["date"]}","duration":"{iso_dur(v["len"])}",'
            f'"contentUrl":"https://www.youtube.com/watch?v={v["id"]}","embedUrl":"https://www.youtube.com/embed/{v["id"]}",'
            f'"interactionStatistic":{{"@type":"InteractionCounter","interactionType":{{"@type":"WatchAction"}},"userInteractionCount":{v["views"]}}}}}')

def video_schema(videos):
    if not videos: return ""
    if len(videos) == 1:
        return f'<script type="application/ld+json">{{"@context":"https://schema.org",{video_obj(videos[0])[1:]}</script>'
    items = ",".join(f'{{"@type":"ListItem","position":{i+1},"item":{video_obj(v)}}}' for i, v in enumerate(videos))
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{items}]}}</script>'

# ---------------------------------------------------------------- head
def head(title, desc, path, depth=0, schema="", lang="en", alt=None, og_image=None):
    p = "../" * depth
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    alts = ""
    if alt:
        for code, ap in alt.items():
            alts += f'<link rel="alternate" hreflang="{code}-IN" href="{SITE}/{"" if ap == "index.html" else ap}">\n'
        alts += f'<link rel="alternate" hreflang="x-default" href="{SITE}/{"" if alt.get("en","index.html") == "index.html" else alt.get("en")}">\n'
    hi_fonts = "&family=Tiro+Devanagari+Hindi:ital@0;1&family=Mukta:wght@300;400;600" if lang == "hi" else ""
    img = og_image or OG_IMAGE
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-video-preview:-1">
<link rel="canonical" href="{canonical}">
{alts}<meta property="og:type" content="website">
<meta property="og:locale" content="{'hi_IN' if lang == 'hi' else 'en_IN'}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Sri Lanka for Indians">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{img}">
<meta name="geo.region" content="LK">
<meta name="theme-color" content="#101A16">
<link rel="icon" href="{p}assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://i.ytimg.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@300;400;500{hi_fonts}&display=swap">
<link rel="stylesheet" href="{p}assets/css/style.css?v={ASSET_V}">
{schema}
</head>
<body>
"""

LOGO_SVG = """<svg viewBox="0 0 80 100" role="img" aria-hidden="true">
        <path d="M40 4 C40 4 72 46 72 68 a32 32 0 1 1 -64 0 C8 46 40 4 40 4 Z" fill="none" stroke="#C9A75A" stroke-width="2"/>
        <path d="M40 18 C40 18 63 50 63 67 a23 23 0 1 1 -46 0 C17 50 40 18 40 18 Z" fill="none" stroke="#C9A75A" stroke-width="1" opacity=".45"/>
        <circle cx="40" cy="69" r="5.5" fill="#E6C987"/>
      </svg>"""

def tax_ribbon(depth=0, lang="en"):
    p = "../" * depth
    if lang == "hi":
        return f"""<a class="tax-ribbon" href="{p}hi/port-city-tax.html"><span class="tr-big">0%</span><span class="tr-txt">कॉर्पोरेट टैक्स, <b>15 साल</b> तक &middot; पोर्ट सिटी कोलंबो के रणनीतिक निवेश</span><span class="tr-go">आंकड़े देखें &rarr;</span></a>
"""
    return f"""<a class="tax-ribbon" href="{p}port-city-tax.html"><span class="tr-big">0%</span><span class="tr-txt">corporate tax for up to <b>15 years</b> &middot; Port City Colombo strategic investments</span><span class="tr-go">2026 rules &rarr;</span></a>
"""

def header(depth=0, lang="en", alt_path=None):
    p = "../" * depth
    if lang == "hi":
        nav = f"""      <a href="{p}hi/shaadi.html">शादी</a>
      <a href="{p}hi/property.html">प्रॉपर्टी</a>
      <a class="nav-tax" href="{p}hi/port-city-tax.html">टैक्स हॉलिडे</a>
      <a href="{p}hi/yatra.html">यात्रा</a>
      <a href="{p}watch.html">वीडियो</a>
      <a class="nav-lang" href="{p}{alt_path or 'index.html'}" hreflang="en" lang="en">English</a>
      <a class="btn btn-wa" href="{wa_link('नमस्ते, मुझे srilankaforindians.com से आपका नंबर मिला')}" rel="noopener">WhatsApp</a>"""
        home = f"{p}hi/index.html"
        burger = "मेनू"
    else:
        nav = f"""      <a href="{p}weddings.html">Weddings</a>
      <a href="{p}real-estate.html">Estates</a>
      <a class="nav-tax" href="{p}port-city-tax.html">Tax Holiday</a>
      <a href="{p}why/index.html">Why Sri Lanka</a>
      <a href="{p}travel.html" class="hide-m">Journeys</a>
      <a href="{p}watch.html">Watch</a>
      <a class="nav-lang" href="{p}{alt_path or 'hi/index.html'}" hreflang="hi" lang="hi">हिंदी</a>
      <a class="btn btn-wa" href="{wa_link('Hi, I found you on srilankaforindians.com')}" rel="noopener">WhatsApp</a>"""
        home = f"{p}index.html"
        burger = "Menu"
    return tax_ribbon(depth, lang) + f"""<header class="site-head">
  <div class="wrap">
    <a class="logo" href="{home}" aria-label="Sri Lanka for Indians home">
      {LOGO_SVG}
      <span class="word">Sri Lanka<em>For Indians</em></span>
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Open menu">
    <label for="nav-toggle" class="nav-burger">{burger}</label>
    <nav aria-label="Main">
{nav}
    </nav>
  </div>
</header>
"""

def cta_banner(line, sub, wa_text, lang="en"):
    if lang == "hi":
        b1, b2 = "WhatsApp पर बात करें", "ईमेल करें"
    else:
        b1, b2 = "WhatsApp your guide", "Email us"
    return f"""<section class="band">
  <div class="wrap">
    <div class="cta-banner">
      <div><h2>{line}</h2><p>{sub}</p><p class="wa-num">WhatsApp <span class="num">{WA_DISPLAY}</span></p></div>
      <div class="btns">
        <a class="btn btn-primary" href="{wa_link(wa_text)}" rel="noopener">{b1}</a>
        <a class="btn btn-ghost" href="mailto:hello@srilankaforindians.com">{b2}</a>
      </div>
    </div>
  </div>
</section>
"""

WA_ICON = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.7l-.4-.2-3.8 1.2 1.2-3.7-.3-.4a10.4 10.4 0 0 1-1.6-5.6C5.2 10 10 5.3 16 5.3S26.8 10 26.8 15.8 22 26.4 16 26.4zm5.9-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'

def footer(depth=0, lang="en", extra_js=""):
    p = "../" * depth
    float_text = "नमस्ते, मुझे श्रीलंका के बारे में जानकारी चाहिए" if lang == "hi" else "Hi, I want to explore Sri Lanka"
    return f"""<a class="wa-float" href="{wa_link(float_text)}" rel="noopener" aria-label="WhatsApp {WA_DISPLAY}">{WA_ICON}<span>WhatsApp</span></a>
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="{p}index.html" style="margin-bottom:18px">
          {LOGO_SVG}
          <span class="word">Sri Lanka<em>For Indians</em></span>
        </a>
        <p class="small">The island next door. Weddings, estates, enterprise and life in Sri Lanka, curated for Indians.</p>
        <p class="small">WhatsApp <a href="{WA}" rel="noopener" class="num">{WA_DISPLAY}</a><br><a href="mailto:hello@srilankaforindians.com">hello@srilankaforindians.com</a></p>
      </div>
      <div><h4>Pursuits</h4><ul>
        <li><a href="{p}weddings.html">Weddings</a></li>
        <li><a href="{p}real-estate.html">Estates</a></li>
        <li><a href="{p}business.html">Enterprise</a></li>
        <li><a href="{p}port-city-tax.html">Port City tax holidays</a></li>
        <li><a href="{p}logistics.html">Logistics</a></li>
        <li><a href="{p}second-home.html">The second address</a></li>
        <li><a href="{p}travel.html">Journeys</a></li>
      </ul></div>
      <div><h4>Why Sri Lanka</h4><ul>
        <li><a href="{p}why/technology.html">Technology</a></li>
        <li><a href="{p}why/bpo-kpo.html">BPO and KPO</a></li>
        <li><a href="{p}why/spices.html">Spices</a></li>
        <li><a href="{p}why/tea.html">Tea</a></li>
        <li><a href="{p}why/gems-jewellery.html">Gems</a></li>
        <li><a href="{p}why/ports-shipping.html">Ports</a></li>
        <li><a href="{p}why/index.html">All 16 sectors</a></li>
      </ul></div>
      <div><h4>Guides</h4><ul>
        <li><a href="{p}guides/visa-for-indians.html">Visa for Indians</a></li>
        <li><a href="{p}guides/trip-cost-from-india.html">Trip cost</a></li>
        <li><a href="{p}guides/ramayana-trail.html">Ramayana trail</a></li>
        <li><a href="{p}guides/ferry-india-to-sri-lanka.html">India to Sri Lanka ferry</a></li>
        <li><a href="{p}guides/port-city-vs-gift-city-vs-dubai.html">Port City vs GIFT City vs Dubai</a></li>
        <li><a href="{p}watch.html">Watch: India on Sri Lanka</a></li>
        <li><a href="{p}hi/index.html" lang="hi">हिंदी में पढ़ें</a></li>
      </ul></div>
    </div>
    <p class="disclaimer">Sri Lanka for Indians is an independent guide and introduction service. We are not affiliated with the Government of Sri Lanka, the Colombo Port City Economic Commission or any tourism authority. Videos and posts shown belong to their creators and are embedded from YouTube and Instagram. Nothing on this site is legal, tax or investment advice. Visa rules, tax incentives and property laws change; verify current terms with the official source and licensed professionals before acting. Overseas investment by Indian residents is subject to RBI and FEMA regulations; consult your chartered accountant.</p>
  </div>
</footer>
<script src="{p}assets/js/site.js?v={ASSET_V}" defer></script>
{extra_js}</body>
</html>
"""

# ---------------------------------------------------------------- media blocks
def fmt_views(n):
    n = int(n)
    if n >= 10_000_000: return f"{n/1_000_000:.0f}M views"
    if n >= 1_000_000: return f"{n/1_000_000:.1f}M views"
    if n >= 100_000: return f"{n/100_000:.1f} lakh views".replace(".0 ", " ")
    if n >= 1_000: return f"{n/1000:.0f}K views"
    return f"{n} views"

def yt_card(v):
    t = esc(v["title"])
    return f"""<article class="yt-card">
  <button class="yt" type="button" data-id="{v['id']}" aria-label="Play: {t}">
    <img src="https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg" alt="{t}" loading="lazy" width="480" height="360">
    <span class="yt-play" aria-hidden="true"></span>
    <span class="yt-len">{v['len_txt']}</span>
  </button>
  <div class="yt-meta"><b>{t}</b><span>{esc(v['ch'])} &middot; {fmt_views(v['views'])}</span></div>
</article>"""

def yt_grid(videos, cols="c3"):
    return f'<div class="yt-grid {cols}">' + "\n".join(yt_card(v) for v in videos) + "</div>"

def ig_embed(r):
    who = f"@{esc(r['user'])} on Instagram" if r.get("user") else "View on Instagram"
    title = f"Instagram reel by @{esc(r['user'])}" if r.get("user") else "Instagram reel about Sri Lanka"
    return f"""<figure class="ig">
  <iframe src="https://www.instagram.com/reel/{r['code']}/embed" title="{title}" loading="lazy" scrolling="no" allowtransparency="true"></iframe>
  <figcaption><a href="https://www.instagram.com/reel/{r['code']}/" rel="noopener">{who}</a></figcaption>
</figure>"""

def ig_grid(reels):
    return '<div class="ig-grid">' + "\n".join(ig_embed(r) for r in reels) + "</div>"

def film(v, caption=None):
    cap = f'<p class="small film-cap">{esc(v["title"])} &middot; {esc(v["ch"])}</p>'
    return f"""<div class="film">
    <iframe src="https://www.youtube-nocookie.com/embed/{v['id']}?rel=0&modestbranding=1" title="{esc(v['title'])}" allow="encrypted-media; picture-in-picture; fullscreen" loading="lazy" allowfullscreen></iframe>
  </div>{cap}"""
