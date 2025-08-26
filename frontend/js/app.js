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

  const civWrap = document.getElementById("citizenshipOptions");
  civWrap.innerHTML = COUNTRIES.map(c => `
    <li>
      <label class="option-row">
        <input type="checkbox" name="citizenship" value="${c}">
        <span>${c}</span>
      </label>
    </li>
  `).join("");

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
            <label class="option-row">
              <input type="radio" name="${q.id}" value="${c.id}">
              <span>${c.text}</span>
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
