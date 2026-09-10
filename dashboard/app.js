const state = { data: null, activeResearchTab: "expert" };

const $ = (selector) => document.querySelector(selector);

function setText(selector, value) {
  const node = $(selector);
  if (node) node.textContent = value ?? "—";
}

function documentLink(path) {
  return `/document?path=${encodeURIComponent(path)}`;
}

function setSource(selector, path) {
  const node = $(selector);
  if (!node) return;
  node.href = documentLink(path);
}

function cleanText(value) {
  return (value || "").replace(/&amp;/g, "&").replace(/<br\s*\/?>(\s*)/gi, " ").trim();
}

function percentFromValue(value) {
  const parsed = Number.parseFloat(String(value || "").replace(/[^\d.-]/g, ""));
  return Number.isFinite(parsed) ? parsed : 0;
}

function renderPortfolio(portfolio) {
  setText("#metric-equity", portfolio.equity);
  setText("#metric-cash", portfolio.cash);
  setText("#metric-long-value", portfolio.longValue);
  setText("#metric-return", `Since start · ${portfolio.return}`);
  setText("#metric-exposure", `${portfolio.positions.length} position rows reconciled`);
  setText("#metric-positions", portfolio.positionSummary);
  setText("#metric-orders", `${portfolio.positionRows} broker rows · ${portfolio.openOrders}`);
  setText("#open-order-detail", portfolio.openOrderDetail);
  setSource("#portfolio-source", portfolio.source);
  setSource("#order-source", portfolio.source);

  const body = $("#portfolio-body");
  body.replaceChildren();
  portfolio.positions.forEach((position) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td><div class="holding-name"><span class="ticker"></span><span><span class="instrument-label"></span></span></div></td>
      <td></td><td></td><td></td><td class="align-right"></td>`;
    row.querySelector(".ticker").textContent = position.ticker;
    row.querySelector(".instrument-label").textContent = position.instrument;
    row.children[1].textContent = position.quantity;
    row.children[2].textContent = position.price;
    row.children[3].textContent = position.marketValue;
    const pnl = row.children[4];
    pnl.textContent = position.pnl;
    pnl.className = `align-right ${position.positive ? "pnl-positive" : "pnl-negative"}`;
    body.appendChild(row);
  });
}

function actionClass(action) {
  return { BUY: "action-buy", SELL: "action-sell", HOLD: "action-hold" }[action] || "action-note";
}

function renderDecisions(portfolio) {
  const list = $("#decision-list");
  list.replaceChildren();
  portfolio.decisions.slice(0, 8).forEach((decision) => {
    const item = document.createElement("article");
    item.className = "decision-item";
    item.innerHTML = `<span class="decision-ticker"></span><span class="action-badge"></span><span class="decision-text"></span>`;
    item.querySelector(".decision-ticker").textContent = decision.ticker;
    const badge = item.querySelector(".action-badge");
    badge.className = `action-badge ${actionClass(decision.action)}`;
    badge.textContent = decision.action;
    item.querySelector(".decision-text").textContent = decision.short;
    list.appendChild(item);
  });
  setSource("#decisions-source", "memory/logs/2026-09-02.md");
}

function renderSummary(data) {
  const { summary, portfolio } = data;
  setText("#summary-copy", summary.voice);
  setText("#summary-source", summary.source);
  setText("#summary-updated", summary.updated);
  setText("#date-stamp", `Session · ${summary.date}`);
  setText("#reconciled-label", `Reconciled ${portfolio.generated}`);
  setSource("#summary-link", summary.source);
  setSource("#shortlist-source", data.shortlist.source);
}

function renderResearch(data) {
  const rows = data.shortlist.categories[state.activeResearchTab] || [];
  const list = $("#candidate-list");
  list.replaceChildren();
  rows.slice(0, 6).forEach((candidate) => {
    const item = document.createElement("article");
    item.className = "candidate-row";
    const name = candidate.Name || candidate.Company || "";
    const reason = candidate.Reason || candidate.Reasons || candidate.Summary || candidate["Category rank and score"] || "No additional context in shortlist.";
    const meta = candidate.Direction || candidate.Price || candidate.Strength || candidate["RRF score"] || "";
    item.innerHTML = `<span class="rank"></span><div><div class="candidate-title"><strong class="ticker"></strong><span class="candidate-name"></span></div><p class="candidate-summary"></p></div><span class="candidate-meta"></span>`;
    item.querySelector(".rank").textContent = `#${candidate.Rank || "—"}`;
    item.querySelector(".ticker").textContent = candidate.Ticker || "—";
    item.querySelector(".candidate-name").textContent = cleanText(name);
    item.querySelector(".candidate-summary").textContent = cleanText(reason);
    item.querySelector(".candidate-meta").textContent = cleanText(meta);
    list.appendChild(item);
  });
  const notes = $("#research-notes");
  notes.replaceChildren();
  const latest = data.research.filter((item) => ["GTLB", "MMED", "AMRZ", "MLM", "MSTR"].includes(item.ticker)).slice(0, 8);
  const label = document.createElement("span");
  label.textContent = "Latest analysis: ";
  notes.appendChild(label);
  latest.forEach((item, index) => {
    const link = document.createElement("a");
    link.className = "research-link";
    link.href = documentLink(item.path);
    link.target = "_blank";
    link.rel = "noreferrer";
    link.textContent = `${item.ticker} ${item.kind}`;
    notes.appendChild(link);
    if (index < latest.length - 1) notes.appendChild(document.createTextNode(" · "));
  });
}

