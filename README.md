# ai-act-fine-exposure

**The EU AI Act's fine math is now in a draft regulation. Here's what it says you'd owe.**

On 2026-10-12, the European Commission published draft implementing regulation **Ares(2026)9589403** setting AI Act investigation and fine procedures — public consultation closes **Nov 9, 2026** (NeoTeo). Days earlier, the AI Office sent its first RFIs to frontier providers; wrong answers can cost up to €15M / 3% (Unite.AI).

`ai-act-fine-exposure` encodes the draft's fine math deterministically:
- **Three tiers** — prohibited practices (€35M / 7%), high-risk & systemic-risk obligations (€15M / 3%), transparency obligations (€7.5M / 1.5%)
- **SME "lower-of" rule** — the draft's reduced exposure for SMEs/startups
- **Per-day periodic penalties** — continuing-infringement estimates

Fixed disclaimer on every output: **not legal advice** — the draft is under consultation and may change.

## What it does NOT do
It's an exposure model, not a compliance tool and not counsel. It can't assess whether your system actually violates anything.

## Usage
```
python -m ai_act_fine_exposure 50000000 high-risk --sme --days 30
```

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

