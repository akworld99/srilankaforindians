from sitekit import *
from media import tagged, pick, reels, BY_ID
from sectors import SECTORS
from guides import GUIDES

TIER1 = [("chennai","Chennai"),("mumbai","Mumbai"),("delhi","Delhi NCR"),("bengaluru","Bengaluru"),("hyderabad","Hyderabad"),("kolkata","Kolkata"),("ahmedabad","Ahmedabad"),("pune","Pune")]

def tax_mega(depth=0):
    p = "../" * depth
    bars = [("India", 25.17, ""), ("Singapore", 17, ""), ("Dubai, UAE", 9, ""), ("Port City Colombo", 7.5, "hl")]
    bar_html = "\n".join(
        f'<div class="bar {c}"><span>{n}</span><span class="track"><span class="fill" style="width:{v/30*100:.0f}%"></span></span><span class="pct">{v}%</span></div>'
        for n, v, c in bars)
    return f"""<section class="tax-mega" id="tax">
  <div class="wrap">
    <div class="tm-left">
      <div class="zero wide" aria-label="7.5 percent">7.5%</div>
      <div class="zero-label">Corporate tax &middot; Port City Colombo</div>
      <ul class="tm-ladder">
        <li><b>7.5%</b><span>For 4 years. Approved secondary businesses</span></li>
        <li><b>0%</b><span>For 8 to 15 years. Large primary projects</span></li>
        <li><b>100%</b><span>Foreign ownership, foreign currency operations</span></li>
      </ul>
    </div>
    <div>
      <span class="eyebrow">The headline Indian CFOs reread</span>
      <h2>Under a third of India's corporate tax. <em>Eighty minutes from Chennai.</em></h2>
      <p>Approved Port City businesses can pay 7.5% corporate tax for their first four years of operations, against India's 25.17% headline rate. The biggest projects, designated primary Businesses of Strategic Importance, pay 0% for 8 to 15 years depending on investment size. Add 100% foreign ownership and foreign currency operations, an hour from home and outside the region that rattled every boardroom in 2026.</p>
      <div class="bars" aria-label="Headline corporate income tax rates">
        {bar_html}
      </div>
      <p class="small">Headline corporate rates. India: 22% plus 10% surcharge plus 4% cess for domestic companies. Port City figure is the concessionary rate for approved secondary Businesses of Strategic Importance, for 4 years, under Regulation 01 of 2025 and the Port City (Amendment) Act No. 1 of 2026. Since 20 January 2026, staff of newly approved Port City companies pay normal income tax.</p>
      <div style="display:flex; gap:16px; flex-wrap:wrap; margin-top:18px">
        <a class="btn btn-primary" href="{p}port-city-tax.html">Calculate your saving</a>
        <a class="btn btn-ghost" href="{p}guides/port-city-vs-gift-city-vs-dubai.html">Port City vs GIFT City vs Dubai</a>
      </div>
    </div>
  </div>
</section>
"""

