/* 모바일 개편 (2026-09-23) — 아래쪽 탭 표시 · 관찰 목록 판정 칩.
 *
 * 탭: Material 인스턴트 이동은 페이지 본문만 갈아끼워 탭 표시가 옛 페이지에 남을 수
 *     있다. 이동할 때마다 주소로 지금 탭을 다시 맞춘다.
 * 칩: 줄의 data-f 와 칩의 data-f 가 같으면 보인다. 주소 끝이 #buy 면 매수 칩이 켜진
 *     채로 열린다(홈의 「이미 지난 신호」 줄). 페이지 안에 id="buy" 요소는 없다 —
 *     있으면 브라우저가 그 요소로 먼저 스크롤한다(rules/common/screen-layout.md).
 */
(function () {
  "use strict";

  function markTab() {
    var tabs = document.querySelectorAll(".m-tab[data-tab]");
    if (!tabs.length) return;
    var root = new URL(tabs[0].getAttribute("href"), location.href).pathname;   // 사이트 뿌리
    var rel = location.pathname.indexOf(root) === 0 ? location.pathname.slice(root.length) : "";
    tabs.forEach(function (a) {
      var key = a.getAttribute("data-tab");
      var on = key === "" ? rel === "" || rel === "index.html" : rel.indexOf(key) === 0;
      if (on) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
  }

  function initChips() {
    var bar = document.getElementById("wl-chips");
    var list = document.getElementById("wl-list");
    if (!bar || !list || bar.dataset.ready) return;
    bar.dataset.ready = "1";
    var chips = bar.querySelectorAll(".wl-chip");
    var rows = list.querySelectorAll(".wl-row");

    function apply(f) {
      chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c.dataset.f === f)); });
      rows.forEach(function (r) { r.hidden = f !== "all" && r.dataset.f !== f; });
      list.dataset.active = f;
    }
    chips.forEach(function (c) {
      c.addEventListener("click", function () { apply(c.dataset.f); });
    });
    if (location.hash === "#buy" && bar.querySelector('[data-f="buy"]')) apply("buy");
  }

  function boot() { markTab(); initChips(); }

  if (window.document$ && window.document$.subscribe) {
    window.document$.subscribe(boot);
  } else {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
