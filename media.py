"""Verified YouTube videos and Instagram reels (checked live on 15 Oct 2026: real IDs, upload dates, views, embeddable).
To add a video: append to RAW as id|date|channel|views|seconds|title, tag it, rerun build.py."""

RAW = """
NGoCQ3HyxQs|2022-04-17|Scenic Relaxation|538932|3646|Sri Lanka 4K: Scenic Relaxation Film With Calming Music|scenic
q0mbKsKG-ng|2020-05-24|Beautiful Destinations|2170614|281|Sri Lanka: Heart of the Indian Ocean|scenic
8g9ccCkT-u0|2023-06-01|Lalit Choudhary Films|104675|100|Sri Lanka: 4K Cinematic Travel Film|scenic
dbM8AMmEdgY|2026-10-15|Think School|9477|3258|Kumar Sangakkara Reveals: Why Sri Lanka Could Be the Next Big Real Estate Opportunity|business,estate
iLhRCwjywU8|2026-10-06|Sivaangi Vlogs|573803|1689|Exploring Sri Lanka|creators
gaLWS85uCzA|2024-09-14|Travel with AK|479254|2130|First Impression of Sri Lanka|creators
CW6jTV-hTok|2026-08-25|Shiwali Bhola|392138|1680|First 48 Hours in Sri Lanka, and This Happened|creators
cRQu04IaAUk|2026-10-07|Harish Bali Travels|341320|2042|Delhi to Sri Lanka: Colombo, Nuwara Eliya and Kandy, Local Food and Markets|creators
eiyQbvnxI-Y|2022-08-06|Curly Tales|336503|1812|Sri Lankan Sunday Brunch With Jacqueline Fernandez|creators,food
Bu86Z_7VzAA|2025-02-27|Khushboo Vasudeva|257430|1422|Sri Lanka Budget Travel Guide from India: Costs, Itinerary and More|creators,guide
52E5aIUxzj8|2026-07-27|Noyonika Deb|252468|902|Sri Lanka Vlog Part 2: Mirissa, Boutiques and Breakfast Spots|creators
jmJlx-UIDsk|2026-01-22|That Quirky Miss|230284|1603|First Trip of 2026 With Sri Lanka Tourism: Beach Life, Cafes and Parties|creators
RCHD60fpDnA|2026-02-25|Garima's Good Life|155535|1401|Sri Lanka Tour Package: Tourist Places, Itinerary and Budget|creators,guide
YGeivlm5C78|2025-08-23|Kritika Goel|136607|1511|3 Weeks Living in Weligama, Sri Lanka|creators,secondhome
dbH61QhpZIY|2023-10-07|Curly Tales|100696|995|Sunday Brunch With Muttiah Muralitharan|creators,food
VpQiRlaI5bo|2026-06-25|Traveling Banda|82043|810|Sri Lanka Tour Guide 2026: India to Sri Lanka Trip Plan, Visa, Budget and Itinerary|guide
13_rx2SwFgY|2026-05-10|Harshita Karma|74310|870|My First International Trip to Sri Lanka|creators
qCWQAeRXhZU|2026-09-29|Heena Bhatia|57514|964|India to Sri Lanka: Flights, Visa, Currency and SIM, All You Need to Know|guide
oriToNJZG-k|2026-10-02|Heena Bhatia|56166|1022|The Developed Side of Sri Lanka: 24 Hours in Colombo|creators,colombo
7j335oyBKH8|2026-09-16|viral rao|14740|921|Is the Ella Train Really Worth It? India to Sri Lanka Series|creators
6_-lwBnX3rc|2026-07-20|TravelAway|10267|1841|Is Sri Lanka's East Coast Worth It? Luxury Guide for Indian Vegetarian Families|guide,food
Tw_Ki1aw0us|2025-04-09|Backpacker Sudhi|824548|1781|India to Sri Lanka by Passenger Ship (Malayalam)|ferry
QfFRvTem4zM|2026-10-13|Sudheer The Explorer|78018|1876|India to Sri Lanka by Ferry: Nagapattinam to Jaffna|ferry
XOWAaOTSCtM|2026-09-05|Travel with Soul Voyage|1412|157|Sri Lanka ETA 2026: Free Visa for Indian Passport Holders, Application Guide|visa
WvMdSZ7fmJY|2025-05-21|Lights and Magic|552694|272|Anchana and Raam: Tamil Destination Wedding in Sri Lanka, Kandalama|wedding
gamg1oTsXQg|2026-08-04|SEN South Era Network|57474|960|Why India's Big Fat Weddings Are Fuelling Sri Lanka's Economic Comeback|wedding,business
b1RrqsxLGms|2024-03-13|Lights and Magic|45550|524|Alavi and Prottoy: Sri Lankan Destination Wedding|wedding
YI61kqW-hyE|2024-11-19|Newsfirst Sri Lanka|3965|291|Fabulous Indian Wedding in the Isle of Paradise, Sri Lanka|wedding
Qbf7BM4OV28|2023-09-11|Lights and Magic|4730|480|Malar and TK: Indian Destination Wedding in Sri Lanka|wedding
GHyNEH0kQ3o|2026-07-31|Vineet Dixit|52426|487|Sri Lanka's Incredible Economic Comeback: Bankruptcy to Recovery|business
rIa82ugYTN8|2026-07-06|Mint|53067|321|Sri Lanka Is Now an Upper Middle Income Country: Why Isn't India There Yet?|business
1vIJYuajxik|2026-07-07|Wired World|8217|1133|Sri Lanka 2026: Bankrupt Se Upper Middle Income Kaise Bane? (Hindi)|business,hindi
hvOeE4eW8As|2026-08-12|Port City Colombo|3436|275|Invest in Port City Colombo: South Asia's Business and Lifestyle Hub|portcity,business
B2OIRRQbz8I|2026-08-29|Walking Pixels 4K|33585|1726|Colombo Port City Beach Plaza: Full Walking Tour 2026|portcity,estate
GHGrijFEpgU|2026-04-10|The Walk Around The World|27122|4244|This Doesn't Feel Like Sri Lanka: Port City Colombo 2026 in 4K|portcity,estate
WjjvHceiip0|2025-02-25|Port City BPO|3801|143|Port City BPO Corporate Video|bpo
jOEz-ON842A|2026-09-02|Global Logistics|99012|899|Vizhinjam vs Colombo: Can India Really Build a Global Transshipment Hub?|ports
jvRH8dcbLpg|2019-10-30|Sri Lanka Ports Authority|32137|560|Port of Colombo|ports
OhO5fKkHTH8|2024-02-09|Business Insider|3206374|606|How the World's Most Expensive Cinnamon Is Produced|spices
Mkl1GAE04sg|2025-02-21|South China Morning Post|52536|788|What Makes Sri Lanka the Tea Island of the World?|tea
6PViyPfd000|2026-02-24|GO Asia|11505|3117|Sri Lanka: Inside Tea's Empire (Documentary)|tea
0tyHQkz2rwg|2024-04-30|Davud Akhundzada|232994|3339|Inside the Gem Mines of Ratnapura, Sri Lanka|gems
7hLq8Imgplo|2024-02-16|Kajan Vlogs|324895|2087|Gem Mining in Ratnapura: Blue Sapphires (Tamil)|gems
vD-y2-Uv4ug|2022-01-05|Brandix Lanka|18184|202|Celebrating Our 50 Year Journey|apparel
4YVaZWJYGzI|2019-05-28|MAS Holdings|42518|55|The People Behind the Sri Lanka Cricket Jersey|apparel
D1nxIlWT6o0|2023-05-19|Sheneller|381017|1619|The Best Wellness Retreat in Sri Lanka: Ulpotha|wellness
T-P-dpm6bZE|2023-05-12|Sheneller|99697|1319|The Best Ayurveda Wellness Retreat in the World? Barberyn Resorts|wellness
2SUXqcjFIgI|2024-11-07|SriLankan Airlines|360107|310|Relive the Epic of the Ramayana Trail|ramayana
kRjSsHlA9_0|2026-03-09|Tours and Foods|2608|567|Complete Sri Lanka Ramayana Tour Plan: 10 Day Itinerary|ramayana
iXQ3ij9h6WM|2026-01-10|Wout of the World|31071|2102|Spotting Leopards in Yala National Park|wildlife
AVTidW78qNQ|2025-08-03|NiKo Diaries|23976|1144|Grand Opening: City of Dreams Sri Lanka with Hrithik Roshan, BnS, Yohani, Umara and Umariya|cod
FDoDcwf_pDc|2025-08-13|Irfan's view|473642|941|Most Luxurious Hotel: City of Dreams, Sri Lanka|cod,luxury
rBoKEVmCx0Y|2025-05-18|Wandering Shey|41342|1590|Cinnamon Life Colombo Hotel Review: Luxury Hotel in City of Dreams Sri Lanka|cod,hotel
dVuI5bFoUOY|2025-03-08|Andrew Dobson|95064|1211|ITC Ratnadipa Colombo Tour: Best Luxury Hotel in Sri Lankan Capital|hotel,luxury
3oVYpDEXeLU|2026-03-21|Kripal Amanna|201059|2919|Checking Into Colombo's Finest Destination: A Luxury Escape With The Boss|luxury
PnfdGFtZOPI|2025-10-24|DesiGirl Traveller|168222|2038|48 Hrs in Colombo, Sri Lanka: Best Places to Visit, Local Food, Casino and Nightlife|nightlife
IzKwdP6hcLY|2024-07-03|The Rooftop Guide|8503|192|Best Rooftop Bars in Colombo|nightlife
9119VUOlspA|2026-09-05|Walking Pixels 4K|11768|968|Colombo Port City Waterfront Night Walk: Illuminated Foot Bridge and Galle Face Skyline|portcity,nightlife
zqba47Zl-Wk|2026-04-15|Aarush Bhola Fit - Mess|924471|1165|Full Enjoy at Sri Lanka: Boys Trip|friends
bu0jyUlkwdc|2026-04-19|Chirag Khanna|78250|1429|Sri Lanka with the boys|friends
"""

