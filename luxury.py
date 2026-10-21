"""Luxury and nightlife section: Colombo for the wealthy Indian weekend.
Hard line: no gambling tips and no help moving money for gambling."""
import re
from sitekit import *
from media import pick
from cities import ALL_CITIES

D = 1  # pages live in /luxury/

RESPONSIBLE = ("<p class=\"small resp\">Casinos in Sri Lanka are for adults only. Set a limit before you go in and treat it as entertainment. "
               "Indian forex cards and LRS remittances cannot be used for gambling, so we do not arrange gaming funds, credit or junkets.</p>")

def vip_form(occasion=""):
    cities = "".join(f'<option>{c[1]}</option>' for c in ALL_CITIES) + "<option>Elsewhere</option>"
    occ = ["Luxury weekend", "Bachelor party", "Bachelorette", "Anniversary or honeymoon", "Birthday", "Corporate offsite", "New Year's Eve"]
    occ_html = "".join(f'<option{" selected" if o == occasion else ""}>{o}</option>' for o in occ)
    wants = ["Suite at City of Dreams", "Sea view suite elsewhere", "Yacht or boat day", "Fine dining", "Nightlife tables",
             "Spa", "Golf", "Concert or cricket tickets", "Private car and driver"]
    wants_html = "".join(f'<label class="chk"><input type="checkbox" name="w" value="{w}"><span>{w}</span></label>' for w in wants)
    return f"""<form class="calc vip" id="vip" onsubmit="return false">
  <div class="calc-grid">
    <div class="field"><label for="vip-from">Flying from</label><select id="vip-from">{cities}</select></div>
    <div class="field"><label for="vip-when">When</label><input id="vip-when" type="text" placeholder="e.g. 12 to 14 Dec"></div>
    <div class="field"><label for="vip-guests">Guests</label><input id="vip-guests" type="number" min="1" value="2"></div>
    <div class="field"><label for="vip-occ">Occasion</label><select id="vip-occ">{occ_html}</select></div>
    <div class="field"><label for="vip-budget">Budget per person</label><select id="vip-budget">
      <option>&#8377;1 to 2 lakh</option><option selected>&#8377;2 to 5 lakh</option><option>&#8377;5 lakh and up</option></select></div>
  </div>
  <fieldset class="vip-wants"><legend>What should we line up?</legend>{wants_html}</fieldset>
  <div class="field" style="margin-top:18px"><label for="vip-notes">Anything else</label><input id="vip-notes" type="text" placeholder="Veg or Jain food, a surprise, a show you want to catch"></div>
  <div class="cta-row" style="margin-top:26px"><button class="btn btn-primary" id="vip-send" type="button">Send on WhatsApp</button>
  <span class="small">Opens WhatsApp with your plan filled in. A real person replies the same day.</span></div>
</form>
<script>
(function(){{
  var b=document.getElementById('vip-send'); if(!b) return;
  b.addEventListener('click',function(){{
    function v(id){{var e=document.getElementById(id);return e?e.value.trim():'';}}
    var w=[].slice.call(document.querySelectorAll('#vip input[name=w]:checked')).map(function(x){{return x.value;}});
    var t='Hi, I want a VIP weekend in Colombo.\\n'+
      'Flying from: '+v('vip-from')+'\\nWhen: '+(v('vip-when')||'flexible')+'\\nGuests: '+v('vip-guests')+
      '\\nOccasion: '+v('vip-occ')+'\\nBudget per person: '+v('vip-budget').replace('\\u20B9','Rs ')+
      (w.length?'\\nLine up: '+w.join(', '):'')+(v('vip-notes')?'\\nNotes: '+v('vip-notes'):'');
    if(typeof gtag==='function') gtag('event','generate_lead',{{method:'vip_form',occasion:v('vip-occ'),page_path:location.pathname}});
    window.open('{WA}?text='+encodeURIComponent(t),'_blank','noopener');
  }});
}})();
</script>"""

