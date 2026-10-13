// Free visitor resource: healthy makeup habits and natural-beauty guidance.
(function () {
  if (typeof pages === 'undefined') return;

  const freeGuidePromo = `
    <section class="section soft">
      <div class="container">
        <div class="split-banner" style="background:linear-gradient(120deg,#2B1036,#4A235A,#7a4766)">
          <div class="inner">
            <div>
              <div class="eyebrow" style="color:var(--gold-2)">Free visitor resource · No signup · No payment</div>
              <h2>Healthy Makeup & Natural Beauty</h2>
              <p>Makeup can help soften the appearance of breakouts, dark marks, uneven tone, scars or tiredness, and it can be a beautiful form of self-expression. But it should enhance what is already there—not teach you that your natural face is a problem.</p>
            </div>
            <div style="display:flex;justify-content:flex-end;align-items:center">
              <a class="btn btn-gold" href="#/makeupguide">Read the free guide →</a>
            </div>
          </div>
        </div>
      </div>
    </section>`;

  const healthyMakeupGuide = function () {
    return `<main class="fade">
      ${pageHero('Free Beauty Guide','Healthy Makeup. Natural Beauty.','A practical Elyra Suite guide to using makeup with care, confidence and respect for your natural features.',`<a class="btn btn-gold" href="#guide-start">Start the guide</a><a class="btn btn-light" href="#/beauty">Explore Beauty Services</a>`)}

      <section class="section" id="guide-start">
        <div class="container image-feature reverse">
          <div>
            ${sectionHead('The Elyra Approach','Makeup should support confidence—not replace natural beauty.','Healthy beauty starts with skin care, clean tools, suitable products and a mindset that sees makeup as an option for expression rather than a requirement for worth.')}
            <p class="section-copy">Makeup can visually soften the appearance of blemishes, breakouts, dark marks, uneven tone, scars or tiredness. It does not cure skin conditions, and it should not be used to hide active irritation, open skin or signs of infection. Your natural face is not something that needs to be corrected before it can be beautiful.</p>
          </div>
          <div class="photo-panel logo-overlay"><img src="${MEDIA.store}" alt="Elyra Suite healthy makeup and natural beauty guide" loading="eager"/></div>
        </div>
      </section>

      <section class="section soft">
        <div class="container">
          ${sectionHead('Six Healthy Makeup Habits','Simple practices that protect both the look and the skin.','These are everyday beauty habits—not medical treatment.',true)}
          <div class="grid-3">
            <article class="card"><div class="card-icon">01</div><h3>Skin first</h3><p>Start with clean hands and a gently cleansed face. Moisturise appropriately and use sun protection during the day before building the makeup look.</p></article>
            <article class="card"><div class="card-icon">02</div><h3>Keep tools clean</h3><p>Wash brushes and reusable sponges regularly, allow them to dry properly and avoid sharing eye or lip products. Dirty tools can transfer oil, bacteria and old product back onto the skin.</p></article>
            <article class="card"><div class="card-icon">03</div><h3>Correct lightly</h3><p>Use concealer or colour correction only where needed, then build thin layers. The goal can be an even, polished finish without hiding every natural feature or texture.</p></article>
            <article class="card"><div class="card-icon">04</div><h3>Choose comfort over pressure</h3><p>If a product feels heavy, burns, stings or causes unusual irritation, stop using it. Patch-test unfamiliar products when practical and pay attention to how your skin responds.</p></article>
            <article class="card"><div class="card-icon">05</div><h3>Remove makeup before sleep</h3><p>Gently remove makeup at the end of the day and cleanse the skin. Sleeping in makeup can leave product, oil and debris sitting on the face for longer than necessary.</p></article>
            <article class="card"><div class="card-icon">06</div><h3>Let natural beauty stay visible</h3><p>Freckles, texture, smile lines and individual features are part of a real face. Makeup can highlight, soften or transform a look—but confidence should not depend on covering everything.</p></article>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          ${sectionHead('When You Have Breakouts or Blemishes','Cover with care. Do not confuse coverage with treatment.','A good makeup routine can reduce the visual contrast of a blemish while still keeping the approach gentle.',true)}
          <div class="grid-2">
            <article class="card"><h3>What makeup can do</h3><p>It can soften redness, dark marks and uneven tone for an event, photoshoot, workday or personal preference. Light spot-concealing often looks more natural than piling heavy product over the whole face.</p></article>
            <article class="card"><h3>What makeup cannot do</h3><p>It does not treat acne, heal broken skin or replace appropriate skin care. Avoid applying makeup over open wounds, actively infected-looking areas or severe irritation; those situations deserve proper care rather than extra coverage.</p></article>
          </div>
        </div>
      </section>

      <section class="section soft">
        <div class="container">
          <div class="split-banner">
            <div class="inner">
              <div><div class="eyebrow" style="color:var(--gold-2)">A simple reminder</div><h2>Your face is already yours before the makeup begins.</h2><p>Use beauty products to express, enhance, celebrate or create a look. A polished finish can be powerful, but natural beauty does not disappear when the makeup comes off.</p></div>
              <div class="metric-row">
                <div class="metric"><strong>Clean</strong><span>hands, skin and tools</span></div>
                <div class="metric"><strong>Light</strong><span>layers where possible</span></div>
                <div class="metric"><strong>You</strong><span>before and after makeup</span></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      ${cta('Want help creating a look that still feels like you?','Tell Elyra Suite the occasion, finish, coverage level and style you want. The goal is a look that supports confidence rather than replacing your natural identity.','Beauty Enquiry')}
    </main>`;
  };

  pages.makeupguide = healthyMakeupGuide;

  if (typeof more !== 'undefined' && Array.isArray(more) && !more.some(([, route]) => route === 'makeupguide')) {
    more.push(['Free Beauty Guide','makeupguide']);
  }

  if (pages.home) {
    const originalHome = pages.home;
    pages.home = function () {
      return originalHome().replace('</main>', freeGuidePromo + '</main>');
    };
  }

  if (pages.resources) {
    const originalResources = pages.resources;
    pages.resources = function () {
      const feature = `<section class="section"><div class="container">${sectionHead('Free Beauty Guide','Healthy Makeup & Natural Beauty','Learn how to use makeup to soften the appearance of blemishes and uneven tone while keeping skin care, hygiene and natural beauty at the centre.',true)}<div class="grid-2"><article class="card"><div class="card-icon">✦</div><h3>What you will learn</h3><p>Clean-tool habits, lighter coverage, makeup around breakouts, removing makeup properly, and why makeup should enhance rather than replace your natural features.</p></article><article class="card"><div class="eyebrow">Free to everyone</div><h3>No email gate. No payment.</h3><p>Visitors can open and use the guide immediately. It is designed as practical beauty education, not a sales requirement.</p><a class="btn btn-plum" style="margin-top:20px" href="#/makeupguide">Open the free guide →</a></article></div></div></section>`;
      return originalResources().replace('<section class="section soft">', feature + '<section class="section soft">');
    };
  }

  if (typeof SEO !== 'undefined') {
    SEO.makeupguide = ['Free Healthy Makeup & Natural Beauty Guide | Elyra Suite','A free Elyra Suite guide to healthy makeup habits, blemish coverage, clean tools, skin-friendly routines and enhancing natural beauty.'];
  }
})();
