#!/usr/bin/env python3
"""Generates all pages except index.html. Edit content here, run: python3 build.py"""
import os, html, datetime

SITE = "https://srilankaforindians.com"
WA = "https://wa.me/94770000000"

def head(title, desc, path, depth=0, schema=""):
    p = "../" * depth
    canonical = SITE + "/" + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Sri Lanka for Indians">
<link rel="icon" href="{p}assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@300;400;500&display=swap">
<link rel="stylesheet" href="{p}assets/css/style.css">
{schema}
</head>
<body>
"""

def header(depth=0):
    p = "../" * depth
    return f"""<header class="site-head">
  <div class="wrap">
    <a class="logo" href="{p}index.html" aria-label="Sri Lanka for Indians home">
      <svg viewBox="0 0 80 100" role="img" aria-hidden="true">
        <path d="M40 4 C40 4 72 46 72 68 a32 32 0 1 1 -64 0 C8 46 40 4 40 4 Z" fill="none" stroke="#C9A75A" stroke-width="2"/>
        <path d="M40 18 C40 18 63 50 63 67 a23 23 0 1 1 -46 0 C17 50 40 18 40 18 Z" fill="none" stroke="#C9A75A" stroke-width="1" opacity=".45"/>
        <circle cx="40" cy="69" r="5.5" fill="#E6C987"/>
      </svg>
      <span class="word">Sri Lanka<em>For Indians</em></span>
    </a>
    <nav aria-label="Main">
      <a href="{p}weddings.html">Weddings</a>
      <a href="{p}real-estate.html">Estates</a>
      <a href="{p}business.html">Enterprise</a>
      <a href="{p}logistics.html" class="hide-m">Logistics</a>
      <a href="{p}second-home.html" class="hide-m">Residences</a>
      <a href="{p}travel.html">Journeys</a>
      <a class="btn btn-wa" href="{WA}?text=Hi%2C%20I%20found%20you%20on%20srilankaforindians.com" rel="noopener">WhatsApp</a>
    </nav>
  </div>
</header>
"""

def cta_banner(line, sub, wa_text, depth=0):
    return f"""<section class="band">
  <div class="wrap">
    <div class="cta-banner">
      <div><h2>{line}</h2><p>{sub}</p></div>
      <div class="btns">
        <a class="btn btn-primary" href="{WA}?text={wa_text}" rel="noopener">WhatsApp your guide</a>
        <a class="btn btn-ghost" href="mailto:hello@srilankaforindians.com">Email us</a>
      </div>
    </div>
  </div>
</section>
"""

def footer(depth=0):
    p = "../" * depth
    return f"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="{p}index.html" style="margin-bottom:18px">
          <svg viewBox="0 0 80 100" style="height:42px" aria-hidden="true">
            <path d="M40 4 C40 4 72 46 72 68 a32 32 0 1 1 -64 0 C8 46 40 4 40 4 Z" fill="none" stroke="#C9A75A" stroke-width="2"/>
            <path d="M40 18 C40 18 63 50 63 67 a23 23 0 1 1 -46 0 C17 50 40 18 40 18 Z" fill="none" stroke="#C9A75A" stroke-width="1" opacity=".45"/>
            <circle cx="40" cy="69" r="5.5" fill="#E6C987"/>
          </svg>
          <span class="word">Sri Lanka<em>For Indians</em></span>
        </a>
        <p class="small">The island next door. Weddings, estates, enterprise and life in Sri Lanka, curated for Indians.</p>
      </div>
      <div><h4>Pursuits</h4><ul>
        <li><a href="{p}weddings.html">Weddings</a></li>
        <li><a href="{p}real-estate.html">Estates</a></li>
        <li><a href="{p}business.html">Enterprise and Port City</a></li>
        <li><a href="{p}logistics.html">Logistics</a></li>
      </ul></div>
      <div><h4>Live</h4><ul>
        <li><a href="{p}second-home.html">The second address</a></li>
        <li><a href="{p}travel.html">Journeys</a></li>
        <li><a href="{p}from/chennai.html">From Chennai</a></li>
        <li><a href="{p}from/mumbai.html">From Mumbai</a></li>
      </ul></div>
      <div><h4>Talk to us</h4><ul>
        <li><a href="{WA}" rel="noopener">WhatsApp</a></li>
        <li><a href="mailto:hello@srilankaforindians.com">hello@srilankaforindians.com</a></li>
      </ul></div>
    </div>
    <p class="disclaimer">Sri Lanka for Indians is an independent guide and introduction service. We are not affiliated with the Government of Sri Lanka, the Colombo Port City Economic Commission or any tourism authority. Nothing on this site is legal, tax or investment advice. Visa rules, tax incentives and property laws change; verify current terms with the official source and licensed professionals before acting. Overseas investment by Indian residents is subject to RBI and FEMA regulations; consult your chartered accountant.</p>
  </div>
</footer>
</body>
</html>
"""

PAGES = {}

