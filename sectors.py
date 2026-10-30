"""Why Sri Lanka, by sector. Each page: hero facts, three reasons, the India angle, videos, FAQ, CTA.
Export figures: Sri Lanka Export Development Board 2025 full year, as reported by Daily FT (Jan 2026)."""
from sitekit import *
from media import pick

EDB = "Source: Export Development Board 2025 full year figures, reported by Daily FT."

SECTORS = [
dict(slug="technology", name="Technology", eyebrow="Why Sri Lanka for tech",
 h1="An engineering bench <em>on India's own clock.</em>",
 lead="Sri Lanka runs on IST, educates its engineers in English, and has quietly built product teams for global software houses for two decades. For Indian tech firms, it is the delivery centre an hour away that does not compete with Bengaluru for the same people.",
 facts=[("$1.64B","ICT and BPM service exports in 2025, up 8.8%"),("IST","Colombo runs on UTC+5:30. No time zone gymnastics"),("100%","Foreign ownership inside Port City Colombo")], source=EDB,
 reasons=[("Talent","Product grade engineers","Global enterprise software houses, including IFS and WSO2, run major engineering in Colombo. The talent pool is used to building products, not just tickets."),
          ("Continuity","An India plus one that is close","Port City pitches itself to Indian GCCs as a business continuity and disaster recovery site. Same clock, short flight, separate grid and jurisdiction."),
          ("Retention","A smaller pond","A tight knit market where reputations travel fast. Strong employers find teams tend to stay together longer than in India's hottest hubs.")],
 india="Indian IT services and product companies use Colombo for 20 to 200 person centres: QA, support, product engineering and Tamil or English customer facing roles. Inside Port City, qualifying strategic projects can earn corporate tax holidays, and smaller approved firms a 7.5% rate for four years.",
 videos=["hvOeE4eW8As","GHyNEH0kQ3o"],
 faq=[("Is Sri Lanka good for software development outsourcing?","Yes for many teams. Sri Lanka exported $1.64 billion of ICT and BPM services in 2025, its engineers work in English, and Colombo shares India's time zone. Global software firms such as IFS and WSO2 run large engineering teams there."),
      ("Can an Indian IT company set up inside Port City Colombo?","Yes. Port City allows full foreign ownership, and approved Businesses of Strategic Importance can receive corporate tax holidays of 8 to 15 years under Regulation 01 of 2025. Approval comes from the Colombo Port City Economic Commission.")]),

dict(slug="bpo-kpo", title="Why Sri Lanka for BPO and KPO: A Guide for Indian Companies", desc="Why Sri Lanka for BPO and KPO? A finance, accounting and legal outsourcing base trusted by UK and Australian clients, English speaking teams, and a 7.5% tax rate for approved Port City firms.", name="BPO and KPO", eyebrow="Why Sri Lanka for BPO and KPO",
 h1="Finance, legal and voice teams <em>that clients trust.</em>",
 lead="Sri Lanka built its outsourcing reputation on finance and accounting for UK and Australian clients. It has one of the largest pools of CIMA trained management accountants outside Britain, and a legal system that works in English.",
 facts=[("$1.64B","ICT and BPM exports in 2025"),("CIMA","One of the largest CIMA communities outside the UK"),("English","The language of contracts, courts and boardrooms")], source=EDB,
 reasons=[("F&amp;A","Finance and accounting depth","Accounts payable, management reporting and FP&amp;A teams staffed by CIMA and ACCA trained professionals."),
          ("Legal","Legal process outsourcing","A common law influenced system and English language legal practice suit document review and contract work."),
          ("Voice","Neutral accents, Commonwealth clients","Customer experience desks serving the UK and Australia with strong time zone overlap.")],
 india="Indian KPO and BPO firms add a Colombo floor to diversify delivery for clients who ask for a second country. The same clock and an 80 minute hop from Chennai keep management simple.",
 videos=["WjjvHceiip0","GHyNEH0kQ3o"],
 faq=[("Why do companies outsource finance and accounting to Sri Lanka?","Sri Lanka has a deep pool of CIMA and ACCA trained accountants, strong English, and long experience serving UK and Australian clients."),
      ("Can an Indian BPO open a centre in Sri Lanka?","Yes. Indian firms can incorporate locally with full foreign ownership in most service sectors, or apply for Port City status. We introduce you to incorporation partners.")]),

dict(slug="gcc", name="Global Capability Centres", eyebrow="Why Sri Lanka for GCCs",
 h1="The India plus one <em>Port City is built for.</em>",
 lead="India is the GCC capital of the world. Port City Colombo has said publicly that it wants to complement that, offering smaller, specialised centres and a business continuity site outside India's own grid and jurisdiction.",
 facts=[("India +1","Port City's stated pitch to Indian GCCs"),("8 to 15 yrs","Corporate tax holidays for strategic investments"),("80 min","Chennai to Colombo")], source="Port City Colombo deputy MD Thulci Aluwihare, interview with Moneycontrol, July 2026.",
 reasons=[("Resilience","Business continuity and DR","A second site with separate power, telecoms and jurisdiction, close enough for weekly leadership visits."),
          ("Specialism","Small, sharp centres","Rather than 5,000 seat campuses, Colombo suits 50 to 300 person centres of excellence."),
          ("Economics","Dollar operations, lower corporate tax","Port City transacts in designated foreign currencies, and approved businesses can get corporate tax holidays or a 7.5% rate. Since January 2026, staff of new entrants pay normal income tax.")],
 india="If your board has asked for concentration risk to be addressed, a Colombo centre is the cheapest credible answer: same clock, short flight, English working language, and a corporate tax regime built to pull in strategic investment.",
 videos=["hvOeE4eW8As","GHGrijFEpgU"],
 faq=[("What is an India plus one GCC strategy?","Running most capability in India while keeping a smaller second centre in another country for resilience, client requirements or specialist skills. Port City Colombo actively markets itself for this role."),
      ("What incentives does Port City offer GCCs?","Approved primary Businesses of Strategic Importance can receive 8 to 15 year corporate tax holidays, secondary businesses a 7.5% rate for 4 years, subject to approval. Since 20 January 2026, staff of newly approved companies pay normal income tax.")]),

dict(slug="fintech", name="Fintech and Finance", eyebrow="Why Sri Lanka for finance",
 h1="A financial district <em>built from the sea up.</em>",
 lead="Port City Colombo is a special economic zone with its own regulator, its own rulebook, and the Colombo International Financial Centre rising inside it. It transacts in designated foreign currencies and is ring fenced from domestic monetary shocks.",
 facts=[("16","Designated foreign currencies for transactions"),("100%","Foreign ownership inside the zone"),("8 to 15 yrs","Corporate tax holidays for primary BSIs")], source="Port City Colombo and Regulation 01 of 2025.",
 reasons=[("Treasury","Regional treasury and holding","Multi currency operations without domestic exchange control friction."),
          ("Wealth","Family offices","A second jurisdiction for family capital, an hour from home."),
          ("Payments","Payments and fintech","Build for South Asia from a zone designed for cross border finance.")],
 india="Compare it honestly with GIFT City, which offers a 10 out of 15 year tax holiday inside India. Port City adds jurisdictional diversification and corporate tax holidays for strategic investments. Our comparison guide lays both side by side.",
 videos=["GHGrijFEpgU","hvOeE4eW8As"],
 faq=[("Is Port City Colombo a financial centre?","Yes. It is a special economic zone with financial services as a core use, including the planned Colombo International Financial Centre, and it allows transactions in 16 designated foreign currencies."),
      ("Port City Colombo or GIFT City?","GIFT City keeps you inside Indian law with a 10 out of 15 year tax holiday for IFSC units. Port City adds a separate jurisdiction, full foreign ownership and corporate tax holidays for strategic investments. See our full comparison guide.")]),

dict(slug="spices", name="Spices", eyebrow="Why Sri Lanka for spices",
 h1="The home of <em>true cinnamon.</em>",
 lead="Sri Lanka grows Cinnamomum verum, the true cinnamon the world calls Ceylon cinnamon. Pure Ceylon Cinnamon holds EU Geographical Indication protection. Pepper, cloves, nutmeg and cardamom grow alongside it in the wet zone.",
 facts=[("$450M","Spices and essential oils exports in 2025"),("EU GI","Pure Ceylon Cinnamon is a protected Geographical Indication"),("C. verum","True cinnamon, distinct from cassia")], source=EDB,
 reasons=[("Purity","Ceylon cinnamon, not cassia","True cinnamon is milder and naturally far lower in coumarin than cassia, which matters to health brands and regulators."),
          ("Range","Pepper, cloves, nutmeg, cardamom","A compact spice garden with smallholder supply and established exporters."),
          ("Oils","Essential oils","Cinnamon leaf and bark oils, citronella and more for fragrance and wellness formulators.")],
 own_note="Ownership note: foreign stakes in growing and primary processing of spices are capped at 40% unless the BOI approves more. Value added processing, export brands and export trading are open to full foreign ownership. See <a href=\"../guides/start-a-company-in-sri-lanka.html\">how to set up a company</a>.",
 india="Indian Ayurveda, FMCG and spice processing brands source Ceylon cinnamon for premium lines. The India to Sri Lanka Free Trade Agreement, in force since 2000, gives duty concessions on many goods, though some spice lines carry quotas or conditions. Check the current schedule with your customs broker.",
 videos=["OhO5fKkHTH8"],
 faq=[("What is the difference between Ceylon cinnamon and cassia?","Ceylon cinnamon is Cinnamomum verum, grown mainly in Sri Lanka. It has thin, layered quills, a milder taste and far less coumarin than cassia, which comes from related species grown in China, Indonesia and Vietnam."),
      ("Can Indian companies import spices from Sri Lanka duty free?","The India to Sri Lanka Free Trade Agreement gives duty concessions on many products, but some spices are subject to quotas or conditions. Confirm the current tariff line with a customs broker before contracting.")]),

dict(slug="tea", name="Tea", eyebrow="Why Sri Lanka for tea",
 h1="The island that <em>taught the world Ceylon.</em>",
 lead="Commercial tea in Ceylon began on the Loolecondera estate in 1867. Today tea earns Sri Lanka over a billion and a half dollars a year, and the Ceylon name, guarded by the Lion logo of the Sri Lanka Tea Board, still commands a premium.",
 facts=[("$1.51B","Tea exports in 2025"),("1867","James Taylor's first commercial plantation at Loolecondera"),("Lion logo","Sri Lanka Tea Board mark for pure Ceylon tea")], source=EDB,
 reasons=[("Brand","Origin that sells itself","Ceylon is one of the few tea origins consumers recognise by name."),
          ("Tourism","Estate bungalows","Colonial planters' bungalows in Nuwara Eliya, Ella and Hatton are now boutique stays."),
          ("Value add","Packaging and blends","Flavoured, speciality and private label packing for export.")],
 own_note="Ownership note: foreign stakes in growing and primary processing of tea are capped at 40% unless the BOI approves more. Blending, packing, brands and export trading are open to full foreign ownership. See <a href=\"../guides/start-a-company-in-sri-lanka.html\">how to set up a company</a>.",
 india="Indian tea brands blend Ceylon for premium ranges, and investors are turning hill country bungalows into heritage hotels. The Colombo auction remains one of the world's important tea marketplaces.",
 videos=["Mkl1GAE04sg","6PViyPfd000"],
 faq=[("What makes Ceylon tea different?","Grown across distinct elevations from low country to high grown estates above 1,200 metres, Ceylon teas range from bold and malty to bright and floral, and pure Ceylon tea carries the Sri Lanka Tea Board's Lion logo."),
      ("Can I invest in a tea estate bungalow as a foreigner?","Land is restricted for foreigners, but long leases and approved structures are used for hospitality projects. Speak to a licensed property lawyer before committing.")]),

dict(slug="gems-jewellery", name="Gems and Jewellery", eyebrow="Why Sri Lanka for gems",
 h1="Your Neelam and Pukhraj <em>began here.</em>",
 lead="Ratnapura literally means city of gems. Ceylon blue sapphires, yellow sapphires and the rare pink orange padparadscha are mined from its gravels. For Indian jewellers and the jyotish market, Sri Lanka is the source, not the middleman.",
 facts=[("Ratnapura","The city of gems, heart of sapphire mining"),("Neelam","Ceylon blue sapphire, prized for its cornflower blue"),("Padparadscha","A rare pink orange sapphire tied to Sri Lanka")], source="National Gem and Jewellery Authority of Sri Lanka.",
 reasons=[("Source","Buy at origin","Rough and cut stones direct from Ratnapura and Beruwala dealers."),
          ("Certification","Government testing","The National Gem and Jewellery Authority tests and certifies stones. Insist on it."),
          ("Trade","Cutting and setting","A skilled lapidary trade that works alongside Jaipur and Surat.")],
 india="Jaipur and Mumbai jewellers, Surat cutters and gemstone astrology retailers all source Ceylon sapphires. Buy only certified stones, declare them correctly at Indian customs, and work with an introduced dealer, not a beach tout.",
 videos=["0tyHQkz2rwg","7hLq8Imgplo"],
 faq=[("Is Ceylon blue sapphire good for Neelam?","Ceylon blue sapphires are among the most sought after for Neelam because of their bright, even blue. Always ask for a certificate from a recognised lab such as Sri Lanka's National Gem and Jewellery Authority."),
      ("Where are gems mined in Sri Lanka?","Mainly around Ratnapura in the Sabaragamuwa province, with trading also centred in Beruwala and Colombo.")]),

dict(slug="apparel-textiles", name="Apparel and Textiles", eyebrow="Why Sri Lanka for apparel",
 h1="Where the world's <em>best brands get made.</em>",
 lead="Apparel is Sri Lanka's largest goods export. Its manufacturers make lingerie, sportswear and performance wear for leading global labels, and the island built its name on ethical, compliant factories.",
 facts=[("$4.91B","Apparel and textile exports in 2025"),("No.1","The island's largest merchandise export"),("Ethical","Built on compliant, certified manufacturing")], source=EDB,
 reasons=[("Specialism","Intimates and performance wear","Groups like MAS and Brandix supply some of the most demanding brands in the world."),
          ("Compliance","Audit ready factories","Global buyers trust Sri Lankan compliance standards."),
          ("Inputs","Fabric from India","Much of the island's fabric and yarn can come from Tiruppur, Surat and Ludhiana.")],
 india="Indian mills supply fabric, Indian brands near shore premium production, and joint ventures combine Indian scale with Sri Lankan finishing. The Free Trade Agreement framework helps, so check the rules of origin for your product.",
 videos=["vD-y2-Uv4ug","4YVaZWJYGzI"],
 faq=[("How big is Sri Lanka's apparel industry?","Apparel and textiles earned $4.91 billion in exports in 2025, Sri Lanka's largest goods export."),
      ("Can Indian textile companies partner with Sri Lankan apparel makers?","Yes. Indian fabric and yarn suppliers already serve Sri Lankan factories, and joint ventures are common. Check rules of origin under the India to Sri Lanka FTA for duty benefits.")]),

dict(slug="graphite-minerals", name="Graphite and Minerals", eyebrow="Why Sri Lanka for minerals",
 h1="Some of the purest graphite <em>on earth.</em>",
 lead="Sri Lanka is one of very few places mining vein graphite, a naturally high purity form dug from underground veins at Bogala and Kahatagaha. Mineral sands at Pulmoddai add ilmenite and rutile.",
 facts=[("Vein","Vein graphite, among the purest natural forms"),("Bogala","Historic underground graphite mine"),("Pulmoddai","Ilmenite and rutile mineral sands")], source="Geological Survey and Mines Bureau of Sri Lanka.",
 reasons=[("Batteries","Anode material","Graphite is central to lithium ion battery anodes, and buyers want non concentrated supply."),
          ("Industry","Refractories and lubricants","Vein graphite has long served high spec industrial uses."),
          ("Sands","Titanium minerals","Ilmenite and rutile feed pigment and metal supply chains.")],
 india="India's battery and EV makers are hunting for diversified graphite supply. Sri Lankan vein graphite is a small but high quality option worth a technical evaluation.",
 videos=[],
 faq=[("What is vein graphite?","A naturally occurring, highly crystalline graphite found in underground veins, notably in Sri Lanka, typically with very high natural carbon content."),
      ("Can Indian companies invest in Sri Lankan mining?","Mining requires licences from the Geological Survey and Mines Bureau and often approval through the Board of Investment. Partner with an experienced local operator.")]),

dict(slug="coconut-coir", name="Coconut and Coir", eyebrow="Why Sri Lanka for coconut",
 h1="From husk to <em>high value export.</em>",
 lead="Sri Lanka's coconut triangle produces desiccated coconut, coconut milk, virgin oil, coir fibre and coconut shell activated carbon, a product where Sri Lankan firms are global leaders.",
 facts=[("Coir","A leading exporter of coir fibre and products"),("Carbon","Coconut shell activated carbon for filters worldwide"),("Kerala","A coconut economy Kerala and Tamil Nadu will recognise")], source="Coconut Development Authority of Sri Lanka.",
 reasons=[("Coir","Fibre, pith and mats","Coir pith for horticulture is in demand from greenhouse growers worldwide."),
          ("Food","Desiccated, milk and oil","Food grade processing with established export certifications."),
          ("Carbon","Activated carbon","Water, gold recovery and air filtration all run on coconut shell carbon.")],
 own_note="Ownership note: foreign stakes in growing and primary processing of coconut are capped at 40% unless the BOI approves more. Downstream manufacturing such as coir products is generally open. See <a href=\"../guides/start-a-company-in-sri-lanka.html\">how to set up a company</a>.",
 india="Kerala and Tamil Nadu coconut businesses can partner rather than compete: sourcing during Indian shortfalls, joint processing, and shared export channels.",
 videos=[],
 faq=[("What coconut products does Sri Lanka export?","Desiccated coconut, coconut milk and cream, virgin coconut oil, coir fibre, coir pith and coconut shell activated carbon."),
      ("Is coir pith from Sri Lanka good for horticulture?","Yes. Washed and buffered coir pith from Sri Lanka is widely used as a growing medium in greenhouses.")]),

dict(slug="ports-shipping", name="Ports and Shipping", eyebrow="Why Sri Lanka for shipping",
 h1="Ten nautical miles <em>from the world's busiest lane.</em>",
 lead="Colombo handled a record 8.29 million TEU in 2025. It sits a few miles off the main east west route, which is why so much Indian cargo changes ships here. Indian capital already runs a terminal and owns the largest shipyard.",
 facts=[("8.29M TEU","Colombo port throughput, 2025 record"),("6 to 10 nm","From the main east west shipping lane"),("51%","Mazagon Dock's stake in Colombo Dockyard")], source="Sri Lanka Ports Authority; The Diplomat, April 2026.",
 reasons=[("Transshipment","The relay point","Feeder to mainline transfers for Indian east and west coast cargo."),
          ("Marine","Repair, bunkering, crew change","Colombo and Hambantota pick up volume whenever Gulf or Red Sea routings wobble."),
          ("Indian presence","Adani and Mazagon Dock","Adani runs the West Container Terminal, and Mazagon Dock bought 51% of Colombo Dockyard in 2026.")],
 own_note="Ownership note: foreign stakes in freight forwarding and shipping agencies are capped at 40% unless the BOI approves more, so many Indian firms enter through a joint venture. See <a href=\"../guides/start-a-company-in-sri-lanka.html\">how to set up a company</a>.",
 india="If your containers already transit Colombo, an entity here gives you control of the relay. Vizhinjam will compete for some volume, which makes a two port strategy smarter, not redundant.",
 videos=["jOEz-ON842A","jvRH8dcbLpg"],
 faq=[("Why is Colombo a transshipment hub for India?","Colombo is a few nautical miles from the main east west shipping lane and has deep water berths, so large vessels call there and smaller feeders carry cargo to and from Indian ports."),
      ("Which Indian companies operate in Sri Lankan ports?","Adani operates the Colombo West Container Terminal with John Keells, and Mazagon Dock Shipbuilders acquired 51% of Colombo Dockyard in 2026.")]),

dict(slug="renewable-energy", name="Renewable Energy", eyebrow="Why Sri Lanka for clean energy",
 h1="Equatorial sun. <em>Monsoon wind.</em>",
 lead="Sri Lanka sits a few degrees off the equator with strong wind corridors around Mannar in the north west. Rooftop and utility solar, wind and the long discussed India to Sri Lanka grid interconnection all point the same way.",
 facts=[("Solar","Year round equatorial irradiance"),("Mannar","Monsoon wind corridor with operating wind farms"),("Grid link","India to Sri Lanka interconnection under study")], source="Ceylon Electricity Board and Sustainable Energy Authority.",
 reasons=[("Solar","Rooftop and utility","Commercial rooftops and ground mount projects with net metering options."),
          ("Wind","North west corridor","Mannar's wind resource is among the best on the island."),
          ("Integration","Regional grid","An interconnection would let clean power flow both ways across the Palk Strait.")],
 india="Indian EPC contractors, module makers and developers bring scale the island needs. Government to government energy cooperation, including around Trincomalee, adds a policy tailwind. Do your diligence on tariffs and offtake.",
 videos=[],
 faq=[("Can Indian companies build solar projects in Sri Lanka?","Yes. Projects are tendered or approved through the Ceylon Electricity Board and Sustainable Energy Authority, often with Board of Investment facilitation."),
      ("Is there an electricity link between India and Sri Lanka?","Not yet. A grid interconnection across the Palk Strait has been studied and discussed by both governments.")]),

dict(slug="hospitality-hotels", name="Hospitality and Hotels", eyebrow="Why Sri Lanka for hotels",
 h1="India is the island's <em>biggest guest.</em>",
 lead="Indians were Sri Lanka's largest source market in 2026, with more than 4.3 lakh arrivals by September. Indian hotel groups are already here, ITC with its Colombo flagship and Taj on the coast, because the guest list is coming from home.",
 facts=[("4.3 lakh","Indian visitors, Jan to Sep 2026"),("No.1","India's rank among source markets"),("32%","India's share of all arrivals in September 2026")], source="SLTDA arrivals data, Sept 2026.",
 reasons=[("Demand","Indian weddings and groups","Large families, weddings and incentive trips fill rooms in blocks."),
          ("Assets","Villas and boutique hotels","South coast villas and hill country bungalows are the sweet spot for new investors."),
          ("Brands","Indian groups present","ITC Ratnadipa in Colombo and Taj properties show the model works.")],
 india="If you run hotels or villas in India, Sri Lanka lets you follow your own guests. Long leases and approved structures make hospitality the most practical real estate play for foreigners.",
 videos=["jmJlx-UIDsk","52E5aIUxzj8"],
 faq=[("How many Indian tourists visit Sri Lanka?","431,162 Indians visited Sri Lanka between January and September 2026, making India the largest source market, according to the Sri Lanka Tourism Development Authority."),
      ("Can foreigners invest in hotels in Sri Lanka?","Yes, typically through long leases and Board of Investment approved structures. Hotels are one of the most common foreign real estate investments.")]),

dict(slug="ayurveda-wellness", name="Ayurveda and Wellness", eyebrow="Why Sri Lanka for wellness",
 h1="An older kind of <em>luxury.</em>",
 lead="Sri Lanka practises Ayurveda alongside its own indigenous medicine tradition, and its retreats, from Barberyn on the coast to Ulpotha in the dry zone, draw wellness travellers from across the world.",
 facts=[("Ayurveda","Shared classical roots with India"),("Deshiya","Sri Lanka's own indigenous medicine tradition"),("Retreats","Destination retreats from coast to jungle")], source="Ministry of Indigenous Medicine, Sri Lanka.",
 reasons=[("Retreats","Proven demand","International guests book week long programmes months ahead."),
          ("Setting","Nature as the product","Jungle, lagoon and tea country settings Indian cities cannot offer."),
          ("Ingredients","Herbs and oils","Local herbal suppliers and oil makers serve both clinics and brands.")],
 india="Kerala style wellness operators and Indian Ayurveda brands can extend into Sri Lanka, and Indian travellers already book retreats here. Wellness tourism pairs naturally with weddings and long stays.",
 videos=["D1nxIlWT6o0","T-P-dpm6bZE"],
 faq=[("Is Sri Lanka good for Ayurveda retreats?","Yes. Sri Lanka has well known Ayurveda and wellness retreats such as Barberyn and Ulpotha, and a long tradition of herbal medicine."),
      ("Is Sri Lankan Ayurveda the same as Indian Ayurveda?","They share classical roots. Sri Lanka also has its own indigenous system, Deshiya Chikitsa, so treatments and herbs can differ.")]),

dict(slug="mice-events", name="MICE and Events", eyebrow="Why Sri Lanka for events",
 h1="Your dealer meet <em>deserves an ocean.</em>",
 lead="Incentive trips, conferences and product launches land easily here: under three hours from every Indian metro, a free visa for every delegate, and new event infrastructure arriving at Port City.",
 facts=[("&#8377;0","Visa fee for Indian delegates since May 2026"),("Under 3 hr","Flights from every Indian metro"),("Air dome","Port City's new event venue, due late 2026")], source="Port City Colombo, Moneycontrol interview, July 2026.",
 reasons=[("Access","Easy for big groups","Free ETAs, direct flights and a single time zone make group logistics simple."),
          ("Venues","Ballrooms to beaches","Colombo five star ballrooms, BMICH, and beach resorts for gala nights."),
          ("Value","Premium feel, sensible cost","Incentive trips that feel international without long haul budgets.")],
 india="Pharma, auto, FMCG and insurance companies run dealer and agent incentives here. We put together venues, flights, visas and gala nights in one plan.",
 videos=["B2OIRRQbz8I","jmJlx-UIDsk"],
 faq=[("Is Sri Lanka good for corporate incentive trips from India?","Yes. It is under three hours from Indian metros, the tourist ETA is free for Indians, and resorts and Colombo hotels regularly host large Indian groups."),
      ("Do business visitors need a different visa?","Conference delegates and business visitors should apply for the appropriate business ETA. Check eta.gov.lk for the current category and fee.")]),

dict(slug="film-production", name="Film and Production", eyebrow="Why Sri Lanka for film",
 title="Filming in Sri Lanka: Incentives and Permits for Indian Crews",
 desc="Does Sri Lanka offer film incentives or rebates? Not a cash rebate yet. What it does offer Indian crews: a single window permit being set up in 2026, low costs and every location within a day.",
 h1="Every location, <em>within a day's drive.</em>",
 lead="Hollywood has known it for decades. The Bridge on the River Kwai was filmed at Kitulgala, and Indiana Jones and the Temple of Doom shot scenes here. Beaches, rainforest, misty highlands and colonial forts sit within a few hours of each other.",
 facts=[("Kitulgala","Where The Bridge on the River Kwai was filmed"),("Temple of Doom","Indiana Jones shot scenes in Sri Lanka"),("1 day","Beach to highlands drive")], source="Production history, Sri Lanka Tourism.",
 reasons=[("Range","Variety in one trip","Song sequences across five looks without changing countries."),
          ("Crews","Local crews and fixers","Experienced production services for ads and features."),
          ("Cost","Sensible budgets","Lower location costs than Europe or Southeast Asia for comparable variety.")],
 india="Bollywood, Tamil and Telugu song shoots, ad films and OTT productions get variety without long haul travel. We connect you with fixers and permit specialists.",
 videos=["q0mbKsKG-ng","8g9ccCkT-u0"],
 faq=[("Which famous films were shot in Sri Lanka?","The Bridge on the River Kwai was filmed at Kitulgala, and Indiana Jones and the Temple of Doom filmed scenes in Sri Lanka."),
      ("Does Sri Lanka offer film incentives or rebates for foreign productions?","Not a cash rebate. Unlike Malaysia or Thailand, Sri Lanka has no percentage rebate on local spend as of October 2026. The saving comes from lower location, crew and hotel costs. In June 2026 the Presidential Secretariat began setting up a single window approval system so foreign films, ads and music videos no longer need separate permits from several agencies."),
     ("Do Indian film crews need permits to shoot in Sri Lanka?","Yes. Filming generally needs approvals and some locations require separate permits. Work with a local fixer who handles them.")]),
]

