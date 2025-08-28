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

// Track the user's current question index for a passage
function getCurrentQ(pid) {
  const v = localStorage.getItem(`current_q_${pid}`);
  return v === null ? null : Number(v);
}
function setCurrentQ(pid, qidx) {
  localStorage.setItem(`current_q_${pid}`, String(qidx));
}
function clearCurrentQ(pid) {
  localStorage.removeItem(`current_q_${pid}`);
}

// --- Event sequencing (per session) ---
function seqKeyForSession() {
  const sid = getSession();
  return sid ? `evseq_${sid}` : "evseq__anon";
}

function getLastSeq() {
  return Number(localStorage.getItem(seqKeyForSession()) || "0");
}
function setLastSeq(n) {
  localStorage.setItem(seqKeyForSession(), String(n));
}

let seqChannel = null;
try { seqChannel = new BroadcastChannel("event_seq"); } catch (_) {}

if (seqChannel) {
  seqChannel.onmessage = (e) => {
    const n = Number(e.data || 0);
    if (n > getLastSeq()) setLastSeq(n);
  };
}

function nextEventSeq() {
  // simple atomic-ish bump; BroadcastChannel reduces cross-tab clashes
  const n = getLastSeq() + 1;
  setLastSeq(n);
  if (seqChannel) seqChannel.postMessage(n);
  return n;
}


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

// ---- Focus & away-time logger ----
function safeUrl(path) {
  // Allow absolute `${API_BASE}/...` or relative `/api/...`
  if (typeof API_BASE === "string" && API_BASE) return `${API_BASE}${path}`;
  return path; // fallback to relative
}

function sendEvent(event_type, meta = {}) {
  const session_id = getSession(); if (!session_id) return;
  const payload = { session_id, event_type, meta, client_ts: Date.now() };
  try {
    fetch(safeUrl("/api/event"), {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload),
      keepalive: true,           // don’t block unloads
    }).catch(() => {});
  } catch (_) {}
}

function beaconEvent(event_type, meta = {}) {
  const session_id = getSession(); if (!session_id) return;
  const payload = JSON.stringify({ session_id, event_type, meta, client_ts: Date.now() });
  try {
    const ok = navigator.sendBeacon(safeUrl("/api/event"), new Blob([payload], { type: "application/json" }));
    if (!ok) throw new Error("sendBeacon returned false");
  } catch {
    // fallback — still non-blocking
    try {
      fetch(safeUrl("/api/event"), {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: payload,
        keepalive: true,
      }).catch(() => {});
    } catch (_) {}
  }
}


