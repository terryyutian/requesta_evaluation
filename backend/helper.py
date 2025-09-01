
from typing import List, Dict, Any, Optional


def normalize_demographics(raw: Dict[str, Any]) -> Dict[str, Any]:
    used: set[str] = set()
    out: Dict[str, Any] = {}

    # Prolific ID
    out["prolific_id"] = raw.get("prolific_id"); used.add("prolific_id")

    # Age
    def _maybe_int(x):
        try:
            s = str(x).strip()
            return int(s) if s != "" else None
        except Exception:
            return None
    out["age"] = _maybe_int(raw.get("q1_age")); used.add("q1_age")

    # Gender
    out["gender"] = raw.get("q2_gender"); used.add("q2_gender")

    # Citizenship (list[str])
    c = raw.get("citizenship")
    if isinstance(c, list):
        out["citizenship"] = c
    elif c in (None, ""):
        out["citizenship"] = []
    else:
        out["citizenship"] = [c]
    used.add("citizenship")

    # Ethnicity (merge "Other" text)
    eth = raw.get("q4_ethnicity")
    other = (raw.get("q4_ethnicity_other") or "").strip()
    out["ethnicity"] = other if eth == "Multiple ethnicity / Other" and other else eth
    used.update({"q4_ethnicity", "q4_ethnicity_other"})

    # Education
    out["education"] = raw.get("q5_education"); used.add("q5_education")

    # First language + L2 details
    q6 = (raw.get("q6_english_first") or "").strip().lower()
    used.add("q6_english_first")

    def _maybe_float(x):
        try:
            s = str(x).strip()
            return float(s) if s != "" else None
        except Exception:
            return None

    if q6 == "yes":
        out["first_language"] = "English"
        # Explicitly mark L2 fields as used so they don't end up in extras
        used.update({"q7_native_language","q8_start_age","q9_years_studied","q10_years_in_us"})
    elif q6 == "no":
        out["first_language"] = (raw.get("q7_native_language") or "").strip() or None
        used.add("q7_native_language")
        out["l2"] = {
            "start_age": _maybe_float(raw.get("q8_start_age")),
            "years_studied": _maybe_float(raw.get("q9_years_studied")),
            "years_in_us": _maybe_float(raw.get("q10_years_in_us")),
        }
        used.update({"q8_start_age","q9_years_studied","q10_years_in_us"})
    else:
        out["first_language"] = None
        # If neither yes/no, don't keep stray L2 values in extras
        used.update({"q7_native_language","q8_start_age","q9_years_studied","q10_years_in_us"})

    # Everything else → extras (but not L2 when not applicable)
    out["extras"] = {k: v for k, v in raw.items() if k not in used}
    return out