def hub():
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; Luxury</p>
  <span class="eyebrow">Luxury and nightlife</span>
  <h1>Colombo, <em>after dark.</em></h1>
  <p class="lead">Suites over the Indian Ocean, a billion dollar integrated resort, sunsets on the Port City promenade and tables at the city's best rooms. All of it 80 minutes from Chennai, on Indian time, with a free visa. Tell us the weekend you want and we line it up.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#plan">Plan a VIP weekend</a></div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">The new address</span>
  <h2>South Asia's first <em>integrated resort.</em></h2>
  <p class="lead">City of Dreams Sri Lanka, built by Macau's Melco and John Keells for more than USD 1.2 billion, had its grand opening in Colombo in August 2025: 800 rooms across two hotels, a luxury mall, ballrooms, 17 restaurants and bars, and a casino. It changed what a Colombo weekend can be.</p>
  <div class="grid c3" style="margin-top:36px">
    <a class="card link-card" href="city-of-dreams-sri-lanka.html"><span class="tag">The resort</span><h3>City of Dreams, explained</h3><p>Two hotels, 17 places to eat, shows, and the casino's entry rules.</p><span class="go">Read the guide &rarr;</span></a>
    <a class="card link-card" href="luxury-weekend-in-colombo.html"><span class="tag">Two nights</span><h3>The luxury weekend</h3><p>ITC Ratnadipa or Nüwa, Ministry of Crab, a private yacht at sunset.</p><span class="go">See the plan &rarr;</span></a>
    <a class="card link-card" href="colombo-nightlife.html"><span class="tag">After dark</span><h3>Colombo nightlife</h3><p>Rooftops, supper clubs and the rules that catch first timers out.</p><span class="go">Where to go &rarr;</span></a>
    <a class="card link-card" href="bachelor-party-in-colombo.html"><span class="tag">Groups</span><h3>Bachelor and bachelorette</h3><p>The two night plan: rooftops, a boat, Bentota and a big Saturday.</p><span class="go">Plan the weekend &rarr;</span></a>
    <a class="card link-card" href="events-calendar.html"><span class="tag">Dates</span><h3>Events calendar</h3><p>Deepavali to New Year's Eve and the temple processions after.</p><span class="go">See what is on &rarr;</span></a>
    <a class="card link-card" href="../guides/new-year-in-sri-lanka-from-india.html"><span class="tag">31 December</span><h3>New Year in Colombo</h3><p>Fireworks over Galle Face and Port City, galas and beach parties.</p><span class="go">Plan New Year &rarr;</span></a>
  </div>
  {RESPONSIBLE}
</div></section>

<section class="band ink"><div class="wrap">
  <span class="eyebrow">On film</span>
  <h2>Indians who <em>went first.</em></h2>
  <div style="margin-top:36px">{yt_grid(pick("FDoDcwf_pDc","3oVYpDEXeLU","zqba47Zl-Wk"))}</div>
</div></section>

<section class="band sand" id="plan"><div class="wrap">
  <span class="eyebrow">VIP weekend concierge</span>
  <h2>Tell us the weekend. <em>We handle the rest.</em></h2>
  <p class="lead" style="margin-bottom:28px">Flights, suites, transfers, tables, a boat, a show. One message, one person on the island who answers it.</p>
  {vip_form()}
</div></section>
""" + cta_banner("Rather just talk?", "Message us on WhatsApp with the dates and the mood. We reply the same day.", "Hi, I want to plan a luxury weekend in Colombo")
    schema = crumb_schema([("Luxury", "luxury/index.html")]) + "\n" + video_schema(pick("FDoDcwf_pDc","3oVYpDEXeLU","zqba47Zl-Wk"))
    return head("Colombo Luxury Weekends and Nightlife for Indians",
                "Plan a luxury weekend in Colombo from India: City of Dreams suites, Port City marina, fine dining and nightlife, 80 minutes from Chennai. Send your plan on WhatsApp.",
                "luxury/index.html", D, schema) + header(D) + body + footer(D)

def lux_page(slug, crumb, title, desc, eyebrow, h1, lead, body, faqs, vids=(), occasion="", responsible=False, source=""):
    vids = pick(*vids) if vids else []
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    built = {k for k, _ in PAGES}
    others = "".join(f'<a href="{s_}.html">{c_}</a>' for s_, c_ in NAV if s_ != slug and s_ in built)
    vid_block = f"""<section class="band sand"><div class="wrap">
  <span class="eyebrow">On film</span>
  <h2>See it <em>before you fly.</em></h2>
  <div style="margin-top:36px">{yt_grid(vids, 'c3' if len(vids) > 2 else 'c2')}</div>
