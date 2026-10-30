"""Utility pages that answer high volume searches: LKR to INR converter."""
from sitekit import *

FALLBACK_LKR_PER_INR = 3.49   # 30 Oct 2026, open.er-api.com: 1 INR = 3.4898 LKR
RATE_DATE = "30 October 2026"

def fmt_in(n):
    """Indian digit grouping: 1,00,000"""
    n = round(n)
    s = str(int(n))
    if len(s) <= 3: return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head: parts.insert(0, head)
    return ",".join(parts) + "," + tail

def converter_js(r, hi=False):
    swap_from = ('भारतीय रुपये (INR)', 'श्रीलंकाई रुपये (LKR)') if hi else ('Indian rupees (INR)', 'Sri Lankan rupees (LKR)')
    return f"""<script>
(function(){{
  var rate={r}, dir='lkr', amt=document.getElementById('fx-amt'), out=document.getElementById('fx-out'), meta=document.getElementById('fx-meta');
  function ind(n){{return n<100 ? n.toFixed(2) : Math.round(n).toLocaleString('en-IN');}}
  function run(){{
    var v=parseFloat(amt.value)||0;
    out.textContent = dir==='lkr' ? '\\u20B9'+ind(v/rate) : 'LKR '+ind(v*rate);
  }}
  document.getElementById('fx-swap').addEventListener('click',function(){{
    dir = dir==='lkr' ? 'inr' : 'lkr';
    document.getElementById('fx-from-l').textContent = dir==='lkr' ? '{swap_from[1]}' : '{swap_from[0]}';
    document.getElementById('fx-to-l').textContent = dir==='lkr' ? '{swap_from[0]}' : '{swap_from[1]}';
    run();
  }});
  amt.addEventListener('input',run);
  fetch('https://open.er-api.com/v6/latest/INR').then(function(r){{return r.json();}}).then(function(j){{
    if(!j||!j.rates||!j.rates.LKR) return;
    rate=j.rates.LKR;
    var d=new Date(j.time_last_update_unix*1000).toLocaleDateString('en-IN',{{day:'numeric',month:'long',year:'numeric'}});
    meta.innerHTML='1 INR = '+rate.toFixed(2)+' LKR &middot; 1 LKR = &#8377;'+(1/rate).toFixed(3)+' &middot; {"लाइव रेट, अपडेट " if hi else "Live rate, updated "}'+d+'. {"बैंक या कार्ड अपना मार्जिन जोड़ते हैं।" if hi else "Indicative mid market rate; your bank or card will add a margin."}';
    document.querySelectorAll('[data-lkr]').forEach(function(td){{td.textContent='\\u20B9'+ind(td.dataset.lkr/rate);}});
    document.querySelectorAll('[data-inr]').forEach(function(td){{td.textContent='LKR '+ind(td.dataset.inr*rate);}});
    run();
    if(typeof gtag==='function') gtag('event','fx_rate_loaded');
  }}).catch(function(){{}});
  run();
}})();
</script>
"""

