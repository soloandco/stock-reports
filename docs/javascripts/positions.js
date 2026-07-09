// 오픈 포지션 — 시드 입력 → 종목별 주수·손익(원) + 포트폴리오 요약 실시간 계산.
// 시드는 localStorage(브라우저)에만 저장되며 서버·공개 저장소로 전송되지 않는다.
// 계산: 트레이드당 리스크 고정 % (1R = 시드 × 리스크%). instant navigation 대응(document$).
document$.subscribe(function () {
  var dataEl = document.getElementById("pos-data");
  var seedEl = document.getElementById("seed-input");
  var riskEl = document.getElementById("risk-input");
  var sumEl  = document.getElementById("seed-summary");
  if (!dataEl || !seedEl || !riskEl) return;   // 포지션 페이지 아님

  var positions;
  try { positions = JSON.parse(dataEl.textContent); } catch (e) { return; }

  // ── 순수 계산 ────────────────────────────────────────────────────────
  // seed·riskPct·entry·stop·current → {shares, invested, pnl, riskAmt}
  function computeRow(seed, riskPct, entry, stop, current) {
    var oneR = seed * riskPct / 100;
    var perShareRisk = entry - stop;
    if (seed <= 0 || riskPct <= 0 || perShareRisk <= 0) {
      return { shares: 0, invested: 0, pnl: 0, riskAmt: 0 };
    }
    var shares = Math.floor(oneR / perShareRisk);
    return {
      shares:   shares,
      invested: shares * entry,
      pnl:      shares * (current - entry),
      riskAmt:  shares * perShareRisk,
    };
  }

  function won(v) {
    var sign = v < 0 ? "-" : "";
    return sign + "₩" + Math.round(Math.abs(v)).toLocaleString("ko-KR");
  }

  // ── 렌더 ─────────────────────────────────────────────────────────────
  function render() {
    var seed = parseFloat(seedEl.value) || 0;
    var risk = parseFloat(riskEl.value) || 0;
    localStorage.setItem("sa_seed", seedEl.value);
    localStorage.setItem("sa_risk", riskEl.value);

    var totPnl = 0, totInvested = 0, totRisk = 0, active = 0;

    positions.forEach(function (p) {
      var r = computeRow(seed, risk, p.entry, p.stop, p.current);
      var shEl = document.querySelector('.js-shares[data-ticker="' + p.ticker + '"]');
      var plEl = document.querySelector('.js-pnl[data-ticker="' + p.ticker + '"]');
      if (seed <= 0) {
        if (shEl) shEl.textContent = "—";
        if (plEl) plEl.textContent = "—";
        return;
      }
      if (shEl) shEl.textContent = r.shares.toLocaleString("ko-KR") + "주";
      if (plEl) {
        plEl.textContent = won(r.pnl);
        plEl.style.color = r.pnl > 0 ? "#26a69a" : (r.pnl < 0 ? "#ef5350" : "");
      }
      totPnl += r.pnl; totInvested += r.invested; totRisk += r.riskAmt;
      if (r.shares > 0) active++;
    });

    if (!sumEl) return;
    if (seed <= 0) { sumEl.innerHTML = ""; return; }
    var oneR = seed * risk / 100;
    var pnlColor = totPnl > 0 ? "#26a69a" : (totPnl < 0 ? "#ef5350" : "inherit");
    sumEl.innerHTML =
      '<table class="seed-summary-table"><tbody>' +
      '<tr><th>트레이드당 리스크 (1R)</th><td>' + won(oneR) + '</td></tr>' +
      '<tr><th>체결 가능 포지션</th><td>' + active + ' / ' + positions.length + '</td></tr>' +
      '<tr><th>총 투입 원금</th><td>' + won(totInvested) + '</td></tr>' +
      '<tr><th>총 감수 리스크</th><td>' + won(totRisk) +
        ' <span style="opacity:.6">(시드의 ' + (seed > 0 ? (totRisk / seed * 100).toFixed(1) : 0) + '%)</span></td></tr>' +
      '<tr><th>총 미실현 손익</th><td style="color:' + pnlColor + ';font-weight:700">' + won(totPnl) + '</td></tr>' +
      '</tbody></table>';
  }

  // ── 초기값 복원 + 이벤트 ─────────────────────────────────────────────
  var savedSeed = localStorage.getItem("sa_seed");
  var savedRisk = localStorage.getItem("sa_risk");
  if (savedSeed !== null) seedEl.value = savedSeed;
  if (savedRisk !== null && savedRisk !== "") riskEl.value = savedRisk;

  seedEl.addEventListener("input", render);
  riskEl.addEventListener("input", render);
  render();
});