</div></section>""" if vids else ""
    page_body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; <a href="index.html">Luxury</a> &rsaquo; {crumb}</p>
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <div class="cta-row"><a class="btn btn-primary" href="#plan">Plan it with us</a></div>
</div></section>
<section class="band"><div class="wrap prose">
{body}
{RESPONSIBLE if responsible else ""}
{f'<p class="source">{source}</p>' if source else ""}
</div></section>
{vid_block}
<section class="band" id="plan"><div class="wrap">
  <span class="eyebrow">VIP weekend concierge</span>
  <h2>Send us the plan. <em>We line it up.</em></h2>
  <div style="margin-top:26px">{vip_form(occasion)}</div>
</div></section>
<section class="band sand"><div class="wrap">
  <span class="eyebrow">Quick answers</span>
  <div style="margin-top:20px; max-width:880px">{faq_html}</div>
  <h3 style="margin-top:44px">More from Colombo after dark</h3>
  <div class="chips" style="margin-top:16px">{others}<a href="../guides/new-year-in-sri-lanka-from-india.html">New Year in Sri Lanka</a></div>
</div></section>
""" + cta_banner("Rather just talk?", "Message us on WhatsApp with the dates and the mood. We reply the same day.", f"Hi, I read your page on {crumb}")
    schema = crumb_schema([("Luxury", "luxury/index.html"), (crumb, f"luxury/{slug}.html")]) + "\n" + faq_schema(faqs)
    if vids: schema += "\n" + video_schema(vids)
    return head(title, desc, f"luxury/{slug}.html", D, schema) + header(D) + page_body + footer(D)


def nightlife():
    body = """<h2>Where Colombo goes out</h2>
<div class="table-scroll"><table>
<tr><th>Venue</th><th>Where</th><th>What it is</th></tr>
<tr><td>Gatz</td><td>City of Dreams, Colombo 2</td><td>A supper club with live bands every night; Terry and The Big Spenders play Thursday to Sunday</td></tr>
<tr><td>Flux</td><td>Cinnamon Life, level 24</td><td>Rooftop with DJs, high above the city</td></tr>
<tr><td>Pool + Bar 09</td><td>Cinnamon Life, level 9</td><td>Pool deck bar for sundowners</td></tr>
<tr><td>Sky Lounge</td><td>The Kingsbury, Colombo 1</td><td>Rooftop with skyline and harbour views, live bands on big nights</td></tr>
<tr><td>Honey Beach Club</td><td>The Kingsbury</td><td>Beach club on the hotel's seafront</td></tr>
<tr><td>ON14</td><td>Radisson Colombo, Marine Drive</td><td>Open air rooftop over the ocean, DJ nights every Friday and Saturday</td></tr>
<tr><td>Vistas Rooftop Bar</td><td>NH Collection Colombo</td><td>Relaunched in December 2025 with near panoramic city views</td></tr>
<tr><td>Level 4</td><td>Canal Row, Colombo 1, opposite the World Trade Centre</td><td>Rooftop bar and restaurant with live music, opened April 2025</td></tr>
<tr><td>SunsetBlu</td><td>Hilton Colombo</td><td>Pool bar by evening, nightclub later</td></tr>
<tr><td>Tiki Bar</td><td>Shangri-La Colombo</td><td>Overlooks Galle Face, with a Sri Lankan cocktail menu</td></tr>
<tr><td>Chill Colombo</td><td>The Mall at Port City</td><td>Two storey bar and restaurant for 150 plus, with live music and DJs</td></tr>
</table></div>
<p class="small">Venues confirmed open in 2025 and 2026 reporting. Line ups change weekly; we confirm the night before you go.</p>
<h2>Worth the drive: Smoke &amp; Bitters</h2>
<p>On the south coast at Dikwella, Smoke &amp; Bitters ranked number 14 on Asia's 50 Best Bars in 2025. Pair it with a beach night if you head down to Tangalle or Mirissa.</p>
<h2>Rules worth knowing</h2>
<ul><li><strong>Age:</strong> you must be 21 to buy alcohol in Sri Lanka.</li>
<li><strong>Hours:</strong> hotel bars generally run to midnight, and up to 2 am where the licence allows. Most of the venues above sit in hotels.</li>
<li><strong>Poya days:</strong> bars and liquor shops close on every full moon Poya day. Coming up: 24 November and 23 December 2026, then 22 January and 20 February 2027. Some licensed tourist hotels have been allowed to serve on specific dates, but plan your big night around the Poya.</li>
<li><strong>Happy hours:</strong> the national alcohol authority has told hotels that discounted drinks are an offence, so expect fewer two for one deals than in Goa or Bangkok.</li>
<li><strong>Getting home:</strong> PickMe and Uber work across Colombo. For groups, keep the driver.</li></ul>"""
    faqs = [("What is the nightlife like in Colombo?","Colombo nightlife centres on hotel rooftops, supper clubs and lounges rather than big standalone clubs. Cinnamon Life and City of Dreams, The Kingsbury, the Radisson's ON14 rooftop, Hilton's SunsetBlu and the Shangri-La's Tiki Bar are the main names in 2026."),
            ("What is the drinking age in Sri Lanka?","21. Selling alcohol to anyone under 21 is prohibited under the National Authority on Tobacco and Alcohol Act."),
            ("What time do bars close in Colombo?","Hotel bars generally close at midnight, extended to 2 am where the licence allows. Most of Colombo's nightlife is in hotels."),
            ("Are bars open on Poya days in Sri Lanka?","No. Bars and liquor shops close on every full moon Poya day, about once a month. Check the date before you plan a big night."),
            ("Is Colombo nightlife safe for Indian groups?","Yes for the hotel venues listed here. Use PickMe, Uber or your own driver to get around, and keep an eye on drinks as you would anywhere.")]
    return lux_page("colombo-nightlife", "Colombo nightlife", "Colombo Nightlife 2026: Rooftops, Clubs and Bars for Indians",
        "Where to go out in Colombo in 2026: rooftop bars, supper clubs and lounges at City of Dreams, Kingsbury, Hilton and Port City. Drinking age, closing times and Poya day rules.",
        "Colombo after dark", "Colombo nightlife, <em>2026 edition.</em>",
        "Colombo goes out on rooftops and in supper clubs, not in mega clubs. Here is where the city actually spends its Friday nights, and the rules that catch first timers out.",
        body, faqs, vids=("PnfdGFtZOPI","IzKwdP6hcLY","9119VUOlspA"), occasion="Luxury weekend",
        source="Sources: EconomyNext and Sunday Times on Gatz (2026); Daily FT on Cinnamon Life and Vistas (December 2025); Hayleys on The Kingsbury; Sunday Observer on ON14 (2025); Newswire on Level 4 (2025); The Morning on Tiki Bar (2026); Life.lk on Chill Colombo; Asia's 50 Best Bars 2025; NATA Act No. 27 of 2006; Newsfirst and Ada Derana on liquor hours and Poya closures.")

