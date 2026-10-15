from sitekit import *
from media import VIDEOS, tagged, pick, reels, REELS
from home import tax_mega

def tax_page():
    vids = pick("hvOeE4eW8As", "GHGrijFEpgU", "GHyNEH0kQ3o")
    faqs = [
        ("What is the tax rate in Port City Colombo?", "Under Regulation 01 of 2025, primary Businesses of Strategic Importance can receive corporate income tax holidays of 8 to 15 years depending on investment, secondary businesses a concessionary 7.5% corporate rate for 4 years, and staff of approved businesses have paid 0% personal income tax. All incentives require approval from the Colombo Port City Economic Commission."),
        ("Is Port City Colombo tax free for Indians?", "The incentives apply to approved businesses in the zone regardless of the owner's nationality. Whether an individual Indian pays tax in India depends on Indian tax residency: residents are taxed on global income. Consult a chartered accountant."),
        ("How does Port City compare with Dubai on tax?", "Both offer 0% personal income tax. The UAE charges 9% corporate tax above AED 375,000, with 0% possible on qualifying free zone income, while Port City offers multi year holidays or a 7.5% rate for approved businesses."),
        ("Can Port City incentives change?", "Yes. Incentives were revised in 2023 and again under Regulation 01 of 2025, and commentators have flagged possible changes to the personal tax exemption. Lock in terms in writing with the Commission before you invest."),
    ]
    rows = [
        ("Corporate tax (headline)", "25.17%", "17%", "9%", "8 to 15 yr holiday, or 7.5%"),
        ("Top personal income tax", "39%", "24%", "0%", "0%"),
        ("Foreign ownership", "Sector caps apply", "100%", "100% in most activity", "100%"),
        ("Flight from Chennai", "Home", "4 hr", "4 hr", "1 hr 20 min"),
    ]
    tbl = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td class='hl'>{e}</td></tr>" for a, b, c, d, e in rows)
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">Home</a> &rsaquo; Port City 0% tax</p>
  <span class="eyebrow">Port City Colombo</span>
  <h1>Zero. <em>The most important number on this site.</em></h1>
  <p class="lead">Port City Colombo is a special economic zone with its own tax rulebook. Approved enterprises get corporate tax holidays of up to 15 years, and their staff have paid nothing in personal income tax. Here is exactly how it works, and what it is worth to you.</p>
  <div class="facts">
    <div class="fact"><b>0%</b><span>Personal income tax for staff of approved businesses</span></div>
    <div class="fact"><b>8 to 15 yrs</b><span>Corporate tax holidays for primary Businesses of Strategic Importance</span></div>
    <div class="fact"><b>7.5%</b><span>Concessionary corporate rate for secondary businesses, 4 years</span></div>
  </div>
  <p class="source">Regulation 01 of 2025 under the Colombo Port City Economic Commission framework, effective 30 September 2025 for five years (KPMG summary).</p>
</div></section>

<section class="band" id="calc"><div class="wrap">
  <span class="eyebrow">What would you keep?</span>
  <h2>Your salary, <em>India against Port City.</em></h2>
  <p class="lead">Move the slider to your annual salary. We calculate Indian income tax under the new regime for FY 2025-26, and set it against Port City's zero.</p>
  <div class="taxcalc" style="margin-top:34px">
    <label for="tc-salary" class="field" style="display:block"><span style="display:block; font-size:.66rem; letter-spacing:.32em; text-transform:uppercase; color:var(--gold); margin-bottom:8px">Annual salary</span><span class="tc-val num" id="tc-out-salary">&#8377;50 L</span></label>
    <input type="range" id="tc-salary" min="10" max="500" step="5" value="50" aria-label="Annual salary in lakh rupees">
    <div class="tc-row">
      <div class="tc-cell"><span>Income tax in India (new regime)</span><b class="num" id="tc-india">&#8377;0</b><span id="tc-rate"></span></div>
      <div class="tc-cell"><span>Personal tax inside Port City</span><b class="num">&#8377;0</b><span>0% for approved firms' staff</span></div>
      <div class="tc-cell gold"><span>You would keep, every year</span><b class="num" id="tc-keep">&#8377;0</b><span>Over 5 years: <span id="tc-5yr" class="num">&#8377;0</span></span></div>
    </div>
    <p class="small" style="margin-top:18px">Illustrative only. Uses FY 2025-26 new regime slabs, &#8377;75,000 standard deduction, section 87A rebate, surcharge and 4% cess. The saving applies only if you are not an Indian tax resident: broadly, under 182 days a year in India, with extra rules for high earning citizens. Indian residents are taxed on global income. Talk to your CA.</p>
  </div>
</div></section>

{tax_mega()}

