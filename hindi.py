"""Hindi pages (hi-IN) with hreflang pairs to the English versions."""
from sitekit import *
from media import pick, BY_ID, reels

D = 1  # all Hindi pages live in /hi/

def hi_head(title, desc, path, en_path, schema=""):
    return head(title, desc, path, D, schema, lang="hi", alt={"en": en_path, "hi": path})

def hi_tax_band():
    bars = [("भारत (टॉप स्लैब)", 39, ""), ("सिंगापुर", 24, ""), ("दुबई", 0, "zero-bar"), ("पोर्ट सिटी कोलंबो", 0, "hl zero-bar")]
    bar_html = "".join(f'<div class="bar {c}"><span>{n}</span><span class="track"><span class="fill" style="width:{v/40*100:.0f}%"></span></span><span class="pct">{v}%</span></div>' for n, v, c in bars)
    return f"""<section class="tax-mega"><div class="wrap">
  <div><div class="zero">0%<small>पर्सनल इनकम टैक्स &middot; पोर्ट सिटी कोलंबो</small></div></div>
  <div>
    <span class="eyebrow">वो आंकड़ा जो CFO दोबारा पढ़ते हैं</span>
    <h2>दुबई जैसा टैक्स। <em>चेन्नई जितनी दूरी।</em></h2>
    <p>पोर्ट सिटी कोलंबो में मंज़ूरी प्राप्त कंपनियों को 8 से 15 साल तक कॉर्पोरेट टैक्स हॉलिडे मिलता है, या सेकेंडरी बिज़नेस के लिए 7.5% की दर, और उनके कर्मचारियों ने अब तक शून्य पर्सनल इनकम टैक्स दिया है। दुबई भी शून्य देता है, बस वह चार घंटे दूर है और 2026 में उसी इलाके में है जिसने हर बोर्डरूम को हिला दिया।</p>
    <div class="bars">{bar_html}</div>
    <p class="small">टॉप पर्सनल टैक्स दरें। पोर्ट सिटी के इंसेंटिव Regulation 01 of 2025 के तहत, CPCEC की मंज़ूरी पर निर्भर। भारत के टैक्स रेज़िडेंट की पूरी दुनिया की आय पर टैक्स लगता है, इसलिए आप कहाँ रहते हैं, यही तय करता है कि आप कितना देंगे।</p>
    <div style="display:flex; gap:16px; flex-wrap:wrap; margin-top:18px">
      <a class="btn btn-primary" href="port-city-tax.html">अपनी बचत कैलकुलेट करें</a>
    </div>
  </div>
</div></section>
"""

