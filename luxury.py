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
  <p class="lead">Suites over the Indian Ocean, a USD 1.2 billion integrated resort, marina sunsets at Port City and tables at the city's best rooms. All of it 80 minutes from Chennai, on Indian time, with a free visa. Tell us the weekend you want and we line it up.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#plan">Plan a VIP weekend</a></div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">The new address</span>
  <h2>South Asia's first <em>integrated resort.</em></h2>
  <p class="lead">City of Dreams Sri Lanka, built by Macau's Melco and John Keells, opened in Colombo in August 2025: around 800 rooms, a luxury mall, conference halls and a casino on the beachfront. It changed what a Colombo weekend can be.</p>
  {RESPONSIBLE}
</div></section>

<section class="band sand" id="plan"><div class="wrap">
  <span class="eyebrow">VIP weekend concierge</span>
  <h2>Tell us the weekend. <em>We handle the rest.</em></h2>
  <p class="lead" style="margin-bottom:28px">Flights, suites, transfers, tables, a boat, a show. One message, one person on the island who answers it.</p>
  {vip_form()}
</div></section>
""" + cta_banner("Rather just talk?", "Message us on WhatsApp with the dates and the mood. We reply the same day.", "Hi, I want to plan a luxury weekend in Colombo")
    schema = crumb_schema([("Luxury", "luxury/index.html")])
    return head("Colombo Luxury Weekends and Nightlife for Indians",
                "Plan a luxury weekend in Colombo from India: City of Dreams suites, Port City marina, fine dining and nightlife, 80 minutes from Chennai. Send your plan on WhatsApp.",
                "luxury/index.html", D, schema) + header(D) + body + footer(D)

PAGES = [("index", hub)]

def build(write):
    for slug, fn in PAGES:
        write(f"luxury/{slug}.html", fn())
