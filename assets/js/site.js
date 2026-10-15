/* Lite YouTube: thumbnails load instantly, the player loads only when tapped. */
(function () {
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest("button.yt");
    if (!btn || btn.dataset.loaded) return;
    var id = btn.getAttribute("data-id");
    var f = document.createElement("iframe");
    f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&modestbranding=1&playsinline=1";
    f.title = btn.getAttribute("aria-label") || "YouTube video";
    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
    f.allowFullscreen = true;
    btn.innerHTML = "";
    btn.appendChild(f);
    btn.dataset.loaded = "1";
  });

  /* Personal tax calculator (Port City page). India new regime FY 2025-26, salaried. */
  var range = document.getElementById("tc-salary");
  if (!range) return;
  function indiaTax(gross) {
    var t = Math.max(0, gross - 75000);                 // standard deduction
    var slabs = [[400000,0],[800000,.05],[1200000,.10],[1600000,.15],[2000000,.20],[2400000,.25],[Infinity,.30]];
    var tax = 0, prev = 0;
    for (var i = 0; i < slabs.length; i++) {
      var cap = slabs[i][0], r = slabs[i][1];
      if (t > prev) tax += (Math.min(t, cap) - prev) * r;
      prev = cap;
    }
    if (t <= 1200000) tax = 0;                          // section 87A rebate
    else tax = Math.min(tax, t - 1200000 + 0);          // marginal relief near 12L
    var sc = t > 20000000 ? .25 : t > 10000000 ? .15 : t > 5000000 ? .10 : 0;
    tax = tax * (1 + sc);
    return tax * 1.04;                                  // health and education cess
  }
  function inr(n) {
    if (n >= 10000000) return "₹" + (n / 10000000).toFixed(2) + " Cr";
    if (n >= 100000) return "₹" + (n / 100000).toFixed(2) + " L";
    return "₹" + Math.round(n).toLocaleString("en-IN");
  }
  function run() {
    var lakh = parseFloat(range.value);
    var gross = lakh * 100000;
    var tax = indiaTax(gross);
    document.getElementById("tc-out-salary").textContent = inr(gross);
    document.getElementById("tc-india").textContent = inr(tax);
    document.getElementById("tc-rate").textContent = gross ? (tax / gross * 100).toFixed(1) + "% effective" : "";
    document.getElementById("tc-keep").textContent = inr(tax);
    var yrs = document.getElementById("tc-5yr");
    if (yrs) yrs.textContent = inr(tax * 5);
  }
  range.addEventListener("input", run);
  run();
})();

/* GA4 events: WhatsApp leads, email clicks, video plays, calculator use, outbound links */
(function () {
  function ev(name, params) { if (typeof gtag === "function") gtag("event", name, params || {}); }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a");
    var y = e.target.closest && e.target.closest("button.yt");
    if (y && !y.dataset.tracked) { y.dataset.tracked = "1"; ev("video_play", { video_id: y.getAttribute("data-id"), video_title: y.getAttribute("aria-label") }); }
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var where = a.classList.contains("wa-float") ? "float" : a.closest(".site-head") ? "header" : a.closest(".hero") ? "hero" : a.closest(".cta-banner") ? "cta_banner" : a.closest(".savings") ? "wedding_calculator" : "body";
    if (href.indexOf("wa.me/") > -1) {
      ev("generate_lead", { method: "whatsapp", placement: where, page_path: location.pathname });
      ev("whatsapp_click", { placement: where, page_path: location.pathname });
    } else if (href.indexOf("mailto:") === 0) {
      ev("generate_lead", { method: "email", placement: where, page_path: location.pathname });
    } else if (/^https?:/.test(href) && href.indexOf(location.hostname) === -1) {
      ev("click_outbound", { link_url: href });
    }
  });
  var once = {};
  ["guests", "days", "tier", "origin", "tc-salary"].forEach(function (id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.addEventListener("change", function () {
      var name = id === "tc-salary" ? "tax_calculator_used" : "wedding_calculator_used";
      if (once[name]) return; once[name] = 1;
      ev(name, { page_path: location.pathname });
    });
  });
})();