def index():
    vids = pick("cRQu04IaAUk", "CW6jTV-hTok", "1vIJYuajxik", "Bu86Z_7VzAA", "gaLWS85uCzA", "RCHD60fpDnA")
    faqs = [
        ("क्या भारतीयों को श्रीलंका के लिए वीज़ा चाहिए?", "हाँ, ऑनलाइन ETA लेना होता है। 25 मई 2026 से भारतीयों के लिए 30 दिन का टूरिस्ट ETA (डबल एंट्री) मुफ़्त है। आवेदन केवल आधिकारिक वेबसाइट eta.gov.lk पर करें।"),
        ("क्या भारतीय श्रीलंका में प्रॉपर्टी खरीद सकते हैं?", "विदेशी नागरिक सीधे फ्रीहोल्ड ज़मीन नहीं खरीद सकते, लेकिन ग्राउंड फ्लोर से ऊपर का कॉन्डोमिनियम फ्लैट पूरी तरह अपने नाम खरीद सकते हैं, अगर पूरा भुगतान विदेश से आए पैसे से हो। USD 1,00,000 या उससे अधिक के निवेश पर 5 साल का रेज़िडेंस वीज़ा मिल सकता है।"),
        ("पोर्ट सिटी कोलंबो में टैक्स कितना है?", "Regulation 01 of 2025 के तहत प्राइमरी बिज़नेस को 8 से 15 साल का कॉर्पोरेट टैक्स हॉलिडे, सेकेंडरी बिज़नेस को 4 साल तक 7.5% की दर, और मंज़ूरी प्राप्त कंपनियों के कर्मचारियों के लिए 0% पर्सनल इनकम टैक्स। सभी इंसेंटिव CPCEC की मंज़ूरी पर निर्भर हैं।"),
    ]
    schema = faq_schema(faqs) + "\n" + video_schema(vids)
    body = f"""
<section class="hero has-video">
  <div class="hero-video" aria-hidden="true" style="background-image:url('https://i.ytimg.com/vi/{HERO_ID}/maxresdefault.jpg')">
    <iframe src="https://www.youtube-nocookie.com/embed/{HERO_ID}?autoplay=1&mute=1&loop=1&playlist={HERO_ID}&controls=0&rel=0&playsinline=1&modestbranding=1&cc_load_policy=0&iv_load_policy=3&disablekb=1&fs=0&start=30" title="" tabindex="-1" allow="autoplay; encrypted-media" loading="lazy"></iframe>
  </div>
  <div class="hero-veil"></div>
  <div class="wrap"><div class="hero-inner">
    <span class="eyebrow">नमस्ते &middot; आयुबोवन &middot; वणक्कम</span>
    <h1>हिंद महासागर ने एक द्वीप <em>आपके लिए रखा है।</em></h1>
    <p class="lead">चेन्नई से सिर्फ़ 80 मिनट की उड़ान। समंदर किनारे शादियाँ, डॉलर में कीमत वाले सी फेसिंग घर, और एक ऐसा फाइनेंशियल डिस्ट्रिक्ट जहाँ पर्सनल इनकम टैक्स शून्य है। 2026 के पहले नौ महीनों में 4.3 लाख से ज़्यादा भारतीय श्रीलंका पहुँचे। हम आपके गाइड हैं, शुरू से आख़िर तक।</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="{wa_link('नमस्ते, मैं श्रीलंका के बारे में जानना चाहता/चाहती हूँ')}" rel="noopener">WhatsApp पर बात करें</a>
      <a class="btn btn-ghost" href="shaadi.html">शादी का बजट देखें</a>
    </div>
    <a class="hero-badge" href="port-city-tax.html"><span class="hb-num">0%</span><span class="hb-txt"><b>पोर्ट सिटी कोलंबो</b>पर्सनल इनकम टैक्स। देखें आप कितना बचाएँगे &rarr;</span></a>
  </div></div>
</section>

{hi_tax_band()}

<section class="band"><div class="wrap">
  <span class="eyebrow">हम किसमें मदद करते हैं</span>
  <h2>एक द्वीप। <em>कई मौके।</em></h2>
  <div class="grid c3" style="margin-top:40px">
    <a class="card link-card" href="shaadi.html"><span class="tag">शादी</span><h3>समंदर किनारे डेस्टिनेशन वेडिंग</h3><p>गोवा और उदयपुर से तुलना करें। बारात के लिए वीज़ा मुफ़्त।</p><span class="go">शादी प्लान करें &rarr;</span></a>
    <a class="card link-card" href="property.html"><span class="tag">प्रॉपर्टी</span><h3>डॉलर में कीमत, समंदर का नज़ारा</h3><p>भारतीय क्या खरीद सकते हैं, और 5 साल के वीज़ा का रास्ता।</p><span class="go">नियम पढ़ें &rarr;</span></a>
    <a class="card link-card" href="port-city-tax.html"><span class="tag">0% टैक्स</span><h3>पोर्ट सिटी कोलंबो</h3><p>15 साल तक टैक्स हॉलिडे और 100% विदेशी स्वामित्व।</p><span class="go">आंकड़े देखें &rarr;</span></a>
    <a class="card link-card" href="yatra.html"><span class="tag">यात्रा</span><h3>रामायण ट्रेल, चाय और समंदर</h3><p>मुफ़्त वीज़ा, UPI से भुगतान, और हर शहर से उड़ान।</p><span class="go">यात्रा प्लान करें &rarr;</span></a>
    <a class="card link-card" href="../why/index.html"><span class="tag">बिज़नेस</span><h3>16 सेक्टर, एक नज़र में</h3><p>टेक, BPO, मसाले, चाय, रत्न, कपड़ा, पोर्ट और बहुत कुछ (अंग्रेज़ी में)।</p><span class="go">सेक्टर देखें &rarr;</span></a>
    <a class="card link-card" href="../watch.html"><span class="tag">वीडियो</span><h3>भारतीय क्रिएटर्स की नज़र से</h3><p>50 वीडियो और रील्स, यात्रा से लेकर शादियों तक।</p><span class="go">वीडियो देखें &rarr;</span></a>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">भारत को पसंद है</span>
  <h2>लाखों भारतीयों ने देखा। <em>फिर टिकट बुक किया।</em></h2>
  <p class="lead">भारतीय क्रिएटर्स के असली वीडियो। किसी पर भी टैप करें और यहीं देखें।</p>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">सीधे जवाब</span>
  <h2>हर भारतीय <em>यही पूछता है।</em></h2>
  <div style="margin-top:30px; max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
</div></section>
""" + cta_banner("आपका गाइड बस एक मैसेज दूर है", "बात करने का कोई शुल्क नहीं। हिंदी, तमिल और अंग्रेज़ी में बात करें।", "नमस्ते, मुझे श्रीलंका के बारे में मदद चाहिए", lang="hi")
    return hi_head("श्रीलंका फॉर इंडियंस | शादी, प्रॉपर्टी, पोर्ट सिटी 0% टैक्स और यात्रा",
                   "भारतीयों के लिए श्रीलंका गाइड: डेस्टिनेशन वेडिंग, प्रॉपर्टी, पोर्ट सिटी कोलंबो में 0% पर्सनल इनकम टैक्स, मुफ़्त वीज़ा और यात्रा। WhatsApp पर गाइड से बात करें।",
                   "hi/index.html", "index.html", schema) + header(D, "hi", "index.html") + body + footer(D, "hi")

