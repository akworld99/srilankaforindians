"""Hindi pages (hi-IN) with hreflang pairs to the English versions."""
from sitekit import *
from media import pick, BY_ID, reels

D = 1  # all Hindi pages live in /hi/

def hi_head(title, desc, path, en_path, schema=""):
    return head(title, desc, path, D, schema, lang="hi", alt={"en": en_path, "hi": path})

def hi_tax_band():
    bars = [("भारत", 25.17, ""), ("सिंगापुर", 17, ""), ("दुबई", 9, ""), ("पोर्ट सिटी कोलंबो", 7.5, "hl")]
    bar_html = "".join(f'<div class="bar {c}"><span>{n}</span><span class="track"><span class="fill" style="width:{v/30*100:.0f}%"></span></span><span class="pct">{v}%</span></div>' for n, v, c in bars)
    return f"""<section class="tax-mega"><div class="wrap">
  <div class="tm-left">
    <div class="zero wide" aria-label="7.5 प्रतिशत">7.5%</div>
    <div class="zero-label">कॉर्पोरेट टैक्स &middot; पोर्ट सिटी कोलंबो</div>
    <ul class="tm-ladder">
      <li><b>7.5%</b><span>4 साल तक, मंज़ूर सेकेंडरी बिज़नेस</span></li>
      <li><b>0%</b><span>8 से 15 साल तक, बड़े प्राइमरी प्रोजेक्ट</span></li>
      <li><b>100%</b><span>विदेशी स्वामित्व, विदेशी मुद्रा में काम</span></li>
    </ul>
  </div>
  <div>
    <span class="eyebrow">वो आंकड़ा जो CFO दोबारा पढ़ते हैं</span>
    <h2>भारत के कॉर्पोरेट टैक्स का एक तिहाई से भी कम। <em>चेन्नई से 80 मिनट।</em></h2>
    <p>पोर्ट सिटी के मंज़ूर बिज़नेस पहले 4 साल 7.5% कॉर्पोरेट टैक्स दे सकते हैं, जबकि भारत की हेडलाइन दर 25.17% है। सबसे बड़े प्रोजेक्ट्स (प्राइमरी BSI) पर निवेश के हिसाब से 8 से 15 साल तक कोई कॉर्पोरेट टैक्स नहीं। साथ में 100% विदेशी स्वामित्व और विदेशी मुद्रा में काम।</p>
    <div class="bars">{bar_html}</div>
    <p class="small">कॉर्पोरेट टैक्स की हेडलाइन दरें। पोर्ट सिटी के इंसेंटिव Regulation 01 of 2025 और Amendment Act No. 1 of 2026 के तहत, मंज़ूरी पर निर्भर। 20 जनवरी 2026 से नई मंज़ूर कंपनियों के कर्मचारियों पर सामान्य इनकम टैक्स लगता है।</p>
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
        ("क्या भारतीय श्रीलंका में प्रॉपर्टी खरीद सकते हैं?", "विदेशी नागरिक सीधे फ्रीहोल्ड ज़मीन नहीं खरीद सकते, लेकिन किसी भी फ्लोर पर कॉन्डोमिनियम फ्लैट पूरी तरह अपने नाम खरीद सकते हैं, अगर पूरा भुगतान विदेश से आए पैसे से हो। USD 1,00,000 के निवेश पर 5 साल और USD 2,00,000 पर 10 साल का इन्वेस्टर वीज़ा मिल सकता है।"),
        ("क्या भारतीय बिज़नेस श्रीलंका के साथ रुपये में व्यापार कर सकते हैं?", "हाँ। भारत और श्रीलंका के बीच व्यापार का बिल, भुगतान और सेटलमेंट भारतीय रुपये में हो सकता है। यह स्पेशल रुपी वोस्ट्रो अकाउंट से चलता है जो श्रीलंकाई बैंक भारतीय बैंकों के पास रखते हैं। अक्टूबर 2025 से भारतीय बैंक श्रीलंका के बिज़नेस को व्यापार के लिए रुपये में कर्ज़ भी दे सकते हैं।"),
        ("पोर्ट सिटी कोलंबो में टैक्स कितना है?", "Regulation 01 of 2025 के तहत प्राइमरी BSI को निवेश के हिसाब से 8 से 15 साल का कॉर्पोरेट टैक्स हॉलिडे और सेकेंडरी BSI को 4 साल तक 7.5% की दर मिल सकती है, मंज़ूरी पर निर्भर। 20 जनवरी 2026 से नई मंज़ूर कंपनियों के कर्मचारियों पर सामान्य इनकम टैक्स लगता है; पहले से मंज़ूर कंपनियों को यह छूट 31 जनवरी 2029 तक मिलती है।"),
    ]
    schema = faq_schema(faqs) + "\n" + video_schema(vids)
    body = f"""
