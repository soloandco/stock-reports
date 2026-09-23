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
    trend: "#8a63d2",
    stop: "#c62828"
  };

  /* 수급 누적선은 신호가 아니라 배경 정보다. 매물벽(주황)·지지대(초록)·
     추세선(보라)과 겹치지 않는 청록으로 두고, 아래 별도 칸에만 그린다. */
  function cvdColor() { return isDark() ? "#3fc9c5" : "#0f8f8c"; }

  /* 수급선은 **차트를 하나 더 쌓아서** 그린다. 같은 칸에 넣고 가격축 여백만
     비우면 그 빈 칸까지 가격축이 눈금을 이어 붙여 없는 가격이 찍힌다
     (2026-09-04 실측: 삼성전기 차트에 0·−400·−800원). 축을 나누면 사라진다.

     높이는 가격 300 + 수급 100 = 400px. 시간축(날짜)이 아래 칸으로 내려가
     가격 그림 영역은 지금(320px에서 시간축을 뺀 약 298px)과 거의 같다.
     캔들을 눌러 넣지 않는다 — 폰에서 값이 안 읽힌다(2026-08-29 매물대 사고). */
  var CVD_MAIN_H = 300;
  var CVD_PANE_H = 100;

  /* 물린 비율 칸 (2026-09-14). 최근 1년 거래량 중 현재가보다 비싸게 거래된
     비중(0~100%). 사용자의 「싸다·비싸다고 느끼는 자리」를 선이 아니라 날마다
     하나의 숫자로 옮긴 것이다. 측정(docs/measure-2026-09-14-underwater-ratio.md,
     11년 620종목)에서 **가격 위치와 구분되지 않았고** 앞으로의 수익을 가르지
     못했다 — 표시용이다. 매물대(주황·초록)·수급(청록)과 구분되는 갈색 계열. */
  var UW_PANE_H = 90;
  function uwColor() { return isDark() ? "#d1a35a" : "#9a6b1f"; }

  /* 값이 없는 종목이 있다(거래량 미제공 등). 그럴 땐 아무것도 그리지 않고
     차트 높이도 지금 그대로 둔다. */
  function cvdPoints(data) {
    var raw = data.cvd;
    if (!raw || raw.length !== data.bars.length) return null;
    var pts = [];
    for (var i = 0; i < raw.length; i++) {
      if (raw[i] === null || raw[i] === undefined) continue;
      pts.push({ time: data.bars[i][0], value: raw[i] });
    }
    return pts.length >= 2 ? pts : null;
  }

  function uwPoints(data) {
    var raw = data.underwater;
    if (!raw || raw.length !== data.bars.length) return null;
    var pts = [];
    for (var i = 0; i < raw.length; i++) {
      if (raw[i] === null || raw[i] === undefined) continue;
      pts.push({ time: data.bars[i][0], value: raw[i] });
    }
    return pts.length >= 2 ? pts : null;
  }

  /* 이동평균 50·150·200 = 이 시스템의 Trend Template 판정 근거. 신호선
     (매물벽 주황·지지대 초록·추세선 보라)과 경쟁하지 않게 무채색 계열로 둔다.
     기간이 길수록 진하게 — 장기선이 눈에 먼저 들어와야 국면이 읽힌다. */
  var MA_PERIODS = ["20", "50", "150", "200"];
  var MA_LABEL = {
    // 관습적 이름(단기·중기·장기) 대신 **역할**을 적는다 (2026-08-30 사용자 결정).
    // 50·150·200은 Trend Template 8조건이 실제로 쓰는 선이고 20일선은 참고선이다.
    // 화면 어휘와 전략 어휘가 따로 놀면 "기준을 바꿨냐"는 혼동이 난다.
    "20": "20일선(참고)", "50": "50일선(판정)",
    "150": "150일선(판정)", "200": "200일선(판정)"
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
    var cvd = cvdPoints(data), uw = uwPoints(data);
    var hasSub = !!(cvd || uw);
    // 아래 칸이 있을 때만 손댄다 — 없는 종목의 차트는 지금과 똑같이 남는다.
    if (hasSub) host.style.height = CVD_MAIN_H + "px";
    var chart = LightweightCharts.createChart(host, {
      layout: { background: { color: t.bg }, textColor: t.text, fontSize: 11 },
      grid: { vertLines: { color: t.grid }, horzLines: { color: t.grid } },
      rightPriceScale: { borderVisible: false, scaleMargins: { top: 0.12, bottom: 0.12 } },
      // 아래 칸이 붙으면 날짜는 맨 아래 칸에서 한 번만 보여 준다.
      timeScale: { borderVisible: false, fixLeftEdge: true, fixRightEdge: true,
                   visible: !hasSub },
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

    /* 폰에서 선이 7~8개 겹쳐 읽기 어려웠다(2026-09-23 모바일 개편). 처음에는 현재가 ·
       손절 · 주봉 저항만 보이고, 나머지(이평선·매물대·추세선)는 「선 더 보기」로 켠다. */
    var extras = [];
    var isExtraLine = function (line) { return line.id !== "auto:weekly-resistance"; };

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
        extras.push({ series: s2 });
      });
    }

    var first = data.bars[0][0], last = data.bars[data.bars.length - 1][0];
    (data.lines || []).forEach(function (line) {
      var color = COLORS[line.side] || COLORS.resistance;
      if (line.kind === "level") {
        // 축에는 값만 남긴다. 이름까지 넣으면 폰 폭(가격축 약 50px)에서 잘려
        // 정작 숫자가 안 보였다(2026-08-29 실측). 이름은 아래 범례가 맡는다.
        var pl = candles.createPriceLine({
          price: line.price, color: color, lineWidth: 1,
          lineStyle: LightweightCharts.LineStyle.Solid,
          axisLabelVisible: true, title: ""
        });
        if (isExtraLine(line)) extras.push({ priceLine: pl });
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
        extras.push({ series: s });
      }
    });

    // 손절선 — 매수 상태일 때만 페이지가 data-stop 으로 넘긴다 (알림과 같은 진입 손절)
    var stop = parseFloat(host.getAttribute("data-stop"));
    if (isFinite(stop) && stop > 0) {
      candles.createPriceLine({
        price: stop, color: COLORS.stop, lineWidth: 1,
        lineStyle: LightweightCharts.LineStyle.Dashed,
        axisLabelVisible: true, title: ""
      });
    }

    chart.timeScale().fitContent();
    // 위에서 클래스를 붙이기 전(Material CSS가 살아 있던 순간)에 잡힌 셀 폭이
    // 남아 가격축이 0px로 눌린다. 강제로 다시 재게 한다.
    chart.resize(host.clientWidth, host.clientHeight, true);
    host.removeAttribute("data-loading");
    // 아래 칸들. 시간축(날짜)은 맨 아래 칸에만 둔다. 확대·이동은 전부 함께 움직인다.
    var sync = { charts: [chart], lock: false };
    var anchor = host, panes = [];
    if (cvd) {
      var cp = buildSubPane(anchor, sync, cvd, {
        className: "stock-chart-cvd", height: CVD_PANE_H, color: cvdColor(),
        showTime: !uw
      });
      panes.push({ kind: "cvd", host: cp.host, chart: cp.chart, series: cp.series,
                   colorFn: cvdColor, dot: ".stock-chart-dot--cvd" });
      anchor = cp.host;
    }
    if (uw) {
      var up = buildSubPane(anchor, sync, uw, {
        className: "stock-chart-underwater", height: UW_PANE_H, color: uwColor(),
        showTime: true, fixedRange: [0, 100]
      });
      panes.push({ kind: "uw", host: up.host, chart: up.chart, series: up.series,
                   colorFn: uwColor, dot: ".stock-chart-dot--uw" });
      anchor = up.host;
    }
    var legend = buildLegend(host, anchor, data.lines || [], Object.keys(maSeries), !!cvd,
                             uw ? uw[uw.length - 1].value : null,
                             isFinite(stop) && stop > 0, isExtraLine);
    buildControls(host, chart, data.bars.length, extras, legend);
    return { chart: chart, maSeries: maSeries, panes: panes };
  }


  /* 아래 칸 — 가격 차트 아래에 별도 차트를 쌓고 시간축을 묶는다.
     v4에는 한 차트 안에 칸을 나누는 기능이 없다(v5부터). 축을 공유하면
     가격축이 빈 칸까지 눈금을 이어 붙여 없는 가격을 찍는다.
     수급 누적(2026-09-04)과 물린 비율(2026-09-14)이 같은 함수를 쓴다.
     opts: className · height · color · showTime(맨 아래 칸만 true) ·
           fixedRange([min,max], 물린 비율은 0~100 고정 — 종목 간 비교가 되게) */
  function buildSubPane(anchor, sync, points, opts) {
    var t = theme();
    var mainChart = sync.charts[0];
    var el = document.createElement("div");
    el.className = "stock-chart-sub " + opts.className;
    el.style.height = opts.height + "px";
    el.style.width = "100%";
    anchor.parentNode.insertBefore(el, anchor.nextSibling);

    /* 위 차트의 **그림 영역**과 같은 폭으로 그린다. 위 차트는 오른쪽
       가격축(라벨 길이에 따라 50~90px)만큼 그림이 좁다. 그 폭을 빼지 않으면
       같은 날짜가 두 칸에서 다른 x에 찍힌다 (2026-09-04 실측: 위 282px,
       아래 342px). 폭을 못 재면 전체 폭으로 두고 그림은 그대로 낸다. */
    var plotWidth = function () {
      var full = el.clientWidth;
      try {
        var axis = mainChart.priceScale("right").width();
        return axis > 0 && axis < full ? full - axis : full;
      } catch (e) {
        return full;
      }
    };

    var sub = LightweightCharts.createChart(el, {
      // 라이브러리 로고는 위 차트에 이미 하나 있다 — 같은 그림에 둘은 군더더기.
      layout: { background: { color: t.bg }, textColor: t.text, fontSize: 11,
                attributionLogo: false },
      grid: { vertLines: { color: t.grid }, horzLines: { color: "transparent" } },
      // 축 자체를 없앤다. 값의 뜻은 아래 범례가 맡는다(물린 비율은 마지막 값 %).
      // 대신 아래에서 캔버스 폭을 위 차트의 그림 영역에 맞춘다.
      rightPriceScale: { visible: false },
      timeScale: { borderVisible: false, fixLeftEdge: true, fixRightEdge: true,
                   visible: !!opts.showTime },
      crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
      handleScale: { axisPressedMouseMove: false },
      localization: { locale: "ko-KR" },
      width: plotWidth(), height: el.clientHeight
    });
    el.querySelectorAll("table").forEach(function (x) {
      x.classList.add("lwc-internal");     // 위 차트와 같은 이유(Material 표 규칙)
    });

    var seriesOpts = {
      color: opts.color, lineWidth: 2,
      lastValueVisible: false, priceLineVisible: false,
      crosshairMarkerVisible: false
    };
    if (opts.fixedRange) {
      seriesOpts.autoscaleInfoProvider = function () {
        return { priceRange: { minValue: opts.fixedRange[0], maxValue: opts.fixedRange[1] } };
      };
    }
    var series = sub.addLineSeries(seriesOpts);
    series.setData(points);
    sub.timeScale().fitContent();

    var syncWidth = function () {
      sub.applyOptions({ width: plotWidth(), height: el.clientHeight });
    };

    // 확대·이동을 모든 칸이 함께 움직인다. 서로를 다시 부르지 않게 잠금 하나를 공유한다.
    sync.charts.push(sub);
    sub.timeScale().subscribeVisibleLogicalRangeChange(function (range) {
      broadcast(sync, sub, range);
    });
    if (sync.charts.length === 2) {          // 첫 아래 칸이 위 차트의 구독을 건다
      mainChart.timeScale().subscribeVisibleLogicalRangeChange(function (range) {
        broadcast(sync, mainChart, range);
      });
    }

    if (window.ResizeObserver) {
      new ResizeObserver(syncWidth).observe(el);
    }
    return { host: el, chart: sub, series: series };
  }

  function broadcast(sync, from, range) {
    if (sync.lock || !range) return;
    sync.lock = true;
    try {
      sync.charts.forEach(function (c) {
        if (c !== from) c.timeScale().setVisibleLogicalRange(range);
      });
    } finally { sync.lock = false; }
  }

  /* 선 이름은 차트 밖 글자로 둔다 — 캔버스 안 라벨은 폰에서 잘리고 확대도 안 된다.
     여기서는 구간 표기("매물벽 70.65~75.38")를 그대로 보여줄 수 있다. */
  function buildLegend(host, anchor, lines, maKeys, hasCvd, uwLast, hasStop, isExtraLine) {
    var hasUw = uwLast !== null && uwLast !== undefined;
    if (!lines.length && !(maKeys || []).length && !hasCvd && !hasUw && !hasStop) return null;
    var ul = document.createElement("ul");
    ul.className = "stock-chart-legend";
    ul.setAttribute("data-extra", "off");
    var add = function (color, text, extraClass, isExtra) {
      var li = document.createElement("li");
      if (isExtra) li.className = "is-extra";
      var dot = document.createElement("span");
      dot.className = "stock-chart-dot" + (extraClass ? " " + extraClass : "");
      dot.style.background = color;
      li.appendChild(dot);
      li.appendChild(document.createTextNode(text));
      ul.appendChild(li);
    };
    var mc = maColors();
    (maKeys || []).forEach(function (p) { add(mc[p], MA_LABEL[p] || (p + "일선"), "", true); });
    lines.forEach(function (line) {
      add(line.kind === "trend" ? COLORS.trend
                                : (COLORS[line.side] || COLORS.resistance),
          line.label || "", "", isExtraLine(line));
    });
    if (hasStop) add(COLORS.stop, "손절", "", false);
    // 이름을 "CVD"로 적지 않는다 — 진짜 CVD는 체결 단위로 세는 것이고
    // 이건 봉의 종가 위치로 만든 근사다. 무엇으로 만들었는지 화면에 밝힌다.
    if (hasCvd) add(cvdColor(), "수급 누적(종가 위치 추정)", "stock-chart-dot--cvd");
    // 마지막 값을 범례에 적는다. 칸의 축을 지웠으니 숫자는 여기서 읽는다.
    // 「가격 위치와 구분 안 됨」은 측정 결과(2026-09-14)다. 지우려면 재측정이 먼저.
    if (hasUw) add(uwColor(), "물린 비율 " + Math.round(uwLast) + "% (1년 거래량 기준 · 가격 위치와 구분 안 됨)",
                   "stock-chart-dot--uw");
    anchor.parentNode.insertBefore(ul, anchor.nextSibling);
    return ul;
  }

  /* 차트 위 버튼 줄: 기간(최근 1개월 · 3개월 · 전체)과 「선 더 보기」.
     기간은 가격 칸만 옮기면 아래 칸들이 따라온다(시간축이 묶여 있다). */
  function buildControls(host, chart, nBars, extras, legend) {
    var bar = document.createElement("div");
    bar.className = "stock-chart-ctrl";
    var ranges = [["1개월", 21], ["3개월", 63], ["전체", 0]];
    var rangeBtns = ranges.map(function (r) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = r[0];
      b.setAttribute("aria-pressed", String(r[1] === 0));
      b.addEventListener("click", function () {
        rangeBtns.forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        if (!r[1] || r[1] >= nBars) chart.timeScale().fitContent();
        else chart.timeScale().setVisibleLogicalRange({ from: nBars - r[1], to: nBars - 0.5 });
      });
      bar.appendChild(b);
      return b;
    });
    if (extras.length) {
      var more = document.createElement("button");
      more.type = "button";
      more.className = "sc-lines";
      var setShown = function (on) {
        extras.forEach(function (e) {
          if (e.series) e.series.applyOptions({ visible: on });
          if (e.priceLine) e.priceLine.applyOptions({ lineVisible: on, axisLabelVisible: on });
        });
        if (legend) legend.setAttribute("data-extra", on ? "on" : "off");
        more.setAttribute("aria-pressed", String(on));
        more.textContent = on ? "선 줄이기" : "선 더 보기 (" + extras.length + ")";
      };
      more.addEventListener("click", function () {
        setShown(more.getAttribute("aria-pressed") !== "true");
      });
      bar.appendChild(more);
      setShown(false);
    }
    host.parentNode.insertBefore(bar, host);
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
            (made.panes || []).forEach(function (p) {
              p.series.applyOptions({ color: p.colorFn() });
              p.chart.applyOptions({
                layout: { background: { color: t.bg }, textColor: t.text },
                grid: { vertLines: { color: t.grid },
                        horzLines: { color: "transparent" } }
              });
              var pdot = host.parentNode.querySelector(p.dot);
              if (pdot) pdot.style.background = p.colorFn();
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