def shaadi():
    vids = pick("WvMdSZ7fmJY", "gamg1oTsXQg", "YI61kqW-hyE")
    faqs = [("श्रीलंका में डेस्टिनेशन वेडिंग का खर्च कितना है?", "श्रीलंका के बीच रिसॉर्ट अक्सर वेन्यू, कमरे और खाने में गोवा या उदयपुर से कम कीमत रखते हैं, जबकि अंतरराष्ट्रीय फ्लाइट से अंतर कुछ कम हो जाता है। अपने मेहमानों की संख्या के हिसाब से हमारा कैलकुलेटर चलाएँ और तीन असली कोटेशन मंगवाएँ।"),
            ("क्या हम अपने पंडित और सजावट का सामान ला सकते हैं?", "हाँ। यहाँ के रिसॉर्ट नियमित रूप से भारतीय शादियाँ करवाते हैं, और प्लानर के ज़रिए शादी के सामान और पंडित जी की यात्रा की कागज़ी कार्रवाई आसानी से हो जाती है।")]
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; शादी</p>
  <span class="eyebrow">डेस्टिनेशन वेडिंग</span>
  <h1>हिंद महासागर के किनारे <em>सात फेरे।</em></h1>
  <p class="lead">समंदर किनारे मंडप, भारतीय शादियों को समझने वाले रिसॉर्ट, लाइव चाट काउंटर और साउथ इंडियन सद्या बनाने वाले शेफ़। और बारात के हर मेहमान का वीज़ा मुफ़्त।</p>
  <div class="cta-row"><a class="btn btn-primary" href="#calculator">बजट कैलकुलेट करें</a></div>
</div></section>

