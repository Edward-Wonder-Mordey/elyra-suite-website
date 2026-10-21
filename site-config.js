// Elyra Suite public runtime configuration.
// Keep secrets out of this file: everything here is delivered to the browser.
window.ELYRA_CONFIG = {
  siteBaseUrl: 'https://edward-wonder-mordey.github.io/elyra-suite-website/',
  gaMeasurementId: 'G-3ECH94LV1S',
  eragonovaPartnerUrl: 'https://eragonova.com',
  supabaseUrl: 'https://kqpbdagawllgonzoloao.supabase.co',
  supabasePublishableKey: 'sb_publishable_cJ2zfuTbR-MkIJfDeTld6w_u5ioOpIN',
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