PAGES["weddings.html"] = dict(
    title="Destination Wedding in Sri Lanka: Cost vs Goa, Venues, Visas | Sri Lanka for Indians",
    desc="Plan an Indian destination wedding in Sri Lanka. Compare costs against Goa and Udaipur with our calculator, see beach venues that know Indian weddings, and get 3 real quotes free.",
    body=f"""
<section class="hero"><div class="wrap">
  <span class="eyebrow">Weddings</span>
  <h1>Shaadi by the Indian Ocean. Literally.</h1>
  <p class="lead">Beach mandaps, elephant friendly venues, chefs who can do a live chaat counter and a proper sadhya. Sri Lankan resorts have hosted Indian weddings for years. The difference now: the maths beats Goa for most guest lists, and your baraat's visas arrive in hours.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#calculator">Run the numbers</a>
  <a class="btn btn-ghost" href="{WA}?text=Hi%2C%20planning%20a%20wedding%20in%20Sri%20Lanka" rel="noopener">Talk to a planner</a></div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Why couples are crossing the Palk Strait</h2>
  <div class="grid c3" style="margin-top:28px">
    <div class="card"><span class="tag">Money</span><h3>Your budget stretches further</h3><p>Five star beach resorts price rooms and banquets below comparable Goa and Rajasthan properties. No Goa style liquor licence drama, and alcohol at resort rates, not destination markup rates.</p></div>
    <div class="card"><span class="tag">Logistics</span><h3>Easier than an Indian destination wedding</h3><p>One flight under 3 hours from any metro. ETA visas online in hours. Customs is used to wedding cargo: lehengas, decor, even your panditji's samagri.</p></div>
    <div class="card"><span class="tag">The wow</span><h3>Backdrops Goa cannot match</h3><p>Clifftop lawns in Galle, private beaches on the south coast, tea country manors in Ella, and sunsets your photographer will frame without a single filter.</p></div>
  </div>
</div></section>

<section class="band sand" id="calculator"><div class="wrap">
  <span class="eyebrow">The calculator</span>
  <h2>Goa vs Sri Lanka, on your numbers</h2>
  <p class="lead">Same comparison as a destination wedding inside India: venue, catering and decor package, guest rooms, and flights. Indicative 2026 estimates. We turn these into 3 real resort quotes for free.</p>
  <div class="calc" style="margin-top:30px">
    <div class="calc-grid">
      <div class="field"><label for="guests">Guests</label><input type="number" id="guests" min="30" max="1000" step="10" value="150"></div>
      <div class="field"><label for="days">Days of functions</label><select id="days"><option value="1">1 day</option><option value="2" selected>2 days</option><option value="3">3 days</option></select></div>
      <div class="field"><label for="tier">Style</label><select id="tier"><option value="silver">Smart and simple</option><option value="gold" selected>Premium resort</option><option value="royal">Full royal</option></select></div>
      <div class="field"><label for="origin">Flying from</label><select id="origin"><option value="chennai" selected>Chennai</option><option value="bengaluru">Bengaluru</option><option value="mumbai">Mumbai</option><option value="delhi">Delhi</option><option value="hyderabad">Hyderabad</option><option value="kolkata">Kolkata</option><option value="ahmedabad">Ahmedabad</option><option value="pune">Pune</option></select></div>
    </div>
    <div class="calc-results">
      <div class="result" id="res-india"><h3>Goa / Udaipur <span class="total num" id="total-india">&#8377;0</span></h3>
        <ul><li><span>Venue, catering, decor</span><b class="num" id="in-pkg">&#8377;0</b></li>
        <li><span>Guest rooms</span><b class="num" id="in-rooms">&#8377;0</b></li>
        <li><span>Domestic flights</span><b class="num" id="in-fly">&#8377;0</b></li></ul></div>
      <div class="result win" id="res-sl"><h3>Sri Lanka <span class="total num" id="total-sl">&#8377;0</span></h3>
        <ul><li><span>Venue, catering, decor</span><b class="num" id="sl-pkg">&#8377;0</b></li>
        <li><span>Guest rooms</span><b class="num" id="sl-rooms">&#8377;0</b></li>
        <li><span>International flights</span><b class="num" id="sl-fly">&#8377;0</b></li></ul></div>
    </div>
    <div class="savings" id="savings-box">
      <span id="savings-line">You could save</span> <b class="num" id="savings-amt">&#8377;0</b>
      <p class="small" style="color:#F6F2E6; opacity:.85; margin:8px 0 14px">Indicative planning estimates. Real quotes depend on resort, season and menu.</p>
      <a class="btn btn-primary" href="{WA}?text=Hi%2C%20I%20used%20the%20wedding%20calculator.%20Send%20me%20real%20quotes." rel="noopener">Get 3 real quotes on WhatsApp</a>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Where Indians get married here</h2>
  <div class="table-scroll" style="margin-top:24px"><table>
    <tr><th>Region</th><th>Vibe</th><th>Best for</th><th class="num">Guest sweet spot</th></tr>
    <tr><td>South coast (Bentota to Tangalle)</td><td>Classic beach resort row</td><td>Big fat beach weddings, sangeet on the sand</td><td class="num">100 to 400</td></tr>
    <tr><td>Galle Fort and around</td><td>Colonial boutique, clifftop villas</td><td>Intimate weddings, editorial photos</td><td class="num">40 to 150</td></tr>
    <tr><td>Colombo city</td><td>Five star ballrooms</td><td>Monsoon season backup, corporate crowd</td><td class="num">200 to 800</td></tr>
    <tr><td>Hill country (Kandy, Ella, Nuwara Eliya)</td><td>Tea estates and misty manors</td><td>Small weddings, pre wedding shoots</td><td class="num">30 to 120</td></tr>
  </table></div>
  <h2 style="margin-top:48px">How we run your wedding</h2>
  <div class="steps" style="margin-top:22px; max-width:760px">
    <div class="step"><h3>Brief us on WhatsApp</h3><p>Guest count, dates, functions, budget band. Ten minutes.</p></div>
    <div class="step"><h3>Three venues, real prices, in one week</h3><p>We negotiate as volume buyers, not as a one time NRI couple. You see line item quotes, not brochure PDFs.</p></div>
    <div class="step"><h3>One recce trip, everything decided</h3><p>Two days on the island: venues, menu tasting, decor mockups, pandit and DJ options. Fly home with a signed plan.</p></div>
    <div class="step"><h3>We stand beside you on the day</h3><p>Our coordinator is on site from haldi to vidaai. Your family enjoys the wedding. We handle the island.</p></div>
  </div>
</div></section>
""" + cta_banner("Dates in mind? Lock the venue first.", "Peak season venues go 9 to 12 months out. Free consult, Hindi and Tamil spoken.", "Hi%2C%20planning%20a%20wedding%20in%20Sri%20Lanka"),
    calc=True,
)

