
// --- Basic config ---
const API_BASE = (window.API_BASE_OVERRIDE || "http://127.0.0.1:8000").replace(/\/+$/,"");

// Minimal global error surfacing
window.addEventListener("error", (e) => {
  console.error("[global-error]", e.message, e.filename, e.lineno, e.colno, e.error);
});
window.addEventListener("unhandledrejection", (e) => {
  console.error("[unhandled-rejection]", e.reason);
});

// ---- Session helpers ----
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
function passageOrdinal(idx) {
  const words = ["One", "Two", "Three", "Four", "Five"];
  return words[idx] || String(idx + 1);
}
// Track the user's current question index for a passage
function getCurrentQ(pid) { const v = localStorage.getItem(`current_q_${pid}`); return v === null ? null : Number(v); }
function setCurrentQ(pid, qidx) { localStorage.setItem(`current_q_${pid}`, String(qidx)); }
function clearCurrentQ(pid) { localStorage.removeItem(`current_q_${pid}`); }

// --- Anti-copy guards (no logging) ---
function installGuards() {
  ["copy","cut","paste","contextmenu"].forEach(evt => {
    document.addEventListener(evt, (e) => { e.preventDefault(); });
  });
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && ["c","x","v","a"].includes(e.key.toLowerCase())) {
      e.preventDefault();
    }
  });
}

// ---- Utilities ----
function qs(sel){ return document.querySelector(sel); }
function param(name){ return new URLSearchParams(location.search).get(name); }

