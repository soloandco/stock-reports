/* 관찰 종목 페이지 캔들차트 — TradingView Lightweight Charts로 브라우저에서 그린다.
 *
 * 그림(PNG)을 커밋하지 않는 이유: 관찰 페이지는 48종목이고 매일 갱신돼서
 * 이미지로 올리면 한 번에 1.8MB씩 공개 저장소에 쌓인다(2026-08-29 실측).
 * 숫자 데이터(종목당 약 6KB)만 올리고 여기서 그린다. 덤으로 폰에서 글자가
 * 선명하고(래스터 축소가 없다) 손가락으로 확대·이동할 수 있다.
 *
 * 이 사이트는 폰 기준이다 — 본문 폭이 약 343px이라 높이·글자 크기를 그 폭에
 * 맞춰 잡았다. 바꾸기 전에 375px 뷰포트에서 확인할 것.
 */
(function () {
  "use strict";

  var COLORS = {
    up: "#d24b4b",          // 한국식 — 상승 적, 하락 청
    down: "#2f7ed8",
    resistance: "#e07b39",
    support: "#3aa76d",
    trend: "#8a63d2"
  };

  /* 이동평균 50·150·200 = 이 시스템의 Trend Template 판정 근거. 신호선
     (매물벽 주황·지지대 초록·추세선 보라)과 경쟁하지 않게 무채색 계열로 둔다.
     기간이 길수록 진하게 — 장기선이 눈에 먼저 들어와야 국면이 읽힌다. */
  var MA_PERIODS = ["20", "50", "150", "200"];
  var MA_LABEL = {
    "20": "20일선(단기)", "50": "50일선(중기)",
    "150": "150일선(장기)", "200": "200일선(대세)"
  };

  /* 50·150·200은 Trend Template 판정 근거라 뺄 수 없고, 20일선은 통상적인
     단기선이다. 기간이 길수록 진하게 — 장기선이 먼저 눈에 들어와야 국면이 읽힌다. */
  function maColors() {
    return isDark()
      ? { "20": "#464c53", "50": "#5f666e", "150": "#98a1aa", "200": "#dfe4e8" }
      : { "20": "#c2c8ce", "50": "#98a0a8", "150": "#6b737b", "200": "#2b3138" };
  }

  function isDark() {
    var s = document.body.getAttribute("data-md-color-scheme");
    return s === "slate";
  }

  function theme() {
    return isDark()
      ? { bg: "transparent", text: "#b9bfc7", grid: "rgba(255,255,255,0.07)" }
      : { bg: "transparent", text: "#4a5157", grid: "rgba(0,0,0,0.07)" };
  }

  /* 대각 추세선을 차트 폭 전체로 연장한다. 두 앵커만으로는 화면 좌우 끝까지
     닿지 않아 선이 공중에 떠 보인다. */
  function extendTrend(line, firstTime, lastTime) {
    var x0 = Date.parse(line.from[0]), x1 = Date.parse(line.to[0]);
    if (!isFinite(x0) || !isFinite(x1) || x1 === x0) return null;
    var slope = (line.to[1] - line.from[1]) / (x1 - x0);
    var at = function (t) { return line.from[1] + slope * (Date.parse(t) - x0); };
    var a = at(firstTime), b = at(lastTime);
    if (!isFinite(a) || !isFinite(b) || a <= 0 || b <= 0) return null;
    return [
      { time: firstTime, value: Math.round(a * 100) / 100 },
      { time: lastTime, value: Math.round(b * 100) / 100 }
    ];
  }

  function render(host, data) {
    if (!window.LightweightCharts) return fail(host, "차트 라이브러리를 불러오지 못했습니다.");
    var t = theme();
    var chart = LightweightCharts.createChart(host, {
      layout: { background: { color: t.bg }, textColor: t.text, fontSize: 11 },
      grid: { vertLines: { color: t.grid }, horzLines: { color: t.grid } },
      rightPriceScale: { borderVisible: false, scaleMargins: { top: 0.12, bottom: 0.12 } },
      timeScale: { borderVisible: false, fixLeftEdge: true, fixRightEdge: true },
      crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
      handleScale: { axisPressedMouseMove: false },
      localization: {
        locale: "ko-KR",
        priceFormatter: function (p) { return p.toLocaleString("ko-KR"); }
      },
      // autoSize를 쓰지 않는다: 컨테이너(343px)보다 44px 넓은 캔버스를 그려
      // 오른쪽 가격축 라벨이 잘렸다(2026-08-29 실측, x=403까지 뻗음).
      // 폭을 직접 주고 아래 ResizeObserver로 따라가게 한다.
      width: host.clientWidth,
      height: host.clientHeight
    });

    if (window.ResizeObserver) {
      new ResizeObserver(function () {
        chart.applyOptions({ width: host.clientWidth, height: host.clientHeight });
      }).observe(host);
    }

    /* 🚨 Material은 클래스 없는 표를 본문 표로 스타일링한다
       (.md-typeset table:not([class])). Lightweight Charts는 내부 레이아웃에
       <table>을 쓰므로 그 규칙에 걸려 display·테두리·min-width가 먹고 셀 배치가
       무너진다(2026-08-29 실측: 캔버스가 컨테이너 밖 44px). 클래스를 하나 붙이면
       선택자가 빗나가 간섭이 통째로 사라진다 — 이 사이트의 표 규칙과 같은 원리다. */
    host.querySelectorAll("table").forEach(function (t) {
      t.classList.add("lwc-internal");
    });

    var candles = chart.addCandlestickSeries({
      upColor: COLORS.up, downColor: COLORS.down,
      borderUpColor: COLORS.up, borderDownColor: COLORS.down,
      wickUpColor: COLORS.up, wickDownColor: COLORS.down
    });
    candles.setData(data.bars.map(function (b) {
      return { time: b[0], open: b[1], high: b[2], low: b[3], close: b[4] };
    }));

    // 이동평균 — 캔들 뒤에 깔리도록 먼저 그린다
    var maSeries = {};
    var mc = maColors();
    if (data.mas) {
      MA_PERIODS.forEach(function (period) {
        var vals = data.mas[period];
        if (!vals) return;
        var pts = [];
        for (var i = 0; i < vals.length; i++) {
          if (vals[i] === null || vals[i] === undefined) continue;
          pts.push({ time: data.bars[i][0], value: vals[i] });
        }
        if (pts.length < 2) return;          // 값이 없으면 선을 만들지 않는다
        var s2 = chart.addLineSeries({
          color: mc[period], lineWidth: 1,
          lastValueVisible: false, priceLineVisible: false,
          crosshairMarkerVisible: false
        });
        s2.setData(pts);
        maSeries[period] = s2;
      });
    }

    var first = data.bars[0][0], last = data.bars[data.bars.length - 1][0];
    (data.lines || []).forEach(function (line) {
      var color = COLORS[line.side] || COLORS.resistance;
      if (line.kind === "level") {
        // 축에는 값만 남긴다. 이름까지 넣으면 폰 폭(가격축 약 50px)에서 잘려
        // 정작 숫자가 안 보였다(2026-08-29 실측). 이름은 아래 범례가 맡는다.
        candles.createPriceLine({
          price: line.price, color: color, lineWidth: 1,
          lineStyle: LightweightCharts.LineStyle.Solid,
          axisLabelVisible: true, title: ""
        });
      } else if (line.kind === "trend") {
        var pts = extendTrend(line, first, last);
        if (!pts) return;
        var s = chart.addLineSeries({
          color: COLORS.trend, lineWidth: 2,
          lineStyle: LightweightCharts.LineStyle.Dashed,
          lastValueVisible: false, priceLineVisible: false,
          crosshairMarkerVisible: false
        });
        s.setData(pts);
      }
    });

    chart.timeScale().fitContent();
    // 위에서 클래스를 붙이기 전(Material CSS가 살아 있던 순간)에 잡힌 셀 폭이
    // 남아 가격축이 0px로 눌린다. 강제로 다시 재게 한다.
    chart.resize(host.clientWidth, host.clientHeight, true);
    host.removeAttribute("data-loading");
    buildLegend(host, data.lines || [], Object.keys(maSeries));
    return { chart: chart, maSeries: maSeries };
  }

  /* 선 이름은 차트 밖 글자로 둔다 — 캔버스 안 라벨은 폰에서 잘리고 확대도 안 된다.
     여기서는 구간 표기("매물벽 70.65~75.38")를 그대로 보여줄 수 있다. */
  function buildLegend(host, lines, maKeys) {
    if (!lines.length && !(maKeys || []).length) return;
    var ul = document.createElement("ul");
    ul.className = "stock-chart-legend";
    var add = function (color, text) {
      var li = document.createElement("li");
      var dot = document.createElement("span");
      dot.className = "stock-chart-dot";
      dot.style.background = color;
      li.appendChild(dot);
      li.appendChild(document.createTextNode(text));
      ul.appendChild(li);
    };
    var mc = maColors();
    (maKeys || []).forEach(function (p) { add(mc[p], MA_LABEL[p] || (p + "일선")); });
    lines.forEach(function (line) {
      add(line.kind === "trend" ? COLORS.trend
                                : (COLORS[line.side] || COLORS.resistance),
          line.label || "");
    });
    host.parentNode.insertBefore(ul, host.nextSibling);
  }

  function fail(host, msg) {
    host.removeAttribute("data-loading");
    host.textContent = msg;
    host.classList.add("stock-chart--failed");
  }

  function init(host) {
    var src = host.getAttribute("data-src");
    if (!src) return;
    host.setAttribute("data-loading", "1");
    fetch(src, { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        if (!data || !data.bars || !data.bars.length) {
          // 차트가 없다고 페이지를 망가뜨리지 않는다 — 자리만 비운다.
          host.remove();
          return;
        }
        var made = render(host, data);
        // 테마 전환(라이트↔다크)에 색을 따라가게 한다. 이평선은 무채색이라
        // 테마가 바뀌면 배경에 묻히므로 함께 갈아끼운다.
        if (made && made.chart && window.MutationObserver) {
          new MutationObserver(function () {
            var t = theme(), mc = maColors();
            made.chart.applyOptions({
              layout: { background: { color: t.bg }, textColor: t.text },
              grid: { vertLines: { color: t.grid }, horzLines: { color: t.grid } }
            });
            Object.keys(made.maSeries).forEach(function (p) {
              made.maSeries[p].applyOptions({ color: mc[p] });
            });
            host.parentNode.querySelectorAll(".stock-chart-legend .stock-chart-dot")
              .forEach(function (dot, i) {
                if (i < Object.keys(made.maSeries).length) {
                  dot.style.background = mc[Object.keys(made.maSeries)[i]];
                }
              });
          }).observe(document.body, { attributes: true,
                                      attributeFilter: ["data-md-color-scheme"] });
        }
      })
      .catch(function (e) {
        console.warn("stock-chart:", e);
        host.remove();   // 데이터를 못 받으면 조용히 사라진다(빈 상자 방지)
      });
  }

  function boot() {
    document.querySelectorAll(".stock-chart[data-src]").forEach(init);
  }

  if (window.document$ && window.document$.subscribe) {
    window.document$.subscribe(boot);   // Material 인스턴트 로딩 대응
  } else {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
