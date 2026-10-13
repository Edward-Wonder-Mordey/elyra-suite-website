// Free visitor resource: healthy makeup habits and natural-beauty guidance.
(function () {
  if (typeof pages === 'undefined') return;

  const pdfGuide = 'assets/Elyra_Suite_Healthy_Makeup_Guide.pdf';

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
            <div style="display:flex;justify-content:flex-end;align-items:center;gap:10px;flex-wrap:wrap">
              <a class="btn btn-gold" href="#/makeupguide">Read the free guide →</a>
              <a class="btn btn-light" href="${pdfGuide}" download>Save the one-page PDF</a>
            </div>
          </div>
        </div>
      </div>
    </section>`;

  const healthyMakeupGuide = function () {
    return `<main class="fade">
      ${pageHero('Free Beauty Guide','Healthy Makeup. Natural Beauty.','A practical Elyra Suite guide to using makeup with care, confidence and respect for your natural features.',`<a class="btn btn-gold" href="#guide-start">Start the guide</a><a class="btn btn-light" href="${pdfGuide}" download>Download one-page PDF</a>`)}

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
          ${sectionHead('Prepare the Skin First','Good makeup starts before foundation.','A simple preparation routine can help makeup sit more comfortably and reduce the temptation to use unnecessary layers.',true)}
          <div class="grid-3">
            <article class="card"><h3>Cleanse gently</h3><p>Begin with clean hands and clean skin. Avoid harsh scrubbing immediately before makeup, especially when the skin already feels irritated.</p></article>
            <article class="card"><h3>Moisturise</h3><p>Use a moisturiser that suits your skin and allow it to settle. Hydrated skin often gives makeup a smoother, more comfortable base.</p></article>
            <article class="card"><h3>Protect during the day</h3><p>Use suitable sun protection as part of your daytime skin routine. Makeup should sit on top of skin care—not replace it.</p></article>
          </div>
        </div>
      </section>

      <section class="section soft">
        <div class="container">
          ${sectionHead('Hygiene & Product Safety','Beautiful makeup should also be clean makeup.','Small hygiene habits help reduce unnecessary contamination and irritation.',true)}
          <div class="grid-3">
            <article class="card"><h3>Do not share everything</h3><p>Avoid sharing mascara, eyeliner, lip products and other items that touch the eyes or mouth directly. Disposable applicators are useful when products must be used across different people.</p></article>
            <article class="card"><h3>Clean reusable tools</h3><p>Wash brushes and sponges regularly, rinse them well and let them dry completely before storing them. Keep makeup bags and work surfaces clean too.</p></article>
            <article class="card"><h3>Watch product condition</h3><p>Replace products that develop an unusual smell, texture, colour or separation, and follow the product's storage and use guidance.</p></article>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          ${sectionHead('Patch-Test Unfamiliar Products','Give sensitive skin a chance to respond first.','A small test can be useful before using a new product widely, especially if your skin is reactive.',true)}
          <div class="grid-2">
            <article class="card"><h3>Start small</h3><p>Try a small amount on a limited area and give the skin time to respond before applying the product across the face. Follow the manufacturer's directions where provided.</p></article>
            <article class="card"><h3>Stop if something feels wrong</h3><p>Persistent burning, swelling, severe itching, rash or worsening irritation is a reason to stop using the product. If a reaction is severe or does not settle, seek appropriate professional care.</p></article>
          </div>
        </div>
      </section>

      <section class="section soft">
        <div class="container">
          ${sectionHead('When You Have Breakouts or Blemishes','Cover with care. Do not confuse coverage with treatment.','A good makeup routine can reduce the visual contrast of a blemish while still keeping the approach gentle.',true)}
          <div class="grid-2">
            <article class="card"><h3>What makeup can do</h3><p>It can soften redness, dark marks and uneven tone for an event, photoshoot, workday or personal preference. Light spot-concealing often looks more natural than piling heavy product over the whole face.</p></article>
            <article class="card"><h3>What makeup cannot do</h3><p>It does not treat acne, heal broken skin or replace appropriate skin care. Avoid applying makeup over open wounds, actively infected-looking areas or severe irritation; those situations deserve proper care rather than extra coverage.</p></article>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          ${sectionHead('Know When Makeup Is Not the Solution','Some concerns need care, not concealment.','Makeup is cosmetic. It should not delay attention for persistent, painful or severe skin problems.',true)}
          <div class="grid-2">
            <article class="card"><h3>Choose comfort over coverage</h3><p>If the skin is broken, very painful, significantly swollen, persistently irritated or appears infected, adding more makeup may make the area harder to assess and less comfortable.</p></article>
            <article class="card"><h3>Seek appropriate help</h3><p>Persistent or severe skin concerns are better discussed with an appropriate health professional. Makeup can support confidence while the skin is cared for, but it should not replace treatment when treatment is needed.</p></article>
          </div>
        </div>
      </section>

      <section class="section soft">
        <div class="container">
          ${sectionHead('Healthy Makeup Checklist','A simple routine to remember.','Keep this sequence in mind whenever you are preparing a look.',true)}
          <div class="split-banner" style="background:linear-gradient(120deg,#2B1036,#4A235A,#6B3279)">
            <div class="inner">
              <div><div class="eyebrow" style="color:var(--gold-2)">Quick checklist</div><h2>Clean skin → moisturise → clean tools → light layers.</h2><p>Do not cover open wounds → remove makeup before sleeping → clean tools again → let your skin rest.</p><a class="btn btn-gold" href="${pdfGuide}" download style="margin-top:14px">Save the printable PDF</a></div>
              <div class="metric-row">
                <div class="metric"><strong>Clean</strong><span>skin, hands and tools</span></div>
                <div class="metric"><strong>Care</strong><span>before extra coverage</span></div>
                <div class="metric"><strong>Rest</strong><span>remove makeup at the end</span></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <p class="quote">“Makeup should work with your natural beauty, not make you feel that your natural face is incomplete.”</p>
          <p class="section-copy" style="max-width:760px;margin:22px auto 0;text-align:center">Use makeup to express, enhance, celebrate or create a look. A polished finish can be powerful, but your beauty does not disappear when the makeup comes off.</p>
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
      const feature = `<section class="section"><div class="container">${sectionHead('Free Beauty Guide','Healthy Makeup & Natural Beauty','Learn how to use makeup to soften the appearance of blemishes and uneven tone while keeping skin care, hygiene and natural beauty at the centre.',true)}<div class="grid-2"><article class="card"><div class="card-icon">✦</div><h3>What you will learn</h3><p>Skin preparation, clean-tool habits, product safety, patch testing, lighter coverage, makeup around breakouts, when not to cover a skin concern, and why makeup should enhance rather than replace your natural features.</p></article><article class="card"><div class="eyebrow">Free to everyone</div><h3>No email gate. No payment.</h3><p>Visitors can read the full guide immediately or save the one-page checklist. It is designed as practical beauty education, not a sales requirement.</p><div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:20px"><a class="btn btn-plum" href="#/makeupguide">Open the free guide →</a><a class="btn btn-outline" href="${pdfGuide}" download>Download PDF</a></div></article></div></div></section>`;
      return originalResources().replace('<section class="section soft">', feature + '<section class="section soft">');
    };
  }

  if (typeof SEO !== 'undefined') {
    SEO.makeupguide = ['Free Healthy Makeup & Natural Beauty Guide | Elyra Suite','A free Elyra Suite guide to skin preparation, makeup hygiene, patch testing, blemish coverage, clean tools and enhancing natural beauty.'];
  }
})();
