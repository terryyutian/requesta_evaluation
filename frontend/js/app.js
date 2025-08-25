// --- Basic config ---
const API_BASE = (window.API_BASE_OVERRIDE || "http://127.0.0.1:8000").replace(/\/+$/,"");

// --- Session helpers ---
function getSession() { return localStorage.getItem("session_id"); }
function setSession(id) { localStorage.setItem("session_id", id); }
function getAssignedPassages() { return JSON.parse(localStorage.getItem("assigned_passages") || "[]"); }
function setAssignedPassages(ids) { localStorage.setItem("assigned_passages", JSON.stringify(ids)); }
function setBackClicks(pid, n) { localStorage.setItem(`back_clicks_${pid}`, String(n)); }
function getBackClicks(pid) { return Number(localStorage.getItem(`back_clicks_${pid}`) || 0); }
function setVisitCount(pid, n) { localStorage.setItem(`passage_visits_${pid}`, String(n)); }
function getVisitCount(pid) { return Number(localStorage.getItem(`passage_visits_${pid}`) || 0); }
function setMCQAnswers(pid, answers) { localStorage.setItem(`answers_${pid}`, JSON.stringify(answers)); }
function getMCQAnswers(pid) { return JSON.parse(localStorage.getItem(`answers_${pid}`) || "{}"); }

// --- Anti-copy & monitoring ---
function installGuards() {
  const log = (event_type, meta={}) => {
    const session_id = getSession();
    if (!session_id) return;
    fetch(`${API_BASE}/api/event`, {
      method: "POST", headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ session_id, event_type, meta })
    }).catch(()=>{});
  };

  // Disable copying/cutting/pasting/context
  ["copy","cut","paste","contextmenu"].forEach(evt => {
    document.addEventListener(evt, (e) => { e.preventDefault(); log("guard_"+evt, {}); });
  });

  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && ["c","x","v","a"].includes(e.key.toLowerCase())) {
      e.preventDefault();
      log("guard_keyblock", { key: e.key });
    }
  });

  // Visibility & focus/blur
  document.addEventListener("visibilitychange", () => {
    log("visibility_change", { hidden: document.hidden });
  });
  window.addEventListener("blur", () => log("window_blur", {}));
  window.addEventListener("focus", () => log("window_focus", {}));
}

// --- Utilities ---
function qs(sel){ return document.querySelector(sel); }
function qsa(sel){ return Array.from(document.querySelectorAll(sel)); }
function param(name){ return new URLSearchParams(location.search).get(name); }
function sleep(ms){ return new Promise(r=>setTimeout(r,ms)); }