EXISTING = [("weddings.html","Weddings"),("real-estate.html","Real Estate"),("logistics.html","Logistics"),("second-home.html","Second Home"),("travel.html","Travel")]

def page(s):
    depth = 1
    vids = pick(*s["videos"]) if s["videos"] else []
    facts = "".join(f'<div class="fact"><b>{v}</b><span>{l}</span></div>' for v, l in s["facts"])
    reasons = "".join(f'<div class="card"><span class="tag">{t}</span><h3>{h}</h3><p>{p}</p></div>' for t, h, p in s["reasons"])
    i = SECTORS.index(s)
    others = [SECTORS[(i + k) % len(SECTORS)] for k in range(1, 9)]
    chips = "".join(f'<a href="{x["slug"]}.html">{x["name"]}</a>' for x in others)
    vid_block = f"""<section class="band sand"><div class="wrap">
  <span class="eyebrow">On film</span>
  <h2>See it <em>for yourself.</em></h2>
  <div style="margin-top:36px">{yt_grid(vids, 'c2')}</div>
</div></section>""" if vids else ""
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faq"])
    plain = re.sub("<[^>]+>", "", s["h1"])
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; <a href="index.html">Why Sri Lanka</a> &rsaquo; {s['name']}</p>
  <span class="eyebrow">{s['eyebrow']}</span>
  <h1>{s['h1']}</h1>
  <p class="lead">{s['lead']}</p>
  <div class="facts">{facts}</div>
  <p class="source">{s['source']}</p>
  <div class="cta-row"><a class="btn btn-primary" href="{wa_link('Hi, I am exploring Sri Lanka for ' + s['name'])}" rel="noopener">Talk to a sector guide</a>
  <a class="btn btn-ghost" href="../port-city-tax.html">Port City 7.5% tax</a></div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">Three reasons</span>
  <h2>Why {s['name'].lower() if s['name'] not in ('MICE and Events',) else 'events'} <em>works here.</em></h2>
  <div class="grid c3" style="margin-top:40px">{reasons}</div>