<section class="band" id="calculator"><div class="wrap">
  <span class="eyebrow">शादी का हिसाब</span>
  <h2>गोवा बनाम श्रीलंका, <em>आपके आंकड़ों पर।</em></h2>
  <div class="calc" style="margin-top:36px">
    <div class="calc-grid">
      <div class="field"><label for="guests">मेहमान</label><input type="number" id="guests" min="30" max="1000" step="10" value="150"></div>
      <div class="field"><label for="days">फंक्शन के दिन</label><select id="days"><option value="1">1 दिन</option><option value="2" selected>2 दिन</option><option value="3">3 दिन</option></select></div>
      <div class="field"><label for="tier">स्टाइल</label><select id="tier"><option value="silver">सादा</option><option value="gold" selected>प्रीमियम रिसॉर्ट</option><option value="royal">पूरा शाही</option></select></div>
      <div class="field"><label for="origin">कहाँ से उड़ान</label><select id="origin"><option value="chennai" selected>चेन्नई</option><option value="bengaluru">बेंगलुरु</option><option value="mumbai">मुंबई</option><option value="delhi">दिल्ली</option><option value="hyderabad">हैदराबाद</option><option value="kolkata">कोलकाता</option><option value="ahmedabad">अहमदाबाद</option><option value="pune">पुणे</option></select></div>
    </div>
    <div class="calc-results">
      <div class="result" id="res-india"><h3>गोवा / उदयपुर <span class="total num" id="total-india">&#8377;0</span></h3><ul>
        <li><span>वेन्यू, खाना, सजावट</span><b class="num" id="in-pkg">&#8377;0</b></li>
        <li><span>मेहमानों के कमरे</span><b class="num" id="in-rooms">&#8377;0</b></li>
        <li><span>घरेलू उड़ानें</span><b class="num" id="in-fly">&#8377;0</b></li></ul></div>
      <div class="result win" id="res-sl"><h3>श्रीलंका <span class="total num" id="total-sl">&#8377;0</span></h3><ul>
        <li><span>वेन्यू, खाना, सजावट</span><b class="num" id="sl-pkg">&#8377;0</b></li>
        <li><span>मेहमानों के कमरे</span><b class="num" id="sl-rooms">&#8377;0</b></li>
        <li><span>अंतरराष्ट्रीय उड़ानें</span><b class="num" id="sl-fly">&#8377;0</b></li></ul></div>
    </div>
    <div class="savings"><span id="savings-line">अंतर</span> <b class="num" id="savings-amt">&#8377;0</b>
      <p class="small" style="margin:12px 0 18px">अनुमानित आंकड़े। असली कीमत रिसॉर्ट, सीज़न और मेन्यू पर निर्भर है। हम तीन रिसॉर्ट से असली कोटेशन मुफ़्त मंगवाते हैं।</p>
      <a class="btn btn-primary" href="{wa_link('नमस्ते, मैंने शादी का कैलकुलेटर देखा। कृपया 3 असली कोटेशन भेजें।')}" rel="noopener">3 असली कोटेशन पाएँ</a></div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">असली शादियाँ</span>
  <h2>जो पहले <em>कर चुके हैं।</em></h2>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
  <div style="margin-top:40px">{ig_grid(reels('wedding', 3))}</div>
</div></section>

<section class="band"><div class="wrap">
  <div style="max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