<section class="hero has-video">
  <div class="hero-video" aria-hidden="true" style="background-image:url('https://i.ytimg.com/vi/{HERO_ID}/maxres2.jpg')">
    <iframe src="https://www.youtube-nocookie.com/embed/{HERO_ID}?autoplay=1&mute=1&loop=1&playlist={HERO_ID}&controls=0&rel=0&playsinline=1&modestbranding=1&cc_load_policy=0&iv_load_policy=3&disablekb=1&fs=0&start=120" title="" tabindex="-1" allow="autoplay; encrypted-media" loading="lazy"></iframe>
  </div>
  <div class="hero-veil"></div>
  <div class="wrap"><div class="hero-inner">
    <span class="eyebrow">नमस्ते &middot; आयुबोवन &middot; वणक्कम</span>
    <h1>हिंद महासागर ने एक द्वीप <em>आपके लिए रखा है।</em></h1>
    <p class="lead">चेन्नई से सिर्फ़ 80 मिनट की उड़ान। समंदर किनारे शादियाँ, डॉलर में कीमत वाले सी फेसिंग घर, एक ऐसा फाइनेंशियल डिस्ट्रिक्ट जहाँ मंज़ूर बिज़नेस 7.5% कॉर्पोरेट टैक्स देते हैं, और रुपये में व्यापार। 2026 के पहले नौ महीनों में 4.3 लाख से ज़्यादा भारतीय श्रीलंका पहुँचे। हम आपके गाइड हैं, शुरू से आख़िर तक।</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="{wa_link('नमस्ते, मैं श्रीलंका के बारे में जानना चाहता/चाहती हूँ')}" rel="noopener">WhatsApp पर बात करें</a>
      <a class="btn btn-ghost" href="shaadi.html">शादी का बजट देखें</a>
    </div>
    <div class="hero-badges">
      <a class="hero-badge" href="port-city-tax.html"><span class="hb-num">7.5%</span><span class="hb-txt"><b>पोर्ट सिटी कोलंबो</b>मंज़ूर बिज़नेस के लिए कॉर्पोरेट टैक्स। देखें क्या आप योग्य हैं &rarr;</span></a>
      <a class="hero-badge" href="#inr"><span class="hb-num">&#8377;</span><span class="hb-txt"><b>रुपये में व्यापार</b>श्रीलंका के साथ सौदे का बिल और भुगतान INR में &rarr;</span></a>
    </div>
  </div></div>
</section>

{hi_tax_band()}

{inr_band(D, "hi")}

