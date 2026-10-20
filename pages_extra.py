from sitekit import *
from media import VIDEOS, tagged, pick, reels, REELS
from home import tax_mega

def tax_page():
    vids = pick("hvOeE4eW8As", "GHGrijFEpgU", "GHyNEH0kQ3o")
    faqs = [
        ("What is the tax rate in Port City Colombo in 2026?", "Approved primary Businesses of Strategic Importance can receive corporate income tax holidays of 8 to 15 years after implementation, depending on investment size, under Regulation 01 of 2025. Secondary businesses can get a concessionary 7.5% corporate rate for 4 years. Other Port City companies pay normal Sri Lankan tax."),
        ("Is there still 0% personal income tax in Port City?", "Not for new companies. The Colombo Port City Economic Commission (Amendment) Act No. 1 of 2026, certified on 20 January 2026, made employment income taxable from day one for companies approved on or after that date. Companies approved earlier keep a staff exemption for a 3 year transition, until 31 January 2029."),
        ("How big does an investment need to be for the 15 year tax holiday?", "The longest holidays are reserved for the largest projects. Reporting in March 2026 described the full 15 years as applying to investments of USD 1 billion or more, with shorter holidays for lower tiers. Smaller approved businesses look at the secondary category: 7.5% for four years."),
        ("How does Port City compare with Dubai on tax?", "The UAE charges 9% corporate tax above AED 375,000 and no personal income tax. Port City offers corporate tax holidays or a 7.5% rate to approved strategic businesses, but staff of newly approved companies now pay normal Sri Lankan income tax."),
        ("Can Port City incentives change again?", "Yes. They were cut in 2023, restructured under Regulation 01 of 2025 and amended by Act No. 1 of 2026, which also introduced performance monitoring and reviews. Get your incentives written into your agreement before you invest."),
    ]
    rows = [
        ("Corporate tax (headline)", "25.17%", "17%", "9%", "0% for 8 to 15 yrs (primary BSI) or 7.5% for 4 yrs (secondary)"),
        ("Personal income tax (top)", "39%", "24%", "0%", "Normal Sri Lankan rates for staff of companies approved since 20 Jan 2026"),
        ("Foreign ownership", "Sector caps apply", "100%", "100% in most activity", "100%"),
        ("Flight from Chennai", "Home", "4 hr", "4 hr", "1 hr 20 min"),
    ]
    tbl = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td class='hl'>{e}</td></tr>" for a, b, c, d, e in rows)
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">Home</a> &rsaquo; Port City 7.5% tax</p>
  <span class="eyebrow">Port City Colombo &middot; 2026 rules</span>
  <h1>7.5% corporate tax. <em>Zero for the biggest bets.</em></h1>
  <p class="lead">Port City Colombo is a special economic zone with its own tax rulebook. Approved businesses can pay 7.5% corporate tax for their first four years, under a third of India's 25.17%. The largest projects, designated primary Businesses of Strategic Importance, pay nothing for 8 to 15 years, depending on how much they invest. Here is what changed in 2026, who qualifies, and what it is worth.</p>
  <div class="facts">
    <div class="fact"><b>7.5%</b><span>Corporate tax for approved secondary businesses, first 4 years of operations</span></div>
    <div class="fact"><b>0%</b><span>Corporate tax during the holiday for primary Businesses of Strategic Importance</span></div>
    <div class="fact"><b>8 to 15 yrs</b><span>Holiday length, scaled to investment. The full 15 years is for the largest projects</span></div>
  </div>
  <p class="source">Regulation 01 of 2025 (effective 30 September 2025 for five years) and the Colombo Port City Economic Commission (Amendment) Act No. 1 of 2026, certified 20 January 2026.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="cta-banner" style="background:var(--card); color:var(--ink); border-color:var(--gold)">
    <div style="max-width:72ch">
      <span class="eyebrow">What changed in January 2026</span>
      <h2 style="color:var(--ink)">The staff tax exemption is gone <em>for new companies.</em></h2>
      <p style="color:var(--ink-soft)">Until 2026, staff of approved Port City companies paid no personal income tax. The Amendment Act No. 1 of 2026 ended that for companies approved on or after 20 January 2026: their employees are taxed from day one. Companies approved before that keep the exemption for a three year transition, from 1 February 2026 to 31 January 2029. Corporate tax holidays for strategic investments remain, now with performance monitoring and reviews.</p>
    </div>
  </div>
</div></section>