PAGES["real-estate.html"] = dict(
    title="Can Indians Buy Property in Sri Lanka? Condos, Port City, Investor Visa | Sri Lanka for Indians",
    desc="How Indians buy real estate in Sri Lanka in 2026: condominium ownership rules, Port City apartments, the USD 100,000 investor residence visa, taxes, and the exact buying process.",
    body=f"""
<section class="hero"><div class="wrap">
  <span class="eyebrow">Real Estate</span>
  <h1>Own a sea view home an hour from India.</h1>
  <p class="lead">Yes, Indians can buy here. Condominiums outright, land on long lease, and Port City apartments inside a special economic zone. Prices in Colombo sit well below Mumbai, Bengaluru and Dubai for comparable sea facing stock, and a USD 100,000 property investment can anchor a renewable 5 year residence visa.</p>
  <div class="cta-row"><a class="btn btn-primary" href="{WA}?text=Hi%2C%20I%20want%20to%20buy%20property%20in%20Sri%20Lanka" rel="noopener">Get the buyer's shortlist</a>
  <a class="btn btn-ghost" href="#rules">Read the rules first</a></div>
</div></section>

<section class="band" id="rules"><div class="wrap">
  <h2>The rules, without the fog</h2>
  <div class="grid c2" style="margin-top:28px">
    <div class="card"><span class="tag">Can do</span><h3>What Indians can buy</h3>
      <ul style="padding-left:18px; margin:0">
        <li>Condominium units above ground floor, owned outright, paid fully by inward foreign remittance</li>
        <li>Land on long lease, commonly up to 99 years</li>
        <li>Property through approved company structures, with local legal advice</li>
        <li>Apartments inside Port City Colombo under the SEZ framework</li>
        <li>Shares of listed Sri Lankan property companies</li>
      </ul></div>
    <div class="card"><span class="tag">Cannot do</span><h3>What stays off the table</h3>
      <ul style="padding-left:18px; margin:0">
        <li>Freehold land in your own name as a foreigner</li>
        <li>Freehold land through a company that is 50% or more foreign owned</li>
        <li>Local bank mortgages as a non resident; plan to fund from India or abroad</li>
        <li>Paying in cash outside banking channels. Everything flows through an Inward Investment Account</li>
      </ul></div>
  </div>
  <p class="small" style="margin-top:18px">Rules summarised from the Land (Restrictions on Alienation) Act and 2026 practice. Always confirm with a licensed Colombo property lawyer. We introduce you to ours.</p>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>Three ways Indians are buying in 2026</h2>
  <div class="grid c3" style="margin-top:28px">
    <div class="card"><span class="tag">Yield</span><h3>Colombo sea facing condos</h3><p>Two and three bed units in Colombo 3, 4 and Dehiwala, bought for dollar linked rental yield from expats and long stay tourists. Entry from around USD 150k.</p></div>
    <div class="card"><span class="tag">Trophy</span><h3>Port City apartments</h3><p>New builds inside the SEZ with its own regulatory regime and marina lifestyle. The long game on South Asia's newest address. Entry varies by tower and phase.</p></div>
    <div class="card"><span class="tag">Lifestyle</span><h3>South coast villas on lease</h3><p>Galle and Weligama villa plays: long lease land, build or renovate, run as a boutique rental when you are not there. The Bali playbook, 4 hours closer to home.</p></div>
  </div>
  <h2 style="margin-top:48px">The investor visa angle</h2>
  <p class="lead">Invest USD 100,000 or more in qualifying property through an Inward Investment Account and you can apply for a renewable 5 year residence visa. Larger investments unlock longer options. For families wanting a second base near India, this is the cleanest route on the table.</p>
</div></section>

<section class="band"><div class="wrap">
  <h2>How a purchase actually runs</h2>
  <div class="steps" style="margin-top:22px; max-width:760px">
    <div class="step"><h3>Shortlist and inspect</h3><p>We send a vetted shortlist with real prices and rental histories. You fly in for one inspection weekend, or we video walk every unit.</p></div>
    <div class="step"><h3>Legal check</h3><p>Independent lawyer verifies title, condo plan approval and developer standing. Non negotiable, and it costs less than you think.</p></div>
    <div class="step"><h3>Money moves correctly</h3><p>Funds come from India via banking channels into an Inward Investment Account, keeping your repatriation rights clean and your CA happy with FEMA.</p></div>
    <div class="step"><h3>Transfer, register, hand over keys</h3><p>Deed executed, registered, and if you want, our partner starts renting it the same month.</p></div>
  </div>
</div></section>
""" + cta_banner("Want the current shortlist?", "We track every Colombo and south coast project worth an Indian buyer's time. Prices, yields, red flags.", "Hi%2C%20send%20me%20the%20Sri%20Lanka%20property%20shortlist"),
)

