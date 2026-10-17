# ai-act-fine-exposure

**The EU AI Act's draft fine regulation puts real numbers on violations — up to €35M or 7% of turnover.**

On 2026-10-12 the European Commission published draft implementing regulation **Ares(2026)9589403** (consultation closes **Nov 9, 2026**). Most teams have no idea what their exposure is. This tool encodes the draft's fine math deterministically so you can see the number in 10 seconds.

## 30-second quickstart
```
python ai_act_fine_exposure.py 50000000 prohibited
```

## Example output
```
{
  "tier": "Prohibited AI practices (Art. 5)",
  "annual_revenue_eur": 50000000.0,
  "is_sme": false,
  "worst_case_eur": 35000000,
  "per_day_estimate_eur": 70000.0,
  "days_noncompliant": 0,
  "accumulated_per_day_eur": 0.0,
  "basis": "max(EUR 35,000,000 fixed cap, 7.0% of EUR 50,000,000 turnover)",
  "disclaimer": "Not legal advice. Figures encode the DRAFT implementing regulation Ares(2026)9589403 (consultation closes 2026-11-09) and AI Act Art. 99 tiers; the draft may change. Consult counsel before acting."
}
```

Add `--sme` for the draft's SME lower-of rule, `--days N` for continuing-infringement per-day estimates.

## What it does NOT do
An exposure model, not a compliance tool and not counsel. It can't assess whether your system actually violates anything — and the draft it's based on is under consultation and may change.

## Built by Ingenious AI

This tool is built and maintained by **Ingenious AI**. Get early access to our AI security platforms:

- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20DisclosureGuard
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ModelMinder
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20TermsWatch
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Vibe-Code%20Audit
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Rogue-Agent%20Defense
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20BreachHunter
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ChatBreaker
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Agent%20Flight%20Recorder
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Agent%20Auth%20Gateway
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20DomainGuard
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ContentCraft%20AI



> Built by Ingenious AI with Muse — get free tokens with invite code `2HCQH1`