</div></section>
""" + cta_banner("तारीख़ तय है? पहले वेन्यू बुक करें।", "पीक सीज़न के वेन्यू 9 से 12 महीने पहले बुक हो जाते हैं।", "नमस्ते, हम श्रीलंका में शादी प्लान कर रहे हैं", lang="hi")
    schema = faq_schema(faqs) + "\n" + video_schema(vids)
    return hi_head("श्रीलंका में डेस्टिनेशन वेडिंग: गोवा से तुलना, खर्च और वेन्यू | Sri Lanka for Indians",
                   "भारतीयों के लिए श्रीलंका में डेस्टिनेशन वेडिंग: गोवा और उदयपुर से खर्च की तुलना का कैलकुलेटर, बीच वेन्यू, मुफ़्त वीज़ा और 3 असली कोटेशन।",
                   "hi/shaadi.html", "weddings.html", schema) + header(D, "hi", "weddings.html") + body + footer(D, "hi", extra_js=f'<script src="../assets/js/calculator.js?v={ASSET_V}"></script>\n')

def property_page():
    vids = pick("dbM8AMmEdgY", "B2OIRRQbz8I", "GHGrijFEpgU")
    faqs = [("क्या भारतीय श्रीलंका में फ्लैट खरीद सकते हैं?", "हाँ। विदेशी नागरिक ग्राउंड फ्लोर से ऊपर का कॉन्डोमिनियम फ्लैट पूरी तरह अपने नाम खरीद सकते हैं, अगर पूरा भुगतान विदेश से आए पैसे (Inward Investment Account) से हो। फ्रीहोल्ड ज़मीन पर रोक है; ज़मीन लंबी लीज़ पर ली जाती है।"),
            ("क्या प्रॉपर्टी खरीदने से रेज़िडेंस वीज़ा मिलता है?", "USD 1,00,000 या उससे अधिक के योग्य प्रॉपर्टी निवेश पर 5 साल का रिन्यू होने वाला रेज़िडेंस वीज़ा मिल सकता है।"),
            ("भारत से पैसा भेजने के नियम क्या हैं?", "भारत से विदेश में निवेश RBI और FEMA के नियमों के तहत होता है, जिसमें व्यक्तियों के लिए LRS सीमा शामिल है। पैसा भेजने से पहले अपने CA से बात करें।")]
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; प्रॉपर्टी</p>
  <span class="eyebrow">प्रॉपर्टी</span>
  <h1>भारत से एक घंटे दूर, <em>समंदर के सामने घर।</em></h1>
  <p class="lead">हाँ, भारतीय यहाँ खरीद सकते हैं। कॉन्डोमिनियम फ्लैट पूरी तरह अपने नाम, ज़मीन लंबी लीज़ पर, और पोर्ट सिटी में नए अपार्टमेंट। USD 1,00,000 के निवेश पर 5 साल का रेज़िडेंस वीज़ा।</p>
  <div class="cta-row"><a class="btn btn-primary" href="{wa_link('नमस्ते, मैं श्रीलंका में प्रॉपर्टी खरीदना चाहता/चाहती हूँ')}" rel="noopener">शॉर्टलिस्ट मंगवाएँ</a></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="grid c2">
    <div class="card"><span class="tag">कर सकते हैं</span><h3>भारतीय क्या खरीद सकते हैं</h3><ul style="padding-left:18px">
      <li>ग्राउंड फ्लोर से ऊपर के कॉन्डोमिनियम फ्लैट, पूरा भुगतान विदेश से आए पैसे से</li>
      <li>ज़मीन लंबी लीज़ पर, आमतौर पर 99 साल तक</li>
      <li>पोर्ट सिटी कोलंबो के अपार्टमेंट</li>
      <li>लिस्टेड प्रॉपर्टी कंपनियों के शेयर</li></ul></div>
    <div class="card"><span class="tag">नहीं कर सकते</span><h3>क्या मना है</h3><ul style="padding-left:18px">
      <li>विदेशी नागरिक के नाम पर फ्रीहोल्ड ज़मीन</li>
      <li>50% या अधिक विदेशी स्वामित्व वाली कंपनी के ज़रिए फ्रीहोल्ड ज़मीन</li>
      <li>गैर निवासी के रूप में स्थानीय बैंक से होम लोन</li>
      <li>बैंकिंग चैनल के बाहर नकद भुगतान</li></ul></div>
  </div>
  <p class="small" style="margin-top:16px">नियमों का सारांश। हमेशा कोलंबो के लाइसेंस प्राप्त प्रॉपर्टी वकील से पुष्टि करें। हम आपको उनसे मिलवाते हैं।</p>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">थिंक स्कूल &times; कुमार संगकारा</span>
  <h2>"अगला बड़ा रियल एस्टेट मौका।" <em>उन्हीं के शब्दों में।</em></h2>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
</div></section>

<section class="band"><div class="wrap">
  <div style="max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
</div></section>
""" + cta_banner("मौजूदा शॉर्टलिस्ट चाहिए?", "कोलंबो और साउथ कोस्ट के हर प्रोजेक्ट पर हमारी नज़र है। कीमत, किराया और जोखिम।", "नमस्ते, कृपया श्रीलंका प्रॉपर्टी शॉर्टलिस्ट भेजें", lang="hi")
    schema = faq_schema(faqs) + "\n" + video_schema(vids)
    return hi_head("क्या भारतीय श्रीलंका में प्रॉपर्टी खरीद सकते हैं? नियम, वीज़ा और पोर्ट सिटी | Sri Lanka for Indians",
                   "भारतीयों के लिए श्रीलंका प्रॉपर्टी गाइड: कॉन्डोमिनियम खरीदने के नियम, USD 1,00,000 पर 5 साल का वीज़ा, पोर्ट सिटी अपार्टमेंट और RBI/FEMA नियम।",
                   "hi/property.html", "real-estate.html", schema) + header(D, "hi", "real-estate.html") + body + footer(D, "hi")