PAGES["business.html"] = dict(
    title="Port City Colombo for Indian Companies: 0% Personal Tax, 8 to 15 Year Holidays | Sri Lanka for Indians",
    desc="Set up in Sri Lanka from India. Port City Colombo tax incentives explained: 0% personal income tax, corporate holidays up to 15 years, 7.5% concessionary rate, 100% foreign ownership, India plus one strategy.",
    body=f"""
<section class="hero"><div class="wrap">
  <span class="eyebrow">Business</span>
  <h1>Your India plus one address, one hour away.</h1>
  <p class="lead">Port City Colombo has said it out loud: its target audience is India. GCC back offices, IT delivery centres, fintech, family offices. English speaking talent, dollar denominated operations, and a tax regime that makes CFOs re read the page. Here is that page.</p>
  <div class="cta-row"><a class="btn btn-primary" href="{WA}?text=Hi%2C%20exploring%20a%20Sri%20Lanka%20or%20Port%20City%20setup" rel="noopener">Scope your setup</a></div>
</div></section>

<section class="band ink"><div class="wrap">
  <h2>The headline numbers</h2>
  <div class="figures">
    <div class="figure"><b>0%</b><span>Personal income tax inside Port City for staff of approved businesses, remunerated in foreign currency</span></div>
    <div class="figure"><b>8&ndash;15 yrs</b><span>Corporate income tax holidays for primary Businesses of Strategic Importance, scaled to investment</span></div>
    <div class="figure"><b>7.5%</b><span>Concessionary corporate rate for secondary businesses, 4 years from commercial operations</span></div>
  </div>
  <div class="grid c3">
    <div class="card" style="background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.18); color:inherit"><h3 style="color:#FFFDF8">100% yours</h3><p>Full foreign ownership, no local partner requirement inside the zone.</p></div>
    <div class="card" style="background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.18); color:inherit"><h3 style="color:#FFFDF8">16 currencies</h3><p>Transact in designated foreign currencies, ring fenced from domestic monetary shocks.</p></div>
    <div class="card" style="background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.18); color:inherit"><h3 style="color:#FFFDF8">Free repatriation</h3><p>Profits and capital move out through the SEZ framework without domestic exchange control friction.</p></div>
  </div>
  <p class="small" style="opacity:.75; margin-top:18px">Per Regulation 01 of 2025 under the CPCEC framework. Every incentive requires Commission approval and depends on category and investment thresholds. Confirm current terms with a licensed advisor; this page is a guide, not advice.</p>
</div></section>

<section class="band"><div class="wrap">
  <h2>Who this actually fits</h2>
  <div class="grid c2" style="margin-top:28px">
    <div class="card"><span class="tag">IT and GCC</span><h3>Business continuity and delivery centres</h3><p>Port City pitches itself as a resilient business continuity and disaster recovery location for Indian global capability centres. Same time zone band as India, English speaking graduates, costs below tier 1 Indian metros for senior talent retention.</p></div>
    <div class="card"><span class="tag">Trade</span><h3>Regional HQs and trading desks</h3><p>Sit beside one of Asia's busiest transshipment ports with multi currency banking. Commodity, shipping and sourcing desks covering South Asia, Africa and the Gulf run naturally from Colombo.</p></div>
    <div class="card"><span class="tag">Fintech and finance</span><h3>Offshore structures with substance</h3><p>The Colombo International Financial Centre is rising inside the zone. Early movers get positioning that latecomers will pay for.</p></div>
    <div class="card"><span class="tag">Family offices</span><h3>A second corporate address</h3><p>After 2026, concentration risk is a board topic. A Colombo entity diversifies jurisdiction without moving far from home.</p></div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>Setup, step by step</h2>
  <div class="steps" style="margin-top:22px; max-width:760px">
    <div class="step"><h3>Pick the right vehicle</h3><p>Port City Authorised Person status, a standard Sri Lankan company, or BOI route. The right answer depends on what you do and how much you invest. We map it in one call.</p></div>
    <div class="step"><h3>Approvals and incorporation</h3><p>Our partner firms handle CPCEC or Registrar filings, bank accounts and office space. Typical timelines run in weeks, not quarters.</p></div>
    <div class="step"><h3>Hire and operate</h3><p>Recruitment partners, payroll, and the practical stuff nobody writes about: schools, housing and flights for the leadership you relocate.</p></div>
  </div>
  <p class="small">Indian outbound investment runs under RBI's Overseas Investment rules. Structure the India side with your CA before money moves. We will happily get on that call too.</p>
</div></section>
""" + cta_banner("Thinking Colombo for 2027 budgets?", "Get a one page feasibility note for your use case: entity, incentives, costs, timeline.", "Hi%2C%20send%20me%20a%20Port%20City%20feasibility%20note"),
)

