// Content-integrity notes for areas where availability, proof or programme details
// must be confirmed before they are presented as current commercial facts.
(function () {
  const notice = (title, body) => `<section class="section" style="padding-top:34px;padding-bottom:0"><div class="container"><div class="notice" style="max-width:980px;margin:0 auto"><strong style="display:block;color:var(--plum);margin-bottom:6px">${title}</strong>${body}</div></div></section>`;

  if (pages?.portfolio) {
    const original = pages.portfolio;
    pages.portfolio = function () {
      return original().replace(
        '<section class="section"><div class="container image-feature">',
        notice('About this showcase','The imagery on this page presents Elyra Suite service directions and brand presentation. Genuine client case studies, before-and-after work and testimonials are published only when suitable material and permission are available.') + '<section class="section"><div class="container image-feature">'
      );
    };
  }

  if (pages?.shop) {
    const original = pages.shop;
    pages.shop = function () {
      return original().replace(
        '<section class="section"><div class="container shop-showcase">',
        notice('Availability & pricing','Store categories show the types of products Elyra Suite can discuss. Current stock, specifications, colours, quantities, pricing, delivery and order terms are confirmed directly before purchase.') + '<section class="section"><div class="container shop-showcase">'
      );
    };
  }

  if (pages?.academy) {
    const original = pages.academy;
    pages.academy = function () {
      return original().replace(
        '<section class="section"><div class="container image-feature">',
        notice('Programme confirmation','Submitting interest does not by itself create an enrolment. Dates, fees, delivery format, completion requirements and any certificate offered are confirmed for the specific programme or cohort before registration is finalised.') + '<section class="section"><div class="container image-feature">'
      );
    };
  }
})();
