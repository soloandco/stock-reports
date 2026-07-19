// 테마(라이트/다크) 전환을 헤더 → 햄버거 드로어로 이동.
// 헤더는 로고(제목)·검색·햄버거만 남긴다 (2026-07-19 사용자 요청).
// 팔레트 토글은 label[for="__palette_N"]이라 DOM 어디로 옮겨도 체크박스와
// 연결이 유지된다 — Material의 팔레트 스크립트도 id로 접근하므로 영향 없음.
document$.subscribe(function () {
  var option = document.querySelector(".md-header__option");   // 팔레트 토글 묶음
  var navList = document.querySelector(
    ".md-sidebar--primary .md-nav--primary > .md-nav__list");
  if (!option || !navList) return;
  if (option.closest(".md-nav__list")) return;   // 같은 페이지에서 재실행됨

  var li = document.createElement("li");
  li.className = "md-nav__item sa-theme-item";

  var label = document.createElement("span");
  label.className = "sa-theme-label";
  label.textContent = "테마";

  li.appendChild(label);
  li.appendChild(option);        // 헤더에서 떼어내 드로어로 이동
  navList.appendChild(li);
});