PAGES["logistics.html"] = dict(
    title="Colombo Port and Sri Lanka Logistics for Indian Companies | Sri Lanka for Indians",
    desc="Why Indian shippers, forwarders and 3PLs set up in Sri Lanka: Colombo's record 8.29 million TEU, Indian run West Container Terminal, Hambantota, bunkering and the transshipment play.",
    body=f"""
<section class="hero"><div class="wrap">
  <span class="eyebrow">Logistics</span>
  <h1>The port that moves India's cargo.</h1>
  <p class="lead">Colombo sits 6 to 10 nautical miles off the main east west shipping lane and handled a record 8.29 million TEU in 2025. A huge share of that is Indian transshipment. Adani runs the West Container Terminal. Mazagon Dock bought the island's biggest shipyard. Indian logistics money is already here. The question is whether yours is.</p>
  <div class="cta-row"><a class="btn btn-primary" href="{WA}?text=Hi%2C%20exploring%20Sri%20Lanka%20logistics%20opportunities" rel="noopener">Talk logistics</a></div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Why Colombo matters to Indian cargo</h2>
  <div class="grid c3" style="margin-top:28px">
    <div class="card"><span class="tag">Position</span><h3>On the lane, not near it</h3><p>Mainline vessels barely deviate to call Colombo. For Indian east and west coast cargo, it is the natural relay point between feeder and mothership.</p></div>
    <div class="card"><span class="tag">Capacity</span><h3>Deep water, new terminals</h3><p>WCT and ECT add deep water berths for the largest vessels. When Red Sea and Gulf routings wobble, Colombo picks up volume.</p></div>
    <div class="card"><span class="tag">Ownership</span><h3>Indian skin in the game</h3><p>Adani in the port, Mazagon Dock in the shipyard, IOC in fuel retail. Indian corporates did their diligence and wrote cheques. Follow the fleet.</p></div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>Plays for Indian logistics firms</h2>
  <div class="table-scroll" style="margin-top:24px"><table>
    <tr><th>Play</th><th>Who it fits</th><th>Why Sri Lanka</th></tr>
    <tr><td>Transshipment and NVOCC desk</td><td>Forwarders, consolidators</td><td>Sit where the boxes change ships; serve Indian ports from one control tower</td></tr>
    <tr><td>Entrepot and value added warehousing</td><td>3PLs, e commerce exporters</td><td>Free port provisions allow re export processing without import duty friction</td></tr>
    <tr><td>Bunkering and marine services</td><td>Fuel traders, ship chandlers, crewing</td><td>Hambantota and Colombo bunkering grow with every rerouted sailing</td></tr>
    <tr><td>Regional HQ with Port City treasury</td><td>Mid size carriers and 3PLs</td><td>Multi currency banking next to the port, SEZ incentives on the entity</td></tr>
    <tr><td>Ship repair and marine industry</td><td>Engineering firms</td><td>Colombo Dockyard under Indian ownership anchors a growing cluster</td></tr>
  </table></div>
  <p class="small" style="margin-top:16px">Sector data points: SLPA and industry reporting, 2025 to 2026. Verify current berth and zone terms per project.</p>
</div></section>
""" + cta_banner("Moving boxes through Colombo already?", "Then you should have an entity here. We connect you to port side partners, agents and the SEZ route.", "Hi%2C%20exploring%20a%20logistics%20setup%20in%20Sri%20Lanka"),
)