def bachelor():
    body = """<h2>A two night plan that works</h2>
<div class="table-scroll"><table>
<tr><th>When</th><th>Plan</th></tr>
<tr><td>Friday afternoon</td><td>Land in Colombo, check in at City of Dreams, The Kingsbury or a Galle Face hotel. Pool time</td></tr>
<tr><td>Friday sunset</td><td>Rooftop drinks at ON14 or Flux at Cinnamon Life</td></tr>
<tr><td>Friday night</td><td>Dinner, then live music at Gatz supper club or DJs at SunsetBlu</td></tr>
<tr><td>Saturday day</td><td>A crewed catamaran sail, or a day in Bentota for jet skis, water skiing and donut rides on the river</td></tr>
<tr><td>Saturday night</td><td>The big night: a reserved table at Sky Lounge or Flux, with the group's driver on standby</td></tr>
<tr><td>Sunday</td><td>Late brunch, Tiki Bar at the Shangri-La for one last view of Galle Face, fly home</td></tr>
</table></div>
<h2>On the water</h2>
<p>Sail Lanka Charter runs crewed catamarans from Colombo, Mirissa and Trincomalee, by the hour, day or week, including sunset sails. Port City's new marina is still being built and is due in 2027, so confirm the departure point when you book.</p>
<h2>For the bachelorette</h2>
<ul><li>Spa morning at your hotel, then a long lunch by the pool.</li>
<li>Shopping at One Galle Face and The Mall at Port City.</li>
<li>Sundowners at Vistas or Level 4, dinner, then the supper club.</li>
<li>A south coast extension: two nights in a Galle or Tangalle villa, and Smoke &amp; Bitters at Dikwella.</li></ul>
<h2>Group logistics</h2>
<ul><li><strong>Visa:</strong> the tourist ETA is free for Indians. Each person applies on eta.gov.lk.</li>
<li><strong>Dates:</strong> avoid Poya days, when bars close. Next: 24 November and 23 December 2026, 22 January and 20 February 2027.</li>
<li><strong>Age:</strong> everyone needs to be 21 to drink.</li>
<li><strong>Getting around:</strong> one van and driver for the whole weekend beats six cabs.</li>
<li><strong>Casino:</strong> City of Dreams has one. It is optional, adults only, and a night out is not a strategy. Agree a limit as a group.</li></ul>"""
    faqs = [("Is Colombo good for a bachelor party from India?","Yes for a short, high end weekend: two nights of rooftops, a supper club, a boat or Bentota water sports day, and five star hotels, 80 minutes from Chennai with a free visa."),
            ("How many days do you need for a bachelor weekend in Colombo?","Two nights covers it. Add two nights on the south coast for a longer trip."),
            ("Can we hire a yacht in Colombo?","Crewed catamaran sails run from Colombo, Mirissa and Trincomalee. Port City's marina is due in 2027, so confirm the departure point when you book."),
            ("What should groups avoid when planning?","Poya days, when bars close, and arriving without a driver for the group. Book tables at the rooftop bars ahead on Friday and Saturday.")]
    return lux_page("bachelor-party-in-colombo", "Bachelor and bachelorette weekends", "Bachelor Party in Colombo from India: The 2 Night Plan",
        "Plan a bachelor or bachelorette weekend in Colombo from India: rooftops, a supper club, a catamaran or Bentota water sports day, and five star stays. Visa, Poya days and group tips.",
        "Bachelor and bachelorette", "The last weekend, <em>done properly.</em>",
        "Goa is crowded and Bangkok is four hours away. Colombo is 80 minutes from Chennai, the visa is free, and the whole weekend fits into five star hotels, a boat and three very good rooftops.",
        body, faqs, vids=("zqba47Zl-Wk","bu0jyUlkwdc","PnfdGFtZOPI"), occasion="Bachelor party", responsible=True,
        source="Sources: venue and charter details from EconomyNext, Daily FT, Sunday Observer and Booking Manager on Sail Lanka Charter; Sunday Observer on the Port City marina (January 2025); Cinnamon Bentota Beach water sports.")