def build(write):
    hero_poster = f"https://i.ytimg.com/vi/{HERO_ID}/maxres2.jpg"
    loved = pick("iLhRCwjywU8","CW6jTV-hTok","cRQu04IaAUk","gaLWS85uCzA","eiyQbvnxI-Y","Bu86Z_7VzAA")
    schema = video_schema([BY_ID[FILM_ID]] + loved)
    schema += "\n" + f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Sri Lanka for Indians","url":"{SITE}","logo":"{SITE}/assets/img/logo.svg","description":"Guide and matchmaking service helping Indians plan weddings, buy real estate, set up businesses and travel in Sri Lanka.","areaServed":["IN","LK"],"contactPoint":{{"@type":"ContactPoint","telephone":"+94716147945","contactType":"customer service","availableLanguage":["English","Hindi","Tamil"]}}}}</script>'''
    schema += "\n" + f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"Sri Lanka for Indians","url":"{SITE}","inLanguage":["en-IN","hi-IN"]}}</script>'''
    faqs = [
        ("Do Indians need a visa for Sri Lanka?", "Indian passport holders apply online for an Electronic Travel Authorisation before flying. Since 25 May 2026 the 30 day tourist ETA, with double entry, is free for Indians. Apply only on the official eta.gov.lk portal."),
        ("Can an Indian buy property in Sri Lanka?", "Foreigners cannot own freehold land directly, but can buy condominium units above ground floor outright when paid through an inward foreign remittance. Land is typically held on long lease. A property investment of USD 100,000 or more can support a renewable 5 year residence visa."),
        ("What is the tax rate in Port City Colombo?", "Under Regulation 01 of 2025, primary Businesses of Strategic Importance get corporate income tax holidays of 8 to 15 years, secondary businesses a 7.5% concessionary rate for 4 years, and all incentives need approval. Since 20 January 2026, staff of newly approved Port City companies pay normal income tax; earlier approvals keep a staff exemption until January 2029."),
        ("How much does a destination wedding in Sri Lanka cost compared to India?", "Sri Lankan beach resorts often price venue, rooms and catering below comparable Goa or Udaipur packages, while international flights narrow the gap depending on your city. Run your own numbers in our calculator and ask us for three real resort quotes."),
        ("Can Indian businesses trade with Sri Lanka in rupees?", "Yes. India and Sri Lanka trade can be invoiced, paid and settled in Indian rupees through Special Rupee Vostro Accounts that Sri Lankan banks hold with Indian banks. Since October 2025, Indian banks can also lend rupees to Sri Lankan businesses for cross border trade."),
        ("How far is Sri Lanka from India?", "Colombo is about 1 hour 20 minutes by air from Chennai, around 2 hours from Bengaluru and Hyderabad, and about 2 hours 30 minutes from Mumbai. A passenger ferry also runs between Nagapattinam and Kankesanthurai near Jaffna."),
    ]
    schema += "\n" + faq_schema(faqs)

    sectors_chips = "\n".join(f'<a href="why/{s["slug"]}.html">{s["name"]}</a>' for s in SECTORS)
    guide_cards = "\n".join(
        f'<a class="card link-card" href="guides/{g["slug"]}.html"><span class="tag">Guide</span><h3>{g["h1"]}</h3><p>{g["card"]}</p><span class="go">Read the guide &rarr;</span></a>'
        for g in GUIDES[:6])
    faq_html = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

    body = f"""
<section class="hero has-video">
  <div class="hero-video" aria-hidden="true" style="background-image:url('{hero_poster}')">
    <iframe src="https://www.youtube-nocookie.com/embed/{HERO_ID}?autoplay=1&mute=1&loop=1&playlist={HERO_ID}&controls=0&rel=0&playsinline=1&modestbranding=1&cc_load_policy=0&iv_load_policy=3&disablekb=1&fs=0&start=120" title="" tabindex="-1" allow="autoplay; encrypted-media" loading="lazy"></iframe>
  </div>
  <div class="hero-veil"></div>
  <div class="wrap">
    <div class="hero-inner">
      <span class="eyebrow">Namaste &middot; Ayubowan &middot; Vanakkam</span>
      <h1>The Indian Ocean kept an island <em>for you.</em></h1>
      <p class="lead">Eighty minutes from Chennai: clifftop weddings above the ocean, sea facing residences priced in dollars, and a financial district where approved businesses pay 7.5% corporate tax, and trade you can invoice in rupees. More than 4.3 lakh Indians arrived in the first nine months of 2026. Allow us to show you why the wisest of them stayed longer.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="{wa_link('Hi, I want to explore Sri Lanka')}" rel="noopener">WhatsApp your guide</a>
        <a class="btn btn-ghost" href="#calculator">The wedding ledger</a>
      </div>
      <div class="hero-badges">
        <a class="hero-badge" href="port-city-tax.html"><span class="hb-num">7.5%</span><span class="hb-txt"><b>Port City Colombo</b>Corporate tax for approved businesses. See if you qualify &rarr;</span></a>
        <a class="hero-badge" href="#inr"><span class="hb-num">&#8377;</span><span class="hb-txt"><b>Trade in rupees</b>Invoice and settle Sri Lanka deals in INR. How it works &rarr;</span></a>
      </div>
    </div>
  </div>
  <div class="hero-foot">Weddings &middot; Estates &middot; Enterprise &middot; The Second Address</div>
</section>

{tax_mega()}

<div class="wrap" style="padding-block:0">
  <div class="statbar">
    <div class="stat"><b class="num">4,31,162</b><span>Indian visitors, January to September 2026. India is Sri Lanka's No.1 market. Source: SLTDA</span></div>
    <div class="stat"><b>80 min</b><span>Chennai to Colombo by air. Same clock too: Sri Lanka runs on IST</span></div>
    <div class="stat"><b>&#8377;0</b><span>Visa fee for Indians. Free 30 day double entry ETA since 25 May 2026</span></div>
    <div class="stat"><b>UPI</b><span>Pay at LankaQR merchants across the island with your Indian UPI app</span></div>
  </div>
</div>

{inr_band(0)}
<section class="band" id="loved">
  <div class="wrap">
    <span class="eyebrow">Loved by India</span>
    <h2>Lakhs of Indians watched. <em>Then they booked.</em></h2>
    <p class="lead">Real videos from Indian creators, celebrities and business channels. Tap any one to play it here.</p>
    <div style="margin-top:40px">{yt_grid(loved)}</div>
    <h3 style="margin-top:56px">On Instagram right now</h3>
    <div style="margin-top:20px">{ig_grid(reels('travel', 3))}</div>
    <div style="margin-top:34px"><a class="btn btn-ghost" href="watch.html">Watch all 50 videos and reels</a></div>
  </div>
</section>

<section class="band sand" id="pillars">
  <div class="wrap">
    <span class="eyebrow">The portfolio</span>
    <h2>One island. <em>Six pursuits.</em></h2>
    <p class="lead">Choose yours. Each ends the same way: you tell us what you seek, and we place you with partners we have vetted, priced and stood beside.</p>
    <div class="grid c3" style="margin-top:44px">
      <a class="card link-card" href="weddings.html"><span class="tag">Weddings</span><h3>Vows above the Indian Ocean</h3><p>Clifftop mandaps, resorts fluent in Indian weddings, free visas for the whole baraat.</p><span class="go">Plan the wedding &rarr;</span></a>
      <a class="card link-card" href="real-estate.html"><span class="tag">Estates</span><h3>A sea facing address, held in dollars</h3><p>Condominiums Indians may own outright, Port City residences, and a 5 year visa route from USD 100,000.</p><span class="go">How buying works &rarr;</span></a>
      <a class="card link-card" href="port-city-tax.html"><span class="tag">Enterprise</span><h3>Port City: 7.5% corporate tax</h3><p>Approved businesses pay 7.5% for four years; the biggest projects 0% for 8 to 15. Full foreign ownership.</p><span class="go">See the tax numbers &rarr;</span></a>
      <a class="card link-card" href="logistics.html"><span class="tag">Logistics</span><h3>The port on the main lane</h3><p>Colombo moved a record 8.29 million TEU in 2025, much of it Indian cargo.</p><span class="go">The logistics plays &rarr;</span></a>
      <a class="card link-card" href="second-home.html"><span class="tag">The second address</span><h3>A residence 400 km from home</h3><p>Visas, schools, and what a month in Colombo truly costs.</p><span class="go">Plan the residence &rarr;</span></a>
      <a class="card link-card" href="travel.html"><span class="tag">Journeys</span><h3>Ramayana trails, leopards, tea</h3><p>Itineraries composed for Indian travellers, veg and Jain tables mapped.</p><span class="go">Begin the journey &rarr;</span></a>
    </div>
    <h3 style="margin-top:56px">Why Sri Lanka for your sector</h3>
    <div class="chips" style="margin-top:18px">{sectors_chips}</div>
  </div>
</section>

<section class="band" id="calculator">
  <div class="wrap">
    <span class="eyebrow">The wedding ledger</span>
    <h2>Goa against Sri Lanka, <em>on your numbers.</em></h2>
    <p class="lead">The same guest list, the same functions. See where the budget goes further, flights included.</p>
    <div class="calc" style="margin-top:40px">
      <div class="calc-grid">
        <div class="field"><label for="guests">Guests</label><input type="number" id="guests" min="30" max="1000" step="10" value="150"></div>
        <div class="field"><label for="days">Days of functions</label><select id="days"><option value="1">1 day</option><option value="2" selected>2 days</option><option value="3">3 days</option></select></div>
        <div class="field"><label for="tier">Style</label><select id="tier"><option value="silver">Understated</option><option value="gold" selected>Premium resort</option><option value="royal">Full royal</option></select></div>
        <div class="field"><label for="origin">Flying from</label><select id="origin"><option value="chennai" selected>Chennai</option><option value="bengaluru">Bengaluru</option><option value="mumbai">Mumbai</option><option value="delhi">Delhi</option><option value="hyderabad">Hyderabad</option><option value="kolkata">Kolkata</option><option value="ahmedabad">Ahmedabad</option><option value="pune">Pune</option></select></div>
      </div>
      <div class="calc-results">
        <div class="result" id="res-india"><h3>Goa / Udaipur <span class="total num" id="total-india">&#8377;0</span></h3><ul>
          <li><span>Venue, catering, decor</span><b class="num" id="in-pkg">&#8377;0</b></li>
          <li><span>Guest rooms</span><b class="num" id="in-rooms">&#8377;0</b></li>
          <li><span>Domestic flights</span><b class="num" id="in-fly">&#8377;0</b></li></ul></div>
        <div class="result win" id="res-sl"><h3>Sri Lanka <span class="total num" id="total-sl">&#8377;0</span></h3><ul>
          <li><span>Venue, catering, decor</span><b class="num" id="sl-pkg">&#8377;0</b></li>
          <li><span>Guest rooms</span><b class="num" id="sl-rooms">&#8377;0</b></li>
          <li><span>International flights</span><b class="num" id="sl-fly">&#8377;0</b></li></ul></div>
      </div>
      <div class="savings" id="savings-box">
        <span id="savings-line">Sri Lanka could save you</span> <b class="num" id="savings-amt">&#8377;0</b>
        <p class="small" style="margin:12px 0 18px">Indicative planning estimates. Real quotes depend on resort, season and menu. We return exact numbers from three resorts, free.</p>
        <a class="btn btn-primary" href="{wa_link('Hi, I used the wedding calculator. Please send me 3 real quotes.')}" rel="noopener">Receive three real quotes</a>
      </div>
    </div>
  </div>
</section>

<section class="band sand" id="film">
  <div class="wrap">
    <span class="eyebrow">Think School &times; Kumar Sangakkara</span>
    <h2>"The next big real estate opportunity." <em>In his words.</em></h2>
    <p class="lead">India's favourite business explainer channel sat down with Sri Lanka's most respected cricketer to ask why the island is back on investors' maps.</p>
    <div style="margin-top:36px">{film(BY_ID[FILM_ID])}</div>
  </div>
</section>

<section class="band" id="why-now">
  <div class="wrap">
    <span class="eyebrow">Why now</span>
    <h2>Three reasons 2026 is <em>the year.</em></h2>
    <div class="grid c3" style="margin-top:40px">
      <div class="card"><span class="tag">The second address</span><h3>The Gulf taught everyone a lesson</h3><p>2026 showed what happens when money, office and family all sit in one contested region. Sri Lanka does not replace Dubai. It is the second address kept an hour from home.</p></div>
      <div class="card"><span class="tag">Momentum</span><h3>India is Sri Lanka's biggest bet</h3><p>Indian firms run Colombo's West Container Terminal and the island's largest shipyard. Port City expects a quarter of its investment from India. You would not be early. You would be on time.</p></div>
      <div class="card"><span class="tag">Ease</span><h3>It keeps getting easier</h3><p>A free visa. UPI at the counter. A ferry from Nagapattinam. Flights from every metro. For Tamil speakers, half the island already speaks your language.</p></div>
    </div>
  </div>
</section>

<section class="band sand" id="matchmaking">
  <div class="wrap">
    <span class="eyebrow">Matchmaking, the other kind</span>
    <h2>Tell us what you seek. <em>We know who to call.</em></h2>
    <p class="lead">We are not a listing site. We are your guide. Every planner, developer, lawyer and agent we introduce has been vetted, priced and reference checked. You deal with them directly. We remain at your side until it is done.</p>
    <div class="grid c3" style="margin-top:40px">
      <div class="card"><div class="steps"><div class="step"><h3>Brief us</h3><p>A wedding for 200. A residence under USD 250,000. A Port City entity. One WhatsApp message opens the file.</p></div></div></div>
      <div class="card"><div class="steps" style="counter-reset:step 1"><div class="step"><h3>Matched in 48 hours</h3><p>Two or three vetted partners, real prices rather than brochure prices, introductions arranged.</p></div></div></div>
      <div class="card"><div class="steps" style="counter-reset:step 2"><div class="step"><h3>We remain with you</h3><p>From first visit to final signature, one person on the island answers your messages. Us.</p></div></div></div>
    </div>
  </div>
</section>

{cta_banner("Your guide is one message away", "A conversation costs nothing. Hindi, Tamil and English spoken.", "Hi, I want to explore Sri Lanka for ")}

<section class="band sand" id="guides">
  <div class="wrap">
    <span class="eyebrow">Straight guides</span>
    <h2>Everything Indians <em>actually search for.</em></h2>
    <div class="grid c3" style="margin-top:40px">{guide_cards}</div>
  </div>
</section>

<section class="band" id="cities">
  <div class="wrap">
    <span class="eyebrow">From your city</span>
    <h2>Composed for <em>every Indian city.</em></h2>
    <p class="lead">Flights, costs and plans from where you actually live.</p>
    <div class="city-grid" style="margin-top:36px">
      {{CITY_LINKS}}
    </div>
  </div>
</section>

<section class="band sand" id="faq">
  <div class="wrap">
    <span class="eyebrow">Straight answers</span>
    <h2>Questions every Indian <em>asks us.</em></h2>
    <div style="margin-top:36px; max-width:880px">{faq_html}</div>
  </div>
</section>
"""
    from cities import ALL_CITIES
    links = "\n      ".join(f'<a href="from/{c[0]}.html">{c[1]}</a>' for c in ALL_CITIES)
    body = body.replace("{CITY_LINKS}", links)
    page = head("Sri Lanka for Indians | Weddings, Real Estate, Port City 7.5% Tax and Travel",
                "India's guide to Sri Lanka. Destination weddings, property Indians can buy, Port City Colombo's 7.5% corporate tax for approved businesses, a free visa for Indians and travel from every Indian city. Talk to a guide on WhatsApp.",
                "index.html", schema=schema, alt={"en": "index.html", "hi": "hi/index.html"}) \
        + header(alt_path="hi/index.html") + body + footer(extra_js=f'<script src="assets/js/calculator.js?v={ASSET_V}"></script>\n')
    write("index.html", page)