PAGES["second-home.html"] = dict(
    title="Sri Lanka as a Second Home for Indians: Visas, Cost of Living, Schools | Sri Lanka for Indians",
    desc="Make Sri Lanka your second destination: residence visa routes including the USD 100,000 property visa, what a month in Colombo costs, schools, healthcare and the one hour commute home to India.",
    body=f"""
<section class="hero"><div class="wrap">
  <span class="eyebrow">Second Destination</span>
  <h1>A second address, 400 km from home.</h1>
  <p class="lead">Dubai is 3,000 km away and had a complicated year. Singapore is expensive. Sri Lanka is an hour from Chennai, runs on English, takes UPI, and lets you build a base without leaving your parents a long flight behind. This is the quiet option smart families are taking seriously.</p>
  <div class="cta-row"><a class="btn btn-primary" href="{WA}?text=Hi%2C%20exploring%20Sri%20Lanka%20as%20a%20second%20home" rel="noopener">Plan your move</a></div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Ways to stay long term</h2>
  <div class="grid c3" style="margin-top:28px">
    <div class="card"><span class="tag">Property route</span><h3>Investor residence visa</h3><p>USD 100,000 or more into qualifying property supports a renewable 5 year residence visa. Buy the apartment, get the base.</p></div>
    <div class="card"><span class="tag">Business route</span><h3>Resident visa via your company</h3><p>Directors and key staff of registered businesses, including Port City entities, qualify for employment and investor visas.</p></div>
    <div class="card"><span class="tag">Flexible route</span><h3>Long stays without committing</h3><p>Tourist ETAs with extensions let you trial island life for months before you buy anything. Try one monsoon first. We mean it.</p></div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>What a month in Colombo really costs</h2>
  <div class="table-scroll" style="margin-top:24px"><table>
    <tr><th>Item</th><th class="num">Colombo (indicative)</th><th>Compare with</th></tr>
    <tr><td>3 bed sea view apartment rent</td><td class="num">&#8377;1.2 to 2.5 lakh</td><td>Half of comparable Mumbai, a third of Dubai Marina</td></tr>
    <tr><td>International school, per child per year</td><td class="num">&#8377;6 to 18 lakh</td><td>Below Dubai and Singapore brackets</td></tr>
    <tr><td>Full time driver and house help</td><td class="num">&#8377;45,000 to 80,000 total</td><td>Comparable with Indian metros</td></tr>
    <tr><td>Dinner for two, good restaurant</td><td class="num">&#8377;4,000 to 8,000</td><td>Goa beach shack to Bandra bistro range</td></tr>
    <tr><td>Flight home for a weekend</td><td class="num">&#8377;14,000 to 22,000 return</td><td>You can attend the Sunday family lunch</td></tr>
  </table></div>
  <p class="small" style="margin-top:16px">Indicative 2026 ranges from local listings and expat budgets. Exchange rates move; treat as planning bands.</p>
</div></section>

<section class="band"><div class="wrap">
  <h2>The honest trade offs</h2>
  <div class="grid c2" style="margin-top:28px">
    <div class="card"><span class="tag">You gain</span><h3>Time, air and ocean</h3><p>Shorter commutes, cleaner air than most metros, beaches 20 minutes from the office, and a pace that lets families actually see each other. Plus a hedge: assets and options outside one country's system, still an hour from home.</p></div>
    <div class="card"><span class="tag">You accept</span><h3>Emerging market life</h3><p>Imported goods cost more. Bureaucracy takes patience. The economy is recovering from a hard crisis and policies can shift. This works for people who plan properly, which is why you talk to us first.</p></div>
  </div>
</div></section>
""" + cta_banner("Want the Second Home starter pack?", "Visa checklist, 10 buildings we like, school list and a one week trial itinerary.", "Hi%2C%20send%20me%20the%20second%20home%20starter%20pack"),
)

