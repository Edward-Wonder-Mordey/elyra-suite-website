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
        [MEDIA.beauty,'Beauty & Confidence'],
        [MEDIA.bridal,'Bridal & Celebration'],
        [MEDIA.academy,'Learning & Opportunity'],
        [MEDIA.business,'Business & Administration'],
        [MEDIA.social,'Digital & Brand Growth'],
        [MEDIA.consulting,'Consulting & Leadership']
      ].map(([img,label])=>`<div style="position:relative;aspect-ratio:4/3;border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.05)"><img src="${img}" alt="${label}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block"/><div style="position:absolute;inset:auto 0 0;padding:28px 12px 10px;background:linear-gradient(transparent,rgba(31,12,38,.88));color:#fff;font-size:.68rem;font-weight:800;letter-spacing:.04em">${label}</div></div>`).join('')}
    </div>
  </div>`;
  return originalFooter().replace('<div class="footer-grid">',visualBand+'<div class="footer-grid">');
};