async function api(path, options={}) {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, options);
  if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`);
  return res.json();
}

function ensureSessionOrRedirect() {
  if (!getSession()) location.href = "consent.html";
}

installGuards();

// --- Page controllers (each page calls its init if present) ---

// consent.html
async function initConsent() {
  qs("#agree").addEventListener("click", async () => {
    const r = await api("/api/session/start", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({ source: "web", consent: true })
    });
    setSession(r.session_id);

    // Thank-you "conversation" box mimic (simple modal-style)
    qs("#thanks").style.display = "block";
    qs("#next").focus();
  });

  qs("#next").addEventListener("click", () => {
    location.href = "demographic.html";
  });
}

// demographic.html
async function initDemographic() {
  ensureSessionOrRedirect();

  // Toggle Other text for Q4
  function syncEthnicityOther() {
    const otherChecked = document.querySelector('input[name="q4_ethnicity"][value="Multiple ethnicity / Other"]')?.checked;
    const otherInput = document.querySelector('input[name="q4_ethnicity_other"]');
    if (otherInput) {
      otherInput.style.display = otherChecked ? "block" : "none";
      if (!otherChecked) otherInput.value = "";
    }
  }

  // Show/hide Q7–Q10 when Q6 = No
  function syncL2Block() {
    const val = (document.querySelector('input[name="q6_english_first"]:checked') || {}).value;
    const block = document.getElementById("l2-block");
    const needL2 = (val === "No");
    block.style.display = needL2 ? "block" : "none";

    // Conditionally require Q7–Q10 only if needed
    ["q7_native_language","q8_start_age","q9_years_studied","q10_years_in_us"].forEach(name => {
      const el = document.querySelector(`[name="${name}"]`);
      if (!el) return;
      if (needL2) el.setAttribute("required", "required");
      else { el.removeAttribute("required"); el.value = ""; }
    });
  }

  // initial sync
  syncEthnicityOther();
  syncL2Block();

  // listeners
  document.querySelectorAll('input[name="q4_ethnicity"]').forEach(el => el.addEventListener("change", syncEthnicityOther));
  document.querySelectorAll('input[name="q6_english_first"]').forEach(el => el.addEventListener("change", syncL2Block));

  const form = qs("#demo-form");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fd = new FormData(form);
    // start with scalar fields
    const payload = Object.fromEntries(fd.entries());
    // capture multi-select citizenship as an array
    payload.citizenship = fd.getAll("citizenship");

    // Age validation (must be number ≥ 18)
    const age = Number(payload.q1_age);
    if (!Number.isFinite(age) || age < 18) {
      alert("You must be at least 18 years old to participate.");
      return;
    }

    // If Q4 isn't "Other", drop the free-text
    if (payload.q4_ethnicity !== "Multiple ethnicity / Other") {
      delete payload.q4_ethnicity_other;
    }

    // If Q6 = Yes, drop Q7–Q10 to respect skip
    if (payload.q6_english_first === "Yes") {
      delete payload.q7_native_language;
      delete payload.q8_start_age;
      delete payload.q9_years_studied;
      delete payload.q10_years_in_us;
    }

    await api(`/api/demographics?session_id=${encodeURIComponent(getSession())}`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });

    const rnd = await api(`/api/randomize?session_id=${encodeURIComponent(getSession())}`, { method: "POST" });
    setAssignedPassages(rnd.passage_ids);
    location.href = "passage.html?index=0";
  });
}

// passage.html
async function initPassage() {
  ensureSessionOrRedirect();
  const idx = Number(param("index") || "0");
  const assigned = getAssignedPassages();
  const pid = assigned[idx];
  if (!pid) { location.href = "consent.html"; return; }

  // visit counting
  const visits = getVisitCount(pid) + 1;
  setVisitCount(pid, visits);

  const t0 = performance.now();
  const data = await api(`/api/passage/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  qs("#title").textContent = data.title;
  qs("#text").textContent = data.text;

  qs("#next").addEventListener("click", async () => {
    const t1 = performance.now();
    await api("/api/event", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        session_id: getSession(),
        event_type: "passage_view_complete",
        meta: { passage_id: pid, visit_ms: Math.round(t1 - t0), visit_index: visits }
      })
    });
    location.href = `questions.html?index=${idx}`;
  });
}

