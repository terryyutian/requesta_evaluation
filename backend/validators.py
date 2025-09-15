# backend/validators.py
from __future__ import annotations
from typing import Any, Dict, List, Tuple, Set

EXPECTED_CHOICE_IDS = {"a", "b", "c", "d"}

def _err(errors: List[str], msg: str) -> None:
    errors.append(msg)

def _warn(warnings: List[str], msg: str) -> None:
    warnings.append(msg)

def _choices_ok(q: Dict[str, Any], errors: List[str], where: str) -> bool:
    ok = True
    ch = q.get("choices")
    if not isinstance(ch, list) or len(ch) < 2:
        _err(errors, f"{where}: choices must be a non-empty list (got {type(ch).__name__})")
        return False
    # Ensure each choice has id/text, ids unique, and (optionally) are a–d
    seen: Set[str] = set()
    for c in ch:
        cid = str(c.get("id", "")).strip()
        txt = str(c.get("text", "")).strip()
        if not cid or not txt:
            _err(errors, f"{where}: each choice must have non-empty id/text")
            ok = False
        if cid in seen:
            _err(errors, f"{where}: duplicate choice id '{cid}'")
            ok = False
        seen.add(cid)
    # If exactly 4 choices, recommend a–d
    if len(ch) == 4 and not seen.issubset(EXPECTED_CHOICE_IDS):
        _warn(warnings, f"{where}: 4 choices but ids are not a/b/c/d ({sorted(seen)})")
    return ok

def _question_ok(q: Dict[str, Any], errors: List[str], warnings: List[str], where: str) -> None:
    qid = str(q.get("question_id") or "").strip()
    if not qid:
        _err(errors, f"{where}: missing question_id")
    prompt = str(q.get("prompt") or "").strip()
    if not prompt:
        _err(errors, f"{where}: missing prompt")
    _choices_ok(q, errors, where)
    cc = str(q.get("correct_choice_id") or "").strip()
    if not cc:
        _err(errors, f"{where}: missing correct_choice_id")
    else:
        ch_ids = {str(c.get("id") or "").strip() for c in (q.get("choices") or [])}
        if cc not in ch_ids:
            _err(errors, f"{where}: correct_choice_id '{cc}' not in choices {sorted(ch_ids)}")

def validate_content(
    PASSAGES: Dict[str, Any], QUESTIONS: Dict[str, Any], VOCAB: List[Dict[str, Any]]
) -> Dict[str, List[str]]:
    """
    Returns {"errors": [...], "warnings": [...]}.
    Errors should block deployment; warnings are safe but recommended fixes.
    """
    errors: List[str] = []
    warnings: List[str] = []

    # --- Passages vs. Questions cross-check ---
    p_keys = set(PASSAGES.keys())
    q_keys = set(QUESTIONS.keys())

    for k in sorted(p_keys - q_keys):
        _warn(warnings, f"PASSAGES has '{k}' but QUESTIONS missing it.")
    for k in sorted(q_keys - p_keys):
        _err(errors, f"QUESTIONS has '{k}' but PASSAGES missing it.")

    # --- Passages shape ---
    for k, p in PASSAGES.items():
        if not isinstance(p, dict):
            _err(errors, f"PASSAGES['{k}'] must be an object/dict.")
            continue
        for field in ("id", "title", "text"):
            if not isinstance(p.get(field), str) or not p.get(field).strip():
                _err(errors, f"PASSAGES['{k}']: '{field}' must be a non-empty string.")

    # --- Questions shape & quality ---
    global_seen_qids: Set[str] = set()
    for k, node in QUESTIONS.items():
        qnode = node.get("questions") if isinstance(node, dict) else None
        if not isinstance(qnode, dict):
            _err(errors, f"QUESTIONS['{k}'] must contain a 'questions' dict.")
            continue

        for src in ("baseline", "requesta"):
            qlist = qnode.get(src)
            if not isinstance(qlist, list):
                _err(errors, f"QUESTIONS['{k}']['questions']['{src}'] must be a list.")
                continue
            if len(qlist) < 6:
                _err(errors, f"QUESTIONS['{k}']['{src}'] has {len(qlist)} items; need ≥ 6 (5 RC + 1 attention).")

            # exactly one attention check recommended (id starts with 'QX')
            attn = [q for q in qlist if str(q.get("question_id") or "").upper().startswith("QX")]
            if len(attn) == 0:
                _warn(warnings, f"QUESTIONS['{k}']['{src}'] has no attention check (QX*).")
            elif len(attn) > 1:
                _warn(warnings, f"QUESTIONS['{k}']['{src}'] has multiple attention checks ({len(attn)}).")

            seen_here: Set[str] = set()
            for i, q in enumerate(qlist, start=1):
                where = f"QUESTIONS['{k}']['{src}'][{i}]"
                _question_ok(q, errors, warnings, where)
                qid = str(q.get("question_id") or "").strip()
                if qid:
                    if qid in seen_here:
                        _err(errors, f"{where}: duplicate question_id within set: '{qid}'")
                    seen_here.add(qid)
                    if qid in global_seen_qids:
                        _warn(warnings, f"{where}: question_id '{qid}' is duplicated across sets/passages.")
                    global_seen_qids.add(qid)

    # --- Vocab checks ---
    seen_vids: Set[str] = set()
    seen_tokens: Set[str] = set()
    for i, v in enumerate(VOCAB, start=1):
        if not isinstance(v, dict):
            _err(errors, f"VOCAB[{i}] must be an object/dict.")
            continue
        vid = str(v.get("id") or "").strip()
        tok = str(v.get("token") or "").strip()
        isw = v.get("is_word")
        if not vid:
            _err(errors, f"VOCAB[{i}] missing 'id'.")
        if not tok:
            _err(errors, f"VOCAB[{i}] missing 'token'.")
        if not isinstance(isw, bool):
            _err(errors, f"VOCAB[{i}] 'is_word' must be boolean.")
        if vid:
            if vid in seen_vids: _err(errors, f"VOCAB duplicate id '{vid}'.")
            seen_vids.add(vid)
        if tok:
            if tok in seen_tokens: _warn(warnings, f"VOCAB duplicate token '{tok}'.")
            seen_tokens.add(tok)

    return {"errors": errors, "warnings": warnings}