def _len_txt(s):
    s = int(s); h, r = divmod(s, 3600); m, sec = divmod(r, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"

VIDEOS = []
for line in RAW.strip().splitlines():
    vid, date, ch, views, ln, title, tags = line.split("|")
    VIDEOS.append(dict(id=vid, date=date, ch=ch, views=int(views), len=int(ln), len_txt=_len_txt(ln), title=title, tags=tags.split(",")))
BY_ID = {v["id"]: v for v in VIDEOS}

def tagged(tag, n=None):
    out = [v for v in VIDEOS if tag in v["tags"]]
    out.sort(key=lambda v: -v["views"])
    return out[:n] if n else out

def pick(*ids): return [BY_ID[i] for i in ids]

# Instagram reels found on public tag pages, 15 Oct 2026
REELS = [
    dict(code="DanL7DtMrQN", user="beingzahrajani", tag="travel"),
    dict(code="Dcv6-DkhcYT", user="aishwaryanu", tag="travel"),
    dict(code="DX3YGHxRAqI", user="", tag="travel"),
    dict(code="DXop77WjBbW", user="priyal_udeshi", tag="travel"),
    dict(code="DYmqRqqTXi6", user="sonalagarwal2912", tag="travel"),
    dict(code="DZLKt8Btmgd", user="feeyaa.aa", tag="travel"),
    dict(code="DPwn56Ck0js", user="hell0busra", tag="travel"),
    dict(code="DQl7nshCNTZ", user="beyonddestinysl", tag="wedding"),
    dict(code="DBtbKVphkzY", user="", tag="wedding"),
    dict(code="DR9iv_rjApq", user="", tag="wedding"),
    dict(code="DNM9t8LIe8k", user="joel_outschoorn", tag="wedding"),
]
def reels(tag, n=None):
    out = [r for r in REELS if r["tag"] == tag]
    return out[:n] if n else out