// questions.html
async function initQuestions() {
  ensureSessionOrRedirect();
  const idx = Number(param("index") || "0");
  const assigned = getAssignedPassages();
  const pid = assigned[idx];
  if (!pid) { location.href = "consent.html"; return; }

  const t0 = performance.now();
  const payload = await api(`/api/questions/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  const container = qs("#qwrap");
  container.innerHTML = "";
  payload.questions.forEach((q, i) => {
    const card = document.createElement("div"); card.className = "card qcard";
    card.innerHTML = `
      <div class="badge">Q${i+1}</div>
      <h3>${q.prompt}</h3>
      <ul class="choices">
        ${q.choices.map(c => `
          <li class="choice">
            <label>
              <input type="radio" name="${q.id}" value="${c.id}"> ${c.text}
            </label>
          </li>`).join("")}
      </ul>
    `;
    container.appendChild(card);
  });

  qs("#backToPassage").addEventListener("click", async () => {
    const clicks = getBackClicks(pid) + 1;
    setBackClicks(pid, clicks);
    await api("/api/event", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        session_id: getSession(),
        event_type: "navigate_back_to_passage",
        meta: { passage_id: pid, count: clicks }
      })
    });
    location.href = `passage.html?index=${idx}`;
  });

  qs("#submit").addEventListener("click", async () => {
    const answers = {};
    payload.questions.forEach(q => {
      const picked = qs(`input[name="${q.id}"]:checked`);
      answers[q.id] = picked ? picked.value : null;
    });

    setMCQAnswers(pid, answers);

    const t1 = performance.now();
    const res = await api("/api/submit_mcq", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        session_id: getSession(),
        passage_id: pid,
        answers: answers,
        time_on_questions_ms: Math.round(t1 - t0),
        back_to_passage_clicks: getBackClicks(pid)
      })
    });

    localStorage.setItem(`mcq_result_${pid}`, JSON.stringify(res));
    location.href = `posttask.html?index=${idx}`;
  });
}

// posttask.html
async function initPostTask() {
  ensureSessionOrRedirect();
  const idx = Number(param("index") || "0");
  const assigned = getAssignedPassages();
  const pid = assigned[idx];
  if (!pid) { location.href = "consent.html"; return; }

  const data = await api(`/api/posttask_data/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);

  qs("#passageTitle").textContent = data.passage.title;
  qs("#passageText").textContent = data.passage.text;

  const right = qs("#review");
  right.innerHTML = "";
  data.questions.forEach(q => {
    const row = document.createElement("div"); row.className = "card";
    const icon = q.is_correct ? "✅" : "❌";
    const you = q.choices.find(c => c.id === q.user_choice_id)?.text || "(no answer)";
    const correct = q.choices.find(c => c.id === q.correct_choice_id)?.text || "(unknown)";

    row.innerHTML = `
      <div class="badge">${icon} ${q.is_correct ? "Correct" : "Incorrect"}</div>
      <h3>${q.prompt}</h3>
      <p><b>Your answer:</b> ${you}</p>
      <p><b>Correct answer:</b> ${correct}</p>
      <div>
        <span class="thumb" data-q="${q.question_id}" data-v="1">👍</span>
        <span class="thumb" data-q="${q.question_id}" data-v="-1">👎</span>
      </div>
    `;
    right.appendChild(row);
  });

  const ratings = {};
  right.addEventListener("click", (e) => {
    const t = e.target;
    if (t.classList.contains("thumb")) {
      ratings[t.dataset.q] = Number(t.dataset.v);
      t.style.borderColor = "var(--accent)";
    }
  });

  qs("#continue").addEventListener("click", async () => {
    await api("/api/posttask", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        session_id: getSession(),
        passage_id: pid,
        ratings
      })
    });

    const nextIdx = idx + 1;
    if (nextIdx < assigned.length) {
      location.href = `passage.html?index=${nextIdx}`;
    } else {
      location.href = "vocab.html";
    }
  });
}

// vocab.html
async function initVocab() {
  ensureSessionOrRedirect();

  let current = null;
  let lastShownAt = null;

  async function ensureStarted() {
    await api(`/api/vocab/start?session_id=${encodeURIComponent(getSession())}`, { method:"POST" });
  }

  async function loadNext() {
    const r = await api(`/api/vocab/next?session_id=${encodeURIComponent(getSession())}`);
    if (r.done) {
      location.href = "thanks.html";
      return;
    }
    current = r.item;
    qs("#remaining").textContent = r.remaining;
    qs("#token").textContent = current.token;
    lastShownAt = performance.now();
  }

  qs("#yes").addEventListener("click", () => submit(true));
  qs("#no").addEventListener("click", () => submit(false));

  async function submit(isWord) {
    const rt = Math.round(performance.now() - lastShownAt);
    await api("/api/vocab/answer", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        session_id: getSession(),
        item_id: current.id,
        is_word: isWord,
        rt_ms: rt
      })
    });
    await loadNext();
  }

  await ensureStarted();
  await loadNext();
}

// simple router by data-page attribute
document.addEventListener("DOMContentLoaded", () => {
  const page = document.body.dataset.page;
  const map = {
    "consent": initConsent,
    "demographic": initDemographic,
    "passage": initPassage,
    "questions": initQuestions,
    "posttask": initPostTask,
    "vocab": initVocab
  };
  if (map[page]) map[page]();
});