function startFocusLogger(meta = {}) {
  const page = meta.page || (document.body.dataset.page || "unknown");
  const baseMeta = { page, ...meta };

  // page_load
  const now = Date.now();
  sendEvent("page_load", { ...baseMeta, ts: now });

  // state
  const state = {
    inFocus: false,
    focusStart: null,
    awayStart: null,
  };

  function startFocus(reason = "focus") {
    // Close any away segment first
    if (state.awayStart != null) {
      const dur = Date.now() - state.awayStart;
      sendEvent("away_from_study", {
        ...baseMeta,
        start_ts: state.awayStart,
        duration_ms: dur,
        reason: "resume",
      });
      state.awayStart = null;
    }
    if (!state.inFocus) {
      state.inFocus = true;
      state.focusStart = Date.now();
    }
  }

  function endFocus(reason = "blur") {
    if (state.inFocus && state.focusStart != null) {
      const start = state.focusStart;
      const dur = Date.now() - start;
      // Use beacon on lifecycle boundaries
      beaconEvent("focus_segment", {
        ...baseMeta,
        start_ts: start,
        duration_ms: dur,
        reason,
      });
      state.inFocus = false;
      state.focusStart = null;
      state.awayStart = Date.now();
    }
  }

  // Initial
  if (!document.hidden) startFocus("initial");

  // Transitions
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) endFocus("visibility_hidden");
    else startFocus("visibility_visible");
  });
  window.addEventListener("focus", () => startFocus("window_focus"));
  window.addEventListener("blur", () => endFocus("window_blur"));
  window.addEventListener("pagehide", () => endFocus("pagehide"));
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

  // --- Render citizenship checkboxes (Q3) ---
  const COUNTRIES = [
    "Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria",
    "Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan",
    "Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei Darussalam","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon",
    "Canada","Cape Verde","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Republic of the...","Costa Rica",
    "Côte d'Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic",
    "Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France",
    "Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau",
    "Guyana","Haiti","Honduras","Hong Kong (S.A.R.)","Hungary","Iceland","India","Indonesia","Iran","Iraq",
    "Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait",
    "Kyrgyzstan","Lao People's Democratic Republic","Latvia","Lebanon","Lesotho","Liberia","Libyan Arab Jamahiriya","Liechtenstein","Lithuania","Luxembourg",
    "Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico",
    "Micronesia, Federated States of...","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal",
    "Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau",
    "Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Republic of Moldova","Romania",
    "Russian Federation","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal",
    "Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea",
    "Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Tajikistan","Thailand",
    "The former Yugoslav Republic of Macedonia","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda",
    "Ukraine","United Arab Emirates","United Kingdom of Great Britain and Northern Ireland","United Republic of Tanzania","United States of America","Uruguay","Uzbekistan","Vanuatu","Venezuela, Bolivarian Republic of...","Viet Nam",
    "Yemen","Zambia","Zimbabwe"
  ];

  // --- Render citizenship checkboxes into dropdown (Q3) ---
  const civWrap = document.getElementById("citizenshipOptions");
  const civSearch = document.getElementById("citizenshipSearch");
  const civSummary = document.getElementById("citizenshipSummary");
  const civDetails = document.getElementById("citizenshipDropdown");
  const civClose = document.getElementById("citizenshipClose");

  // Build list items
  civWrap.innerHTML = COUNTRIES.map(c => `
    <li>
      <label class="option-row">
        <input type="checkbox" name="citizenship" value="${c}">
        <span>${c}</span>
      </label>
    </li>
  `).join("");

  // Update summary "(N selected)"
  function updateCitizenshipSummary() {
    const n = document.querySelectorAll('input[name="citizenship"]:checked').length;
    civSummary.textContent = `(${n} selected)`;
  }
  updateCitizenshipSummary();

  // Selection change listeners
  civWrap.addEventListener("change", (e) => {
    if (e.target && e.target.name === "citizenship") updateCitizenshipSummary();
  });

  // Simple search/filter
  civSearch.addEventListener("input", () => {
    const q = civSearch.value.trim().toLowerCase();
    for (const li of civWrap.querySelectorAll("li")) {
      const label = li.textContent.toLowerCase();
      li.style.display = label.includes(q) ? "" : "none";
    }
  });

  // Close dropdown on "Done"
  civClose.addEventListener("click", () => { civDetails.open = false; });

  // --- existing logic for Q4 "Other" and Q6 skip ---
  function syncEthnicityOther() {
    const otherChecked = document.querySelector('input[name="q4_ethnicity"][value="Multiple ethnicity / Other"]')?.checked;
    const otherInput = document.querySelector('input[name="q4_ethnicity_other"]');
    if (otherInput) {
      otherInput.style.display = otherChecked ? "block" : "none";
      if (!otherChecked) otherInput.value = "";
    }
  }
  function syncL2Block() {
    const val = (document.querySelector('input[name="q6_english_first"]:checked') || {}).value;
    const block = document.getElementById("l2-block");
    const needL2 = (val === "No");
    block.style.display = needL2 ? "block" : "none";
    ["q7_native_language","q8_start_age","q9_years_studied","q10_years_in_us"].forEach(name => {
      const el = document.querySelector(`[name="${name}"]`);
      if (!el) return;
      if (needL2) el.setAttribute("required", "required");
      else { el.removeAttribute("required"); el.value = ""; }
    });
  }
  syncEthnicityOther();
  syncL2Block();
  document.querySelectorAll('input[name="q4_ethnicity"]').forEach(el => el.addEventListener("change", syncEthnicityOther));
  document.querySelectorAll('input[name="q6_english_first"]').forEach(el => el.addEventListener("change", syncL2Block));

  // --- submission ---
  const form = qs("#demo-form");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fd = new FormData(form);
    const payload = Object.fromEntries(fd.entries());

    // Multi-select citizenship from checkboxes
    payload.citizenship = Array.from(document.querySelectorAll('input[name="citizenship"]:checked')).map(i => i.value);

    // Age validation
    const age = Number(payload.q1_age);
    if (!Number.isFinite(age) || age < 18) {
      alert("You must be at least 18 years old to participate.");
      return;
    }

    if (payload.q4_ethnicity !== "Multiple ethnicity / Other") {
      delete payload.q4_ethnicity_other;
    }
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
  const pid = assigned?.[idx];
  if (!pid) { location.href = "consent.html"; return; }

  // Start granular focus logging for this page (non-blocking)
  startFocusLogger({ page: "passage", passage_id: pid });

  // visit counting
  const visits = getVisitCount(pid) + 1;
  setVisitCount(pid, visits);

  // load passage
  const t0 = performance.now();
  const data = await api(`/api/passage/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  qs("#title").textContent = data.title;

  // paragraph rendering
  const wrap = qs("#text");
  if (wrap) {
    wrap.innerHTML = "";
    const raw = (data.text || "").replace(/\r\n/g, "\n").trim();
    const paragraphs = raw.split(/\n\s*\n+/);
    for (const para of paragraphs) {
      const p = document.createElement("p");
      const lines = para.split("\n");
      lines.forEach((line, i) => {
        p.appendChild(document.createTextNode(line));
        if (i < lines.length - 1) p.appendChild(document.createElement("br"));
      });
      wrap.appendChild(p);
    }
  }

  // compute target question (resume current if present)
  const currentQ = getCurrentQ(pid);
  const hasCurrent = (currentQ !== null && !Number.isNaN(currentQ));
  const targetQ = hasCurrent ? currentQ : 0;
  const nextHref = `questions.html?index=${idx}&q=${targetQ}`;

  // Preferred: anchor link with href so navigation is native & non-blocking
  const nextLink = document.getElementById("nextLink");
  if (nextLink) {
    nextLink.setAttribute("href", nextHref);
    nextLink.addEventListener("click", () => {
      const t1 = performance.now();
      // fire-and-forget; never block navigation
      beaconEvent("passage_view_complete", {
        passage_id: pid,
        visit_ms: Math.round(t1 - t0),
        visit_index: visits
      });
    }, { once: true });
  }

  // Fallback: support a button with id="next" if your HTML still uses it
  const nextBtn = document.getElementById("next");
  if (!nextLink && nextBtn) {
    nextBtn.setAttribute("type", "button");
    nextBtn.addEventListener("click", () => {
      const t1 = performance.now();
      beaconEvent("passage_view_complete", {
        passage_id: pid,
        visit_ms: Math.round(t1 - t0),
        visit_index: visits
      });
      location.href = nextHref; // direct navigation
    }, { once: true });
  }

  // Back to Current Question button
  const backToQ = document.getElementById("backToQuestion");
  if (backToQ) {
    if (hasCurrent) {
      backToQ.style.display = "";
      backToQ.addEventListener("click", () => { location.href = nextHref; });
    } else {
      backToQ.style.display = "none";
    }
  }
}



async function initQuestions() {
  ensureSessionOrRedirect();

  const idx = Number(param("index") || "0");            // passage index (0 or 1)
  const qidx = Math.max(0, Number(param("q") || "0"));  // question index within passage
  const assigned = getAssignedPassages();
  const pid = assigned[idx];
  if (!pid) { location.href = "consent.html"; return; }

  // Start page focus logging early (we'll fill question_id after fetch)
  startFocusLogger({ page: "questions", passage_id: pid, q_index: qidx });

  // Keys for per-passage state
  const answersKey = `answers_${pid}`;
  const timeKey = `qtime_${pid}`; // total per-passage (kept if you use it)

  // Start per-page timer
  const pageStart = performance.now();

  // Fetch questions for this passage
  const payload = await api(`/api/questions/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  const total = payload.questions.length;
  const q = payload.questions[qidx];

  // If q index out of range, normalize
  if (!q) {
    location.href = `questions.html?index=${idx}&q=0`;
    return;
  }

  // Update focus logger with question_id (optional refinement)
  // (This sends a small "context" event; purely optional)
  sendEvent("context_update", { page: "questions", passage_id: pid, q_index: qidx, question_id: q.id });

  // Render the single question
  const container = qs("#qwrap");
  container.innerHTML = "";
  const card = document.createElement("div"); card.className = "qcard";
  card.innerHTML = `
    <div class="badge">Q${qidx + 1} of ${total}</div>
    <h3>${q.prompt}</h3>
    <ul class="choices">
      ${q.choices.map(c => `
        <li class="choice">
          <label class="option-row">
            <input type="radio" name="${q.id}" value="${c.id}">
            <span>${c.text}</span>
          </label>
        </li>`).join("")}
    </ul>
  `;
  container.appendChild(card);

  // Keep track of "current question" for quick return from passage page
  setCurrentQ(pid, qidx);

  // Pre-select saved answer if any
  const savedAll = getMCQAnswers(pid);
  const savedVal = savedAll[q.id];
  if (savedVal) {
    const radio = qs(`input[name="${q.id}"][value="${savedVal}"]`);
    if (radio) radio.checked = true;
  }

  // Save answer on change
  container.addEventListener("change", (e) => {
    if (e.target && e.target.name === q.id) {
      const picked = e.target.value;
      const current = getMCQAnswers(pid);
      current[q.id] = picked;
      setMCQAnswers(pid, current);
    }
  });

  // Progress label
  qs("#progress").textContent = `Q${qidx + 1} of ${total}`;

  // Back to passage (log + go)
  qs("#backToPassage").addEventListener("click", async () => {
    // count a back click (optional existing behavior)
    const clicks = getBackClicks(pid) + 1;
    setBackClicks(pid, clicks);
    sendEvent("navigate_back_to_passage", { passage_id: pid, count: clicks, q_index: qidx, question_id: q.id });

    location.href = `passage.html?index=${idx}`;
  });

  // Prev / Next / Submit controls
  const prevBtn = qs("#prevQuestion");
  const nextBtn = qs("#nextQuestion");
  const submitBtn = qs("#submit");

  prevBtn.style.display = qidx === 0 ? "none" : "";
  if (qidx < total - 1) {
    nextBtn.style.display = "";
    submitBtn.style.display = "none";
  } else {
    nextBtn.style.display = "none";
    submitBtn.style.display = "";
  }

  prevBtn.addEventListener("click", () => {
    location.href = `questions.html?index=${idx}&q=${qidx - 1}`;
  });

  nextBtn.addEventListener("click", () => {
    location.href = `questions.html?index=${idx}&q=${qidx + 1}`;
  });

  submitBtn.addEventListener("click", async () => {
    // Build full answers dict
    const answers = {};
    payload.questions.forEach(qq => {
      answers[qq.id] = savedAll[qq.id] ?? null;
    });

    // (Optional) total time-on-questions per passage
    const totalPrev = Number(localStorage.getItem(timeKey) || 0);
    const totalNow = totalPrev + Math.round(performance.now() - pageStart);
    localStorage.setItem(timeKey, String(totalNow));

    const res = await api("/api/submit_mcq", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        session_id: getSession(),
        passage_id: pid,
        answers: answers,
        time_on_questions_ms: totalNow,
        back_to_passage_clicks: getBackClicks(pid)
      })
    });

    localStorage.setItem(`mcq_result_${pid}`, JSON.stringify(res));
    // Clear markers for this passage
    localStorage.removeItem(timeKey);
    clearCurrentQ(pid);

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

  // build paragraphs from data.passage.text
  const wrap = qs("#passageText");
  wrap.innerHTML = "";

  const raw = (data.passage.text || "").replace(/\r\n/g, "\n").trim();
  const paragraphs = raw.split(/\n\s*\n+/); // split on blank lines

  for (const para of paragraphs) {
    const p = document.createElement("p");
    // keep single line breaks inside paragraph
    const lines = para.split("\n");
    lines.forEach((line, i) => {
      p.appendChild(document.createTextNode(line));
      if (i < lines.length - 1) p.appendChild(document.createElement("br"));
    });
    wrap.appendChild(p);
  }

  const right = qs("#review");
  right.innerHTML = "";

  data.questions.forEach(q => {
    const row = document.createElement("div");
    row.className = "card";

    const icon = q.is_correct ? "✅" : "❌";

    // Build full option list with markers for correct and user's choice
    const listHTML = q.choices.map(c => {
      const isUser = c.id === q.user_choice_id;
      const isCorrect = c.id === q.correct_choice_id;

      const badges = [
        isCorrect ? '<span class="badge-sm ok">Correct</span>' : '',
        isUser ? '<span class="badge-sm">Your choice</span>' : ''
      ].join(' ');

      return `
        <li class="${isCorrect ? 'correct' : ''} ${isUser ? 'selected' : ''}">
          <div class="choice-line">
            <span>${c.text}</span> ${badges}
          </div>
        </li>`;
    }).join("");

    row.innerHTML = `
      <div class="badge">${icon} ${q.is_correct ? "Correct" : "Incorrect"}</div>
      <h3>${q.prompt}</h3>
      <ul class="review-choices">
        ${listHTML}
      </ul>
      <div style="margin-top:8px;">
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
