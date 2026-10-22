# Elyra Suite Website Completion Checklist

Internal working checklist for the Elyra Suite website.

## Completed / in place

- Brand name is consistently **Elyra Suite**.
- Tagline: **Beauty • Business • Excellence**.
- Core service architecture covers beauty, bridal/events, store, administration, business support, social media, Academy and consulting.
- Email-first contact flow with WhatsApp as the secondary channel.
- Privacy, terms, booking/cancellation and store/returns policy pages.
- No invented testimonials are published; portfolio/testimonial permission language is in place.
- Route-aware page titles and descriptions.
- Organization structured data, robots.txt, sitemap.xml and web manifest.
- Owner handbook and automated handbook build workflow.
- Independent strategic-partner relationship with Eragonova Enterprise.
- Eragonova partner link now resolves through public runtime configuration to https://eragonova.com.
- Google Analytics 4 is configured in `site-config.js` with Measurement ID `G-3ECH94LV1S`; the Elyra web stream recently showed activity.
- Runtime configuration separates deploy-time settings from page content.
- Accessibility/browser quality layer adds skip navigation, current-page semantics, safer external-link attributes, image decoding hints and form autocomplete hints.

## Still to complete

### Secure client portal — current scope
- Supabase Auth and Row Level Security support the authenticated client/admin portal.
- Public self-registration is not enabled; access is authorized and account-based.
- Client feedback can be submitted for review; only genuine submissions with consent are published after admin approval.
- Online checkout, payment processing and a public student-account system are not implemented.
- Future additions such as private document storage, billing, messaging, notifications or expanded staff workspaces should be described as planned until implemented and tested.

### External business inputs
- Add official Instagram/Facebook/TikTok/YouTube URLs when confirmed.
- Check GA4 Realtime periodically; the measurement ID is already configured in the public site settings.
- Complete Google Search Console verification and sitemap submission if not already done.
- Decide whether Elyra Suite will use a custom domain; update canonical URLs, sitemap, runtime config and DNS when available.

### Proof and commercial content
- Add genuine client/learner testimonials only with permission.
- Add real portfolio case studies or before/after imagery only when approved for publication.
- Add confirmed Academy dates, fees and completion/certificate details when programmes are scheduled.
- Add confirmed store inventory, pricing and fulfilment details when products are ready for sale.

### Final QA and handbook
- Test desktop/mobile/tablet navigation and all email/WhatsApp actions.
- Verify legal/policy copy against actual operating practices before wider commercial use.
- Recheck accessibility, metadata and public links after the secure portal and any custom domain are added.
- Update the Owner's Handbook when portal capabilities, analytics, domain, social links or other site behavior changes.
