"""City landing pages for Tier 1 and Tier 2 India. Flight notes are deliberately conservative:
'direct' only where scheduled direct service is well established; others say 'via' a hub."""
from sitekit import *
from media import pick

# slug, name, flight time, return fare band, flights note, local hook, tier, videos
ALL_CITIES = [
 ("chennai","Chennai","1 hr 20 min","&#8377;7,000 to 14,000","Daily direct flights on IndiGo, Air India and SriLankan. The closest metro to the island, and the ferry to Jaffna leaves from your own state.","Tamil works across the north and east and much of Colombo. For Chennai families this is the easiest foreign country on earth.",1,["iLhRCwjywU8","QfFRvTem4zM","oriToNJZG-k"]),
 ("mumbai","Mumbai","2 hr 30 min","&#8377;9,000 to 18,000","Direct flights most days on SriLankan and Indian carriers.","Mumbai money is already here: shipping desks, film shoots and wedding planners all run Colombo routes.",1,["CW6jTV-hTok","jmJlx-UIDsk","gamg1oTsXQg"]),
 ("delhi","Delhi NCR","3 hr 30 min","&#8377;11,000 to 22,000","Direct flights on SriLankan and IndiGo.","Swap one winter smog week for Galle sea air. Many NCR firms are weighing Port City as their India plus one.",1,["cRQu04IaAUk","Bu86Z_7VzAA","GHyNEH0kQ3o"]),
 ("bengaluru","Bengaluru","1 hr 45 min","&#8377;8,000 to 16,000","Multiple daily direct flights. Weekend trips are genuinely practical.","Bengaluru tech teams are exactly who Port City is courting for business continuity centres.",1,["gaLWS85uCzA","52E5aIUxzj8","hvOeE4eW8As"]),
 ("hyderabad","Hyderabad","1 hr 50 min","&#8377;8,000 to 16,000","Regular direct flights on IndiGo and SriLankan.","Pharma and IT firms from Hyderabad fit the island's GCC pitch, and big Telugu weddings fit its resorts.",1,["VpQiRlaI5bo","WvMdSZ7fmJY","hvOeE4eW8As"]),
 ("kolkata","Kolkata","2 hr 45 min","&#8377;10,000 to 21,000","Direct and one stop options via Chennai.","Puja holidays line up with the start of the west coast season. Plan accordingly.",1,["13_rx2SwFgY","Bu86Z_7VzAA","q0mbKsKG-ng"]),
 ("ahmedabad","Ahmedabad","3 to 4 hr","&#8377;10,000 to 20,000","One stop via Mumbai or Chennai on most days.","Gujarati family groups and diamond traders were among the first to spot Ceylon sapphires and Colombo property.",1,["RCHD60fpDnA","0tyHQkz2rwg","hvOeE4eW8As"]),
 ("pune","Pune","3 to 4 hr","&#8377;9,000 to 18,000","Via Mumbai, Bengaluru or Chennai.","Pune's auto and IT exporters already ship through Colombo. Visit the port your containers transit.",1,["jmJlx-UIDsk","jOEz-ON842A","GHyNEH0kQ3o"]),
 ("kochi","Kochi","1 hr 10 min","&#8377;6,500 to 13,000","Short direct flights; the quickest international hop many Malayalis will ever take.","Kerala and Sri Lanka share the coconut, the lagoon and the Ayurveda economy. The island feels like home, with leopards.",2,["Tw_Ki1aw0us","D1nxIlWT6o0","iXQ3ij9h6WM"]),
 ("thiruvananthapuram","Thiruvananthapuram","About 1 hr","&#8377;6,500 to 13,000","Direct flights operate between Thiruvananthapuram and Colombo; check current schedules.","The closest Indian state capital to Colombo. Wellness operators from Kerala are natural partners here.",2,["Tw_Ki1aw0us","T-P-dpm6bZE","52E5aIUxzj8"]),
 ("madurai","Madurai","About 1 hr","&#8377;6,500 to 13,000","Direct flights have operated between Madurai and Colombo; check current schedules.","From the Meenakshi temple to the Ramayana trail, temple towns on both sides of the strait share a story.",2,["2SUXqcjFIgI","iLhRCwjywU8","QfFRvTem4zM"]),
 ("tiruchirappalli","Tiruchirappalli","About 1 hr","&#8377;6,500 to 13,000","Direct flights connect Trichy and Colombo; check current schedules.","Trichy's links to Sri Lanka are old and personal. Families cross for weddings, temples and trade.",2,["iLhRCwjywU8","WvMdSZ7fmJY","QfFRvTem4zM"]),
 ("coimbatore","Coimbatore","2 to 3 hr","&#8377;7,000 to 14,000","Via Chennai or Bengaluru.","Tiruppur and Coimbatore textile exporters supply fabric to Sri Lankan apparel makers. See the factories you sell to.",2,["vD-y2-Uv4ug","iLhRCwjywU8","WvMdSZ7fmJY"]),
 ("mangaluru","Mangaluru","3 to 4 hr","&#8377;9,000 to 17,000","Via Bengaluru, Chennai or Mumbai.","Coastal Karnataka families will feel at home on Sri Lanka's south coast: coconut, fish curry and temple festivals.",2,["gaLWS85uCzA","52E5aIUxzj8","q0mbKsKG-ng"]),
 ("visakhapatnam","Visakhapatnam","3 to 4 hr","&#8377;9,000 to 18,000","Via Chennai, Hyderabad or Bengaluru.","A port city meeting a port city. Vizag's shipping and logistics trade will recognise Colombo's transshipment business.",2,["jOEz-ON842A","VpQiRlaI5bo","WvMdSZ7fmJY"]),
 ("bhubaneswar","Bhubaneswar","4 to 5 hr","&#8377;10,000 to 20,000","Via Kolkata, Chennai or Bengaluru.","Odisha's temple trail travellers will find a second one here, from Kandy to the Ramayana sites.",2,["2SUXqcjFIgI","13_rx2SwFgY","q0mbKsKG-ng"]),
 ("jaipur","Jaipur","4 to 5 hr","&#8377;12,000 to 24,000","Via Delhi or Mumbai.","Jaipur's gem trade and royal wedding planners both have reasons to know Sri Lanka: sapphires from Ratnapura and palaces by the sea.",2,["7hLq8Imgplo","WvMdSZ7fmJY","cRQu04IaAUk"]),
 ("surat","Surat","4 to 5 hr","&#8377;11,000 to 22,000","Via Mumbai or Delhi.","Surat's diamond and textile traders will recognise two of Sri Lanka's biggest trades: gems and apparel.",2,["0tyHQkz2rwg","vD-y2-Uv4ug","hvOeE4eW8As"]),
 ("vadodara","Vadodara","4 to 5 hr","&#8377;11,000 to 22,000","Via Mumbai or Delhi.","Gujarati family groups travel well here: veg food is easy, temples are many, and the beaches are uncrowded.",2,["6_-lwBnX3rc","RCHD60fpDnA","q0mbKsKG-ng"]),
 ("indore","Indore","4 to 5 hr","&#8377;11,000 to 22,000","Via Mumbai or Delhi.","Indore's business families are weighing a second address. Sri Lanka puts one an easy hop from Mumbai.",2,["cRQu04IaAUk","dbM8AMmEdgY","6_-lwBnX3rc"]),
 ("nagpur","Nagpur","4 to 5 hr","&#8377;11,000 to 22,000","Via Mumbai, Bengaluru or Hyderabad.","Central India's travellers get beaches, hills and wildlife in one week, with a free visa.",2,["Bu86Z_7VzAA","iXQ3ij9h6WM","q0mbKsKG-ng"]),
 ("chandigarh","Chandigarh","5 to 6 hr","&#8377;12,000 to 24,000","Via Delhi.","Punjabi wedding energy on a Sri Lankan beach is a thing. Planners here have seen it and loved it.",2,["WvMdSZ7fmJY","CW6jTV-hTok","gamg1oTsXQg"]),
 ("lucknow","Lucknow","5 to 6 hr","&#8377;12,000 to 24,000","Via Delhi.","The Ramayana trail resonates nowhere more than in UP. Group yatras from Lucknow are a growing route.",2,["2SUXqcjFIgI","kRjSsHlA9_0","cRQu04IaAUk"]),
 ("varanasi","Varanasi","5 to 6 hr","&#8377;12,000 to 24,000","Via Delhi or Kolkata.","From the ghats to Sita Amman temple: pilgrims from Kashi complete a circle many families have dreamed of.",2,["2SUXqcjFIgI","kRjSsHlA9_0","q0mbKsKG-ng"]),
 ("bhopal","Bhopal","5 to 6 hr","&#8377;11,000 to 22,000","Via Delhi or Mumbai.","A city of lakes heading to an island of lagoons. Family trips and honeymoons from Bhopal suit the hill and coast circuit.",2,["7j335oyBKH8","52E5aIUxzj8","q0mbKsKG-ng"]),
]

