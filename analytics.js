(function () {
  "use strict";

  if (location.hostname !== "coderdreamworld.github.io" ||
      !location.pathname.startsWith("/hanzi-cards/")) return;

  var ID = "G-V23C1X2DQX";

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

  start();
  window.addEventListener("pageshow", function (event) {
    if (event.persisted && window.gtag) {
      window.gtag("event", "page_view", Object.assign({ send_to: ID }, pageDetails()));
    }
  });
})();