async function api(path, options={}) {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, options);
  if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`);
  return res.json();
}

function ensureSessionOrRedirect() {
  if (!getSession()) location.href = "consent.html";
}

// ---- Navigation hint to suppress false "blur" on in-app nav ----
let INAPP_NAV = false;
function markInAppNavigation() {
  INAPP_NAV = true;
  setTimeout(() => { INAPP_NAV = false; }, 2000);
}

// --- Logging helpers (fire-and-forget, never blocks UI) ---
function ffPost(path, body) {
  try {
    const url = `${API_BASE}${path}`;
    const json = JSON.stringify(body);
    const blob = new Blob([json], { type: "application/json" });
    if (navigator.sendBeacon) {
      navigator.sendBeacon(url, blob);
    } else {
      fetch(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: json, keepalive: true }).catch(()=>{});
    }
  } catch (_) {}
}

/**
 * Start attention tracking for a page bucket.
 * If rcMeta is provided, we also emit detailed RC focus/blur segments
 * and optionally warn on refocus after a long blur.
 * rcMeta = { passage_id, page_name_for_active }
 * warnOnReturnMs: number | null  (e.g., 5000 to warn when returning after >=5s blur)
 */
function startPageAttention(bucket, rcMeta, warnOnReturnMs = null) {
  const session_id = getSession();
  if (!session_id) return { stop: () => {} };

  let focused = (!document.hidden && document.hasFocus());
  let activeStart = focused ? Date.now() : null;
  let blurStart = !focused ? Date.now() : null;

  function sendActiveSegment(end) {
    if (activeStart == null) return;
    const dur = Math.max(0, end - activeStart);
    if (dur > 0) {
      ffPost("/api/log/attention", { session_id, bucket, elapsed_ms: dur });
      if (rcMeta) {
        ffPost("/api/log/rc_event", {
          session_id,
          passage_id: rcMeta.passage_id,
          page_name: rcMeta.page_name_for_active || "unknown",
          status: "active",
          start_time: activeStart,
          duration_ms: dur
        });
      }
    }
    activeStart = null;
  }

  function sendBlurSegment(end) {
    if (!rcMeta || blurStart == null) return;
    const dur = Math.max(0, end - blurStart);
    if (dur > 0) {
      ffPost("/api/log/rc_event", {
        session_id,
        passage_id: rcMeta.passage_id,
        page_name: "unknown",
        status: "blur",
        start_time: blurStart,
        duration_ms: dur
      });
    }
    blurStart = null;
  }

  function onFocus() {
    const now = Date.now();
    if (focused) return;

    // Capture blur duration before sending/clearing
    const priorBlurDur = blurStart != null ? (now - blurStart) : 0;

    // close blur segment
    sendBlurSegment(now);

    // Show warning only for RC pages, over threshold, and not due to in-app nav
    if (rcMeta && warnOnReturnMs != null && priorBlurDur >= warnOnReturnMs && !INAPP_NAV) {
      alert("Please stay focused on the reading comprehension task.");
    }

    focused = true;
    activeStart = now;
  }

  function onBlur() {
    const now = Date.now();
    if (!focused) return;
    // close active segment
    sendActiveSegment(now);
    focused = false;
    blurStart = now;
  }

  function visHandler() {
    if (document.hidden) onBlur(); else onFocus();
  }
  window.addEventListener("focus", onFocus);
  window.addEventListener("blur", onBlur);
  document.addEventListener("visibilitychange", visHandler);

  function flush() {
    const now = Date.now();
    if (focused) {
      // Closing active segment
      sendActiveSegment(now);
    } else if (!INAPP_NAV) {
      // Only record a blur segment on unload if not doing in-app navigation
      sendBlurSegment(now);
    }
  }
  window.addEventListener("pagehide", flush);
  window.addEventListener("beforeunload", flush);

  return { stop: flush };
}

installGuards();

// --- Page controllers ---
// consent.html
async function initConsent() {
  startPageAttention("consent");

  const agreeBtn = document.getElementById("agree");
  const thanksBox = document.getElementById("thanks");
  const nextBtn   = document.getElementById("next");

  if (!agreeBtn || !thanksBox || !nextBtn) {
    console.error("[consent] Missing DOM nodes", { agreeBtn, thanksBox, nextBtn });
    return;
  }

  agreeBtn.type = "button";
  agreeBtn.addEventListener("click", async () => {
    agreeBtn.disabled = true;
    try {
      const r = await api("/api/session/start", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({ source: "web", consent: true })
      });
      setSession(r.session_id);
      thanksBox.style.display = "block";
      nextBtn.focus();
    } catch (err) {
      console.error("[consent] session start failed:", err);
      alert("We had a temporary issue starting your session, but you can continue.");
      setSession(crypto?.randomUUID?.() || ("tmp_" + Date.now()));
      thanksBox.style.display = "block";
      nextBtn.focus();
    } finally {
      agreeBtn.disabled = false;
    }
  }, { once: true });

  nextBtn.addEventListener("click", () => {
    if (!getSession()) { alert("Please click I Agree first."); return; }
    markInAppNavigation();
    location.href = "demographic.html";
  });
}

// demographic.html
async function initDemographic() {
  startPageAttention("demographic");

  // --- Q6 → L2 (Q7–Q10) gating ---
  const L2_FIELDS = ["q7_native_language","q8_start_age","q9_years_studied","q10_years_in_us"];
  const l2Tpl   = document.getElementById("l2-template");
  const l2Mount = document.getElementById("l2-mount");

  function q6IsNo() {
    return (document.querySelector('input[name="q6_english_first"]:checked')?.value || "")
      .trim().toLowerCase() === "no";
  }

  function setL2Required(on) {
    L2_FIELDS.forEach(n => {
      const el = document.querySelector(`[name="${n}"]`);
      if (el) el.required = !!on;
    });
  }

  function clearL2Values() {
    L2_FIELDS.forEach(n => {
      const el = document.querySelector(`[name="${n}"]`);
      if (!el) return;
      if (el.tagName === "SELECT") el.selectedIndex = 0;
      else el.value = "";
    });
  }

  function ensureL2Mounted() {
    let el = document.getElementById("l2-block");
    if (!el && l2Tpl && l2Mount) {
      l2Mount.appendChild(l2Tpl.content.cloneNode(true));
      el = document.getElementById("l2-block");
    }
    return el;
  }

  function showL2() {
    const el = ensureL2Mounted();
    if (!el) return;
    el.setAttribute("data-show", "1");
    setL2Required(true);
  }

  function hideL2({ clear=true } = {}) {
    const el = document.getElementById("l2-block");
    if (el) el.removeAttribute("data-show");
    setL2Required(false);
    if (clear) clearL2Values();
  }

  function syncL2({ init=false } = {}) {
    if (q6IsNo()) showL2();
    else hideL2({ clear: !init });
  }

  // Initial + resilience passes
  syncL2({ init: true });
  requestAnimationFrame(() => syncL2({}));
  setTimeout(() => syncL2({}), 250);
  window.addEventListener("pageshow", () => syncL2({}));

  // React to user changes
  document.addEventListener("change", (e) => {
    if (e.target?.name === "q6_english_first") syncL2({});
  });

  // --- the rest of initDemographic() ---
  ensureSessionOrRedirect();

  // Dropdown plumbing for Q3
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

  const civWrap = document.getElementById("citizenshipOptions");
  const civSearch = document.getElementById("citizenshipSearch");
  const civSummary = document.getElementById("citizenshipSummary");
  const civDetails = document.getElementById("citizenshipDropdown");
  const civClose = document.getElementById("citizenshipClose");
  const civDisplay = document.getElementById("citizenshipDisplay");

  civWrap.innerHTML = COUNTRIES.map(c => `
    <li>
      <label class="option-row">
        <input type="checkbox" name="citizenship" value="${c}">
        <span>${c}</span>
      </label>
    </li>
  `).join("");

  function updateCitizenshipSummary() {
    const selected = Array.from(document.querySelectorAll('input[name="citizenship"]:checked')).map(i => i.value);
    const joined = selected.join("; ");
    const hasAny = selected.length > 0;
    civDisplay.textContent = hasAny ? joined : "Select countries…";
    civDisplay.classList.toggle("placeholder", !hasAny);
    civDisplay.title = hasAny ? joined : "";
    civSummary.textContent = `(${selected.length} selected)`;
  }
  updateCitizenshipSummary();

  civWrap.addEventListener("change", (e) => {
    if (e.target && e.target.name === "citizenship") updateCitizenshipSummary();
  });
  civSearch.addEventListener("input", () => {
    const q = civSearch.value.trim().toLowerCase();
    for (const li of civWrap.querySelectorAll("li")) {
      const label = li.textContent.toLowerCase();
      li.style.display = label.includes(q) ? "" : "none";
    }
  });
  civClose?.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    try { civDetails.open = false; } catch (_) {}
    civDetails.removeAttribute("open");
    const summary = civDetails.querySelector(".dropdown-summary");
    summary?.focus({ preventScroll: true });
  });

  // submission
  const form = qs("#demo-form");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(form);
    const payload = Object.fromEntries(fd.entries());
    payload.citizenship = Array.from(document.querySelectorAll('input[name="citizenship"]:checked')).map(i => i.value);

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
    markInAppNavigation();
    location.href = "instructions.html?index=0";
  });
}

// instructions.html
async function initRCInstructions() {
  ensureSessionOrRedirect();

  const idx = Number(param("index") || "0");
  const assigned = getAssignedPassages();
  if (!assigned || !assigned[idx]) { location.href = "demographic.html"; return; }

  startPageAttention("reading_instruction");

  const startLink = document.getElementById("startLink");
  const agreeBtn  = document.getElementById("agree");
  const agreedKey = `rc_agree_${getSession()}`;
  const nextHref  = `passage.html?index=${idx}`;

  startLink.setAttribute("href", nextHref);

  function showStart() {
    if (agreeBtn)  agreeBtn.style.display = "none";
    if (startLink) startLink.style.display = "inline-block";
  }
  if (localStorage.getItem(agreedKey) === "1") showStart();

  if (agreeBtn) {
    agreeBtn.addEventListener("click", () => {
      localStorage.setItem(agreedKey, "1");
      showStart();
    }, { once: true });
  }
  if (startLink) {
    startLink.addEventListener("click", () => { markInAppNavigation(); }, { once: true });
  }
}

// passage.html
async function initPassage() {
  ensureSessionOrRedirect();

  const idx = Number(param("index") || "0");
  const assigned = getAssignedPassages();
  const pid = assigned?.[idx];
  if (!pid) { location.href = "consent.html"; return; }

  const bucket = (idx === 0) ? "reading_task1" : "reading_task2";
  const pageName = (idx === 0) ? "p1" : "p2";
  // Warn when returning after >= 5s blur on RC pages
  startPageAttention(bucket, { passage_id: pid, page_name_for_active: pageName }, 5000);

  const visits = getVisitCount(pid) + 1;
  setVisitCount(pid, visits);

  const data = await api(`/api/passage/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  qs("#title").textContent = `Passage ${passageOrdinal(idx)}`;

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

  // Build target for next step
  const isReread = (param("r") === "1");
  const currentQ = getCurrentQ(pid);
  const hasCurrent = Number.isInteger(currentQ) && currentQ >= 0;
  const targetQForNext = (isReread && hasCurrent) ? currentQ : 0;
  const nextHref = `questions.html?index=${idx}&q=${targetQForNext}`;

  const nextLink = document.getElementById("nextLink");
  const backToQ  = document.getElementById("backToQuestion");

  if (isReread && hasCurrent) {
    // Show only the "Back to Current Question →" button
    if (nextLink) nextLink.style.display = "none";
    if (backToQ) {
      backToQ.textContent = "Back to Current Question →";
      backToQ.style.display = "";
      backToQ.onclick = () => { markInAppNavigation(); location.href = nextHref; };
    }
  } else {
    // Regular first-time flow: show only the Next link
    if (backToQ) backToQ.style.display = "none";
    if (nextLink) {
      nextLink.style.display = "inline-block";
      nextLink.setAttribute("href", nextHref);
      // mark in-app nav to avoid false blur warnings
      nextLink.addEventListener("click", () => { markInAppNavigation(); }, { once: true });
    }
  }
}

