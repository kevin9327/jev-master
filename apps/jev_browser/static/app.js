const SAMPLES = {
  mixed:
    "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.",
  ticket:
    "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.",
  gate:
    "Voice transcript: yeah go ahead and send the pending transfer, I already checked the amount.",
  pitch: `Pitch: Relays is a marketplace that matches independent HVAC techs with
building managers in rust-belt cities. We have 40 paying buildings in
Cleveland, $18k MRR, and a two-sided waitlist in Detroit. Moat is local
dispatch density plus a licensed-tech network, not a model. Raising a
$1.2M pre-seed to hire two ops leads and expand to Pittsburgh.`,
};

const QUESTIONS = {
  mixed: [
    { type: "choice", id: "department", instructions: "Which team should handle this" },
    { type: "score", id: "frustration", instructions: "How frustrated the customer appears" },
    { type: "noul", id: "is_urgent", instructions: "The message conveys urgency or time-sensitivity" },
  ],
  ticket: [
    { type: "choice", id: "department", instructions: "Which team should handle this" },
    { type: "score", id: "frustration", instructions: "How frustrated the customer appears" },
    { type: "noul", id: "is_urgent", instructions: "The message conveys urgency or time-sensitivity" },
  ],
  gate: [
    { type: "choice", id: "intent", instructions: "What action is the user requesting?" },
    { type: "score", id: "stakes", instructions: "How irreversible is the requested action if it is wrong?" },
    { type: "noul", id: "is_explicit", instructions: "The user explicitly confirmed the action in this utterance" },
  ],
  pitch: [
    { type: "score", id: "market", instructions: "How large and reachable is the stated market?" },
    { type: "score", id: "feasibility", instructions: "How technically and operationally feasible is this plan?" },
    { type: "score", id: "differentiation", instructions: "How distinct is the wedge versus a generic marketplace?" },
    { type: "choice", id: "stage", instructions: "Which financing stage does this pitch match?" },
    { type: "noul", id: "has_traction", instructions: "The pitch cites concrete paying customers or revenue" },
  ],
};

const stateEl = document.getElementById("state");
const runEl = document.getElementById("run");
const statusEl = document.getElementById("status");
const picker = document.getElementById("app-picker");
const qList = document.getElementById("question-list");
const decisionEmpty = document.getElementById("decision-empty");
const decisionBody = document.getElementById("decision-body");
const answersBody = document.getElementById("answers-body");
const rawJson = document.getElementById("raw-json");

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function fmt(n, digits = 3) {
  const x = Number(n);
  if (!Number.isFinite(x)) return String(n);
  return x.toFixed(digits);
}

function selectedApp() {
  const on = picker.querySelector('[aria-checked="true"]');
  return (on && on.dataset.app) || "mixed";
}

function setApp(app, { fillSample = true } = {}) {
  picker.querySelectorAll("[data-app]").forEach((btn) => {
    btn.setAttribute("aria-checked", String(btn.dataset.app === app));
  });
  if (fillSample) {
    const known = Object.values(SAMPLES).some((s) => stateEl.value.trim() === s.trim());
    if (!stateEl.value.trim() || known) stateEl.value = SAMPLES[app];
  }
  renderQuestions(app);
}

function renderQuestions(app) {
  qList.innerHTML = QUESTIONS[app]
    .map(
      (q) => `<li>
        <span class="chip ${esc(q.type)}">${esc(q.type)}</span>
        <div class="q-copy"><strong>${esc(q.id)}</strong><span>${esc(q.instructions)}</span></div>
      </li>`
    )
    .join("");
}

function badgeClass(value) {
  const key = String(value || "").toLowerCase();
  if (["act", "pass"].includes(key)) return key;
  if (["escalate", "reject"].includes(key)) return key;
  if (["confirm", "hold"].includes(key)) return key;
  return "other";
}

function renderValue(value) {
  if (value && typeof value === "object") {
    return Object.entries(value)
      .map(([k, v]) => `${esc(k)}=${esc(typeof v === "number" ? fmt(v, 4) : v)}`)
      .join(" · ");
  }
  if (typeof value === "number") return esc(fmt(value, 4));
  return esc(value);
}

function renderDecision(decision) {
  if (!decision || typeof decision !== "object") {
    decisionEmpty.hidden = false;
    decisionBody.hidden = true;
    decisionEmpty.textContent = "Composer returned no decision object.";
    return;
  }
  decisionEmpty.hidden = true;
  decisionBody.hidden = false;
  const action = decision.action || decision.verdict || "";
  const who = decision.department || decision.intent || decision.stage || decision.handler || "";
  const extra = decision.handler && decision.department ? ` → ${decision.handler}` : decision.reason ? ` · ${decision.reason}` : "";
  const skip = new Set(["action", "verdict"]);
  const fields = Object.entries(decision)
    .filter(([k]) => !skip.has(k))
    .map(
      ([k, v]) => `<div><dt>${esc(k)}</dt><dd>${renderValue(v)}</dd></div>`
    )
    .join("");
  decisionBody.innerHTML = `
    <div class="headline">
      ${action ? `<span class="badge ${badgeClass(action)}">${esc(action)}</span>` : ""}
      <span class="who">${esc(who)}${esc(extra)}</span>
    </div>
    <dl class="fields">${fields}</dl>
  `;
}

