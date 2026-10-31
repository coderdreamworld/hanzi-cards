(function () {
  "use strict";

  if (location.hostname !== "coderdreamworld.github.io" ||
      !location.pathname.startsWith("/hanzi-cards/")) return;

  var ID = "G-V23C1X2DQX";
  var KEY = "hz.analytics.consent.v1";
  var choice;
  try { choice = localStorage.getItem(KEY); } catch (e) {}

  function pageDetails() {
    var details = { page_location: location.origin + location.pathname };
    if (document.referrer) {
      try {
        var referrer = new URL(document.referrer);
        details.page_referrer = referrer.origin + referrer.pathname;
      } catch (e) {}
    }
    return details;
  }

  function start() {
    if (window.hzAnalyticsStarted) return;
    window.hzAnalyticsStarted = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("consent", "default", {
      analytics_storage: "granted",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied"
    });
    window.gtag("js", new Date());
    window.gtag("config", ID, Object.assign({
      allow_google_signals: false,
      allow_ad_personalization_signals: false
    }, pageDetails()));
    var script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + ID;
    document.head.appendChild(script);
  }

  function save(value) {
    choice = value;
    try { localStorage.setItem(KEY, value); } catch (e) {}
  }

  function ensureStyle() {
    if (document.getElementById("hz-analytics-style")) return;
    var style = document.createElement("style");
    style.id = "hz-analytics-style";
    style.textContent = "#hz-analytics-choice{position:fixed;z-index:10000;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom));max-width:520px;max-height:calc(100dvh - 24px);overflow:auto;margin:auto;padding:14px 16px;background:#fffdf7;color:#4a3226;border:1px solid #eadfca;border-radius:14px;box-shadow:0 8px 28px #4a322633;font:13px/1.5 system-ui,-apple-system,'PingFang SC',sans-serif}#hz-analytics-choice p{margin:0 0 10px}#hz-analytics-choice a{color:#28796e}#hz-analytics-choice .actions{display:flex;justify-content:flex-end;gap:8px}#hz-analytics-choice button{min-height:40px;padding:6px 12px;border:1px solid #d9cab4;border-radius:8px;background:#fff;color:#4a3226;font:inherit;cursor:pointer}#hz-analytics-choice button[data-choice=yes]{background:#dff3ef;border-color:#9bcfc3}#hz-analytics-settings{margin:14px 0 0;padding:6px;border:0;background:transparent;color:#786c64;font:12px system-ui,-apple-system,'PingFang SC',sans-serif;text-decoration:underline;cursor:pointer}";
    document.head.appendChild(style);
  }

  function showChoice() {
    if (document.getElementById("hz-analytics-choice")) return;
    ensureStyle();
    var notice = document.createElement("aside");
    notice.id = "hz-analytics-choice";
    notice.setAttribute("aria-label", "访问统计选择");
    notice.innerHTML = '<p>请由家长选择：本站仅在同意后使用 Google Analytics 记录访问页面、设备类别及大致地区，并使用 Cookie 区分访客。不传送孩子的卡片进度。不同意也能正常使用。<a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer">了解 Google 如何处理信息</a></p><div class="actions"><button type="button" data-choice="no">暂不统计</button><button type="button" data-choice="yes">家长同意统计</button></div>';
    notice.querySelector('[data-choice="no"]').addEventListener("click", function () {
      save("no");
      notice.remove();
      if (window.hzAnalyticsStarted) location.reload();
    });
    notice.querySelector('[data-choice="yes"]').addEventListener("click", function () {
      save("yes");
      notice.remove();
      start();
    });
    document.body.appendChild(notice);
  }

  function init() {
    ensureStyle();
    if (choice === "yes") start();
    else if (choice !== "no") showChoice();
    if (location.pathname === "/hanzi-cards/" ||
        location.pathname === "/hanzi-cards/index.html") {
      var settings = document.createElement("button");
      settings.id = "hz-analytics-settings";
      settings.type = "button";
      settings.textContent = "隐私与统计设置";
      settings.addEventListener("click", showChoice);
      document.body.appendChild(settings);
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
  window.addEventListener("pageshow", function (event) {
    if (event.persisted && choice === "yes" && window.gtag) {
      window.gtag("event", "page_view", Object.assign({ send_to: ID }, pageDetails()));
    }
  });
})();
