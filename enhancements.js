// Public policy pages, trust signals and testimonial collection for Elyra Suite.
const policyUpdated='12 October 2026';

function policyLayout(title,intro,sections){
  return `<main class="fade">${pageHero('Elyra Suite Policies',title,intro)}<section class="section"><div class="container" style="max-width:960px"><div class="card" style="padding:clamp(26px,5vw,48px)"><p class="eyebrow">Last updated ${policyUpdated}</p>${sections.map(([h,body])=>`<section style="padding:24px 0;border-bottom:1px solid var(--line)"><h2 class="serif" style="font-size:clamp(1.8rem,3vw,2.5rem);color:var(--plum);margin:0 0 12px">${h}</h2><div style="color:var(--muted);line-height:1.8">${body}</div></section>`).join('')}<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:30px"><a class="btn btn-plum" href="mailto:${BRAND.email}">Email ${BRAND.email}</a><a class="btn btn-outline" href="#/contact">Contact Elyra Suite</a></div></div></div></section></main>`;
}

function privacy(){
  return policyLayout('Privacy Policy','How Elyra Suite handles information shared through this website, email, WhatsApp and service enquiries.',[
    ['Information you may provide',`<p>When you contact Elyra Suite, you may provide your name, email address, phone or WhatsApp number, service interests, preferred dates, location details relevant to a service, training interests, business information, messages and other information needed to respond to your request.</p>`],
    ['How information is used',`<p>Information is used to respond to enquiries, prepare quotations, discuss bookings, provide services, coordinate training, maintain engagement records, improve customer service and communicate about an active request or relationship.</p>`],
    ['Email and WhatsApp',`<p>Email is Elyra Suite’s primary contact channel. WhatsApp is offered as a secondary option. Information sent through either service is also subject to the privacy and security practices of the email or messaging provider you use.</p>`],
    ['Sharing and service partners',`<p>Elyra Suite does not sell personal information. Information may be shared only when reasonably necessary to provide a requested service, comply with applicable obligations, protect legitimate interests, or coordinate a service the client has asked to involve. Where a request may be better served with a strategic partner, that pathway can be discussed with the client before relevant information is shared.</p>`],
    ['Cookies and analytics',`<p>This website uses Google Analytics 4 to understand aggregate website usage, such as pages viewed and general interaction patterns. Google Analytics may use cookies or similar technologies and may process technical information such as your browser, device, approximate location and interaction events. The measurement ID is configured in the website; Google may process data under its own terms. Elyra Suite does not use this information to identify visitors directly or sell personal information. You can limit cookies through your browser settings. For more information, see Google’s privacy information.</p>`],
    ['Retention and security',`<p>Information is kept only for as long as reasonably necessary for the purpose for which it was collected, normal business records, dispute handling, or applicable legal and administrative requirements. Reasonable care is taken when handling information, although no online transmission or storage method can be guaranteed to be completely secure.</p>`],
    ['Your choices',`<p>You may contact Elyra Suite to ask about personal information you have provided, request a correction, or ask for deletion where appropriate. Some information may need to be retained where there is a legitimate business or legal reason to do so.</p>`],
    ['Children and learners',`<p>Where a learner is a minor, programme registration or participation should be handled with an appropriate parent or guardian where required.</p>`],
    ['Contact',`<p>Privacy questions can be sent to <a href="mailto:${BRAND.email}">${BRAND.email}</a>.</p>`]
  ]);
}

function terms(){
  return policyLayout('Website & Service Terms','General terms for using the Elyra Suite website and starting a service, training, store or consulting enquiry.',[
    ['Website information',`<p>The website provides general information about Elyra Suite services, training, products, consulting and partnership capabilities. Website content is not by itself a confirmed booking, contract, quotation, guarantee of availability or promise of a particular result.</p>`],
    ['Enquiries and confirmations',`<p>An enquiry becomes a confirmed engagement only after Elyra Suite provides written confirmation and any agreed conditions for that service are satisfied. A specific quotation, booking confirmation, proposal, invoice, programme brief or written agreement will take priority where it contains more specific terms.</p>`],
    ['Pricing and availability',`<p>Prices, product availability, programme dates, service scope and timing may vary according to the request. Where these details are not displayed, they are confirmed directly with the client before commitment.</p>`],
    ['Client responsibilities',`<p>Clients should provide accurate contact details, relevant dates, locations, requirements and other information needed to assess or deliver the requested service. Changes that affect scope, timing or cost should be communicated as early as reasonably possible.</p>`],
    ['Intellectual property',`<p>Elyra Suite branding, logos, original website copy, graphics and other original brand materials may not be copied, represented as another business’s work or commercially reused without permission. Third-party materials remain subject to their respective rights.</p>`],
    ['Third-party services and links',`<p>The website may link to email, WhatsApp, Eragonova Enterprise or other external services. Elyra Suite does not control every feature, privacy practice or availability of third-party platforms.</p>`],
    ['Reasonable limitations',`<p>Elyra Suite aims to keep website information useful and current, but cannot guarantee that the site will always be uninterrupted or error-free. Nothing in these terms is intended to remove rights that cannot lawfully be excluded.</p>`],
    ['Governing framework',`<p>These general website and service terms are intended to operate under the applicable laws of Ghana, subject to any more specific written agreement for a particular engagement.</p>`]
  ]);
}

