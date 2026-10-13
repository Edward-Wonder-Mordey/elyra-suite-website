// Analytics-ready hook. No tracking is loaded until a real measurement ID is added.
const ELYRA_ANALYTICS_ID = window.ELYRA_CONFIG?.gaMeasurementId || '';

if (ELYRA_ANALYTICS_ID) {
  const s = document.createElement('script');
  s.async = true;
  s.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(ELYRA_ANALYTICS_ID)}`;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', ELYRA_ANALYTICS_ID, { anonymize_ip: true });

  const trackPage = () => window.gtag('event', 'page_view', {
    page_title: document.title,
    page_location: location.href,
    page_path: location.hash || '#/home'
  });

  window.addEventListener('hashchange', trackPage);
}
