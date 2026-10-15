/* Wedding cost calculator: Indian destination wedding (Goa/Udaipur) vs Sri Lanka.
   All figures are indicative 2026 planning estimates in INR. Replace with partner rate cards as they come in. */
(function () {
  var $ = function (id) { return document.getElementById(id); };
  var guestsEl = $("guests"), daysEl = $("days"), tierEl = $("tier"), originEl = $("origin");
  if (!guestsEl) return;

  // Per guest per day: venue + catering + decor package (destination wedding, exclusive use)
  var PKG = {
    india: { silver: 5200, gold: 9000, royal: 16000 },
    sl:    { silver: 4800, gold: 7800, royal: 14000 }
  };
  // Room per night (2 guests per room)
  var ROOM = {
    india: { silver: 7000, gold: 12000, royal: 24000 },
    sl:    { silver: 5500, gold: 9000, royal: 17000 }
  };
  // Return flights per person
  var FLY_INDIA_DOMESTIC = 9000; // metro to Goa/Udaipur, return
  var FLY_SL = {
    chennai: 14000, bengaluru: 16000, mumbai: 18000, delhi: 22000,
    hyderabad: 16000, kolkata: 21000, ahmedabad: 20000, pune: 18000
  };

  function inr(n) {
    return "₹" + Math.round(n).toLocaleString("en-IN");
  }

  function calc() {
    var guests = Math.max(30, Math.min(1000, parseInt(guestsEl.value, 10) || 150));
    var days = parseInt(daysEl.value, 10) || 2;
    var nights = days + 1; // guests arrive the evening before
    var tier = tierEl.value;
    var origin = originEl.value;
    var rooms = Math.ceil(guests / 2);

    var inPkg = PKG.india[tier] * guests * days;
    var inRooms = ROOM.india[tier] * rooms * nights;
    var inFly = FLY_INDIA_DOMESTIC * guests;
    var inTotal = inPkg + inRooms + inFly;

    var slPkg = PKG.sl[tier] * guests * days;
    var slRooms = ROOM.sl[tier] * rooms * nights;
    var slFly = (FLY_SL[origin] || 16000) * guests;
    var slTotal = slPkg + slRooms + slFly;

    $("in-pkg").textContent = inr(inPkg);
    $("in-rooms").textContent = inr(inRooms);
    $("in-fly").textContent = inr(inFly);
    $("total-india").textContent = inr(inTotal);

    $("sl-pkg").textContent = inr(slPkg);
    $("sl-rooms").textContent = inr(slRooms);
    $("sl-fly").textContent = inr(slFly);
    $("total-sl").textContent = inr(slTotal);

    var diff = inTotal - slTotal;
    var resSl = $("res-sl"), resIn = $("res-india");
    var hi = (document.documentElement.lang || "").indexOf("hi") === 0;
    if (diff >= 0) {
      $("savings-line").textContent = hi ? "श्रीलंका में बचत" : "Sri Lanka could save you";
      $("savings-amt").textContent = inr(diff) + " (" + Math.round((diff / inTotal) * 100) + "%)";
      resSl.classList.add("win"); resIn.classList.remove("win");
    } else {
      $("savings-line").textContent = hi ? "इस सेटअप में भारत सस्ता है, अंतर" : "For this setup, India is cheaper by";
      $("savings-amt").textContent = inr(-diff);
      resIn.classList.add("win"); resSl.classList.remove("win");
    }
  }

  [guestsEl, daysEl, tierEl, originEl].forEach(function (el) {
    el.addEventListener("input", calc);
    el.addEventListener("change", calc);
  });
  calc();
})();
