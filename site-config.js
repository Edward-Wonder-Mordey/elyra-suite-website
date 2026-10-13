// Elyra Suite public runtime configuration.
// Keep secrets out of this file: everything here is delivered to the browser.
window.ELYRA_CONFIG = {
  siteBaseUrl: 'https://edward-wonder-mordey.github.io/elyra-suite-website/',
  gaMeasurementId: '',
  eragonovaPartnerUrl: 'https://eragonova.com',
  social: {
    instagram: '',
    facebook: '',
    tiktok: '',
    youtube: ''
  }
};

// Keep the independent strategic-partner link current without duplicating it
// throughout the page modules.
if (typeof ERAGONOVA !== 'undefined' && window.ELYRA_CONFIG.eragonovaPartnerUrl) {
  ERAGONOVA.site = window.ELYRA_CONFIG.eragonovaPartnerUrl;
}
