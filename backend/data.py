from typing import Dict, List

# --- PLACEHOLDER DATA ---
# Replace with your actual passages, questions, and vocabulary list.

PASSAGES: Dict[str, Dict] = {
    "p1": {
        "id": "p1",
        "title": "Sample Passage 1 (placeholder)",
        "text": "This is a placeholder passage. Replace with real content."
    },
    "p2": {
        "id": "p2",
        "title": "Sample Passage 2 (placeholder)",
        "text": "Another placeholder passage goes here. Replace with real content."
    },
    "p3": {
        "id": "p3",
        "title": "Sample Passage 3 (placeholder)",
        "text": "Third sample passage. Replace with your actual text."
    },
}

QUESTIONS: Dict[str, List[Dict]] = {
    # Each passage id maps to 5 MCQs
    "p1": [
        {
            "id": "p1q1",
            "prompt": "What is the main idea?",
            "choices": [
                {"id": "a", "text": "Option A"},
                {"id": "b", "text": "Option B"},
                {"id": "c", "text": "Option C"},
                {"id": "d", "text": "Option D"},
            ],
            "correct_choice_id": "b"
        },
        # add 4 more...
        {"id": "p1q2","prompt":"Detail question 1","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"c"},
        {"id": "p1q3","prompt":"Detail question 2","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"a"},
        {"id": "p1q4","prompt":"Inference?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"d"},
        {"id": "p1q5","prompt":"Vocabulary-in-context","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"a"},
    ],
    "p2": [
        {"id":"p2q1","prompt":"Main idea?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"a"},
        {"id":"p2q2","prompt":"Detail 1?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"d"},
        {"id":"p2q3","prompt":"Detail 2?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"b"},
        {"id":"p2q4","prompt":"Inference?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"c"},
        {"id":"p2q5","prompt":"Word meaning?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"b"},
    ],
    "p3": [
        {"id":"p3q1","prompt":"Main idea?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"c"},
        {"id":"p3q2","prompt":"Detail 1?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"a"},
        {"id":"p3q3","prompt":"Detail 2?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"d"},
        {"id":"p3q4","prompt":"Inference?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"b"},
        {"id":"p3q5","prompt":"Word meaning?","choices":[{"id":"a","text":"A"},{"id":"b","text":"B"},{"id":"c","text":"C"},{"id":"d","text":"D"}],"correct_choice_id":"c"},
    ],
}

# 60 placeholder vocab strings. Replace with your curated list.
VOCAB: List[Dict] = [
    {"id": f"v{i:02d}", "token": t}
    for i, t in enumerate([
        "elation","brindle","quorp","sindel","nectar","mervin","ploxic","abrupt","fenster","drindle",
        "cobalt","rennet","glaver","saline","protem","dorsal","spline","nacture","bromide","tallow",
        "yarden","plaint","cander","sproot","locust","tramme","worsen","flend","mottle","parlor",
        "camber","thrice","stiple","ardent","crenel","upland","prand","sconce","fallacy","umbrage",
        "wimple","sartor","pion","knurl","gasket","morden","sallet","birl","tinsel","quintet",
        "lithe","dovetail","plorx","vessel","corbel","stanch","eyrie","flitter","truckle","borax"
    ], start=1)
]