<section class="band"><div class="wrap">
  <span class="eyebrow">Side by side</span>
  <h2>India, Singapore, Dubai, <em>Port City.</em></h2>
  <div class="table-scroll" style="margin-top:30px"><table>
    <tr><th></th><th>India</th><th>Singapore</th><th>UAE</th><th class="hl">Port City Colombo</th></tr>
    {tbl}
  </table></div>
  <p class="small" style="margin-top:12px">Headline rates. India: 22% plus 10% surcharge plus 4% cess for domestic companies; top personal rate 30% plus up to 25% surcharge plus 4% cess under the new regime. UAE corporate tax 9% above AED 375,000. Effective rates depend on structure.</p>
  <p style="margin-top:22px"><a class="btn btn-ghost" href="guides/port-city-vs-gift-city-vs-dubai.html">Add GIFT City to the comparison</a></p>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">How to qualify</span>
  <h2>Getting the incentives <em>in writing.</em></h2>
  <div class="steps" style="margin-top:30px; max-width:780px">
    <div class="step"><h3>Pick the category</h3><p>Primary Businesses of Strategic Importance get the long holidays; secondary businesses get 7.5%. The category depends on what you do and how much you invest.</p></div>
    <div class="step"><h3>Apply to the Commission</h3><p>The Colombo Port City Economic Commission is the single window. Your application sets out investment, jobs and activity.</p></div>
    <div class="step"><h3>Sign the agreement</h3><p>Incentives are granted per business. Get the terms, years and conditions in your agreement before money moves.</p></div>
    <div class="step"><h3>Structure the India side</h3><p>Overseas Direct Investment from India runs under RBI rules. Your CA handles the Indian filings; we introduce the Colombo lawyers.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">See Port City</span>
  <h2>Walk the zone <em>before you fly.</em></h2>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
  <h3 style="margin-top:50px">In the news</h3>
  <div style="margin-top:18px; max-width:420px">{ig_grid(reels('tax'))}</div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">Straight answers</span>
  <div style="margin-top:20px; max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
</div></section>
""" + cta_banner("Want the incentives mapped to your business?", "Send us what you do and how big. We reply with the likely category and the next three steps.", "Hi, I want to understand Port City tax incentives for my business")
    schema = crumb_schema([("Port City 0% tax", "port-city-tax.html")]) + "\n" + faq_schema(faqs) + "\n" + video_schema(vids)
    return head("Port City Colombo Tax: 0% Personal Income Tax, 15 Year Holidays, Calculator | Sri Lanka for Indians",
                "Port City Colombo tax explained for Indians: 0% personal income tax for approved firms' staff, 8 to 15 year corporate tax holidays, 7.5% rate for secondary businesses. Salary calculator against Indian tax.",
                "port-city-tax.html", 0, schema, alt={"en": "port-city-tax.html", "hi": "hi/port-city-tax.html"}) \
        + header(alt_path="hi/port-city-tax.html") + body + footer()

def watch_page():
    sections = [
        ("Indian creators on Sri Lanka", "Travel vloggers, celebrities and food shows from India.", tagged("creators")),
        ("Weddings", "Indian and Tamil destination weddings, and why they matter to the island.", tagged("wedding")),
        ("Business, Port City and the comeback", "Explainers from Indian business channels and walk throughs of the new district.", sorted(tagged("business") + [v for v in tagged("portcity") if "business" not in v["tags"]], key=lambda v: -v["views"])),
        ("Guides: visas, costs and getting there", "Practical videos for planning from India.", sorted(tagged("guide") + tagged("visa") + tagged("ferry"), key=lambda v: -v["views"])),
        ("Sectors: spices, tea, gems, apparel and ports", "The industries behind the island.", sorted(tagged("spices") + tagged("tea") + tagged("gems") + tagged("apparel") + tagged("ports") + tagged("bpo"), key=lambda v: -v["views"])),
        ("Ramayana trail, wellness and wildlife", "Pilgrimage, Ayurveda and leopards.", sorted(tagged("ramayana") + tagged("wellness") + tagged("wildlife"), key=lambda v: -v["views"])),
        ("The island from above", "Cinematic films to fall for first.", tagged("scenic")),
    ]
    seen, blocks, all_vids = set(), "", []
    for t, sub, vids in sections:
        vids = [v for v in vids if v["id"] not in seen]
        for v in vids: seen.add(v["id"])
        all_vids += vids
        blocks += f"""<section class="band{' sand' if len(blocks) % 2 else ''}"><div class="wrap">
  <h2>{t}</h2><p class="lead">{sub}</p>
  <div style="margin-top:32px">{yt_grid(vids)}</div>
</div></section>
"""
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">Home</a> &rsaquo; Watch</p>
  <span class="eyebrow">Watch</span>
  <h1>India, <em>on Sri Lanka.</em></h1>
  <p class="lead">{len(all_vids)} videos and {len(REELS)} Instagram reels from Indian creators, couples, business channels and the island itself, with more than {sum(v['views'] for v in all_vids)//10_000_000} crore views between them. Tap any video to play it here.</p>
</div></section>
{blocks}
<section class="band"><div class="wrap">
  <h2>On Instagram</h2><p class="lead">Reels from travellers and wedding creators.</p>
  <div style="margin-top:32px">{ig_grid([r for r in REELS if r['tag'] != 'tax'])}</div>
</div></section>
""" + cta_banner("Seen enough?", "Tell us which video made you want to go. We will plan the trip, the wedding or the move around it.", "Hi, I watched your videos and want to plan Sri Lanka")
    schema = crumb_schema([("Watch", "watch.html")]) + "\n" + video_schema(all_vids)
    return head("Sri Lanka Videos by Indian Creators: Travel, Weddings, Port City | Sri Lanka for Indians",
                "Watch Sri Lanka through Indian eyes: travel vlogs by Indian creators, destination weddings, Think School with Kumar Sangakkara on real estate, Port City walkthroughs, Ramayana trail and more.",
                "watch.html", 0, schema) + header() + body + footer()

def build(write):
    write("port-city-tax.html", tax_page())
    write("watch.html", watch_page())