def events():
    rows = [
        ("8 Nov 2026", "Deepavali", "Public holiday in Sri Lanka. Kovils across Colombo light up"),
        ("8 to 9 Nov 2026", "This Is Michael", "Michael Jackson tribute by Lenny Jay at The Podium, City of Dreams"),
        ("24 Nov 2026", "Il Poya", "Public holiday. Bars and liquor shops close"),
        ("4 Dec 2026", "Marians with News", "Local concert, Colombo"),
        ("5 Dec 2026", "FDY 0", "EDM all nighter, Colombo"),
        ("11 Dec 2026", "Wayo at the Lake", "Concert at Cinnamon Lakeside"),
        ("December 2026", "Australia women in Sri Lanka", "Three ODIs; dates to be confirmed"),
        ("23 Dec 2026", "Unduvap Poya", "Traditional start of the Adam's Peak pilgrimage season. Bars close"),
        ("25 Dec 2026", "Christmas", "Public holiday. Hotel galas and decorated malls"),
        ("31 Dec 2026", "New Year's Eve", "Last year: fireworks over Galle Face Green, Port City and the Lotus Tower. 2026 plans to be announced"),
        ("15 Jan 2027", "Thai Pongal", "Public holiday, celebrated by Tamils across the island"),
        ("22 Jan 2027", "Duruthu Poya", "Kelaniya temple's Duruthu Perahera procession near Colombo in January"),
        ("Late Jan or Feb 2027", "Navam Perahera", "Gangaramaya temple's procession through Colombo. In 2026 it ran on 31 January and 1 February"),
        ("2027, dates to be confirmed", "Galle Literary Festival", "Returns in 2027 after a pause"),
        ("13 to 14 Apr 2027", "Sinhala and Tamil New Year", "The island's biggest festival"),
    ]
    table = "".join(f"<tr><td>{d}</td><td><strong>{n}</strong></td><td>{w}</td></tr>" for d, n, w in rows)
    body = f"""<h2>The season at a glance</h2>
<div class="table-scroll"><table><tr><th>When</th><th>What</th><th>Details</th></tr>{table}</table></div>
<p class="small">Updated October 2026. Concert and sports dates move; we confirm before you book.</p>
<h2>Cricket fans, note</h2>
<p>There is no men's international cricket in Sri Lanka in this window. Sri Lanka tours India for three ODIs and three T20Is from 13 to 27 December 2026, then New Zealand from mid January. The Lanka Premier League ran in July and August 2026.</p>
<h2>Plan around the Poya</h2>
<p>Full moon Poya days are public holidays when bars close. They are also some of the most beautiful nights to be in Sri Lanka, with lanterns and temple processions. Book the party night either side.</p>"""
    faqs = [("What events are on in Colombo in December 2026?","Local concerts on 4, 5 and 11 December, Unduvap Poya on 23 December, Christmas on 25 December and New Year's Eve on 31 December, when Colombo has had fireworks over Galle Face Green and Port City."),
            ("When is Deepavali in Sri Lanka in 2026?","Sunday 8 November 2026, a public holiday in Sri Lanka."),
            ("Is there cricket in Sri Lanka between November 2026 and March 2027?","No men's internationals are scheduled in Sri Lanka in that window. Australia women are due to play three ODIs in Sri Lanka in December 2026."),
            ("When is the Navam Perahera in 2027?","The date is yet to be announced. It is held by Gangaramaya temple around Navam Poya; in 2026 it ran on 31 January and 1 February.")]
    return lux_page("events-calendar", "Events calendar", "Colombo Events Calendar: November 2026 to April 2027",
        "What is on in Colombo and Sri Lanka from November 2026 to April 2027: Deepavali, City of Dreams shows, concerts, Poya days, New Year's Eve, Navam Perahera and Sinhala and Tamil New Year.",
        "Events calendar", "What is on, <em>November to April.</em>",
        "The dates worth building a trip around this season, from Deepavali in Colombo to the New Year's Eve fireworks and the temple processions of the new year.",
        body, faqs, vids=("AVTidW78qNQ","9119VUOlspA"), occasion="Luxury weekend",
        source="Sources: Ada Derana on 2026 public holidays and the Navam Perahera; Sunday Times on This Is Michael at City of Dreams (August 2026); Tickets Ministry December 2026 listings; Ada Derana on New Year's Eve 2025; The Papare and Wikipedia on cricket fixtures; Newswire on the Galle Literary Festival; Gazette 2493/05 on 2027 holidays.")