def page(c):
    slug, name, time, fare, flights, hook, tier, vids_ids = c
    vids = pick(*vids_ids)
    depth = 1
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; From {name}</p>
  <span class="eyebrow">From {name}</span>
  <h1>Sri Lanka from {name}: <em>{time} away.</em></h1>
  <p class="lead">{flights} Return fares typically run {fare} depending on season. {hook}</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="{wa_link(f'Hi, I am from {name} and planning Sri Lanka')}" rel="noopener">Plan from {name}</a>
    <a class="btn btn-ghost" href="../guides/trip-cost-from-india.html">What it costs</a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>What people from {name} <em>come for.</em></h2>
  <div class="grid c3" style="margin-top:28px">
    <a class="card link-card" href="../weddings.html"><span class="tag">Weddings</span><h3>Destination weddings that rival Goa</h3><p>Run your guest list through our calculator, flights included.</p><span class="go">Compare costs &rarr;</span></a>
    <a class="card link-card" href="../real-estate.html"><span class="tag">Property</span><h3>Sea view condos priced in dollars</h3><p>What Indians can buy, and the USD 100,000 residence visa route.</p><span class="go">See the rules &rarr;</span></a>
    <a class="card link-card" href="../port-city-tax.html"><span class="tag">7.5% tax</span><h3>Port City incentives</h3><p>Approved businesses pay 7.5% corporate tax for four years; the largest projects 0% for up to 15.</p><span class="go">Read the numbers &rarr;</span></a>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <h2>Quick facts for <em>{name} travellers.</em></h2>
  <div class="table-scroll" style="margin-top:24px"><table>
    <tr><th>Question</th><th>Answer</th></tr>
    <tr><td>Flight time to Colombo</td><td>{time}</td></tr>
    <tr><td>Typical return fare</td><td class="num">{fare}</td></tr>
    <tr><td>Visa</td><td>Free 30 day tourist ETA for Indians since 25 May 2026. Apply on eta.gov.lk</td></tr>
    <tr><td>Money</td><td>UPI at LankaQR merchants, cards widely accepted, carry some LKR</td></tr>
    <tr><td>Time difference</td><td>None. Sri Lanka runs on IST</td></tr>
  </table></div>
  <p class="small" style="margin-top:12px">Fares are indicative return economy bands and move with season. Check current schedules with airlines.</p>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">Watch before you go</span>
  <h2>Indians who <em>went first.</em></h2>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
</div></section>
""" + cta_banner(f"Flying from {name}?", "One message gets you a plan: trip, wedding, property or business. Your guide on the island replies the same day.", f"Hi, I am from {name}")
    schema = crumb_schema([(f"From {name}", f"from/{slug}.html")]) + "\n" + video_schema(vids)
    title = f"Sri Lanka from {name}: Flights, Trip Cost, Free Visa, Weddings and Investment | Sri Lanka for Indians"
    desc = f"Sri Lanka from {name}: {time} to Colombo, return fares around {fare.replace('&#8377;','Rs ')}, free visa for Indians, weddings, property and Port City's 7.5% corporate tax. Talk to a guide on WhatsApp."
    return head(title, desc, f"from/{slug}.html", depth, schema) + header(depth) + body + footer(depth)

def build(write):
    for c in ALL_CITIES:
        write(f"from/{c[0]}.html", page(c))
