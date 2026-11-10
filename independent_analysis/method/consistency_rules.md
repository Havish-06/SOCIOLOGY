# Consistency rules applied across all 24 final codings

The checkers settled each case separately and flagged three places where the codebook gives no rule, so cases had
been coded differently. These rules were then applied to all 24 Final coding blocks (2026-11-10). The team can change
them; `normalise.py` records exactly which values each rule changed.

## 1. Stigma ladder: where legal action sits

Codebook ladder (Link & Phelan 2001): 1 labelling and stereotyping → 2 separation (boycott calls) → 3 status loss
(cancelled shows, lost venues) → 4 discrimination (bans, arrests, violence).

Added rule:
- A **registered FIR, a court-ordered appearance or a statutory commission's summons** makes the comedian a formal
  accused: at least **step 3**.
- **Arrest, custody, a ban, assault, or vandalism of the venue**: **step 4**.
- A police complaint that is not registered, or a private legal notice: does not by itself raise the step.

## 2. Audience size tier

Subscribers of the comedian's main YouTube channel at the time of the controversy (other fame noted separately):
small < 100K · medium 100K–1M · large 1M–10M · very_large > 10M. "mid" is written as `medium`.
Tiers are approximate where the count at the time could not be checked; the case file says so.

## 3. Election period

`yes` only if the controversy began within **6 months before** a state assembly election in the state where the
action took place, or a Lok Sabha election. All 24 codings already matched this rule; no value changed.

## Changes made

| Case | Field | Before | After | Rule |
|---|---|---|---|---|
| agrima_2020 | highest_stigma_step | 3 | 4 | venue vandalised by MNS activists |
| bharti_2022 | highest_stigma_step | 1 (provisional) | 3 | two registered FIRs (Adampur, Amritsar) |
| virli_2026 | highest_stigma_step | 1 | 3 | NCW notice, summons and hearing |
| kamra_2018, munawar_2021, virdas_2021, virli_2026 | audience_size_tier | mid | medium | spelling |
