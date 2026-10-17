"""ai-act-fine-exposure: EU AI Act draft fine-exposure calculator.

Hook (2026-10-12): the European Commission published draft implementing
regulation Ares(2026)9589403 setting AI Act investigation and fine
procedures; public consultation closes Nov 9, 2026 (NeoTeo). Context:
Oct 14 first AI Office RFIs to frontier providers; wrong answers up to
EUR 15M / 3% (Unite.AI).

Encodes the draft's per-tier fine math, the SME "lower-of" rule, and
per-day periodic penalty estimates. Deterministic arithmetic on the
draft's published figures — NOT legal advice, and the draft is subject
to change during consultation.
"""

VERSION = "1.0.0"

# Fine tiers from the AI Act (Art. 99) as encoded in the draft
# implementing regulation: (fixed_cap_eur, turnover_pct).
TIERS = {
    "prohibited": {
        "label": "Prohibited AI practices (Art. 5)",
        "fixed_cap": 35_000_000,
        "turnover_pct": 0.07,
    },
    "high-risk": {
        "label": "High-risk / GPAI systemic-risk obligations",
        "fixed_cap": 15_000_000,
        "turnover_pct": 0.03,
    },
    "transparency": {
        "label": "Transparency / information obligations",
        "fixed_cap": 7_500_000,
        "turnover_pct": 0.015,
    },
}

# Draft per-day periodic penalty estimate basis (illustrative daily
# fractions of the tier cap used for exposure modeling).
PER_DAY_FRACTION = 0.002  # 0.2% of worst-case fine per day

DISCLAIMER = ("Not legal advice. Figures encode the DRAFT implementing "
              "regulation Ares(2026)9589403 (consultation closes 2026-11-09) "
              "and AI Act Art. 99 tiers; the draft may change. Consult "
              "counsel before acting.")


def compute_fine(annual_revenue_eur, tier, is_sme=False, days_noncompliant=0):
    """Compute worst-case fine exposure.

    annual_revenue_eur: worldwide annual turnover (EUR).
    tier: "prohibited" | "high-risk" | "transparency".
    is_sme: SME/startup -> draft's lower-of rule applies.
    days_noncompliant: days of continuing infringement (per-day estimate).
    Returns dict with worst_case_eur, per_day_eur, basis, disclaimer.
    """
    tier = (tier or "").lower()
    if tier not in TIERS:
        raise ValueError("unknown tier: %r (choose from %s)"
                         % (tier, ", ".join(sorted(TIERS))))
    if annual_revenue_eur is None or float(annual_revenue_eur) < 0:
        raise ValueError("annual_revenue_eur must be a non-negative number")
    revenue = float(annual_revenue_eur)
    t = TIERS[tier]
    pct_amount = revenue * t["turnover_pct"]
    # Standard rule: the HIGHER of fixed cap and turnover percentage.
    worst = max(t["fixed_cap"], pct_amount)
    basis = ("max(EUR %s fixed cap, %.1f%% of EUR %s turnover)"
             % (_fmt(t["fixed_cap"]), t["turnover_pct"] * 100, _fmt(revenue)))
    if is_sme:
        # Draft SME rule: the LOWER of the two amounts.
        worst = min(t["fixed_cap"], pct_amount)
        basis = ("SME lower-of rule: min(EUR %s fixed cap, %.1f%% of EUR %s "
                 "turnover)" % (_fmt(t["fixed_cap"]),
                                t["turnover_pct"] * 100, _fmt(revenue)))
    per_day = worst * PER_DAY_FRACTION
    days = int(days_noncompliant or 0)
    return {
        "tier": t["label"],
        "annual_revenue_eur": revenue,
        "is_sme": bool(is_sme),
        "worst_case_eur": round(worst, 2),
        "per_day_estimate_eur": round(per_day, 2),
        "days_noncompliant": days,
        "accumulated_per_day_eur": round(per_day * days, 2) if days else 0.0,
        "basis": basis,
        "disclaimer": DISCLAIMER,
    }


def _fmt(n):
    return "{:,.0f}".format(n)


def main(argv=None):
    import argparse
    import json
    ap = argparse.ArgumentParser(
        description="EU AI Act draft fine-exposure calculator (not legal "
                    "advice).")
    ap.add_argument("revenue", type=float,
                    help="worldwide annual turnover in EUR")
    ap.add_argument("tier", choices=sorted(TIERS),
                    help="violation tier")
    ap.add_argument("--sme", action="store_true",
                    help="apply the draft SME lower-of rule")
    ap.add_argument("--days", type=int, default=0,
                    help="days of continuing infringement")
    args = ap.parse_args(argv)
    try:
        print(json.dumps(
            compute_fine(args.revenue, args.tier, args.sme, args.days),
            indent=2))
    except ValueError as e:
        print("ERROR: %s" % e)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