</div></section>

<section class="band sand"><div class="wrap prose">
  <span class="eyebrow">The India angle</span>
  <h2>What this means <em>for Indian businesses.</em></h2>
  <p class="lead">{s['india']}</p>
  {('<p class="small">' + s['own_note'] + '</p>') if s.get('own_note') else ''}
</div></section>

{inr_band(depth, tone="")}

{vid_block}

<section class="band"><div class="wrap">
  <span class="eyebrow">Questions</span>
  <h2>Asked by Indian <em>founders and buyers.</em></h2>
  <div style="margin-top:30px; max-width:880px">{faq_html}</div>
  <h3 style="margin-top:48px">More sectors</h3>
  <div class="chips" style="margin-top:16px">{chips}<a href="index.html">All sectors</a></div>
</div></section>
""" + cta_banner(f"Exploring {s['name'].lower()} in Sri Lanka?", "Tell us your plan. We introduce you to the right people in 48 hours.", f"Hi, I want to explore {s['name']} in Sri Lanka")
    schema = crumb_schema([("Why Sri Lanka", "why/index.html"), (s["name"], f"why/{s['slug']}.html")]) + "\n" + faq_schema(s["faq"]) + "\n" + video_schema(vids)
    title = s.get("title") or f"{s['name']} in Sri Lanka for Indian Companies | Sri Lanka for Indians"
    desc = s.get("desc") or re.sub("<[^>]+>", "", s["lead"])[:300]
    return head(title, desc, f"why/{s['slug']}.html", depth, schema) + header(depth) + body + footer(depth)

def hub():
    depth = 1
    cards = "".join(
        f'<a class="card link-card" href="{s["slug"]}.html"><span class="tag">{s["name"]}</span><h3>{re.sub("<[^>]+>","",s["h1"])}</h3><p>{s["facts"][0][0]}: {s["facts"][0][1]}</p><span class="go">Why it works &rarr;</span></a>'
        for s in SECTORS)
    existing = "".join(f'<a href="../{f}">{n}</a>' for f, n in EXISTING)
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; Why Sri Lanka</p>
  <span class="eyebrow">Why Sri Lanka</span>
  <h1>Sixteen reasons Indian money <em>is crossing the strait.</em></h1>
  <p class="lead">Every sector page below starts with the numbers, gives you three reasons, and ends with the India angle. Pick yours.</p>
</div></section>
<section class="band"><div class="wrap">
  <div class="grid c4">{cards}</div>
  <h3 style="margin-top:48px">Also on Sri Lanka for Indians</h3>
  <div class="chips" style="margin-top:16px">{existing}<a href="../port-city-tax.html">Port City 7.5% tax</a><a href="../guides/start-a-company-in-sri-lanka.html">Set up a company</a><a href="../guides/india-sri-lanka-free-trade-agreement.html">India Sri Lanka FTA</a></div>
</div></section>
""" + cta_banner("Your sector is not listed?", "Tell us what you do. If there is an angle in Sri Lanka, we will find it.", "Hi, my sector is ")
    schema = crumb_schema([("Why Sri Lanka", "why/index.html")])
    return head("Why Sri Lanka: 16 Sectors for Indian Businesses",
                "Why Sri Lanka for tech, BPO, GCCs, fintech, spices, tea, gems, apparel, graphite, coconut, ports, renewables, hotels, wellness, events and film. Numbers, reasons and the India angle.",
                "why/index.html", depth, schema) + header(depth) + body + footer(depth)

def build(write):
    write("why/index.html", hub())
    for s in SECTORS:
        write(f"why/{s['slug']}.html", page(s))