<section class="band sand" id="calc"><div class="wrap">
  <span class="eyebrow">What is the holiday worth?</span>
  <h2>Your profits, <em>India against Port City.</em></h2>
  <p class="lead">Set your expected annual profit and the category you might qualify for. We compare corporate tax over the holiday period at India's headline rate against Port City's.</p>
  <div class="taxcalc" style="margin-top:34px">
    <div class="calc-grid">
      <div class="field"><label for="cc-profit">Annual profit</label><span class="tc-val num" id="cc-profit-out">&#8377;25 Cr</span>
        <input type="range" id="cc-profit" min="1" max="500" step="1" value="25" aria-label="Annual profit in crore rupees"></div>
      <div class="field"><label for="cc-route">Port City category</label>
        <select id="cc-route">
          <option value="p15">Primary BSI, 15 year holiday (largest projects)</option>
          <option value="p12">Primary BSI, 12 year holiday</option>
          <option value="p10">Primary BSI, 10 year holiday</option>
          <option value="p8">Primary BSI, 8 year holiday</option>
          <option value="s4" selected>Secondary BSI, 7.5% for 4 years</option>
        </select></div>
    </div>
    <div class="tc-row">
      <div class="tc-cell"><span>Corporate tax in India over <span id="cc-years">4</span> years</span><b class="num" id="cc-india">&#8377;0</b><span>At 25.17% headline</span></div>
      <div class="tc-cell"><span>Corporate tax in Port City</span><b class="num" id="cc-pc">&#8377;0</b><span id="cc-pc-note">During the holiday</span></div>
      <div class="tc-cell gold"><span>Tax saved over the period</span><b class="num" id="cc-save">&#8377;0</b><span>Before dividend tax in India</span></div>
    </div>
    <p class="small" style="margin-top:18px">Illustrative only, using flat profits. Holidays start after the project implementation period and require designation as a Business of Strategic Importance, which depends on investment size and approval. Dividends paid back to Indian shareholders are taxed in India. Under India's place of effective management rule, a foreign company run day to day from India can be taxed as Indian. Talk to your CA and a Colombo tax advisor.</p>
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
    <div class="step"><h3>Size the project</h3><p>Primary Businesses of Strategic Importance fall into four categories by investment and jobs, with holidays of 8, 10, 12 or 15 years. Below those thresholds, the secondary route offers 7.5% for four years.</p></div>
    <div class="step"><h3>Apply to the Commission</h3><p>The Colombo Port City Economic Commission is the single window. Incentives now need Ministry of Finance analysis and carry performance conditions.</p></div>
    <div class="step"><h3>Sign the agreement</h3><p>Get the category, holiday years and conditions in your agreement before money moves. Since 2026, missed performance targets can lead to incentives being suspended or withdrawn.</p></div>
    <div class="step"><h3>Budget payroll properly</h3><p>Staff of newly approved companies pay normal Sri Lankan income tax, so plan salaries and relocation packages on that basis.</p></div>
    <div class="step"><h3>Structure the India side</h3><p>Overseas Direct Investment from India runs under RBI rules. Your CA handles the Indian filings; we introduce the Colombo lawyers.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">See Port City</span>
  <h2>Walk the zone <em>before you fly.</em></h2>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">Straight answers</span>
  <div style="margin-top:20px; max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
</div></section>
""" + cta_banner("Want to know which category you would fall into?", "Send us what you do and how much you plan to invest. We reply with the likely route and the next three steps.", "Hi, I want to understand Port City tax incentives for my business")
    schema = crumb_schema([("Port City 7.5% tax", "port-city-tax.html")]) + "\n" + faq_schema(faqs) + "\n" + video_schema(vids)
    return head("Port City Colombo Tax 2026: 7.5% Corporate Tax Explained",
                "Port City Colombo tax in 2026, explained for Indians: 7.5% corporate tax for approved businesses, 0% for 8 to 15 years on the largest projects, and the end of the staff income tax exemption for new companies. Profit calculator included.",
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
  <div style="margin-top:32px">{ig_grid(REELS)}</div>
</div></section>
""" + cta_banner("Seen enough?", "Tell us which video made you want to go. We will plan the trip, the wedding or the move around it.", "Hi, I watched your videos and want to plan Sri Lanka")
    schema = crumb_schema([("Watch", "watch.html")]) + "\n" + video_schema(all_vids)
    return head("Sri Lanka Videos by Indian Creators | Sri Lanka for Indians",
                "Watch Sri Lanka through Indian eyes: travel vlogs by Indian creators, destination weddings, Think School with Kumar Sangakkara on real estate, Port City walkthroughs, Ramayana trail and more.",
                "watch.html", 0, schema) + header() + body + footer()

def build(write):
    write("port-city-tax.html", tax_page())
    write("watch.html", watch_page())
