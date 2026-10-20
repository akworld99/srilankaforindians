"""Utility pages that answer high volume searches: LKR to INR converter."""
from sitekit import *

FALLBACK_LKR_PER_INR = 3.49   # 20 Oct 2026, open.er-api.com: 1 INR = 3.4946 LKR
RATE_DATE = "20 October 2026"

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
  function ind(n){{return Math.round(n).toLocaleString('en-IN');}}
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
    lkr_rows = "".join(f'<tr><td class="num">LKR {fmt_in(a)}</td><td class="num" data-lkr="{a}">&#8377;{fmt_in(a / r)}</td></tr>'
                       for a in (100, 500, 1000, 2000, 5000, 10000, 25000, 50000, 100000, 1000000))
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
  <p class="lead">Type an amount and switch direction. Quick rule while you travel: <strong style="color:#fff;font-weight:500">divide any Sri Lankan price by 3.5</strong> to get rupees.</p>
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
    return head("Sri Lankan Rupee to INR: Live LKR to Indian Rupee Converter",
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

def build(write):
    write("sri-lankan-rupee-to-inr.html", converter())
    write(HI_PATH, converter_hi())