<section class="band"><div class="wrap">
  <span class="eyebrow">हम किसमें मदद करते हैं</span>
  <h2>एक द्वीप। <em>कई मौके।</em></h2>
  <div class="grid c3" style="margin-top:40px">
    <a class="card link-card" href="shaadi.html"><span class="tag">शादी</span><h3>समंदर किनारे डेस्टिनेशन वेडिंग</h3><p>गोवा और उदयपुर से तुलना करें। बारात के लिए वीज़ा मुफ़्त।</p><span class="go">शादी प्लान करें &rarr;</span></a>
    <a class="card link-card" href="property.html"><span class="tag">प्रॉपर्टी</span><h3>डॉलर में कीमत, समंदर का नज़ारा</h3><p>भारतीय क्या खरीद सकते हैं, और 5 साल के वीज़ा का रास्ता।</p><span class="go">नियम पढ़ें &rarr;</span></a>
    <a class="card link-card" href="port-city-tax.html"><span class="tag">7.5% टैक्स</span><h3>पोर्ट सिटी कोलंबो</h3><p>मंज़ूर बिज़नेस के लिए 7.5% कॉर्पोरेट टैक्स, बड़े प्रोजेक्ट्स पर 15 साल तक 0%, और 100% विदेशी स्वामित्व।</p><span class="go">आंकड़े देखें &rarr;</span></a>
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
    return hi_head("श्रीलंका फॉर इंडियंस: शादी, प्रॉपर्टी, 7.5% टैक्स और यात्रा",
                   "भारतीयों के लिए श्रीलंका गाइड: डेस्टिनेशन वेडिंग, प्रॉपर्टी, पोर्ट सिटी कोलंबो में 15 साल तक कॉर्पोरेट टैक्स हॉलिडे, मुफ़्त वीज़ा और यात्रा। WhatsApp पर गाइड से बात करें।",
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
    faqs = [("क्या भारतीय श्रीलंका में फ्लैट खरीद सकते हैं?", "हाँ। विदेशी नागरिक किसी भी फ्लोर पर कॉन्डोमिनियम फ्लैट पूरी तरह अपने नाम खरीद सकते हैं, अगर पूरा भुगतान डीड से पहले विदेश से आए पैसे (Inward Investment Account) से हो। फ्रीहोल्ड ज़मीन पर रोक है; ज़मीन 99 साल तक की लीज़ पर ली जा सकती है।"),
            ("क्या भारतीय श्रीलंका में ज़मीन खरीद सकते हैं?", "फ्रीहोल्ड नहीं। 2014 के कानून (Land Restrictions on Alienation Act No. 38) के तहत विदेशियों को फ्रीहोल्ड ज़मीन ट्रांसफ़र नहीं हो सकती। ज़मीन 99 साल तक की लीज़ पर लेकर उस पर घर बनाया जा सकता है।"),
            ("क्या प्रॉपर्टी खरीदने से रेज़िडेंस वीज़ा मिलता है?", "हाँ। USD 1,00,000 के योग्य निवेश पर, जिसमें कॉन्डो खरीदना शामिल है, 5 साल का इन्वेस्टर वीज़ा मिल सकता है। USD 2,00,000 पर 10 साल।"),
            ("भारत से कितना पैसा भेज सकते हैं?", "RBI की LRS योजना के तहत हर व्यक्ति साल में USD 2,50,000 तक विदेश में प्रॉपर्टी के लिए भेज सकता है, और परिवार के सदस्य अपनी सीमा जोड़ सकते हैं। साल में 10 लाख रुपये से ऊपर की रकम पर बैंक 20% TCS काटता है, जिसे आप इनकम टैक्स में वापस क्लेम करते हैं।"),
            ("खरीदने पर कौन से टैक्स लगते हैं?", "स्टाम्प ड्यूटी पहले LKR 1,00,000 पर 3% और बाकी पर 4%, VAT रजिस्टर्ड डेवलपर से नए कॉन्डो पर 18% VAT, और लगभग 1% से 3% कानूनी फ़ीस।")]
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; प्रॉपर्टी</p>
  <span class="eyebrow">प्रॉपर्टी</span>
  <h1>भारत से एक घंटे दूर, <em>समंदर के सामने घर।</em></h1>
  <p class="lead">हाँ, भारतीय यहाँ खरीद सकते हैं। किसी भी फ्लोर पर कॉन्डोमिनियम फ्लैट पूरी तरह अपने नाम, ज़मीन 99 साल तक की लीज़ पर, और पोर्ट सिटी में नए अपार्टमेंट। फ्रीहोल्ड ज़मीन नहीं। USD 1,00,000 के निवेश पर 5 साल का इन्वेस्टर वीज़ा।</p>
  <div class="cta-row"><a class="btn btn-primary" href="{wa_link('नमस्ते, मैं श्रीलंका में प्रॉपर्टी खरीदना चाहता/चाहती हूँ')}" rel="noopener">शॉर्टलिस्ट मंगवाएँ</a></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="grid c2">
    <div class="card"><span class="tag">कर सकते हैं</span><h3>भारतीय क्या खरीद सकते हैं</h3><ul style="padding-left:18px">
      <li>किसी भी फ्लोर पर कॉन्डोमिनियम फ्लैट, पूरा भुगतान डीड से पहले विदेश से आए पैसे से</li>
      <li>ज़मीन लीज़ पर, 99 साल तक (2017 से लीज़ टैक्स ख़त्म)</li>
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
    schema = crumb_schema([("प्रॉपर्टी", "hi/property.html")]) + "\n" + faq_schema(faqs) + "\n" + video_schema(vids)
    return hi_head("क्या भारतीय श्रीलंका में प्रॉपर्टी खरीद सकते हैं? 2026 नियम | Sri Lanka for Indians",
                   "हाँ, भारतीय किसी भी फ्लोर पर फ्लैट खरीद सकते हैं और 99 साल की लीज़ पर ज़मीन ले सकते हैं, फ्रीहोल्ड ज़मीन नहीं। 2026 के नियम, खर्च, LRS, TCS और इन्वेस्टर वीज़ा।",
                   "hi/property.html", "real-estate.html", schema) + header(D, "hi", "real-estate.html") + body + footer(D, "hi")

def tax():
    faqs = [("पोर्ट सिटी कोलंबो में 2026 में टैक्स कितना है?", "Regulation 01 of 2025 के तहत प्राइमरी BSI को निवेश के हिसाब से 8 से 15 साल का कॉर्पोरेट टैक्स हॉलिडे और सेकेंडरी BSI को 4 साल तक 7.5% की दर मिल सकती है। बाकी पोर्ट सिटी कंपनियों पर सामान्य श्रीलंकाई टैक्स लगता है।"),
            ("क्या पोर्ट सिटी में अब भी 0% पर्सनल इनकम टैक्स है?", "नई कंपनियों के लिए नहीं। Colombo Port City Economic Commission (Amendment) Act No. 1 of 2026 (20 जनवरी 2026) के बाद, उस तारीख़ या उसके बाद मंज़ूर कंपनियों के कर्मचारियों की सैलरी पर पहले दिन से टैक्स लगता है। पहले से मंज़ूर कंपनियों को यह छूट 31 जनवरी 2029 तक मिलती है।"),
            ("15 साल के टैक्स हॉलिडे के लिए कितना निवेश चाहिए?", "सबसे लंबा हॉलिडे सबसे बड़े प्रोजेक्ट्स के लिए है। मार्च 2026 की रिपोर्ट के अनुसार पूरे 15 साल USD 1 अरब या उससे अधिक के निवेश पर मिलते हैं, छोटे टियर को कम साल। छोटे बिज़नेस के लिए 4 साल तक 7.5% वाला सेकेंडरी रास्ता है।")]
    body = f"""
<section class="hero"><div class="wrap">
  <p class="crumbs"><a href="index.html">होम</a> &rsaquo; पोर्ट सिटी टैक्स</p>
  <span class="eyebrow">पोर्ट सिटी कोलंबो &middot; 2026 के नियम</span>
  <h1>7.5% कॉर्पोरेट टैक्स। <em>सबसे बड़े प्रोजेक्ट्स पर शून्य।</em></h1>
  <p class="lead">पोर्ट सिटी कोलंबो एक स्पेशल इकोनॉमिक ज़ोन है जिसके अपने टैक्स नियम हैं। मंज़ूर बिज़नेस पहले 4 साल 7.5% कॉर्पोरेट टैक्स दे सकते हैं, भारत के 25.17% के एक तिहाई से भी कम। सबसे बड़े प्रोजेक्ट्स (प्राइमरी BSI) पर निवेश के हिसाब से 8 से 15 साल तक कोई कॉर्पोरेट टैक्स नहीं।</p>
  <div class="facts">
    <div class="fact"><b>7.5%</b><span>मंज़ूर सेकेंडरी BSI के लिए पहले 4 साल कॉर्पोरेट टैक्स</span></div>
    <div class="fact"><b>0%</b><span>प्राइमरी BSI पर हॉलिडे के दौरान कॉर्पोरेट टैक्स</span></div>
    <div class="fact"><b>8 से 15 साल</b><span>हॉलिडे की अवधि, निवेश के आकार पर निर्भर</span></div>
  </div>
  <p class="source">Regulation 01 of 2025 और Colombo Port City Economic Commission (Amendment) Act No. 1 of 2026 (20 जनवरी 2026)।</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="cta-banner" style="background:var(--card); color:var(--ink); border-color:var(--gold)">
    <div style="max-width:72ch">
      <span class="eyebrow">जनवरी 2026 में क्या बदला</span>
      <h2 style="color:var(--ink)">नई कंपनियों के कर्मचारियों की <em>टैक्स छूट ख़त्म।</em></h2>
      <p style="color:var(--ink-soft)">2026 से पहले पोर्ट सिटी की मंज़ूर कंपनियों के कर्मचारियों पर पर्सनल इनकम टैक्स नहीं लगता था। Amendment Act No. 1 of 2026 ने 20 जनवरी 2026 या उसके बाद मंज़ूर कंपनियों के लिए यह छूट ख़त्म कर दी। पहले से मंज़ूर कंपनियों को 1 फ़रवरी 2026 से 31 जनवरी 2029 तक तीन साल की छूट मिलती है। रणनीतिक निवेश पर कॉर्पोरेट टैक्स हॉलिडे जारी हैं, अब परफ़ॉर्मेंस मॉनिटरिंग के साथ।</p>
    </div>
  </div>
</div></section>

<section class="band sand"><div class="wrap">
  <span class="eyebrow">हॉलिडे की कीमत कितनी?</span>
  <h2>आपका मुनाफ़ा: <em>भारत बनाम पोर्ट सिटी।</em></h2>
  <div class="taxcalc" style="margin-top:34px">
    <div class="calc-grid">
      <div class="field"><label for="cc-profit">सालाना मुनाफ़ा</label><span class="tc-val num" id="cc-profit-out">&#8377;25 Cr</span>
        <input type="range" id="cc-profit" min="1" max="500" step="1" value="25" aria-label="सालाना मुनाफ़ा, करोड़ रुपये में"></div>
      <div class="field"><label for="cc-route">पोर्ट सिटी कैटेगरी</label>
        <select id="cc-route">
          <option value="p15">प्राइमरी BSI, 15 साल (सबसे बड़े प्रोजेक्ट)</option>
          <option value="p12">प्राइमरी BSI, 12 साल</option>
          <option value="p10">प्राइमरी BSI, 10 साल</option>
          <option value="p8">प्राइमरी BSI, 8 साल</option>
          <option value="s4" selected>सेकेंडरी BSI, 4 साल तक 7.5%</option>
        </select></div>
    </div>
    <div class="tc-row">
      <div class="tc-cell"><span>भारत में <span id="cc-years">4</span> साल का कॉर्पोरेट टैक्स</span><b class="num" id="cc-india">&#8377;0</b><span>25.17% हेडलाइन दर पर</span></div>
      <div class="tc-cell"><span>पोर्ट सिटी में कॉर्पोरेट टैक्स</span><b class="num" id="cc-pc">&#8377;0</b><span id="cc-pc-note">हॉलिडे के दौरान</span></div>
      <div class="tc-cell gold"><span>इस अवधि में टैक्स की बचत</span><b class="num" id="cc-save">&#8377;0</b><span>भारत में डिविडेंड टैक्स से पहले</span></div>
    </div>
    <p class="small" style="margin-top:18px">केवल उदाहरण के लिए। हॉलिडे प्रोजेक्ट लागू होने के बाद शुरू होता है और BSI घोषित होने पर निर्भर है। भारत में शेयरधारकों को मिलने वाले डिविडेंड पर भारत में टैक्स लगता है। अगर विदेशी कंपनी का रोज़ का प्रबंधन भारत से होता है (POEM नियम), तो उसे भारतीय कंपनी माना जा सकता है। अपने CA से बात करें।</p>
  </div>
</div></section>

{hi_tax_band()}

<section class="band"><div class="wrap">
  <div style="max-width:880px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
  <p style="margin-top:20px"><a href="../guides/port-city-vs-gift-city-vs-dubai.html">पोर्ट सिटी बनाम GIFT सिटी बनाम दुबई (अंग्रेज़ी में)</a></p>
</div></section>
""" + cta_banner("जानना है आप किस कैटेगरी में आएँगे?", "बताइए आप क्या करते हैं और कितना निवेश करना चाहते हैं। हम संभावित रास्ता और अगले तीन कदम बताएँगे।", "नमस्ते, मुझे पोर्ट सिटी टैक्स इंसेंटिव समझने हैं", lang="hi")
    return hi_head("पोर्ट सिटी कोलंबो टैक्स 2026: 7.5% कॉर्पोरेट टैक्स | Sri Lanka for Indians",
                   "पोर्ट सिटी कोलंबो टैक्स 2026: रणनीतिक निवेश पर 8 से 15 साल कॉर्पोरेट टैक्स हॉलिडे, छोटे बिज़नेस के लिए 7.5%, और नई कंपनियों के कर्मचारियों की टैक्स छूट ख़त्म। मुनाफ़ा कैलकुलेटर के साथ।",
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
  <p class="lead" style="margin-top:-6px">कीमतें श्रीलंकाई रुपये में होती हैं: 3.5 से भाग दें। <a href="shrilanka-rupaya-inr.html" style="color:var(--gold-bright)">लाइव करेंसी कन्वर्टर</a> देखें।</p>
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
