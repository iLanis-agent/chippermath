# Chipper Math

Wood chipper honesty. The reduction ratio claims sixteen-to-one and the
pile was always going to take the weekend. Chipper Math turns the pile
and the clock into the afternoon.

Live: https://ilanis-agent.github.io/chippermath/

## The two truths

1. **The pile truth** - pile cubic feet / the honest 10:1 reduction norm
   (labeled) is the chips; / your bag size is the bags: a single bag at
   the curb, a working row of paper bags, or a mulch bed's worth.
2. **The weekend truth** - branches x honest minutes each (labeled norms
   by thickness) against your free minutes: done before the charcoal is
   ready, spills past lunch, or a two-weekend pile.

## The boundary

Chipper Math gives no feeding or capacity verdicts. What a chipper can
safely take is the manufacturer's call - follow the manual's capacity
and safety instructions, and never force a branch the machine wasn't
built for.

Illustrative arithmetic with labeled norms - not a measurement of your
chipper, your branches or your weekend.

## Files

- `index.html` - landing page
- `app.html` - the two-truth app
- `engine.js` - pure functions (`pilePlan`, `weekendPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
