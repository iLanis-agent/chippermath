// Chipper Math engine - wood chipper honesty, labeled norms, honest arithmetic.
// No feeding or capacity verdicts: what a chipper can safely take is the
// manufacturer's call. Only pile and schedule arithmetic here.
(function(root){
"use strict";
var REDUCTION = 10;  // labeled norm: honest 10:1 pile-to-chips reduction
function r1(x){ return Math.round(x*10)/10; }
function f1(x){ return r1(x).toFixed(1); }

function pilePlan(pileCuft, bagCuft){
  if (!(pileCuft > 0)) return { error: "the pile cubic feet must be above zero" };
  if (!(bagCuft > 0)) return { error: "the bag cubic feet must be above zero" };
  var chipsRaw = pileCuft / REDUCTION;
  var bagsRaw = chipsRaw / bagCuft;
  var verdict = bagsRaw < 1.5 ? "a single bag at the curb"
    : (bagsRaw <= 6 ? "a working row of paper bags" : "a mulch bed's worth");
  return { chips: r1(chipsRaw), bags: r1(bagsRaw), verdict: verdict };
}
function renderPile(r, pileCuft, bagCuft){
  var bagWord = r.bags === 1 ? "1 bag" : f1(r.bags) + " bags";
  return "The " + pileCuft + "-cubic-foot pile honestly chips to " + f1(r.chips) + " cubic feet at the 10:1 reduction norm - about " + bagWord + " of " + bagCuft + " cubic feet each, " + r.verdict + ".";
}

function weekendPlan(count, avgIn, freeMin){
  if (!(count > 0)) return { error: "the branch count must be above zero" };
  if (!(avgIn > 0)) return { error: "the average inches must be above zero" };
  if (!(freeMin > 0)) return { error: "the free minutes must be above zero" };
  var each = avgIn < 1 ? 0.5 : (avgIn < 2 ? 1.5 : 3); // labeled minutes-per-branch norms
  var totalRaw = count * each;
  var verdict = totalRaw <= freeMin ? "done before the charcoal is ready"
    : (totalRaw <= freeMin * 1.5 ? "spills past lunch" : "a two-weekend pile");
  return { each: r1(each), totalMin: r1(totalRaw), verdict: verdict };
}
function renderWeekend(r, count, avgIn, freeMin){
  var minWord = r.totalMin === 1 ? "1 minute" : f1(r.totalMin) + " minutes";
  return count + " branches at about " + f1(r.each) + " honest minutes each is " + minWord + " - " + r.verdict + ".";
}

root.ChipperMath = { pilePlan: pilePlan, renderPile: renderPile, weekendPlan: weekendPlan, renderWeekend: renderWeekend };
})(typeof window !== "undefined" ? window : globalThis);
