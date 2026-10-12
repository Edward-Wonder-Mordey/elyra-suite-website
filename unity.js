const originalFooter=footer;
footer=function(){
  const visualBand=`<div style="margin-bottom:46px">
    <div style="text-align:center;max-width:780px;margin:0 auto 26px">
      <div class="eyebrow" style="color:var(--gold-2)">Many strengths. One Elyra.</div>
      <h3 class="serif" style="font-size:clamp(2rem,4vw,3.6rem);margin:8px 0 10px;color:#fff">Different paths, connected by one vision.</h3>
      <p style="color:rgba(255,255,255,.7);line-height:1.7;margin:0">Beauty, celebration, learning, administration, digital work and consulting each serve different needs, but they are united by confidence, capability, service and growth.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px">
      ${[
        [MEDIA.portfolio,'Beauty & Transformation'],
        [MEDIA.contact,'Booking & Client Care'],
        [MEDIA.resources,'Knowledge & Resources'],
        [MEDIA.portal,'Connected Client Experience'],
        [MEDIA.consulting,'Business & Leadership']
      ].map(([img,label])=>`<div style="position:relative;aspect-ratio:4/3;border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.05)"><img src="${img}" alt="${label}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block"/><div style="position:absolute;inset:auto 0 0;padding:28px 12px 10px;background:linear-gradient(transparent,rgba(31,12,38,.88));color:#fff;font-size:.68rem;font-weight:800;letter-spacing:.04em">${label}</div></div>`).join('')}
    </div>
  </div>`;
  return originalFooter().replace('<div class="footer-grid">',visualBand+'<div class="footer-grid">');
};

const originalHome=pages.home;
pages.home=function(){
  const linkedVisuals=`<section class="section soft"><div class="container">
    ${sectionHead('Explore the Elyra Experience','Five connected experiences. One premium standard.','Beauty, client care, knowledge, digital access and business leadership work together as part of one connected Elyra Suite experience.',true)}
    <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px">
      ${[
        [MEDIA.contact,'Contact & Booking','Email-first enquiries, appointments and client care.','contact'],
        [MEDIA.resources,'Resources & Blog','Beauty knowledge, entrepreneurship, leadership and practical growth.','resources'],
        [MEDIA.portal,'Client Portal','A connected space for appointments, documents, training and engagement updates.','portal'],
        [MEDIA.consulting,'Consulting & Business Growth','Planning, administration, operations and customer-experience support.','consulting']
      ].map(([img,title,copy,route])=>`<a href="#/${route}" style="position:relative;min-height:320px;border-radius:28px;overflow:hidden;display:block;box-shadow:var(--shadow);border:1px solid var(--line);background:#fff;text-decoration:none"><img src="${img}" alt="${title}" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block"/><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(34,10,41,.02) 30%,rgba(34,10,41,.88) 100%)"></div><div style="position:absolute;left:24px;right:24px;bottom:22px;color:#fff"><div class="eyebrow" style="color:var(--gold-2)">Elyra Suite</div><h3 class="serif" style="font-size:clamp(1.8rem,3vw,2.8rem);margin:6px 0 8px;color:#fff">${title}</h3><p style="margin:0;color:rgba(255,255,255,.82);line-height:1.55">${copy}</p></div></a>`).join('')}
    </div>
  </div></section>`;

  let html=originalHome();
  html=html.replace(`src="${MEDIA.beauty}" alt="Elegant Elyra beauty experience"`,`src="${MEDIA.portfolio}" alt="Elyra Suite beauty, bridal, hair, makeup and nail experience"`);
  html=html.replace('<section class="section"><div class="container">',linkedVisuals+'<section class="section"><div class="container">');
  return html;
};
