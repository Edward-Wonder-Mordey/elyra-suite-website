// Route-aware page titles and descriptions for the Elyra Suite hash-routed site.
const SEO_BASE = window.ELYRA_CONFIG?.siteBaseUrl || 'https://edward-wonder-mordey.github.io/elyra-suite-website/';
const SEO={
 home:['Elyra Suite | Beauty • Business • Excellence','Premium beauty, bridal, business support, training, social media and consulting from Elyra Suite in Kumasi, Ghana.'],
 about:['About Elyra Suite | Beauty, Business & Growth','Discover the Elyra Suite mission, values, professional journey and multidisciplinary brand vision.'],
 beauty:['Elyra Beauty | Hair, Makeup, Nails & Wigs','Explore Elyra Suite hair, wig, makeup and nail services for everyday beauty, events and personal transformation.'],
 bridal:['Bridal & Event Beauty | Elyra Suite','Bridal makeup, hair, beauty coordination, engagement and event beauty services from Elyra Suite.'],
 business:['Business & Administrative Support | Elyra Suite','Administrative support, business documentation, customer service and practical business solutions for entrepreneurs and organisations.'],
 academy:['Elyra Academy | Beauty & Business Training','Practical beauty and business training in wig making, makeup, nails, administration, customer service and entrepreneurship.'],
 partners:['Strategic Partners | Elyra Suite','Explore Elyra Suite strategic partnerships, including complementary collaboration with Eragonova Enterprise.'],
 shop:['Elyra Store | Wigs, Beauty Products & Accessories','Explore Elyra Store categories including wigs, hair extensions, beauty care, nail products, tools and accessories.'],
 social:['Social Media Management | Elyra Suite','Content creation, page management, customer engagement and digital brand support for growing businesses and organisations.'],
 consulting:['Elyra Consulting | Operations & Customer Experience','Practical consulting for operations, administrative systems, process improvement, planning and customer experience.'],
 portfolio:['Portfolio | Elyra Suite','Explore Elyra Suite visual service categories across beauty, bridal, training and professional brand presentation.'],
 resources:['Resources & Blog | Elyra Suite','Beauty tips, business growth, entrepreneurship, leadership, customer experience and empowerment resources from Elyra Suite.'],
 portal:['Client Portal | Elyra Suite','Elyra Suite client engagement information for appointments, documents, training and service updates.'],
 contact:['Contact Elyra Suite | Email, Booking & Enquiries','Contact Elyra Suite by email for beauty bookings, business support, Academy training, consulting, products and partnerships.'],
 privacy:['Privacy Policy | Elyra Suite','Read how Elyra Suite handles information shared through the website, email, WhatsApp and service enquiries.'],
 terms:['Website & Service Terms | Elyra Suite','Read Elyra Suite general website and service terms for enquiries, quotations, bookings and engagements.'],
 bookingpolicy:['Booking & Cancellation Policy | Elyra Suite','Read the Elyra Suite booking, rescheduling and cancellation framework for services, events and training.'],
 returnspolicy:['Store, Returns & Order Policy | Elyra Suite','Read general Elyra Store guidance for product enquiries, orders, changes, returns and delivery arrangements.']
};
function applySEO(){
  const route=getRoute();
  const [title,description]=SEO[route]||SEO.home;
  document.title=title;
  const set=(selector,attr,value)=>{const el=document.querySelector(selector);if(el)el.setAttribute(attr,value)};
  const routeUrl=SEO_BASE+(route==='home'?'':'#/'+route);
  set('meta[name="description"]','content',description);
  set('meta[property="og:title"]','content',title);
  set('meta[property="og:description"]','content',description);
  set('meta[property="og:url"]','content',routeUrl);
  set('meta[name="twitter:title"]','content',title);
  set('meta[name="twitter:description"]','content',description);
}
window.addEventListener('hashchange',applySEO);
window.addEventListener('DOMContentLoaded',applySEO);