def tax():
    faqs = [("पोर्ट सिटी कोलंबो में टैक्स कितना है?", "Regulation 01 of 2025 के तहत प्राइमरी बिज़नेस को निवेश के हिसाब से 8 से 15 साल का कॉर्पोरेट टैक्स हॉलिडे, सेकेंडरी बिज़नेस को 4 साल तक 7.5% की दर, और मंज़ूरी प्राप्त कंपनियों के कर्मचारियों के लिए 0% पर्सनल इनकम टैक्स।"),
            ("क्या भारतीयों के लिए पोर्ट सिटी टैक्स फ्री है?", "इंसेंटिव ज़ोन की मंज़ूरी प्राप्त कंपनियों पर लागू होते हैं, मालिक की राष्ट्रीयता से फ़र्क नहीं पड़ता। लेकिन अगर आप भारत के टैक्स रेज़िडेंट हैं, तो आपकी पूरी दुनिया की आय पर भारत में टैक्स लगता है। अपने CA से सलाह लें।")]
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; पोर्ट सिटी टैक्स</p>
  <span class="eyebrow">पोर्ट सिटी कोलंबो</span>
  <h1>शून्य। <em>इस साइट का सबसे अहम आंकड़ा।</em></h1>
  <p class="lead">पोर्ट सिटी कोलंबो एक स्पेशल इकोनॉमिक ज़ोन है जिसके अपने टैक्स नियम हैं। मंज़ूरी प्राप्त कंपनियों को 15 साल तक कॉर्पोरेट टैक्स हॉलिडे, और उनके कर्मचारियों पर शून्य पर्सनल इनकम टैक्स।</p>
  <div class="facts">
    <div class="fact"><b>0%</b><span>मंज़ूरी प्राप्त कंपनियों के कर्मचारियों पर पर्सनल इनकम टैक्स</span></div>
    <div class="fact"><b>8 से 15 साल</b><span>प्राइमरी बिज़नेस के लिए कॉर्पोरेट टैक्स हॉलिडे</span></div>
    <div class="fact"><b>7.5%</b><span>सेकेंडरी बिज़नेस के लिए 4 साल तक कॉर्पोरेट टैक्स</span></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">आप कितना बचाएँगे?</span>
  <h2>आपकी सैलरी: <em>भारत बनाम पोर्ट सिटी।</em></h2>
  <p class="lead">स्लाइडर को अपनी सालाना सैलरी पर लाएँ। हम FY 2025-26 की न्यू टैक्स रिजीम के हिसाब से भारत का इनकम टैक्स निकालते हैं।</p>
  <div class="taxcalc" style="margin-top:34px">
    <label for="tc-salary" style="display:block"><span style="display:block; font-size:.8rem; color:var(--gold); margin-bottom:8px">सालाना सैलरी</span><span class="tc-val num" id="tc-out-salary">&#8377;50 L</span></label>
    <input type="range" id="tc-salary" min="10" max="500" step="5" value="50" aria-label="सालाना सैलरी, लाख रुपये में">
    <div class="tc-row">
      <div class="tc-cell"><span>भारत में इनकम टैक्स (न्यू रिजीम)</span><b class="num" id="tc-india">&#8377;0</b><span id="tc-rate"></span></div>
      <div class="tc-cell"><span>पोर्ट सिटी में पर्सनल टैक्स</span><b class="num">&#8377;0</b><span>मंज़ूरी प्राप्त कंपनियों के कर्मचारी</span></div>
      <div class="tc-cell gold"><span>हर साल आपकी बचत</span><b class="num" id="tc-keep">&#8377;0</b><span>5 साल में: <span id="tc-5yr" class="num">&#8377;0</span></span></div>
    </div>
    <p class="small" style="margin-top:18px">केवल उदाहरण के लिए। FY 2025-26 न्यू रिजीम स्लैब, &#8377;75,000 स्टैंडर्ड डिडक्शन, धारा 87A रिबेट, सरचार्ज और 4% सेस। यह बचत तभी लागू है जब आप भारत के टैक्स रेज़िडेंट न हों: मोटे तौर पर साल में 182 दिन से कम भारत में, और ज़्यादा कमाने वाले नागरिकों के लिए अतिरिक्त नियम। अपने CA से बात करें।</p>
  </div>