def cod():
    body = """<div class="facts">
  <div class="fact"><b>800</b><span>Rooms across Cinnamon Life (687) and Nüwa (113)</span></div>
  <div class="fact"><b>17</b><span>Restaurants and bars under one roof</span></div>
  <div class="fact"><b>5,000+</b><span>Guests the ballrooms and event spaces can host</span></div>
</div>
<h2>What is inside</h2>
<div class="table-scroll"><table>
<tr><th>Part</th><th>What it is</th></tr>
<tr><td>Cinnamon Life</td><td>The big hotel, 687 rooms, open since October 2024, with the city's largest ballrooms and event spaces</td></tr>
<tr><td>Nüwa</td><td>The top tier: 113 rooms including 19 VIP suites and 15 premium suites, opened in August 2025</td></tr>
<tr><td>The casino</td><td>Opened in August 2025, operated by Melco, with about 119 tables and 250 slot machines</td></tr>
<tr><td>The Shoppes</td><td>The luxury mall inside the resort</td></tr>
<tr><td>Kurundu Spa</td><td>The resort spa</td></tr>
<tr><td>The Podium and ballrooms</td><td>Shows, concerts, fashion weeks and the biggest Indian weddings in Colombo</td></tr>
</table></div>
<h2>Where to eat and drink</h2>
<ul><li><strong>Indiya:</strong> the Indian restaurant, for when the group wants dal and tandoor.</li>
<li><strong>Sapphire Dragon</strong> (Cantonese), <strong>Yoroko</strong> (Japanese), <strong>Bistro des Marées</strong> and <strong>Staten Bar &amp; Grill</strong>.</li>
<li><strong>Gatz:</strong> a two storey champagne bar and supper club with live bands every night.</li>
<li><strong>Flux</strong> (rooftop lounge), <strong>Dreams &amp; Beats</strong> (rooftop pool bar) and <strong>Pool + Bar 09</strong>.</li></ul>
<h2>Shows and big nights</h2>
<p>Hrithik Roshan performed at the opening weekend in August 2025. Mercedes-Benz Fashion Week Sri Lanka ran at Cinnamon Life in October 2026, and This Is Michael, a Michael Jackson tribute, plays The Podium on 8 and 9 November 2026. See the full <a href="events-calendar.html">events calendar</a>.</p>
<h2>Casino basics</h2>
<ul><li>Expect a minimum age of 21, a passport check at the door, and a smart casual dress code: no sleeveless shirts, shorts or slippers.</li>
<li>Sri Lankan citizens pay a USD 100 entry levy. Ask at the door about any charge for foreign passport holders; reports have differed.</li>
<li>Sri Lanka's new Gambling Regulatory Authority came into force on 1 December 2025, with detailed regulations still being finalised in 2026.</li></ul>
<h2>What a night costs</h2>
<p>Rooms at Cinnamon Life were booking at around &#8377;14,600 to 17,800 a night in October 2026. Nüwa suites cost considerably more; we quote on request. Weekends and the Christmas to New Year fortnight run highest.</p>
<h2>Getting there</h2>
<p>City of Dreams is on the beachfront in Colombo 2, next to the Beira Lake and a short drive from Galle Face. Fly into Colombo, 80 minutes from Chennai, about 90 minutes from Bengaluru and two and a half hours from Mumbai.</p>"""
    faqs = [("What is City of Dreams Sri Lanka?","South Asia's first integrated resort, in Colombo, built by John Keells and Macau's Melco. It combines the Cinnamon Life hotel (687 rooms), the Nüwa hotel (113 rooms), a casino, a luxury mall, a spa, ballrooms and about 17 restaurants and bars."),
            ("When did City of Dreams Sri Lanka open?","Cinnamon Life opened in October 2024. The casino and the Nüwa hotel opened with the resort's grand opening on 1 and 2 August 2025."),
            ("Is there an Indian restaurant at City of Dreams Colombo?","Yes. Indiya is the resort's Indian restaurant, alongside Cantonese, Japanese and European dining."),
            ("What are the casino entry rules at City of Dreams Sri Lanka?","Expect a minimum age of 21, a passport check and a smart casual dress code. Sri Lankan citizens pay a USD 100 entry levy; ask at the door about any charge for foreign visitors."),
            ("How much does a room at City of Dreams Colombo cost?","Cinnamon Life rooms were booking at around Rs 14,600 to 17,800 a night in October 2026. Nüwa suites cost more and are quoted on request.")]
    return lux_page("city-of-dreams-sri-lanka", "City of Dreams guide", "City of Dreams Sri Lanka: The Guide for Indian Visitors",
        "City of Dreams Sri Lanka explained for Indians: Cinnamon Life and Nüwa hotels, 17 restaurants including Indiya, shows, the casino's entry rules, room rates and how to plan a weekend.",
        "City of Dreams Sri Lanka", "City of Dreams, <em>explained for Indians.</em>",
        "South Asia's first integrated resort opened in Colombo in August 2025: two hotels, a casino, a mall, a spa and 17 places to eat and drink, built by John Keells and Macau's Melco. Here is what is inside and how to do it well.",
        body, faqs, vids=("FDoDcwf_pDc","AVTidW78qNQ","rBoKEVmCx0Y"), occasion="Luxury weekend", responsible=True,
        source="Sources: Daily FT on the opening (August 2025); Ada Derana on Cinnamon Life (October 2024) and City of Dreams (May 2026); Asia Gaming Brief and ASGAM on the casino, dining and the Gambling Regulatory Authority (2026); Outlook Traveller hotel review (August 2025); Sunday Times on This Is Michael (August 2026); KAYAK rate data (October 2026).")