function renderChoice(id, answer) {
  const rows = Object.entries(answer.probabilities || {})
    .sort((a, b) => b[1] - a[1])
    .map(
      ([name, p]) => `<div class="bar-row">
        <span class="lab">${esc(name)}</span>
        <div class="track"><div class="fill" style="width:${Math.max(0, Math.min(1, p)) * 100}%"></div></div>
        <span class="pct">${esc(fmt(p, 3))}</span>
      </div>`
    )
    .join("");
  return `<article class="card">
    <div class="card-head"><h3>${esc(id)}</h3><span class="chip choice">choice</span></div>
    <div class="meter-label"><span>selected</span><strong>${esc(answer.choice)}</strong></div>
    ${rows}
    <div class="conf bar-row">
      <span class="lab">confidence</span>
      <div class="track"><div class="fill conf" style="width:${Math.max(0, Math.min(1, answer.confidence)) * 100}%"></div></div>
      <span class="pct">${esc(fmt(answer.confidence, 3))}</span>
    </div>
  </article>`;
}

function renderScore(id, answer) {
  const legend = answer.legend || {};
  const keys = Object.keys(legend).sort((a, b) => Number(a) - Number(b));
  const max = keys.length ? Number(keys[keys.length - 1]) : 1;
  const pos = max > 0 ? Math.max(0, Math.min(1, Number(answer.score) / max)) : 0;
  const nearest = keys.reduce((best, k) =>
    Math.abs(Number(k) - Number(answer.score)) < Math.abs(Number(best) - Number(answer.score)) ? k : best
  , keys[0] || "0");
  const legendRows = keys
    .map(
      (k) => `<div class="legend-row ${k === nearest ? "on" : ""}"><span>${esc(k)}</span><span>${esc(legend[k])}</span></div>`
    )
    .join("");
  return `<article class="card">
    <div class="card-head"><h3>${esc(id)}</h3><span class="chip score">score</span></div>
    <div class="meter-label"><span>score</span><strong>${esc(fmt(answer.score, 3))}</strong></div>
    <div class="score-scale"><div class="score-thumb" style="left:${pos * 100}%"></div></div>
    <div class="legend">${legendRows}</div>
    <div class="conf bar-row">
      <span class="lab">confidence</span>
      <div class="track"><div class="fill conf" style="width:${Math.max(0, Math.min(1, answer.confidence)) * 100}%"></div></div>
      <span class="pct">${esc(fmt(answer.confidence, 3))}</span>
    </div>
  </article>`;
}

function renderNoul(id, answer) {
  const n = Number(answer.noul);
  return `<article class="card">
    <div class="card-head"><h3>${esc(id)}</h3><span class="chip noul">noul</span></div>
    <div class="meter-label"><span>0</span><strong>${esc(fmt(n, 3))}</strong><span>1</span></div>
    <div class="track"><div class="fill noul" style="width:${Math.max(0, Math.min(1, n)) * 100}%"></div></div>
  </article>`;
}

function renderAnswers(answers) {
  if (!answers || !Object.keys(answers).length) {
    answersBody.innerHTML = `<p class="empty">No answers yet.</p>`;
    return;
  }
  answersBody.innerHTML = Object.entries(answers)
    .map(([id, answer]) => {
      if (answer.type === "choice") return renderChoice(id, answer);
      if (answer.type === "score") return renderScore(id, answer);
      if (answer.type === "noul") return renderNoul(id, answer);
      return `<article class="card"><h3>${esc(id)}</h3><pre>${esc(JSON.stringify(answer, null, 2))}</pre></article>`;
    })
    .join("");
}

async function run() {
  const state = stateEl.value.trim();
  const app = selectedApp();
  if (!state) {
    statusEl.textContent = "state required";
    return;
  }
  runEl.disabled = true;
  statusEl.textContent = "evaluating jev-latest…";
  try {
    const res = await fetch("/api/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({ state, app }),
    });
    const data = await res.json();
    rawJson.textContent = JSON.stringify(data, null, 2);
    if (!res.ok) {
      decisionEmpty.hidden = false;
      decisionBody.hidden = true;
      decisionEmpty.innerHTML = `<span class="err">${esc(data.error || res.statusText)}</span>`;
      answersBody.innerHTML = `<p class="empty">Request failed.</p>`;
      statusEl.textContent = `error ${res.status}`;
      return;
    }
    renderDecision(data.decision);
    renderAnswers(data.answers);
    const usage = data.usage && Object.keys(data.usage).length
      ? " · " + Object.entries(data.usage).map(([k, v]) => `${k}=${v}`).join(" ")
      : "";
    statusEl.textContent = `${data.model || "jev-latest"} · ${data.endpoint || "POST /v1/systemone"}${usage}`;
  } catch (err) {
    statusEl.textContent = "network error";
    decisionEmpty.hidden = false;
    decisionBody.hidden = true;
    decisionEmpty.innerHTML = `<span class="err">${esc(err.message || err)}</span>`;
  } finally {
    runEl.disabled = false;
  }
}

picker.addEventListener("click", (event) => {
  const btn = event.target.closest("[data-app]");
  if (!btn) return;
  setApp(btn.dataset.app);
});

runEl.addEventListener("click", run);

document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
    event.preventDefault();
    run();
  }
});

stateEl.value = SAMPLES.mixed;
setApp("mixed", { fillSample: false });
statusEl.textContent = "idle · key never in page";