</div></section>

{hi_tax_band()}

<section class="band sand"><div class="wrap">
  <div style="max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
  <p style="margin-top:20px"><a href="../guides/port-city-vs-gift-city-vs-dubai.html">पोर्ट सिटी बनाम GIFT सिटी बनाम दुबई (अंग्रेज़ी में)</a></p>
</div></section>
""" + cta_banner("अपने बिज़नेस के लिए इंसेंटिव समझना है?", "बताइए आप क्या करते हैं। हम संभावित कैटेगरी और अगले तीन कदम बताएँगे।", "नमस्ते, मुझे पोर्ट सिटी टैक्स इंसेंटिव समझने हैं", lang="hi")
    return hi_head("पोर्ट सिटी कोलंबो टैक्स: 0% पर्सनल इनकम टैक्स, 15 साल टैक्स हॉलिडे, कैलकुलेटर | Sri Lanka for Indians",
                   "भारतीयों के लिए पोर्ट सिटी कोलंबो टैक्स: मंज़ूरी प्राप्त कंपनियों के कर्मचारियों पर 0% पर्सनल इनकम टैक्स, 8 से 15 साल कॉर्पोरेट टैक्स हॉलिडे, और भारत से तुलना का सैलरी कैलकुलेटर।",
                   "hi/port-city-tax.html", "port-city-tax.html", faq_schema(faqs)) + header(D, "hi", "port-city-tax.html") + body + footer(D, "hi")

def yatra():
    vids = pick("2SUXqcjFIgI", "cRQu04IaAUk", "CW6jTV-hTok", "QfFRvTem4zM", "Bu86Z_7VzAA", "XOWAaOTSCtM")
    faqs = [("क्या श्रीलंका का वीज़ा भारतीयों के लिए मुफ़्त है?", "25 मई 2026 से भारतीयों के लिए 30 दिन का टूरिस्ट ETA मुफ़्त है, डबल एंट्री के साथ। आवेदन यात्रा से पहले eta.gov.lk पर ऑनलाइन करें।"),
            ("क्या श्रीलंका में UPI चलता है?", "हाँ। फ़रवरी 2024 से LankaQR वाले दुकानदारों पर कई भारतीय UPI ऐप से भुगतान हो सकता है। जाने से पहले ऐप में इंटरनेशनल UPI चालू करें।"),
            ("श्रीलंका में रामायण से जुड़ी जगहें कौन सी हैं?", "सीता अम्मन मंदिर, हकगला (अशोक वाटिका), एल्ला में रावण झरना और रावण गुफा, दिवुरुम्पोला, मुन्नेश्वरम मंदिर, उस्संगोडा और रुमस्साला परंपरा से रामायण से जुड़ी मानी जाती हैं।")]
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; यात्रा</p>
  <span class="eyebrow">यात्रा और वीज़ा</span>
  <h1>गोवा जितना पास। <em>विदेश जितना ख़ास।</em></h1>
  <p class="lead">मुफ़्त वीज़ा, UPI से भुगतान, वही IST टाइम ज़ोन, और हर बड़े शहर से उड़ान। समंदर, पहाड़, चाय के बागान, तेंदुए और रामायण ट्रेल, सब एक हफ़्ते में।</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="grid c3">
    <div class="card"><span class="tag">वीज़ा</span><h3>&#8377;0 वीज़ा फ़ीस</h3><p>25 मई 2026 से भारतीयों के लिए 30 दिन का टूरिस्ट ETA मुफ़्त। आवेदन केवल eta.gov.lk पर।</p></div>
    <div class="card"><span class="tag">पैसा</span><h3>UPI चलता है</h3><p>LankaQR वाले दुकानदारों पर भारतीय UPI ऐप से भुगतान। छोटी दुकानों के लिए कुछ श्रीलंकाई रुपये रखें।</p></div>
    <div class="card"><span class="tag">समय</span><h3>कोई टाइम डिफ़रेंस नहीं</h3><p>श्रीलंका भी IST पर चलता है। चेन्नई से 80 मिनट, दिल्ली से लगभग 3.5 घंटे।</p></div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">रामायण ट्रेल</span>
  <h2>वो कहानी जो <em>हम बचपन से सुनते आए हैं।</em></h2>
  <div class="table-scroll" style="margin-top:28px"><table>
    <tr><th>स्थान</th><th>इलाका</th><th>मान्यता</th></tr>
    <tr><td>सीता अम्मन मंदिर</td><td>सीता एलिया, नुवारा एलिया के पास</td><td>जहाँ माता सीता ने प्रार्थना की थी</td></tr>
    <tr><td>हकगला बॉटनिकल गार्डन</td><td>नुवारा एलिया के पास</td><td>परंपरा से अशोक वाटिका माना जाता है</td></tr>
    <tr><td>रावण झरना और रावण गुफा</td><td>एल्ला</td><td>स्थानीय कथाओं में रावण से जुड़े</td></tr>
    <tr><td>दिवुरुम्पोला</td><td>नुवारा एलिया के पास</td><td>माता सीता की अग्नि परीक्षा का स्थान</td></tr>
    <tr><td>मुन्नेश्वरम मंदिर</td><td>चिलॉ, पश्चिमी तट</td><td>प्राचीन शिव मंदिर, श्रीराम की पूजा से जुड़ा</td></tr>
  </table></div>
  <p style="margin-top:18px"><a href="../guides/ramayana-trail.html">पूरा 7 दिन का प्लान (अंग्रेज़ी में) &rarr;</a></p>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">वीडियो</span>
  <h2>जो भारतीय <em>पहले जा चुके हैं।</em></h2>
  <div style="margin-top:36px">{yt_grid(vids)}</div>
</div></section>

<section class="band sand"><div class="wrap">
  <div style="max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
</div></section>
""" + cta_banner("ट्रिप हम प्लान करें?", "तारीख़, लोगों की संख्या और बजट भेजिए। उसी दिन असली कीमतों के साथ प्लान।", "नमस्ते, मेरी श्रीलंका ट्रिप प्लान करनी है", lang="hi")
    schema = faq_schema(faqs) + "\n" + video_schema(vids)
    return hi_head("श्रीलंका यात्रा गाइड: मुफ़्त वीज़ा, UPI, रामायण ट्रेल और खर्च | Sri Lanka for Indians",
                   "भारतीयों के लिए श्रीलंका यात्रा: 25 मई 2026 से मुफ़्त 30 दिन का ETA, UPI से भुगतान, रामायण ट्रेल की जगहें, और भारतीय क्रिएटर्स के वीडियो।",
                   "hi/yatra.html", "travel.html", schema) + header(D, "hi", "travel.html") + body + footer(D, "hi")

def build(write):
    write("hi/index.html", index())
    write("hi/shaadi.html", shaadi())
    write("hi/property.html", property_page())
    write("hi/port-city-tax.html", tax())
    write("hi/yatra.html", yatra())