function bookingPolicy(){
  return policyLayout('Booking & Cancellation Policy','A clear framework for beauty appointments, bridal and event services, consultations, training and other scheduled engagements.',[
    ['How to request a booking',`<p>Email is the primary booking and enquiry method. Include the requested service, preferred date and time, location where relevant, and important details. WhatsApp remains available as a secondary option.</p>`],
    ['When a booking is confirmed',`<p>A requested date is not reserved merely because an enquiry has been sent. A booking is confirmed only when Elyra Suite provides written confirmation and any stated booking conditions, including a deposit where one is required for that particular service, have been satisfied.</p>`],
    ['Changes and rescheduling',`<p>If you need to change a date, time, service or location, contact Elyra Suite as early as possible. Changes remain subject to availability and may require a revised quotation where the scope, timing, travel or staffing requirement changes.</p>`],
    ['Cancellations',`<p>Cancellation terms can vary by service. Any deposit, cancellation, rescheduling or refund terms stated in a quotation, invoice, bridal/event agreement, programme confirmation or other written booking communication take priority for that engagement.</p>`],
    ['Late arrival and no-shows',`<p>Late arrival or failure to attend may reduce the available service time, require rescheduling or affect whether the service can still be delivered. The appropriate response will depend on the service, schedule and circumstances.</p>`],
    ['Bridal, events and group services',`<p>Bridal, destination, event and group bookings may require additional planning around timing, travel, team coordination, venue access and service sequence. Specific event terms should be confirmed in writing.</p>`],
    ['Training and Academy sessions',`<p>Academy dates, delivery format, attendance expectations, completion requirements and any programme-specific cancellation or transfer terms are confirmed for the relevant programme or cohort.</p>`]
  ]);
}

function returnsPolicy(){
  return policyLayout('Store, Returns & Order Policy','General guidance for Elyra Store enquiries and product orders.',[
    ['Product enquiries',`<p>Product listings and categories introduce the types of products Elyra Suite may offer. Current availability, price, specification, colour, size, texture, quantity and order timing should be confirmed before purchase.</p>`],
    ['Custom and hygiene-sensitive products',`<p>Some beauty products may be personalised, made to order, opened for hygiene reasons or otherwise unsuitable for ordinary resale. Where a product has special return restrictions, those terms should be communicated before or at the point of purchase where applicable.</p>`],
    ['Incorrect, damaged or defective items',`<p>If an order is incorrect, arrives damaged or appears defective, contact Elyra Suite promptly with the order details and clear supporting information so the issue can be reviewed and an appropriate next step discussed. Applicable statutory rights are not intended to be excluded.</p>`],
    ['Order changes',`<p>Requests to change or cancel an order should be made as early as possible. Whether a change can be accepted depends on whether sourcing, preparation, customisation or fulfilment has already begun.</p>`],
    ['Delivery and collection',`<p>Delivery, collection, travel or courier arrangements are confirmed for the specific order. Any third-party delivery service may have its own operational terms.</p>`],
    ['Refunds',`<p>Where a refund is appropriate, the method and timing will depend on the original payment arrangement and the circumstances of the order. Any written product-specific terms supplied with the order take priority.</p>`]
  ]);
}

pages.privacy=privacy;
pages.terms=terms;
pages.bookingpolicy=bookingPolicy;
pages.returnspolicy=returnsPolicy;
if(!more.some(([,r])=>r==='privacy')) more.push(['Policies','privacy']);

const footerWithUnity=footer;
footer=function(){
  const html=footerWithUnity();
  const policyLinks=`<div style="display:flex;gap:14px;flex-wrap:wrap;justify-content:center;padding:18px 0 0;border-top:1px solid rgba(255,255,255,.1);margin-top:26px;font-size:.72rem"><a href="#/privacy">Privacy</a><a href="#/terms">Terms</a><a href="#/bookingpolicy">Booking & Cancellation</a><a href="#/returnspolicy">Store & Returns</a></div>`;
  return html.replace('<div class="footer-bottom">',policyLinks+'<div class="footer-bottom">');
};

const portfolioWithTrust=pages.portfolio;
pages.portfolio=function(){
  const testimonialSection=`<section class="section soft"><div class="container">${sectionHead('Client Stories & Testimonials','Real experiences, shared with permission.','Elyra Suite does not publish invented reviews. Genuine client and learner feedback can be added as it is received and approved.',true)}<div class="grid-2"><article class="card"><div class="card-icon">♡</div><h3>Worked with Elyra Suite?</h3><p>Share what service or programme you used, what stood out, and whether Elyra Suite may publish your feedback with your first name or preferred attribution.</p><a class="btn btn-plum" style="margin-top:20px" href="${emailHref('Elyra Suite Testimonial','Hello Elyra Suite,\n\nService / programme:\nMy experience:\nMay Elyra Suite publish this feedback? Yes / No\nPreferred attribution (optional):\n')}">Share Your Experience →</a></article><article class="card"><div class="card-icon">✦</div><h3>Portfolio Permission</h3><p>Real client photos, transformations and project examples are featured only when suitable imagery is available and the appropriate permission has been given.</p><a class="btn btn-outline" style="margin-top:20px" href="${emailHref('Elyra Suite Portfolio Permission','Hello Elyra Suite,\n\nI would like to discuss permission for my service photos / project to be featured.\n')}">Discuss Permission</a></article></div></div></section>`;
  return portfolioWithTrust().replace('</main>',testimonialSection+'</main>');
};

const contactWithPolicies=pages.contact;
pages.contact=function(){
  return contactWithPolicies().replace('</main>',`<section class="section"><div class="container"><div class="notice" style="max-width:960px;margin:0 auto">By sending an enquiry, you can review Elyra Suite’s <a href="#/privacy" style="font-weight:800;color:var(--plum)">Privacy Policy</a> and <a href="#/bookingpolicy" style="font-weight:800;color:var(--plum)">Booking & Cancellation Policy</a>. Specific written booking or quotation terms take priority for an individual engagement.</div></div></section></main>`);
};
