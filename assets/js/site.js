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

  /* Corporate tax holiday calculator (Port City page). India headline 25.17%. */
  var profit = document.getElementById("cc-profit");
  if (!profit) return;
  var route = document.getElementById("cc-route");
  var hi = (document.documentElement.lang || "").indexOf("hi") === 0;
  function crore(n) {
    if (n >= 100) return "\u20B9" + Math.round(n).toLocaleString("en-IN") + " Cr";
    return "\u20B9" + n.toFixed(n < 10 ? 2 : 1) + " Cr";
  }
  function run() {
    var p = parseFloat(profit.value);
    var r = route.value;
    var years = r === "s4" ? 4 : parseInt(r.slice(1), 10);
    var india = p * 0.2517 * years;
    var pc = r === "s4" ? p * 0.075 * years : 0;
    document.getElementById("cc-profit-out").textContent = crore(p) + (hi ? " / साल" : " a year");
    document.getElementById("cc-years").textContent = years;
    document.getElementById("cc-india").textContent = crore(india);
    document.getElementById("cc-pc").textContent = crore(pc);
    document.getElementById("cc-pc-note").textContent = r === "s4" ? (hi ? "4 साल तक 7.5%" : "At 7.5% for 4 years") : (hi ? "हॉलिडे के दौरान" : "During the holiday");
    document.getElementById("cc-save").textContent = crore(india - pc);
  }
  profit.addEventListener("input", run);
  route.addEventListener("change", run);
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
  ["guests", "days", "tier", "origin", "cc-profit", "cc-route"].forEach(function (id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.addEventListener("change", function () {
      var name = id.indexOf("cc-") === 0 ? "tax_calculator_used" : "wedding_calculator_used";
      if (once[name]) return; once[name] = 1;
      ev(name, { page_path: location.pathname });
    });
  });
})();