// questions.html
async function initQuestions() {
  ensureSessionOrRedirect();

  const idx = Number(param("index") || "0");
  const qidx = Math.max(0, Number(param("q") || "0"));
  const assigned = getAssignedPassages();
  const pid = assigned[idx];
  if (!pid) { location.href = "consent.html"; return; }

  // Fetch questions FIRST
  const payload = await api(`/api/questions/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  const total = payload.questions.length;
  const q = payload.questions[qidx];
  if (!q) { location.href = `questions.html?index=${idx}&q=0`; return; }

  const bucket = (idx === 0) ? "reading_task1" : "reading_task2";
  const pageName = (idx === 0 ? "p1" : "p2") + "q" + (qidx + 1);
  // Warn when returning after >= 5s blur on RC pages
  startPageAttention(bucket, { passage_id: pid, page_name_for_active: pageName }, 5000);

  const pageStart = performance.now();

  // Render single question
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

  // Track current question for quick return
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

  qs("#progress").textContent = `Q${qidx + 1} of ${total}`;

  // Back to passage
  qs("#backToPassage").addEventListener("click", () => {
    const clicks = getBackClicks(pid) + 1;
    setBackClicks(pid, clicks);
    markInAppNavigation();
    location.href = `passage.html?index=${idx}&r=1`;
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
    markInAppNavigation();
    location.href = `questions.html?index=${idx}&q=${qidx - 1}`;
  });
  nextBtn.addEventListener("click", () => {
    markInAppNavigation();
    location.href = `questions.html?index=${idx}&q=${qidx + 1}`;
  });

  submitBtn.addEventListener("click", async () => {
    const answers = {};
    payload.questions.forEach(qq => { answers[qq.id] = savedAll[qq.id] ?? null; });

    const timeKey = `qtime_${pid}`;
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
    localStorage.removeItem(timeKey);
    clearCurrentQ(pid);

    markInAppNavigation();
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

  const bucket = (idx === 0) ? "survey_task1" : "survey_task2";
  startPageAttention(bucket);

  // Fetch payload (passage + correctness + choices)
  const data = await api(`/api/posttask_data/${encodeURIComponent(pid)}?session_id=${encodeURIComponent(getSession())}`);
  qs("#passageTitle").textContent = `Passage ${passageOrdinal(idx)}`;

  // Render passage (left)
  const wrap = qs("#passageText");
  wrap.innerHTML = "";
  const raw = (data.passage.text || "").replace(/\r\n/g, "\n").trim();
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

  // --- Step-by-step review state
  const reviewEl   = qs("#review");
  const progressEl = qs("#ptProgress");
  const prevBtn    = qs("#prevPT");
  const nextBtn    = qs("#nextPT");
  const proceedBtn = qs("#proceed");

  const questions = data.questions || [];
  let cur = 0;

  // Track ratings
  const ratings = {};

  function hasRatingFor(index) {
    const q = questions[index];
    if (!q) return false;
    const r = ratings[q.question_id];
    return r === 1 || r === -1;
  }

  function updateNav() {
    const onLast = (cur === questions.length - 1);
    const curHasRating = hasRatingFor(cur);

    // Previous: show on any question after the first, regardless of rating
    if (prevBtn) prevBtn.style.display = (cur > 0) ? "" : "none";

    // Next/Proceed: only show when current question has a rating
    if (!curHasRating) {
      if (nextBtn)    nextBtn.style.display = "none";
      if (proceedBtn) proceedBtn.style.display = "none";
      return;
    }
    if (nextBtn)    nextBtn.style.display = onLast ? "none" : "";
    if (proceedBtn) proceedBtn.style.display = onLast ? "" : "none";
  }

  // Render one question panel
  function render() {
    const q = questions[cur];
    if (!q) { reviewEl.textContent = "No questions to review."; return; }

    progressEl.textContent = `Question ${cur + 1} of ${questions.length}`;

    const listHTML = q.choices.map(c => {
      const isUser    = c.id === q.user_choice_id;
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

    reviewEl.innerHTML = `
      <div class="badge">${q.is_correct ? "✅ Correct" : "❌ Incorrect"}</div>
      <h3 style="margin-top:8px;">${q.prompt}</h3>
      <ul class="review-choices" style="margin-top:8px;">
        ${listHTML}
      </ul>
      <div style="margin-top:12px;">
        <span class="thumb" data-q="${q.question_id}" data-v="1">👍</span>
        <span class="thumb" data-q="${q.question_id}" data-v="-1">👎</span>
      </div>
    `;

    // apply saved selection styling (if any)
    const existing = ratings[q.question_id];
    if (existing === 1) {
      const up = reviewEl.querySelector('.thumb[data-v="1"]');
      if (up) up.style.borderColor = "var(--accent)";
    } else if (existing === -1) {
      const down = reviewEl.querySelector('.thumb[data-v="-1"]');
      if (down) down.style.borderColor = "var(--accent)";
    }

    updateNav();
  }

  // Delegated click for thumbs in current panel
  reviewEl.addEventListener("click", (e) => {
    const t = e.target;
    if (!t.classList.contains("thumb")) return;
    const qid = t.dataset.q;
    const val = Number(t.dataset.v);

    ratings[qid] = val;

    // reset visual state, then highlight picked
    reviewEl.querySelectorAll(".thumb").forEach(el => { el.style.borderColor = "#1f2a3f"; });
    t.style.borderColor = "var(--accent)";

    updateNav(); // reflect visibility changes immediately
  });

  // navigation
  prevBtn.addEventListener("click", () => {
    if (cur > 0) { cur -= 1; render(); }
  });
  nextBtn.addEventListener("click", () => {
    if (cur < questions.length - 1) { cur += 1; render(); }
  });

  proceedBtn.addEventListener("click", async () => {
    // Guard (should be unreachable if hidden, but safe)
    if (!hasRatingFor(cur)) return;

    await api("/api/posttask", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({ session_id: getSession(), passage_id: pid, ratings })
    });
    const nextIdx = idx + 1;
    markInAppNavigation();
    if (nextIdx < assigned.length) location.href = `passage.html?index=${nextIdx}`;
    else location.href = "vocabulary_instruction.html";
  });

  // Kick off
  render();
}



// vocabulary_instruction.html
async function initVocabInstruction() {
  ensureSessionOrRedirect();

  // Count this time in the "vocabulary" bucket so it rolls up with the vocab task
  startPageAttention("vocabulary");

  const btn = document.getElementById("startVocab");
  if (btn) {
    btn.addEventListener("click", () => {
      markInAppNavigation();               // avoid a false blur segment on nav
      location.href = "vocab.html";
    }, { once: true });
  }
}


// vocab.html
async function initVocab() {
  ensureSessionOrRedirect();
  startPageAttention("vocabulary");

  let current = null;
  let lastShownAt = null;

  async function ensureStarted() {
    await api(`/api/vocab/start?session_id=${encodeURIComponent(getSession())}`, { method:"POST" });
  }
  async function loadNext() {
    const r = await api(`/api/vocab/next?session_id=${encodeURIComponent(getSession())}`);
    if (r.done) {
      markInAppNavigation();
      location.href = "final_check.html";
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

// final_check.html
async function initFinalCheck() {
  ensureSessionOrRedirect();

  const form = document.getElementById("final-form");
  const toolsBlock = document.getElementById("tools-block");
  const otherBox = document.getElementById("toolOther");
  const otherText = document.getElementById("toolOtherText");

  function syncToolsBlock() {
    const used = (document.querySelector('input[name="used_ai_tools"]:checked') || {}).value;
    const show = (used === "Yes");
    toolsBlock.style.display = show ? "block" : "none";
    if (!show) {
      document.querySelectorAll('input[name="tool"]').forEach(cb => cb.checked = false);
      otherText.value = "";
      otherText.style.display = "none";
    }
  }
  document.querySelectorAll('input[name="used_ai_tools"]').forEach(el => el.addEventListener("change", syncToolsBlock));
  syncToolsBlock();

  if (otherBox) {
    otherBox.addEventListener("change", () => {
      otherText.style.display = otherBox.checked ? "block" : "none";
      if (!otherBox.checked) otherText.value = "";
    });
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const used = (document.querySelector('input[name="used_ai_tools"]:checked') || {}).value || null;
    const tools = Array.from(document.querySelectorAll('input[name="tool"]:checked')).map(cb => cb.value);
    const other = (tools.includes("Other") ? (otherText.value || "").trim() : "");

    if (used === "Yes") {
      const hasAny = tools.length > 0 || other.length > 0;
      if (!hasAny) { alert("Please select at least one tool you used or specify it in 'Other'."); return; }
    }

    const payload = { used_ai_tools: used, tools, other_tool: other };
    await api(`/api/final_check?session_id=${encodeURIComponent(getSession())}`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });

    markInAppNavigation();
    location.href = "thanks.html";
  });
}

// thanks.html — record total participation time
async function initThanks() {
  const sid = getSession();
  if (sid) {
    ffPost("/api/log/participation_end", { session_id: sid, finished_at_ms: Date.now() });
  }
}

// --- Router (runs even if JS loads after DOMContentLoaded) ---
function bootstrap() {
  const page = document.body?.dataset?.page;
  const map = {
    "consent": initConsent,
    "demographic": initDemographic,
    "rc_instructions": initRCInstructions,
    "passage": initPassage,
    "questions": initQuestions,
    "posttask": initPostTask,
    "vocab_instruction": initVocabInstruction,
    "vocab": initVocab,
    "final_check": initFinalCheck,
    "thanks": initThanks,
  };
  if (page && map[page]) {
    try { map[page](); } catch (err) { console.error("[bootstrap] init error:", err); }
  } else {
    console.warn("[bootstrap] no init for page:", page);
  }
}
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", bootstrap, { once: true });
} else {
  bootstrap();
}
