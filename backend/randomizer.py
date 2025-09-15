# backend/randomizer.py
import random
from typing import List
from data import PASSAGES, QUESTIONS

def _has_six_any(pid: str) -> bool:
    node = QUESTIONS.get(pid) or {}
    qdict = node.get("questions") or {}
    # consider either source sufficient for this placeholder logic
    for src in ("baseline", "requesta"):
        lst = qdict.get(src) or []
        if isinstance(lst, list) and len(lst) >= 6:
            return True
    return False

def random_two_passages(seed: int | None = None) -> List[str]:
    """
    Placeholder randomization function.
    Randomly picks 2 distinct passage IDs that have at least 6 MCQs
    in either baseline or requesta.
    """
    rng = random.Random(seed)
    candidates = [pid for pid in PASSAGES.keys() if _has_six_any(pid)]
    rng.shuffle(candidates)
    return candidates[:2]