PAGES["travel.html"] = dict(
    title="Sri Lanka Travel Guide for Indians: Visa, Itineraries, Ramayana Trail, Veg Food | Sri Lanka for Indians",
    desc="The Sri Lanka travel guide built for Indian travellers: ETA visa in hours, UPI payments, Ramayana trail, honeymoon and family itineraries, veg and Jain food, and long weekend plans from every metro.",
    body=f"""
<section class="hero"><div class="wrap">
  <span class="eyebrow">Travel</span>
  <h1>Closer than Goa feels on a Friday.</h1>
  <p class="lead">4.3 lakh Indians made the trip in the first nine months of 2026 and made India the island's number one market. Visa online in hours, UPI at the counter, and a country the size of Tamil Nadu packing beaches, leopards, blue whales, tea mountains and the world's most scenic train ride.</p>
  <div class="cta-row"><a class="btn btn-primary" href="{WA}?text=Hi%2C%20planning%20a%20Sri%20Lanka%20trip" rel="noopener">Get a custom itinerary</a></div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Pick your trip</h2>
  <div class="grid c3" style="margin-top:28px">
    <div class="card"><span class="tag">4 days</span><h3>The long weekend</h3><p>Colombo, Galle Fort, one beach town. Fly Friday morning, back Monday night. Works from Chennai and Bengaluru without burning leave.</p></div>
    <div class="card"><span class="tag">7 days</span><h3>The honeymoon classic</h3><p>Kandy, the Ella train, tea country, then two beach nights in Mirissa. The itinerary every Indian couple's Instagram is secretly made of.</p></div>
    <div class="card"><span class="tag">7 to 10 days</span><h3>The Ramayana trail</h3><p>Sita Amman temple, Ashok Vatika at Hakgala, Ravana Falls and more. A pilgrimage circuit with a holiday built around it. Huge with family groups.</p></div>
    <div class="card"><span class="tag">Family</span><h3>Trains, elephants, beaches</h3><p>Pinnawala, the hill train, turtle hatcheries, calm west coast beaches. Grandparents to toddlers, everyone gets a day.</p></div>
    <div class="card"><span class="tag">Wild</span><h3>Leopards and blue whales</h3><p>Yala safaris and Mirissa whale season. The only place this close to India where both fit in one week.</p></div>
    <div class="card"><span class="tag">Food</span><h3>Veg and Jain, sorted</h3><p>Kottu without egg, string hoppers, pure veg Indian restaurants in every tourist town. We keep a live veg and Jain food map for clients.</p></div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>The practicals Indians actually ask</h2>
  <div style="margin-top:24px; max-width:860px">
    <details><summary>Visa</summary><p>Apply at the official eta.gov.lk. Approvals usually land within hours. Sri Lanka has run free visa schemes for Indians; check the fee at application time. Carry the ETA printout or PDF.</p></details>
    <details><summary>Money and UPI</summary><p>UPI works at LankaQR merchants in cities and tourist areas. Carry some LKR cash for small vendors. Cards work in hotels and supermarkets.</p></details>
    <details><summary>Getting around</summary><p>PickMe is the local Ola. Intercity: hire a car with driver for the week, it costs less than you expect and the driver becomes your fixer. The hill train is an experience, book reserved seats early.</p></details>
    <details><summary>Best season</summary><p>West and south coasts shine December to April. East coast (Trinco, Arugam Bay) takes over May to September. There is always a good coast; that is the island's cheat code.</p></details>
    <details><summary>Safety</summary><p>Tourist areas are relaxed and used to Indian visitors. Normal travel sense applies. Solo women travellers rate it above most of South Asia.</p></details>
  </div>
</div></section>
""" + cta_banner("Want it planned for you?", "Tell us dates, group and budget. We send a day by day plan with real hotel prices in 48 hours, free.", "Hi%2C%20plan%20my%20Sri%20Lanka%20trip"),
)

# City pages -------------------------------------------------------------
CITIES = [
    ("chennai","Chennai","1 hr 20 min","₹7,000 to 14,000","Daily direct flights on IndiGo, Air India and SriLankan. The closest metro to the island, and the ferry to Jaffna leaves from your state.","Tamil works across the north and east of Sri Lanka and in much of Colombo. For Chennai families this is the easiest foreign country on earth."),
    ("mumbai","Mumbai","2 hr 30 min","₹9,000 to 18,000","Direct flights most days on SriLankan and Indian carriers.","Mumbai money is already here: shipping desks, film shoots and wedding planners all run Colombo routes."),
    ("delhi","Delhi NCR","3 hr 30 min","₹11,000 to 22,000","Direct flights on SriLankan and IndiGo.","Swap one Gurgaon winter smog week for Galle sea air. Many NCR firms are eyeing Port City as their India plus one."),
    ("bengaluru","Bengaluru","1 hr 45 min","₹8,000 to 16,000","Multiple daily directs. Weekend trips are genuinely practical.","Bengaluru tech teams are exactly who Port City is courting for business continuity centres."),
    ("hyderabad","Hyderabad","1 hr 50 min","₹8,000 to 16,000","Regular direct flights on IndiGo and SriLankan.","Pharma and IT firms from Hyderabad fit the island's GCC pitch, and Ramoji sized weddings fit its resorts."),
    ("kolkata","Kolkata","2 hr 45 min","₹10,000 to 21,000","Direct and one stop options via Chennai.","Durga Puja holidays line up with the start of the west coast season. Plan accordingly."),
    ("ahmedabad","Ahmedabad","2 hr 45 min","₹10,000 to 20,000","One stop via Mumbai or Chennai on most days.","Gujarati travel groups and diamond trade families were among the first to spot Colombo property prices."),
    ("pune","Pune","2 hr 45 min","₹9,000 to 18,000","Via Mumbai or direct seasonal services.","Pune's auto and IT exporters already ship through Colombo. Visit the port your containers transit."),
    ("kochi","Kochi","1 hr 10 min","₹6,500 to 13,000","Short hop directs; the fastest international flight many Malayalis will ever take.","Kerala and Sri Lanka share the coconut, the lagoon and the ayurveda economy. The island feels like home with leopards."),
    ("jaipur","Jaipur","4 hr (one stop)","₹12,000 to 24,000","Connections via Delhi or Mumbai.","Royal wedding planners from Jaipur are quietly adding Sri Lankan palaces and forts to their venue decks."),
    ("coimbatore","Coimbatore","1 hr 15 min","₹6,500 to 13,000","Short directs and Chennai connections.","Textile exporters from Tirupur move cargo through Colombo every week. The flight is shorter than the drive to Ooty."),
    ("lucknow","Lucknow","4 hr (one stop)","₹12,000 to 24,000","Connections via Delhi.","The Ramayana trail resonates nowhere more than UP. Group pilgrimages from Lucknow and Ayodhya are a growing route."),
]

