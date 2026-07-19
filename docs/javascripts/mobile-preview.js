// 모바일 미리보기 토글 — PC에서 본문을 폰 폭으로 좁혀 본다.
// 선택은 localStorage에 기억되고, instant navigation(document$)에도 유지된다.
// 컨테이너 폭만 바꾸는 근사치 — 반응형 전환까지 보려면 브라우저 기기 모드(F12).
document$.subscribe(function () {
  var KEY = "stock-agent:mobile-preview";
  var ON = "mobile-preview";

  function enabled() {
    try { return localStorage.getItem(KEY) === "1"; } catch (e) { return false; }
  }
  function save(v) {
    try { localStorage.setItem(KEY, v ? "1" : "0"); } catch (e) { /* 무시 */ }
  }
  function apply(on, btn) {
    document.body.classList.toggle(ON, on);
    if (btn) {
      btn.classList.toggle("mp-active", on);
      btn.title = on ? "모바일 미리보기 끄기" : "모바일 미리보기 (본문을 폰 폭으로)";
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    }
  }

  // 저장된 상태를 먼저 반영 — 버튼 주입 실패해도 폭은 유지된다
  apply(enabled(), null);

  var header = document.querySelector(".md-header__inner");
  if (!header) return;

  // instant navigation으로 헤더가 교체되면 버튼이 사라지므로 매번 확인 후 주입
  var btn = header.querySelector(".mp-toggle");
  if (!btn) {
    btn = document.createElement("button");
    btn.type = "button";
    btn.className = "md-header__button md-icon mp-toggle";
    btn.textContent = "📱";
    btn.style.cursor = "pointer";
    btn.style.background = "none";
    btn.style.border = "none";
    btn.style.font = "inherit";
    btn.style.fontSize = "1.1rem";
    btn.addEventListener("click", function () {
      var next = !document.body.classList.contains(ON);
      apply(next, btn);
      save(next);
    });
    // 팔레트(다크모드) 토글 옆에 배치 — 없으면 헤더 끝에
    var palette = header.querySelector('[for^="__palette"]');
    if (palette && palette.parentNode === header) {
      header.insertBefore(btn, palette);
    } else {
      header.appendChild(btn);
    }
  }
  apply(enabled(), btn);
});
