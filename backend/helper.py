
from typing import List, Dict, Any, Optional


# put this anywhere in main.py (above the endpoint), or into a small utils module
def normalize_demographics(raw: Dict[str, Any]) -> Dict[str, Any]:
    used: set[str] = set()
    out: Dict[str, Any] = {}

    # Prolific ID (already matching the schema)
    out["prolific_id"] = raw.get("prolific_id"); used.add("prolific_id")

    # Age
    if "q1_age" in raw:
        try:
            out["age"] = int(raw["q1_age"]) if str(raw["q1_age"]).strip() != "" else None
        except Exception:
            out["age"] = None
        used.add("q1_age")

    # Gender
    out["gender"] = raw.get("q2_gender"); used.add("q2_gender")

    # Citizenship (list[str])
    if "citizenship" in raw:
        if isinstance(raw["citizenship"], list):
            out["citizenship"] = raw["citizenship"]
        elif raw["citizenship"] is None:
            out["citizenship"] = None
        else:
            out["citizenship"] = [raw["citizenship"]]
        used.add("citizenship")

    # Ethnicity (merge "Other" text)
    eth = raw.get("q4_ethnicity")
    if eth == "Multiple ethnicity / Other":
        eth = raw.get("q4_ethnicity_other") or eth
    out["ethnicity"] = eth
    used.update({"q4_ethnicity", "q4_ethnicity_other"})

    # Education
    out["education"] = raw.get("q5_education"); used.add("q5_education")

    # First language
    q6 = raw.get("q6_english_first")
    if q6 == "Yes":
        out["first_language"] = "English"
    elif q6 == "No":
        out["first_language"] = raw.get("q7_native_language")
    else:
        out["first_language"] = None
    used.update({"q6_english_first", "q7_native_language"})

    # Everything else → extras
    extras = {k: v for k, v in raw.items() if k not in used}
    out["extras"] = extras

    return out