def converter():
    r = FALLBACK_LKR_PER_INR
    lkr_rows = "".join(f'<tr><td class="num"><a href="lkr-to-inr/{a}-lkr-to-inr.html">LKR {fmt_in(a)}</a></td><td class="num" data-lkr="{a}">&#8377;{fmt_in(a / r)}</td></tr>'
                       for a in (100, 500, 1000, 2000, 5000, 10000, 25000, 50000, 100000, 1000000))
    pop = "".join(f'<a href="lkr-to-inr/{a}-lkr-to-inr.html">{fmt_in(a)} LKR to INR</a>' for a in AMOUNTS)
    inr_rows = "".join(f'<tr><td class="num">&#8377;{fmt_in(a)}</td><td class="num" data-inr="{a}">LKR {fmt_in(a * r)}</td></tr>'
                       for a in (100, 500, 1000, 2000, 5000, 10000, 25000, 50000, 100000))
    faqs = [
        ("What is 1 Sri Lankan rupee in Indian rupees?", f"About 0.29 Indian rupees. Put the other way, 1 Indian rupee buys about {r:.2f} Sri Lankan rupees ({RATE_DATE}). The converter on this page loads the latest rate."),
        ("What is the quick way to convert LKR to INR in your head?", "Divide the Sri Lankan price by 3.5. A LKR 3,500 dinner is about Rs 1,000, and a LKR 700 tuk tuk ride is about Rs 200."),
        ("Is the Indian rupee accepted in Sri Lanka?", "Not for everyday payments. Shops, hotels and tuk tuks price in Sri Lankan rupees. The Indian rupee is on Sri Lanka's list of designated foreign currencies, which matters for banks and trade settlement, not for paying a shopkeeper."),
        ("Can I use UPI in Sri Lanka?", "Yes, at merchants that display a LankaQR code. UPI went live in Sri Lanka in February 2024. Turn on international UPI in your app before you fly."),
        ("How much Indian cash can I carry out of India?", "RBI allows Indian residents travelling abroad to carry up to Rs 25,000 in Indian currency notes, except to Nepal and Bhutan. For anything more, use a forex card, an international debit card or UPI."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">Home</a> &rsaquo; LKR to INR</p>
  <span class="eyebrow">Currency converter</span>
  <h1>Sri Lankan rupee to Indian rupee, <em>live.</em></h1>
  <p class="lead"><strong style="color:#fff;font-weight:500">1 Sri Lankan rupee = &#8377;{1 / r:.3f}</strong> and 1 Indian rupee = LKR {r:.2f} today. Type an amount and switch direction. Quick rule while you travel: <strong style="color:#fff;font-weight:500">divide any Sri Lankan price by 3.5</strong> to get rupees.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="calc fx" id="fx">
    <div class="fx-row">
      <div class="field"><label for="fx-amt" id="fx-from-l">Sri Lankan rupees (LKR)</label><input id="fx-amt" type="number" inputmode="decimal" min="0" value="10000"></div>
      <button class="btn btn-ghost fx-swap" id="fx-swap" type="button" aria-label="Swap direction">&#8646; Swap</button>
      <div class="field"><label id="fx-to-l">Indian rupees (INR)</label><output id="fx-out" class="fx-out" for="fx-amt">&#8377;{fmt_in(10000 / r)}</output></div>
    </div>
    <p class="small fx-meta" id="fx-meta">1 INR = {r:.2f} LKR &middot; 1 LKR = &#8377;{1 / r:.3f} &middot; Rate as of {RATE_DATE}. Indicative mid market rate; your bank or card will add a margin.</p>
  </div>

  <div class="grid c2" style="margin-top:44px">
    <div class="card"><h3>LKR to INR</h3><div class="table-scroll"><table style="min-width:0"><tr><th>Sri Lankan rupees</th><th class="num">Indian rupees</th></tr>{lkr_rows}</table></div></div>
    <div class="card"><h3>INR to LKR</h3><div class="table-scroll"><table style="min-width:0"><tr><th>Indian rupees</th><th class="num">Sri Lankan rupees</th></tr>{inr_rows}</table></div></div>
  </div>
  <h3 style="margin-top:44px">Popular amounts</h3>
  <div class="chips" style="margin-top:16px">{pop}</div>
</div></section>

<section class="band sand"><div class="wrap prose">
  <span class="eyebrow">Paying in Sri Lanka</span>
  <h2>How Indians actually <em>pay on the island.</em></h2>
  <ul>
    <li><strong>UPI:</strong> scan LankaQR codes with your Indian UPI app at shops and restaurants that show them. Enable international UPI first.</li>
    <li><strong>Cards:</strong> Visa and Mastercard work in hotels, malls and most restaurants. A forex card avoids most markups.</li>
    <li><strong>Cash:</strong> take Sri Lankan rupees from an airport ATM for tuk tuks, temples and small shops.</li>
    <li><strong>Indian notes:</strong> you can carry up to Rs 25,000 out of India, but do not plan on spending them in Sri Lanka.</li>
  </ul>
  <p>Doing business rather than travelling? Trade between Indian and Sri Lankan companies can be invoiced and settled in Indian rupees. See <a href="guides/trade-in-rupees-india-sri-lanka.html">how rupee trade works</a>.</p>
  <p>Budgeting a whole trip? See the <a href="guides/trip-cost-from-india.html">Sri Lanka trip cost from India</a> in rupees.</p>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">Quick answers</span>
  <div style="margin-top:20px; max-width:880px">{faq_html}</div>
</div></section>
""" + cta_banner("Planning the trip, not just the money?", "Tell us dates and budget in rupees. We send back a plan with real prices.", "Hi, I want a Sri Lanka plan within my budget")
    js = converter_js(r)
    schema = crumb_schema([("LKR to INR", "sri-lankan-rupee-to-inr.html")]) + "\n" + faq_schema(faqs)
    return head("LKR to INR Today: Sri Lankan Rupee to Indian Rupee Converter",
                f"Convert Sri Lankan rupees to Indian rupees at the live rate. 1 INR is about {r:.2f} LKR: divide Sri Lankan prices by 3.5. Tables, UPI tips and cash rules for Indians.",
                "sri-lankan-rupee-to-inr.html", 0, schema, alt={"en": "sri-lankan-rupee-to-inr.html", "hi": HI_PATH}) + header(0, alt_path=HI_PATH) + body + footer(0, extra_js=js)

HI_PATH = "hi/shrilanka-rupaya-inr.html"

def converter_hi():
    r = FALLBACK_LKR_PER_INR
    lkr_rows = "".join(f'<tr><td class="num">LKR {fmt_in(a)}</td><td class="num" data-lkr="{a}">&#8377;{fmt_in(a / r)}</td></tr>'
                       for a in (100, 500, 1000, 5000, 10000, 50000, 100000))
    faqs = [
        ("1 श्रीलंकाई रुपया कितने भारतीय रुपये के बराबर है?", f"लगभग 0.29 भारतीय रुपये। यानी 1 भारतीय रुपया लगभग {r:.2f} श्रीलंकाई रुपये के बराबर है ({RATE_DATE})। ऊपर का कन्वर्टर ताज़ा रेट दिखाता है।"),
        ("दिमाग में जल्दी कैसे बदलें?", "श्रीलंकाई कीमत को 3.5 से भाग दें। LKR 3,500 का खाना लगभग 1,000 रुपये का है।"),
        ("क्या श्रीलंका में भारतीय रुपया चलता है?", "रोज़मर्रा के भुगतान में नहीं। दुकानें और होटल श्रीलंकाई रुपये में दाम लेते हैं। LankaQR वाली जगहों पर UPI चलता है।"),
        ("भारत से कितना भारतीय कैश ले जा सकते हैं?", "RBI के नियम के अनुसार विदेश यात्रा पर 25,000 रुपये तक के भारतीय नोट ले जा सकते हैं (नेपाल और भूटान को छोड़कर)। बाकी के लिए फॉरेक्स कार्ड या UPI इस्तेमाल करें।"),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; श्रीलंकाई रुपया</p>
  <span class="eyebrow">करेंसी कन्वर्टर</span>
  <h1>श्रीलंकाई रुपया से भारतीय रुपया, <em>लाइव रेट।</em></h1>
  <p class="lead">रकम लिखें और दिशा बदलें। यात्रा का आसान नियम: <strong style="color:#fff;font-weight:500">श्रीलंकाई कीमत को 3.5 से भाग दें</strong>, भारतीय रुपये मिल जाएँगे।</p>
</div></section>
<section class="band"><div class="wrap">
  <div class="calc fx" id="fx">
    <div class="fx-row">
      <div class="field"><label for="fx-amt" id="fx-from-l">श्रीलंकाई रुपये (LKR)</label><input id="fx-amt" type="number" inputmode="decimal" min="0" value="10000"></div>
      <button class="btn btn-ghost fx-swap" id="fx-swap" type="button" aria-label="दिशा बदलें">&#8646; बदलें</button>
      <div class="field"><label id="fx-to-l">भारतीय रुपये (INR)</label><output id="fx-out" class="fx-out" for="fx-amt">&#8377;{fmt_in(10000 / r)}</output></div>
    </div>
    <p class="small fx-meta" id="fx-meta">1 INR = {r:.2f} LKR &middot; रेट {RATE_DATE} का। बैंक या कार्ड अपना मार्जिन जोड़ते हैं।</p>
  </div>
  <div class="table-scroll" style="margin-top:36px; max-width:560px"><table style="min-width:0"><tr><th>श्रीलंकाई रुपये</th><th class="num">भारतीय रुपये</th></tr>{lkr_rows}</table></div>
  <p style="margin-top:26px">पूरी यात्रा का खर्च देखें: <a href="yatra.html">श्रीलंका यात्रा गाइड</a>।</p>
</div></section>
<section class="band sand"><div class="wrap">
  <span class="eyebrow">सीधे जवाब</span>
  <div style="margin-top:20px; max-width:880px">{faq_html}</div>
</div></section>
"""
    js = converter_js(r, hi=True)
    schema = crumb_schema([("श्रीलंकाई रुपया", HI_PATH)]) + "\n" + faq_schema(faqs)
    return head("श्रीलंकाई रुपया से भारतीय रुपया: लाइव कन्वर्टर",
                f"श्रीलंकाई रुपये को भारतीय रुपये में बदलें। 1 INR लगभग {r:.2f} LKR: श्रीलंकाई कीमत को 3.5 से भाग दें। UPI और कैश के नियम भी।",
                HI_PATH, 1, schema, lang="hi", alt={"en": "sri-lankan-rupee-to-inr.html", "hi": HI_PATH}) + header(1, "hi", "sri-lankan-rupee-to-inr.html") + body + footer(1, "hi", extra_js=js)

AMOUNTS = (1, 5, 10, 20, 25, 50, 100, 200, 250, 300, 500, 800, 1000, 1500, 2000, 2500, 3000, 5000, 6000,
           10000, 15000, 17500, 20000, 22000, 25000, 30000, 40000, 50000, 60000, 70000, 75000, 100000, 200000, 500000, 1000000)

def amt_path(a): return f"lkr-to-inr/{a}-lkr-to-inr.html"

def fmt_money(v):
    """Rupee value: paise precision below 100, whole rupees above."""
    return f"{v:,.2f}" if v < 100 else fmt_in(v)

def amount_page(a):
    r = FALLBACK_LKR_PER_INR
    inr = a / r
    with_margin = inr * 1.035
    i = AMOUNTS.index(a)
    near = AMOUNTS[max(0, i - 4): i + 5]
    rows = "".join(
        (f'<tr><td class="num"><strong>LKR {fmt_in(x)}</strong></td><td class="num" data-lkr="{x}"><strong>&#8377;{fmt_money(x / r)}</strong></td></tr>' if x == a else
         f'<tr><td class="num"><a href="{x}-lkr-to-inr.html">LKR {fmt_in(x)}</a></td><td class="num" data-lkr="{x}">&#8377;{fmt_money(x / r)}</td></tr>')
        for x in near)
    chips = "".join(f'<a href="{x}-lkr-to-inr.html">{fmt_in(x)} LKR</a>' for x in AMOUNTS if x != a)
    A = fmt_in(a); I = fmt_money(inr)
    faqs = [
        (f"How much is {A} Sri Lankan rupees in Indian rupees?", f"LKR {A} is about &#8377;{I} at the mid market rate of 1 INR = {r:.2f} LKR ({RATE_DATE}). The converter on this page loads the latest rate."),
        (f"How much will {A} LKR actually cost me with an Indian card?", f"Indian banks and forex cards usually add a markup of 2 to 3.5% plus GST on international spends. At a 3.5% markup, LKR {A} costs you about &#8377;{fmt_money(with_margin)}. A zero markup forex card or UPI on LankaQR keeps it close to &#8377;{I}."),
        ("What is the quick way to convert LKR to INR?", "Divide the Sri Lankan amount by 3.5. It is close enough for shopping, tuk tuks and restaurant bills."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{x}</p></details>" for q, x in faqs)
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="../index.html">Home</a> &rsaquo; <a href="../sri-lankan-rupee-to-inr.html">LKR to INR</a> &rsaquo; {A} LKR</p>
  <span class="eyebrow">LKR to INR today</span>
  <h1>{A} Sri Lankan {"rupee" if a == 1 else "rupees"} = <em data-lkr="{a}">&#8377;{I}</em></h1>
  <p class="lead">At today's rate of 1 INR = {r:.2f} LKR, <strong style="color:#fff;font-weight:500">LKR {A} is about &#8377;{I}</strong>. Quick rule: divide any Sri Lankan price by 3.5.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="calc fx" id="fx">
    <div class="fx-row">
      <div class="field"><label for="fx-amt" id="fx-from-l">Sri Lankan rupees (LKR)</label><input id="fx-amt" type="number" inputmode="decimal" min="0" value="{a}"></div>
      <button class="btn btn-ghost fx-swap" id="fx-swap" type="button" aria-label="Swap direction">&#8646; Swap</button>
      <div class="field"><label id="fx-to-l">Indian rupees (INR)</label><output id="fx-out" class="fx-out" for="fx-amt">&#8377;{I}</output></div>
    </div>
    <p class="small fx-meta" id="fx-meta">1 INR = {r:.2f} LKR &middot; 1 LKR = &#8377;{1 / r:.3f} &middot; Rate as of {RATE_DATE}. Indicative mid market rate; your bank or card will add a margin.</p>
  </div>

  <div class="grid c2" style="margin-top:44px">
    <div class="card"><h3>Amounts near LKR {A}</h3><div class="table-scroll"><table style="min-width:0"><tr><th>Sri Lankan rupees</th><th class="num">Indian rupees</th></tr>{rows}</table></div></div>
    <div class="card"><h3>What you actually pay</h3>
      <div class="table-scroll"><table style="min-width:0">
        <tr><th>How you pay</th><th class="num">Cost of LKR {A}</th></tr>
        <tr><td>Mid market rate</td><td class="num">&#8377;{I}</td></tr>
        <tr><td>Card with 3.5% markup</td><td class="num">&#8377;{fmt_money(with_margin)}</td></tr>
      </table></div>
      <p class="small" style="margin-top:14px">Paying in Sri Lanka? <a href="../guides/money-upi-sim.html">UPI, cards and cash for Indians</a>.</p>
    </div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">Quick answers</span>
  <div style="margin-top:20px; max-width:880px">{faq_html}</div>
  <h3 style="margin-top:44px">Other amounts</h3>
  <div class="chips" style="margin-top:16px">{chips}</div>
  <p style="margin-top:26px">Budgeting the whole trip? See the <a href="../guides/trip-cost-from-india.html">Sri Lanka trip cost from India</a> in rupees, or the <a href="../sri-lankan-rupee-to-inr.html">full LKR to INR converter</a>.</p>
</div></section>
""" + cta_banner("Planning the trip, not just the money?", "Tell us dates and budget in rupees. We send back a plan with real prices.", "Hi, I want a Sri Lanka plan within my budget")
    js = converter_js(r)
    schema = crumb_schema([("LKR to INR", "sri-lankan-rupee-to-inr.html"), (f"{A} LKR", amt_path(a))]) + "\n" + faq_schema(faqs)
    unit = "Rupee" if a == 1 else "Rupees"
    return head(f"{a} LKR to INR Today: {A} Sri Lankan {unit} = \u20b9{I}",
                f"{A} Sri Lankan {unit.lower()} is about \u20b9{I} today (1 INR = {r:.2f} LKR). Live converter, nearby amounts and what it costs on an Indian card.",
                amt_path(a), 1, schema) + header(1) + body + footer(1, extra_js=js)

def build(write):
    write("sri-lankan-rupee-to-inr.html", converter())
    write(HI_PATH, converter_hi())
    for a in AMOUNTS:
        write(amt_path(a), amount_page(a))
