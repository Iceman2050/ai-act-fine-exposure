"""Tests for ai_act_fine_exposure."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_act_fine_exposure import compute_fine, TIERS  # noqa: E402

PASS, FAIL = [], []


def check(name, fn):
    try:
        fn()
        PASS.append(name)
        print("PASS  " + name)
    except Exception as e:  # noqa: BLE001
        FAIL.append((name, repr(e)))
        print("FAIL  %s: %r" % (name, e))


def t_prohibited_uses_higher_of():
    r = compute_fine(1_000_000_000, "prohibited")  # 7% = 70M > 35M cap
    assert r["worst_case_eur"] == 70_000_000.0, r


def t_small_revenue_uses_fixed_cap():
    r = compute_fine(1_000_000, "prohibited")  # 7% = 70k < 35M
    assert r["worst_case_eur"] == 35_000_000.0, r


def t_sme_lower_of_rule():
    r = compute_fine(1_000_000_000, "prohibited", is_sme=True)
    assert r["worst_case_eur"] == 35_000_000.0, r  # min(35M, 70M)
    assert "SME" in r["basis"]


def t_sme_tiny_revenue():
    r = compute_fine(100_000, "transparency", is_sme=True)  # 1.5% = 1500
    assert r["worst_case_eur"] == 1500.0, r


def t_high_risk_tier():
    r = compute_fine(500_000_000, "high-risk")  # 3% = 15M = cap
    assert r["worst_case_eur"] == 15_000_000.0, r


def t_per_day_accumulates():
    r = compute_fine(1_000_000, "prohibited", days_noncompliant=10)
    assert r["accumulated_per_day_eur"] == round(r["per_day_estimate_eur"] * 10, 2)
    assert r["days_noncompliant"] == 10


def t_zero_days_zero_accumulated():
    r = compute_fine(1_000_000, "prohibited")
    assert r["accumulated_per_day_eur"] == 0.0


def t_unknown_tier_errors():
    try:
        compute_fine(1_000_000, "bogus")
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def t_negative_revenue_errors():
    try:
        compute_fine(-5, "prohibited")
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def t_disclaimer_present():
    r = compute_fine(1_000_000, "prohibited")
    assert "Not legal advice" in r["disclaimer"]


def test_all_checks():
    for name, fn in sorted(
            [(k, v) for k, v in globals().items() if k.startswith("t_")]):
        check(name, fn)
    print("\n%d passed, %d failed" % (len(PASS), len(FAIL)))
    assert not FAIL


if __name__ == "__main__":
    test_all_checks()