def weekend():
    body = """<h2>Where to stay</h2>
<div class="table-scroll"><table>
<tr><th>Hotel</th><th>Why</th><th>Price guide</th></tr>
<tr><td><strong>Nüwa, City of Dreams</strong></td><td>The most exclusive rooms in the city: 113 keys, with VIP and premium suites</td><td>On request</td></tr>
<tr><td><strong>Cinnamon Life, City of Dreams</strong></td><td>687 rooms inside the integrated resort, with the rooftop bars and Indiya downstairs</td><td>About &#8377;14,600 to 17,800 a night</td></tr>
<tr><td><strong>ITC Ratnadipa</strong></td><td>India's ITC Hotels, opened April 2024: 352 rooms, nine restaurants and bars, a sky bridge and a helipad</td><td>About USD 205 to 270 a night</td></tr>
<tr><td><strong>Shangri-La Colombo</strong></td><td>500 rooms and 34 suites over Galle Face, with the Tiki Bar</td><td>On request</td></tr>
<tr><td><strong>Galle Face Hotel</strong></td><td>Founded in 1864: 156 rooms of old world grandeur on the sea</td><td>On request</td></tr>
<tr><td><strong>Cinnamon Grand</strong></td><td>Opened in 1975 as the Lanka Oberoi, Oberoi's first hotel outside India</td><td>On request</td></tr>
</table></div>
<p class="small">Rates from KAYAK booking data, October 2026. Weekends and the festive season run higher.</p>
<h2>Where to eat</h2>
<ul><li><strong>Ministry of Crab,</strong> Old Dutch Hospital: Colombo's most famous table, on Asia's 50 Best Restaurants extended list. Book ahead.</li>
<li><strong>Nihonbashi,</strong> now at Port City: the Japanese institution, 30 years old in 2025, with eight private dining rooms.</li>
<li><strong>Indiya, Sapphire Dragon and Yoroko</strong> at City of Dreams.</li></ul>
<h2>What to do</h2>
<ul><li><strong>Port City:</strong> walk the 500 metre Marina Promenade and swim at the free beach. The superyacht marina is due in 2027.</li>
<li><strong>On the water:</strong> Browns' private yacht Saakya takes up to 15 guests from Port City; sunset catamaran sails also run from Colombo.</li>
<li><strong>Spa:</strong> Kurundu Spa at City of Dreams, or your hotel's.</li>
<li><strong>Shopping:</strong> The Shoppes at City of Dreams, One Galle Face and The Mall at Port City.</li>
<li><strong>Nights out:</strong> rooftops, the supper club and live music. See <a href="colombo-nightlife.html">Colombo nightlife</a>.</li></ul>
<h2>The two night plan</h2>
<div class="table-scroll"><table>
<tr><th>When</th><th>Plan</th></tr>
<tr><td>Friday</td><td>Morning flight from Mumbai (about 2.5 hours), Bengaluru (about 1.5) or Delhi (about 3.5). Spa, then dinner at Ministry of Crab and a rooftop nightcap</td></tr>
<tr><td>Saturday</td><td>Port City promenade and beach, a private yacht at sunset, dinner at Nihonbashi, then Gatz</td></tr>
<tr><td>Sunday</td><td>Late breakfast, shopping, fly home</td></tr>
</table></div>
<p>Staying longer? Add two nights in a Galle Fort villa or a tea estate bungalow. See our <a href="../guides/sri-lanka-itinerary-from-india.html">itineraries</a>.</p>"""
    faqs = [("What are the best luxury hotels in Colombo?","Nüwa and Cinnamon Life at City of Dreams, ITC Ratnadipa, Shangri-La Colombo, the Galle Face Hotel and Cinnamon Grand are the top tier in 2026."),
            ("Is there an Indian hotel brand in Colombo?","Yes. ITC Hotels opened ITC Ratnadipa in April 2024, with 352 rooms, nine restaurants and bars and a helipad. Cinnamon Grand opened in 1975 as the Lanka Oberoi."),
            ("Can you hire a yacht in Colombo?","Yes. Browns' private yacht Saakya takes up to 15 guests from Port City, and crewed catamaran sunset sails run from Colombo. Port City's superyacht marina is due in 2027."),
            ("How much does a luxury weekend in Colombo cost from India?","Rooms at Cinnamon Life ran about Rs 14,600 to 17,800 a night and ITC Ratnadipa about USD 205 to 270 in October 2026, before flights, dining and experiences. Suites and the festive season cost more.")]
    return lux_page("luxury-weekend-in-colombo", "Luxury weekend in Colombo", "Luxury Weekend in Colombo from India: Hotels, Dining, Yachts",
        "Plan a luxury weekend in Colombo from India: City of Dreams, ITC Ratnadipa and Shangri-La, Ministry of Crab and Nihonbashi, a private yacht from Port City, and a two night plan.",
        "Luxury weekend", "Two nights in Colombo, <em>done well.</em>",
        "Suites over the Indian Ocean, a crab dinner people fly in for, a private yacht at sunset and a supper club after. Closer than Dubai, cheaper than the Maldives, and on Indian time.",
        body, faqs, vids=("3oVYpDEXeLU","dVuI5bFoUOY","9119VUOlspA"), occasion="Luxury weekend",
        source="Sources: The Week on ITC Ratnadipa (April 2024); Daily FT and Ada Derana on City of Dreams; Daily Mirror on Cinnamon Grand (December 2025), Nihonbashi (June 2025) and Browns' Saakya (June 2025); Port City Colombo on the marina (January 2025); Sunday Times on Port City beach (July 2023); KAYAK rate data (October 2026).")

NAV = [("city-of-dreams-sri-lanka", "City of Dreams guide"), ("luxury-weekend-in-colombo", "Luxury weekend in Colombo"),
       ("colombo-nightlife", "Colombo nightlife"), ("bachelor-party-in-colombo", "Bachelor and bachelorette weekends"),
       ("events-calendar", "Events calendar")]

PAGES = [("index", hub), ("city-of-dreams-sri-lanka", cod), ("luxury-weekend-in-colombo", weekend), ("colombo-nightlife", nightlife), ("bachelor-party-in-colombo", bachelor), ("events-calendar", events)]

def build(write):
    for slug, fn in PAGES:
        write(f"luxury/{slug}.html", fn())
