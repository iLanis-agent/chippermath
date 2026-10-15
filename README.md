# Chipper Math

Wood chipper honesty. The hopper claims three inches, the reduction ratio
claims sixteen-to-one, and the pile was always going to take the weekend.
Chipper Math turns the claim, the pile and the clock into the afternoon.

Live: https://ilanis-agent.github.io/chippermath/

## The three truths

1. **The capacity truth** - the claimed inches x the 0.7 self-feed norm
   (labeled) is the branch that feeds without persuasion; your branch
   against the honest number: self-feeds and asks for more, feeds with
   persuasion, or is a job for the saw, not the hopper.
2. **The pile truth** - pile cubic feet / the honest 10:1 reduction norm
   (labeled) is the chips; / your bag size is the bags: a single bag at
   the curb, a working row of paper bags, or a mulch bed's worth.
3. **The weekend truth** - branches x honest minutes each (labeled norms
   by thickness) against your free minutes: done before the charcoal is
   ready, spills past lunch, or a two-weekend pile.

Illustrative arithmetic with labeled norms - not a measurement of your
chipper, your branches or your weekend. Follow the manual's capacity and
safety instructions.

## Files

- `index.html` - landing page
- `app.html` - the three-truth app
- `engine.js` - pure functions (`capacityPlan`, `pilePlan`, `weekendPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