CITY_BODY = """
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; From {name}</p>
  <span class="eyebrow">From {name}</span>
  <h1>Sri Lanka from {name}: {time} away.</h1>
  <p class="lead">{flights} Return fares typically run {fare} depending on season. {hook}</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="{wa}?text=Hi%2C%20I%27m%20from%20{name_enc}%2C%20planning%20Sri%20Lanka" rel="noopener">Plan from {name}</a>
    <a class="btn btn-ghost" href="../travel.html">See itineraries</a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>What people from {name} come for</h2>
  <div class="grid c3" style="margin-top:28px">
    <a class="card link-card" href="../weddings.html"><span class="tag">Weddings</span><h3>Destination weddings that beat Goa</h3><p>Run your guest list through our calculator, flights from {name} included.</p><span class="go">Compare costs &rarr;</span></a>
    <a class="card link-card" href="../real-estate.html"><span class="tag">Property</span><h3>Sea view condos priced in dollars</h3><p>What Indians can buy, the USD 100k visa route, and the current shortlist.</p><span class="go">See the rules &rarr;</span></a>
    <a class="card link-card" href="../business.html"><span class="tag">Business</span><h3>Port City incentives</h3><p>0% personal tax, holidays up to 15 years for approved businesses. The India plus one address.</p><span class="go">Read the numbers &rarr;</span></a>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>Quick facts for {name} travellers</h2>
  <div class="table-scroll" style="margin-top:24px"><table>
    <tr><th>Question</th><th>Answer</th></tr>
    <tr><td>Flight time</td><td>{time} to Colombo (BIA)</td></tr>
    <tr><td>Typical return fare</td><td class="num">{fare}</td></tr>
    <tr><td>Visa</td><td>Online ETA at eta.gov.lk, usually approved in hours</td></tr>
    <tr><td>Money</td><td>UPI at LankaQR merchants, cards widely accepted, carry some LKR</td></tr>
    <tr><td>Time difference</td><td>None. Sri Lanka runs on IST.</td></tr>
  </table></div>
</div></section>
"""

def city_page(slug, name, time, fare, flights, hook):
    name_enc = name.replace(" ", "%20")
    schema = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},{{"@type":"ListItem","position":2,"name":"From {name}","item":"{SITE}/from/{slug}.html"}}]}}</script>"""
    body = CITY_BODY.format(name=name, time=time, fare=fare, flights=flights, hook=hook, wa=WA, name_enc=name_enc)
    body += cta_banner(f"Flying from {name}?", "One message gets you a plan: trip, wedding, property or business. Your guide on the island replies the same day.", f"Hi%2C%20I%27m%20from%20{name_enc}")
    title = f"Sri Lanka from {name}: Flights, Cost, Weddings and Investment Guide | Sri Lanka for Indians"
    desc = f"Everything for {name} travellers and investors heading to Sri Lanka: {time} flight time, fares from {fare.split(' to ')[0]}, visa in hours, weddings, property and Port City business setup."
    return head(title, desc, f"from/{slug}.html", depth=1, schema=schema) + header(1) + body + footer(1)

# Write everything -------------------------------------------------------
written = []
for fname, pg in PAGES.items():
    html_out = head(pg["title"], pg["desc"], fname) + header() + pg["body"] + footer()
    if pg.get("calc"):
        html_out = html_out.replace("</body>", '<script src="assets/js/calculator.js"></script>\n</body>')
    with open(fname, "w") as f: f.write(html_out)
    written.append(fname)

os.makedirs("from", exist_ok=True)
for c in CITIES:
    path = f"from/{c[0]}.html"
    with open(path, "w") as f: f.write(city_page(*c))
    written.append(path)

# 404
with open("404.html", "w") as f:
    f.write(head("Page not found | Sri Lanka for Indians", "That page drifted out to sea.", "404.html")
        + header() + """
<section class="hero"><div class="wrap" style="text-align:center">
  <h1>Lost at sea.</h1>
  <p class="lead" style="margin-inline:auto">That page does not exist, or it sailed. The island is still here though.</p>
  <div class="cta-row" style="justify-content:center"><a class="btn btn-primary" href="index.html">Back to shore</a></div>
</div></section>
""" + footer())
written.append("404.html")

# sitemap + robots
today = datetime.date.today().isoformat()
urls = ["", *written]
urls = [u for u in urls if u != "404.html"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in ["index.html"] + [w for w in written if w not in ("404.html","index.html")]:
    loc = SITE + "/" + ("" if u == "index.html" else u)
    pr = "1.0" if u == "index.html" else ("0.9" if "/" not in u else "0.7")
    sm.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>")
sm.append("</urlset>")
with open("sitemap.xml","w") as f: f.write("\n".join(sm))
with open("robots.txt","w") as f: f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print("Built:", len(written)+2, "files")
