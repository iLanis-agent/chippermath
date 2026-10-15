#!/usr/bin/env python3
# Chipper Math oracle - mirrors engine.js float-for-float.
# No feeding or capacity verdicts: pile and schedule arithmetic only.
import json, math
REDUCTION = 10
def r1(x): return math.floor(x*10+0.5)/10
def f1(x): return "%.1f" % r1(x)
def jsnum(x):
    i = int(x)
    return i if x == i else x

def pile_plan(pile, bag):
    if not (pile > 0): return {"error": "the pile cubic feet must be above zero"}
    if not (bag > 0): return {"error": "the bag cubic feet must be above zero"}
    chips_raw = pile / REDUCTION
    bags_raw = chips_raw / bag
    verdict = "a single bag at the curb" if bags_raw < 1.5 else ("a working row of paper bags" if bags_raw <= 6 else "a mulch bed's worth")
    return {"chips": jsnum(r1(chips_raw)), "bags": jsnum(r1(bags_raw)), "verdict": verdict}
def render_pile(r, pile, bag):
    bag_word = "1 bag" if r["bags"] == 1 else f1(r["bags"]) + " bags"
    return ("The %s-cubic-foot pile honestly chips to %s cubic feet at the 10:1 reduction norm - about %s of %s cubic feet each, %s."
            % (pile, f1(r["chips"]), bag_word, bag, r["verdict"]))

def weekend_plan(count, avg, free):
    if not (count > 0): return {"error": "the branch count must be above zero"}
    if not (avg > 0): return {"error": "the average inches must be above zero"}
    if not (free > 0): return {"error": "the free minutes must be above zero"}
    each = 0.5 if avg < 1 else (1.5 if avg < 2 else 3)
    total_raw = count * each
    verdict = "done before the charcoal is ready" if total_raw <= free else ("spills past lunch" if total_raw <= free * 1.5 else "a two-weekend pile")
    return {"each": jsnum(r1(each)), "totalMin": jsnum(r1(total_raw)), "verdict": verdict}
def render_weekend(r, count, avg, free):
    min_word = "1 minute" if r["totalMin"] == 1 else f1(r["totalMin"]) + " minutes"
    return ("%s branches at about %s honest minutes each is %s - %s."
            % (count, f1(r["each"]), min_word, r["verdict"]))

CASES = [
    ("pile", (20,2)), ("pile", (45,2)), ("pile", (150,2)),
    ("pile", (12,2)), ("pile", (80,3)), ("pile", (200,2)),
    ("weekend", (40,1.5,90)), ("weekend", (40,1.5,30)), ("weekend", (60,0.5,45)),
    ("weekend", (25,2.5,60)), ("weekend", (100,1.2,120)), ("weekend", (30,0.8,20)),
    ("pile", (0,2)), ("pile", (20,0)),
    ("weekend", (0,1.5,90)), ("weekend", (40,0,90)), ("weekend", (40,1.5,0)),
]
PLANS = {"pile": (pile_plan, render_pile), "weekend": (weekend_plan, render_weekend)}
out = []
for tool, args in CASES:
    plan, render = PLANS[tool]
    r = plan(*args)
    case = {"tool": tool, "args": list(args), "result": r}
    if "error" not in r:
        case["render"] = render(r, *args)
    out.append(case)
print(json.dumps(out, separators=(",", ":")), end="")