function renderWatchlist(portfolio) {
  const list = $("#watch-list");
  list.replaceChildren();
  const watch = portfolio.decisions.filter((decision) => ["AMRZ", "MLM", "PCG", "MSTR", "RBLX"].includes(decision.ticker));
  watch.slice(0, 5).forEach((decision) => {
    const item = document.createElement("article");
    item.className = "watch-item";
    item.innerHTML = `<div class="watch-title"><strong></strong><span class="watch-pill">watch</span></div><p></p>`;
    item.querySelector("strong").textContent = decision.ticker;
    item.querySelector("p").textContent = decision.short;
    list.appendChild(item);
  });
}

function renderGhosts(data) {
  const rows = data.ghosts.rows || [];
  setText("#ghost-count", rows.length || data.portfolio.ghostCount || "0");
  setSource("#ghost-source", data.ghosts.source);
  const list = $("#ghost-list");
  list.replaceChildren();
  rows.slice(-4).reverse().forEach((ghost) => {
    const item = document.createElement("article");
    item.className = "ghost-item";
    item.innerHTML = `<div><strong></strong><p></p></div><span class="ghost-status"></span>`;
    item.querySelector("strong").textContent = ghost.Ticker || "—";
    item.querySelector("p").textContent = ghost["Real path"] || ghost["Next checkpoint"] || "Active comparison";
    item.querySelector(".ghost-status").textContent = ghost.Status || "active";
    list.appendChild(item);
  });
}

function renderLessons(data) {
  $("#lesson-content").innerHTML = data.lessons.html || "<p>No lessons recorded yet.</p>";
  setSource("#lessons-source", data.lessons.source);
}

function renderActivity(data) {
  const list = $("#activity-list");
  list.replaceChildren();
  data.logs.forEach((log) => {
    const item = document.createElement("article");
    item.className = "activity-item";
    item.innerHTML = `<span class="activity-date"></span><p></p><div class="activity-headings"></div><a class="text-link" target="_blank" rel="noreferrer">Open full log ↗</a>`;
    item.querySelector(".activity-date").textContent = log.label;
    item.querySelector("p").textContent = log.preview;
    const tags = item.querySelector(".activity-headings");
    log.headings.forEach((heading) => {
      const tag = document.createElement("span");
      tag.className = "activity-tag";
      tag.textContent = heading.replace(/\s+—.*$/, "");
      tags.appendChild(tag);
    });
    item.querySelector("a").href = documentLink(log.path);
    list.appendChild(item);
  });
  setText("#footer-generated", `Loaded from memory · ${data.generatedAt}`);
}

function render(data) {
  state.data = data;
  renderSummary(data);
  renderPortfolio(data.portfolio);
  renderDecisions(data.portfolio);
  renderResearch(data);
  renderWatchlist(data.portfolio);
  renderGhosts(data);
  renderLessons(data);
  renderActivity(data);
  $("#loading-state").classList.add("is-hidden");
  $("#error-state").classList.add("is-hidden");
  $("#dashboard-content").classList.remove("is-hidden");
}

async function loadDashboard() {
  $("#loading-state").classList.remove("is-hidden");
  $("#error-state").classList.add("is-hidden");
  try {
    const response = await fetch(`/api/dashboard?ts=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`Dashboard request failed: ${response.status}`);
    render(await response.json());
  } catch (error) {
    console.error(error);
    $("#loading-state").classList.add("is-hidden");
    $("#dashboard-content").classList.add("is-hidden");
    $("#error-state").classList.remove("is-hidden");
  }
}

document.querySelectorAll("[data-research-tab]").forEach((tab) => {
  tab.addEventListener("click", () => {
    state.activeResearchTab = tab.dataset.researchTab;
    document.querySelectorAll("[data-research-tab]").forEach((other) => {
      const active = other === tab;
      other.classList.toggle("active", active);
      other.setAttribute("aria-selected", String(active));
    });
    if (state.data) renderResearch(state.data);
  });
});

$("#refresh-button").addEventListener("click", loadDashboard);
$("#retry-button").addEventListener("click", loadDashboard);
loadDashboard();
