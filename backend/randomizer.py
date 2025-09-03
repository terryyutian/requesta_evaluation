import random
from typing import List
from .data import PASSAGES, QUESTIONS

def random_two_passages(seed: int | None = None) -> List[str]:
    """
    Placeholder randomization function.
    Randomly picks 2 distinct passage IDs that both have 5 MCQs.
    """
    rng = random.Random(seed)
    candidates = [pid for pid in PASSAGES.keys() if len(QUESTIONS.get(pid, [])) >= 5]
    rng.shuffle(candidates)
    return candidates[:2]

def maybe_shuffle_choices(questions: list, seed: int | None = None) -> list:
    """
    Optional: shuffle choice order per session.
    """
    rng = random.Random(seed)
    shuffled = []
    for q in questions:
        choices = q["choices"][:]
        rng.shuffle(choices)
        # adjust correct id if shuffling does not preserve id meaning
        # here, choice ids remain attached; no change needed
        shuffled.append({**q, "choices": choices})
    return shuffled
