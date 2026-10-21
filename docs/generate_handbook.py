from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_BREAK
from docx.enum.table import WD_ROW_HEIGHT_RULE
from pathlib import Path

OUT = 'docs/Elyra_Suite_Website_Owners_Handbook.docx'
LOGO = 'docs/Elyra_Suite_Luxury_Monogram_Logo.jpg'

PLUM = '4A235A'
ROSE = 'B76E79'
GOLD = 'DAA537'
CREAM = 'FFF8F0'
CHARCOAL = '1A1A1A'
MUTED = '666166'
LIGHT = 'F8F3F6'
WHITE = 'FFFFFF'
GREEN = 'E8F4EA'
AMBER = 'FFF4D6'
RED = 'FCE8E6'
BLUE = 'EAF1FB'


def set_cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd')
        tcPr.append(shd)
    shd.set(qn('w:fill'), fill)


def set_cell_border(cell, color='D8CCD5', size='4'):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in('w:tcBorders')
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        tag = 'w:' + edge
        el = tcBorders.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            tcBorders.append(el)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), size)
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), color)


def set_run_font(run, name='Liberation Sans'):
    run.font.name = name
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.rFonts
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), name)
    rFonts.set(qn('w:hAnsi'), name)


def style_paragraph_runs(p, font='Liberation Sans', color=None, size=None, bold=None):
    for r in p.runs:
        set_run_font(r, font)
        if color:
            r.font.color.rgb = RGBColor.from_string(color)
        if size:
            r.font.size = Pt(size)
        if bold is not None:
            r.bold = bold


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run('Page ')
    set_run_font(run)
    fldChar1 = OxmlElement('w:fldChar'); fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText'); instrText.set(qn('xml:space'), 'preserve'); instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar'); fldChar2.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1); run._r.append(instrText); run._r.append(fldChar2)
    run2 = paragraph.add_run('  |  Elyra Suite Website Owner’s Handbook')
    set_run_font(run2)
    run2.font.size = Pt(8)
    run2.font.color.rgb = RGBColor.from_string(MUTED)


def add_heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    p.paragraph_format.keep_with_next = True
    return p


def add_body(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(7)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix and text.startswith(bold_prefix):
        r1 = p.add_run(bold_prefix)
        r1.bold = True
        r2 = p.add_run(text[len(bold_prefix):])
        set_run_font(r1); set_run_font(r2)
    else:
        r = p.add_run(text)
        set_run_font(r)
    return p


def add_bullets(doc, items, level=0):
    for item in items:
        p = doc.add_paragraph(style='List Bullet' if level == 0 else 'List Bullet 2')
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(item)
        set_run_font(r)


def add_steps(doc, items):
    for i, item in enumerate(items, 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(0.55)
        p.paragraph_format.first_line_indent = Cm(-0.55)
        r1 = p.add_run(f'{i}. ')
        r1.bold = True
        set_run_font(r1)
        r2 = p.add_run(item)
        set_run_font(r2)


def add_note(doc, title, text, kind='info'):
    fills = {'info': BLUE, 'safe': GREEN, 'warn': AMBER, 'danger': RED, 'brand': CREAM}
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    cell = table.cell(0,0)
    set_cell_shading(cell, fills.get(kind, BLUE))
    set_cell_border(cell, GOLD if kind == 'brand' else 'D8CCD5', '8' if kind == 'brand' else '4')
    p = cell.paragraphs[0]
    r = p.add_run(title + '\n')
    r.bold = True; r.font.color.rgb = RGBColor.from_string(PLUM); set_run_font(r)
    r2 = p.add_run(text)
    r2.font.color.rgb = RGBColor.from_string(CHARCOAL); set_run_font(r2)
    p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def add_table(doc, headers, rows, widths=None, small=False):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False if widths else True
    hdr = t.rows[0].cells
    for i,h in enumerate(headers):
        hdr[i].text = h
        set_cell_shading(hdr[i], PLUM)
        set_cell_border(hdr[i], 'D8CCD5')
        hdr[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        p = hdr[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        style_paragraph_runs(p, color=WHITE, size=8.5 if small else 9, bold=True)
        if widths:
            hdr[i].width = widths[i]
    for row_idx,row in enumerate(rows):
        cells = t.add_row().cells
        fill = WHITE if row_idx % 2 == 0 else LIGHT
        for i,val in enumerate(row):
            cells[i].text = str(val)
            set_cell_shading(cells[i], fill)
            set_cell_border(cells[i], 'E3D9E0')
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            style_paragraph_runs(p, size=7.8 if small else 8.5)
            if widths:
                cells[i].width = widths[i]
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return t


def add_code(doc, text):
    t = doc.add_table(rows=1, cols=1)
    cell = t.cell(0,0)
    set_cell_shading(cell, 'F2EFF1')
    set_cell_border(cell, 'D6CCD4')
    p = cell.paragraphs[0]
    r = p.add_run(text)
    set_run_font(r, 'Liberation Mono')
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor.from_string(CHARCOAL)
    p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def page_break(doc):
    # Major Heading 1 styles already start on a new page. Keeping this as a no-op
    # avoids accidental blank pages when the previous section naturally fills a page.
    pass


doc = Document()
sec = doc.sections[0]
sec.page_width = Cm(21)
sec.page_height = Cm(29.7)
sec.top_margin = Cm(1.7)
sec.bottom_margin = Cm(1.6)
sec.left_margin = Cm(1.7)
sec.right_margin = Cm(1.7)
sec.different_first_page_header_footer = True

# Base styles
styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Liberation Sans'
normal.font.size = Pt(9.5)
normal.font.color.rgb = RGBColor.from_string(CHARCOAL)
normal.paragraph_format.space_after = Pt(6)

for sname, size, color, font in [
    ('Title', 30, PLUM, 'Liberation Serif'),
    ('Heading 1', 20, PLUM, 'Liberation Serif'),
    ('Heading 2', 14, ROSE, 'Liberation Sans'),
    ('Heading 3', 11, PLUM, 'Liberation Sans'),
]:
    st = styles[sname]
    st.font.name = font
    st.font.size = Pt(size)
    st.font.color.rgb = RGBColor.from_string(color)
    st.font.bold = True
    st.paragraph_format.space_before = Pt(10 if sname != 'Heading 1' else 16)
    st.paragraph_format.space_after = Pt(6)
    if sname == 'Heading 1':
        st.paragraph_format.page_break_before = True

# Footer page numbers on all non-first pages
for section in doc.sections:
    p = section.footer.paragraphs[0]
    add_page_number(p)

# COVER
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(36)
if Path(LOGO).exists():
    run = p.add_run(); run.add_picture(LOGO, width=Inches(2.35))

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(12)
r = p.add_run('ELYRA SUITE'); set_run_font(r, 'Liberation Serif'); r.bold=True; r.font.size=Pt(30); r.font.color.rgb=RGBColor.from_string(PLUM)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('WEBSITE OWNER’S HANDBOOK'); set_run_font(r); r.bold=True; r.font.size=Pt(16); r.font.color.rgb=RGBColor.from_string(GOLD)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('A plain-language guide to updating, maintaining and growing the Elyra Suite website'); set_run_font(r); r.font.size=Pt(11); r.font.color.rgb=RGBColor.from_string(MUTED)

p = doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(22)
r=p.add_run('Beauty • Business • Excellence'); set_run_font(r, 'Liberation Serif'); r.bold=True; r.font.size=Pt(15); r.font.color.rgb=RGBColor.from_string(ROSE)

box = doc.add_table(rows=4, cols=2); box.alignment=WD_TABLE_ALIGNMENT.CENTER
cover_rows = [
    ('Live website', 'https://edward-wonder-mordey.github.io/elyra-suite-website/'),
    ('GitHub repository', 'Edward-Wonder-Mordey/elyra-suite-website'),
    ('Primary email', 'elyrasuite@gmail.com'),
    ('Handbook version', 'Version 1.0 — 12 October 2026'),
]
for i,(a,b) in enumerate(cover_rows):
    box.cell(i,0).text=a; box.cell(i,1).text=b
    set_cell_shading(box.cell(i,0), CREAM); set_cell_shading(box.cell(i,1), WHITE)
    set_cell_border(box.cell(i,0), 'E4D4C6'); set_cell_border(box.cell(i,1), 'E4D4C6')
    style_paragraph_runs(box.cell(i,0).paragraphs[0], size=8.5, bold=True, color=PLUM)
    style_paragraph_runs(box.cell(i,1).paragraphs[0], size=8.5)

doc.add_paragraph()
p = doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=p.add_run('Purpose: keep this document with the website and update it whenever the website structure, contact details, services or business systems change.'); set_run_font(r); r.italic=True; r.font.size=Pt(8.5); r.font.color.rgb=RGBColor.from_string(MUTED)

page_break(doc)

# 1 HOW TO USE
add_heading(doc, '1. How to Use This Handbook', 1)
add_body(doc, 'This handbook is written for both technical and non-technical readers. You do not need to understand programming to use most of it. The main goal is to tell you what part of the website controls each item, what is safe to change, and when a change should be handled more carefully.')
add_note(doc, 'The safest rule', 'Change only the part you intend to change. Do not delete brackets, quotation marks, commas, function names or script tags unless you understand why they are there.', 'warn')
add_heading(doc, '1.1 Three levels of changes', 2)
add_table(doc, ['Level', 'Meaning', 'Examples'], [
    ('GREEN — Safe content change', 'Usually a text, email, phone, image or service-list update.', 'Business email, service description, article text, image filename.'),
    ('AMBER — Change carefully', 'May affect navigation, page layout, SEO or several pages at once.', 'Adding a new page, changing navigation, replacing a major homepage section.'),
    ('RED — Technical/backend change', 'Can affect security, payments, logins or deployment.', 'Real client login, online payments, database, authentication, changing the deployment workflow.'),
], widths=[Cm(3.3),Cm(6.4),Cm(7.7)])
add_heading(doc, '1.2 Before every website change', 2)
add_steps(doc, [
    'Open the live website and note what you are changing.',
    'In GitHub, open the exact file listed in this handbook.',
    'Make one logical change at a time.',
    'Write a clear commit message, for example: “Update Elyra contact email” or “Add new Academy course”.',
    'Wait for GitHub Actions to finish the deployment and show a green success check.',
    'Open the live website, hard-refresh the page, and test desktop and mobile views.',
    'If something is wrong, use the file History in GitHub to restore the previous working content.'
])
add_note(doc, 'What “commit” means', 'A commit is simply a saved version of the website in GitHub. Each commit creates a history point you can go back to later.', 'info')

add_heading(doc, '1.3 Guide map', 2)
for text in [
    'Section 2 — Quick “what do I change?” finder',
    'Section 3 — Website structure in simple terms',
    'Section 4 — Brand identity and contact information',
    'Section 5 — File and folder map',
    'Sections 6–10 — How to update pages, services, images, products, Academy and content',
    'Sections 11–14 — Policies, SEO, analytics, domains and social media',
    'Sections 15–18 — GitHub editing, deployment, troubleshooting and maintenance',
    'Appendices — Current service catalog, image map and update log template'
]:
    add_body(doc, text)

page_break(doc)

# 2 QUICK FINDER
add_heading(doc, '2. Quick Change Finder — “If I Want to Change X, Where Do I Go?”', 1)
quick_rows = [
('Email, phone or location','core.js — BRAND at the top','Also update index.html structured business data for phone/email/address.','GREEN'),
('Eragonova partner name, link or logo','core.js — ERAGONOVA','Partnership wording also appears in pages-primary.js and pages-connect.js.','GREEN/AMBER'),
('Main service names or service items','core.js — divisions','These feed service cards and detailed service lists.','GREEN'),
('Top navigation / More menu','core.js — nav and more','Be careful not to break route names.','AMBER'),
('Homepage, About, Beauty wording','pages-primary.js','Homepage is later enhanced by unity.js.','GREEN/AMBER'),
('Bridal page','page-bridal.js','Edit packages, event wording and CTA text here.','GREEN'),
('Business, Social, Academy, Shop, Consulting','pages-business.js','Academy forms and store enquiry text also live here.','GREEN/AMBER'),
('Portfolio, Resources, Partners, Portal, Contact','pages-connect.js','Contact form and route/render logic are also here.','GREEN/AMBER'),
('Homepage hero visual + “Explore the Elyra Experience” + footer image band','unity.js','This file intentionally modifies the original homepage/footer after page definitions load.','AMBER'),
('Privacy, Terms, Booking, Returns, testimonials','enhancements.js','Update policy date if policy wording changes.','AMBER'),
('Page titles/descriptions shown to search/social systems','seo.js','Keep route names matched to the real website.','AMBER'),
('Google Analytics measurement ID','analytics.js','Leave blank until a real ID exists. Update privacy wording after enabling tracking.','AMBER'),
('General colours, spacing, cards, buttons, desktop styling','styles.css','Avoid broad changes unless you can test every page.','AMBER'),
('Mobile/tablet layout','media.css','Always test on a phone after changing.','AMBER'),
('Images and logos','assets/ + MEDIA in core.js','Upload image first, then point MEDIA to the filename.','GREEN'),
('Main metadata, social share image, structured business data, cache version','index.html','Script order matters. Do not rearrange casually.','AMBER'),
('Search crawler instructions','robots.txt','Usually no change unless domain or indexing strategy changes.','AMBER'),
('Sitemap URL','sitemap.xml','Update after moving to a custom domain.','AMBER'),
('Automatic GitHub Pages deployment','.github/workflows/deploy-pages.yml','Do not edit unless deployment is broken or intentionally changing hosting.','RED'),
('This handbook','docs/Elyra_Suite_Website_Owners_Handbook.docx','Download, edit in Word, save, and upload the replacement to the same path.','GREEN'),
]
add_table(doc, ['Change', 'Main file/location', 'Important note', 'Risk'], quick_rows, small=True)

page_break(doc)

# 3 STRUCTURE
add_heading(doc, '3. How the Website Works — Plain English', 1)
add_body(doc, 'The website is a lightweight static website hosted by GitHub Pages. “Static” means there is no private database or server application running behind the public pages. The website files themselves contain the text, images, layout and simple form behaviour.')
add_heading(doc, '3.1 What happens when a visitor opens the site', 2)
add_steps(doc, [
    'index.html loads the website shell, fonts, styles and JavaScript files.',
    'core.js loads the brand details, service catalog, navigation and shared components.',
    'The page files create the individual website sections such as Home, Beauty, Academy and Contact.',
    'unity.js adds the image-rich homepage/footer presentation.',
    'enhancements.js adds policies, testimonial collection and trust-related sections.',
    'seo.js changes the page title and description to match the page being viewed.',
    'analytics.js is ready for analytics, but currently does not track visitors because no measurement ID has been added.',
    'GitHub Pages serves the finished files publicly.'
])
add_heading(doc, '3.2 What the #/home style address means', 2)
add_body(doc, 'The website uses hash routes. A route is the part after #/, for example #/academy or #/contact. This lets the site behave like it has many pages while using one main HTML file.')
add_code(doc, 'Examples:\n#/home      → Home\n#/beauty    → Beauty\n#/academy   → Elyra Academy\n#/contact   → Contact\n#/privacy   → Privacy Policy')
add_note(doc, 'SEO note', 'Hash routing works well for a lightweight site, but if search visibility becomes a major business priority later, a future rebuild with clean page URLs may give more control over search indexing.', 'info')
add_heading(doc, '3.3 Current public page routes', 2)
add_table(doc, ['Route', 'Page'], [
('#/home','Home'),('#/about','About'),('#/beauty','Beauty'),('#/bridal','Bridal & Events'),('#/business','Business Solutions'),('#/academy','Elyra Academy'),('#/partners','Strategic Partners'),('#/shop','Elyra Store'),('#/social','Social Media'),('#/consulting','Consulting'),('#/portfolio','Portfolio'),('#/resources','Resources & Blog'),('#/portal','Client Portal'),('#/contact','Contact & Booking'),('#/privacy','Privacy Policy'),('#/terms','Website & Service Terms'),('#/bookingpolicy','Booking & Cancellation'),('#/returnspolicy','Store & Returns')
], widths=[Cm(4.1), Cm(13.0)], small=True)

page_break(doc)

# 4 BRAND
add_heading(doc, '4. Brand Identity and Contact Information', 1)
add_heading(doc, '4.1 Brand standard', 2)
add_table(doc, ['Item', 'Current value'], [
('Public name','Elyra Suite'),
('Tagline','Beauty • Business • Excellence'),
('Vision line','Empowering confidence through beauty while building opportunities through leadership, administration, and entrepreneurship.'),
('Primary email','elyrasuite@gmail.com'),
('Secondary contact','WhatsApp: +233 53 124 6233'),
('Location','Kumasi, Ashanti Region, Ghana'),
('Strategic partner','Eragonova Enterprise — independent strategic partner'),
])
add_heading(doc, '4.2 Official colour palette', 2)
color_rows = [
('Deep Plum','#4A235A','Primary luxury/brand colour'),('Rose Gold','#B76E79','Secondary feminine accent'),('Champagne Gold','#DAA537','Premium highlight/accent'),('Cream','#FFF8F0','Warm light background'),('Charcoal Black','#1A1A1A','Text and dark contrast')
]
add_table(doc, ['Colour', 'Hex code', 'Use'], color_rows)
add_heading(doc, '4.3 Changing email, phone or location', 2)
add_body(doc, 'The simplest contact values live in core.js at the very top inside BRAND. Change the value, not the label or punctuation around it.')
add_code(doc, "const BRAND={name:'Elyra Suite',tagline:'Beauty • Business • Excellence',phone:'+233 53 124 6233',phoneRaw:'233531246233',email:'elyrasuite@gmail.com',location:'Kumasi, Ashanti Region, Ghana'};")
add_bullets(doc, [
    'phone is the version people see.',
    'phoneRaw is the WhatsApp version: country code + digits only, with no spaces or + sign.',
    'email controls the email links and forms throughout the site.',
    'location is shown on the Contact page.'
])
add_note(doc, 'Do not stop at core.js', 'If email, phone or address changes, also update the hard-coded structured business data in index.html so search engines receive the correct information.', 'warn')

page_break(doc)

# 5 FILE MAP
add_heading(doc, '5. File and Folder Map', 1)
add_body(doc, 'Think of each file as a department. You normally only need to enter the department that owns the thing you want to change.')
file_rows = [
('index.html','The front door','Loads styles/scripts, general SEO metadata, social-share image and structured business information.'),
('core.js','Shared business data','Brand/contact details, partner details, image map, service catalog, navigation, footer and shared cards.'),
('pages-primary.js','Main public pages','Home, About and Beauty content.'),
('page-bridal.js','Bridal page','Bridal packages, bridal experience and event service wording.'),
('pages-business.js','Business/training/store pages','Business, Social Media, Academy, Store and Consulting.'),
('pages-connect.js','Connection/content pages','Portfolio, Resources, Partners, Client Portal, Contact and central route/render behaviour.'),
('unity.js','Visual enhancement layer','Homepage hero image, connected experience cards and “Many strengths. One Elyra.” footer image band.'),
('enhancements.js','Trust & policy layer','Privacy/terms/booking/returns pages, testimonial collection, portfolio permission and contact policy note.'),
('seo.js','Search titles/descriptions','Route-specific page titles and descriptions.'),
('analytics.js','Analytics switch','Google Analytics-ready code; inactive while ID is blank.'),
('styles.css','Main appearance','Colours, typography, cards, buttons, grids, desktop layout.'),
('media.css','Mobile appearance','Responsive behaviour for smaller screens.'),
('assets/','Images and logos','All brand logo files and website imagery.'),
('robots.txt','Search bot instruction','Tells crawlers they may index the site and points to the sitemap.'),
('sitemap.xml','Search map','Public site URL used by search engines.'),
('site.webmanifest','Install/browser identity','Basic app/browser identity and icons.'),
('.github/workflows/deploy-pages.yml','Automatic publishing','Publishes every approved commit on main to GitHub Pages.'),
('.nojekyll','GitHub Pages support','Prevents Jekyll processing. Normally never touch.'),
]
add_table(doc, ['File', 'Simple meaning', 'What it controls'], file_rows, widths=[Cm(4.4),Cm(4.2),Cm(8.5)], small=True)
add_note(doc, 'Important', 'A page may be defined in one file and later visually enhanced in another. The clearest example is Home: base Home content is in pages-primary.js, but the visible hero image and connected-image showcase are modified later by unity.js.', 'brand')

page_break(doc)

# 6 NAV + SERVICES
add_heading(doc, '6. Navigation, Services and Business Divisions', 1)
add_heading(doc, '6.1 Current main navigation', 2)
add_body(doc, 'The top navigation is defined in core.js. There are two groups: nav for the visible main menu and more for the More dropdown.')
add_code(doc, "nav → Home, About, Beauty, Bridal, Business, Academy, Partners\nmore → Shop, Social Media, Consulting, Portfolio, Resources, Client Portal, Contact, Policies")
add_heading(doc, '6.2 To rename a menu item', 2)
add_steps(doc, [
    'Open core.js.',
    'Find nav or more.',
    'Change only the first value (the visible label) if the page route should stay the same.',
    'Do not change the second value unless you are intentionally changing the route and will update every reference to that route.'
])
add_code(doc, "['Academy','academy']\nFirst value = what visitors see.\nSecond value = route used by the website.")
add_heading(doc, '6.3 Current eight business divisions', 2)
service_rows = [
('01','Beauty & Personal Care','Hair, makeup and nails'),('02','Beauty Products Store','Wigs, extensions, care, cosmetics, accessories'),('03','Bridal & Events','Bridal packages, wedding/event coordination, VIP'),('04','Administrative Support','VA, email, calendar, data, appointments, customer support'),('05','Business Support Services','Registration guidance, company profiles, plans, proposals, quotations/invoices, policies, systems'),('06','Social Media Management','Content, pages, platforms, engagement, brand strategy'),('07','Elyra Academy','Beauty and business training'),('08','Corporate Consulting','Operations, systems, planning, process and customer experience')
]
add_table(doc, ['No.', 'Division', 'What it covers'], service_rows)
add_heading(doc, '6.4 To add or remove a service item', 2)
add_steps(doc, [
    'Open core.js.',
    'Find the correct division inside const divisions.',
    'Find the correct group, such as Hair, Makeup, Nails, Services or Training.',
    'Add a new quoted item inside the square brackets, separated by a comma.',
    'Commit and test the service card and detailed page.'
])
add_note(doc, 'Example', 'If a new beauty service called “Loc Styling” is added, place it in the Hair list inside division 01. Do not create a new division just for one service.', 'safe')

page_break(doc)

# 7 PAGE OWNERSHIP
add_heading(doc, '7. Page-by-Page Update Guide', 1)
page_rows = [
('Home','pages-primary.js + unity.js','Core hero wording, service overview, featured work, Academy, partnership; unity.js replaces hero visual and adds connected experience showcase.'),
('About','pages-primary.js','Story, mission, vision, promise, values, professional journey, professional development, brand architecture.'),
('Beauty','pages-primary.js','Beauty hero, beauty experience, service groups and planning.'),
('Bridal & Events','page-bridal.js','Bridal packages, wedding glam team, destination/VIP positioning and event beauty flow.'),
('Business Solutions','pages-business.js','Administrative support, business services and support categories.'),
('Social Media','pages-business.js','Content direction, page management, customer engagement and service list.'),
('Elyra Academy','pages-business.js','Training tracks, scheduling structure, certificate wording and registration form.'),
('Elyra Store','pages-business.js','Shop categories, product enquiry wording and email/WhatsApp enquiry links.'),
('Consulting','pages-business.js','Consulting areas and service descriptions.'),
('Portfolio','pages-connect.js + enhancements.js','Portfolio categories, transformation framework, real-testimonial and permission section.'),
('Resources','pages-connect.js','Article cards, article text and resource themes.'),
('Partners','pages-connect.js','Eragonova partnership page and collaboration explanation.'),
('Client Portal','pages-connect.js','Public portal explanation only — not a real login backend.'),
('Contact','pages-connect.js + enhancements.js','Contact page, email-first form, WhatsApp secondary, policy notice.'),
('Policies','enhancements.js','Privacy, Terms, Booking/Cancellation, Store/Returns.'),
]
add_table(doc, ['Page', 'Edit here', 'What to change there'], page_rows, widths=[Cm(3.3),Cm(4.3),Cm(9.5)], small=True)

add_heading(doc, '7.1 Homepage special note', 2)
add_body(doc, 'The Home page is intentionally layered. pages-primary.js builds the original Home page. unity.js then changes the hero image and inserts the “Explore the Elyra Experience” section. If you change a Home image in pages-primary.js and do not see the result, check unity.js because it may be overriding that part afterward.')
add_note(doc, 'Script order matters', 'index.html loads the files in a specific order. unity.js and enhancements.js depend on earlier page files already existing. Reordering scripts can stop parts of the site from working.', 'danger')

page_break(doc)

# 8 IMAGES
add_heading(doc, '8. Logos and Images', 1)
add_heading(doc, '8.1 Official logo files', 2)
logo_rows = [
('assets/logo-horizontal.webp','Website header and footer'),('assets/logo-emblem.webp','Favicon, hero overlays, small brand applications'),('assets/logo-crest.webp','Secondary brand applications'),('assets/logo-monogram.webp','Product/brand decorative use')
]
add_table(doc, ['File', 'Current use'], logo_rows)
add_heading(doc, '8.2 Current image map', 2)
image_rows = [
('MEDIA.beauty','assets/Image Oct 12, 2026, 06_20_48 PM-1.png','Beauty lifestyle'),
('MEDIA.bridal','assets/Image Oct 12, 2026, 06_20_51 PM-2.png','Bridal'),
('MEDIA.store','assets/Image Oct 12, 2026, 06_20_53 PM-3.png','Beauty products'),
('MEDIA.academy','assets/Image Oct 12, 2026, 06_20_55 PM-4.png','Academy/training'),
('MEDIA.social','assets/Image Oct 12, 2026, 06_20_57 PM-5.png','Social/digital'),
('MEDIA.business','assets/Image Oct 12, 2026, 06_20_58 PM-6.png','Business/admin'),
('MEDIA.about','assets/Image Oct 12, 2026, 07_51_32 PM-1.png','About/brand story'),
('MEDIA.consulting','assets/Image Oct 12, 2026, 07_51_34 PM-2.png','Consulting/strategy'),
('MEDIA.portal','assets/Image Oct 12, 2026, 07_51_36 PM-3.png','Client Portal dashboard visual'),
('MEDIA.resources','assets/Image Oct 12, 2026, 07_51_38 PM-4.png','Resources & Blog'),
('MEDIA.contact','assets/Image Oct 12, 2026, 07_51_40 PM-5.png','Booking/client care'),
('MEDIA.portfolio','assets/Image Oct 12, 2026, 07_51_42 PM-6.png','Beauty portfolio collage and current Home hero'),
('MEDIA.storePremium','assets/Image Oct 12, 2026, 08_12_15 PM-1.png','Premium Store showcase'),
]
add_table(doc, ['Key used in code', 'Actual file', 'Purpose'], image_rows, widths=[Cm(3.2),Cm(7.9),Cm(6.0)], small=True)
add_heading(doc, '8.3 To replace an image', 2)
add_steps(doc, [
    'Prepare the new image. Use a clear landscape image where possible; WebP is preferred for smaller file size, but PNG/JPG can work.',
    'Upload the new file into assets/ in GitHub.',
    'Open core.js and find MEDIA.',
    'Replace the old filename with the new filename for the correct key.',
    'Commit, wait for deployment, and check the page on desktop and phone.'
])
add_note(doc, 'Better than overwriting', 'For important changes, upload the new image with a new clear filename and update the MEDIA mapping. This makes rollback easier than silently replacing a file with the same name.', 'safe')

page_break(doc)

# 9 CONTACT + FORMS
add_heading(doc, '9. Contact, Booking and Form Behaviour', 1)
add_body(doc, 'Email is the main contact method. WhatsApp is the second option. This is implemented across the Contact page, Academy registration and Store enquiries.')
add_heading(doc, '9.1 Current behaviour', 2)
add_bullets(doc, [
    'Primary email: elyrasuite@gmail.com.',
    'Secondary WhatsApp: +233 53 124 6233.',
    'The website does not currently send form data to a private server.',
    'When a visitor completes a form, the website prepares a message for the visitor’s email app.',
    'WhatsApp buttons prepare a message and open WhatsApp as an alternative.'
])
add_heading(doc, '9.2 If you want a real web form later', 2)
add_body(doc, 'A “real web form” means the visitor submits directly on the website and Elyra receives the message even if the visitor has no email app configured. This requires a form service or backend.')
add_bullets(doc, [
    'Simple option: a trusted form service such as Formspree or an equivalent provider.',
    'Advanced option: a custom backend that stores messages and sends notifications.',
    'Before enabling storage, update the Privacy Policy to explain what is collected and where it is processed.',
    'Never place private API keys, payment secrets or passwords directly in public GitHub files.'
])
add_note(doc, 'Technical-change boundary', 'Changing the wording of the form is a normal content edit. Connecting a database, mail server or private API is a technical/backend change.', 'danger')

page_break(doc)

# 10 OPERATIONS
add_heading(doc, '10. Academy, Store, Resources, Portfolio and Testimonials', 1)
add_heading(doc, '10.1 Academy updates', 2)
add_body(doc, 'Academy content is in pages-business.js. Current tracks include Wig Making, Wig Installation, Makeup Artistry, Nail Technology, Office Administration, Customer Service, Business Management Basics and Entrepreneurship.')
add_bullets(doc, [
    'To add a new training track, add it to the tracks array and also place it under the appropriate Beauty or Business Training display section.',
    'When real dates are available, replace the general “request next cohort” wording with confirmed dates and registration deadlines.',
    'Only describe a certificate as accredited if there is genuine accreditation. Otherwise use programme completion or Elyra-issued completion wording.'
])
add_heading(doc, '10.2 Store updates', 2)
add_body(doc, 'The Store is currently enquiry-based, not a live e-commerce checkout. Product categories are defined in pages-business.js.')
add_bullets(doc, [
    'To add a product category, add a new entry to the products list.',
    'To show real prices, add prices only when they are confirmed and maintain them consistently.',
    'If stock changes frequently, consider a proper e-commerce system rather than manually editing code every day.',
    'If online payments are added, use a secure payment provider and never expose secret keys in the repository.'
])
add_heading(doc, '10.3 Resources / Blog updates', 2)
add_body(doc, 'Resources are currently simple expandable guides inside pages-connect.js. Each article is stored as category, title and two text sections.')
add_bullets(doc, [
    'For a small number of articles, continue adding them to the articles list.',
    'If the blog grows substantially, move to a proper content system or individual article pages.',
    'Keep advice practical and avoid publishing medical, legal or financial claims without appropriate review.'
])
add_heading(doc, '10.4 Portfolio and testimonials', 2)
add_body(doc, 'Portfolio categories live in pages-connect.js. The genuine-testimonial collection section is added by enhancements.js.')
add_bullets(doc, [
    'Real client photos should be added with permission.',
    'Before/after examples should clearly be the same service/client and should not be misleadingly edited.',
    'Testimonials should be genuine and published with permission and preferred attribution.',
    'Do not invent star ratings, clients, student numbers, celebrities, results or business achievements.'
])

page_break(doc)

# 11 PARTNERS PORTAL
add_heading(doc, '11. Strategic Partnership and Client Portal', 1)
add_heading(doc, '11.1 Eragonova Enterprise partnership', 2)
add_body(doc, 'The partner identity is defined in core.js inside ERAGONOVA. The Home partnership block is in pages-primary.js and the dedicated Partners page is in pages-connect.js. The two brands are presented as independent strategic partners.')
add_code(doc, "ERAGONOVA = name + tagline + relationship type + website URL + logo URL")
add_bullets(doc, [
    'If the Eragonova website URL changes, update it in core.js.',
    'If the Eragonova logo path changes, update the logo URL in core.js.',
    'If the partnership scope changes, update the wording on both the Home block and Partners page.',
    'Do not change the relationship wording to imply ownership, merger or group structure unless that becomes factually correct.'
])
add_heading(doc, '11.2 Client Portal status', 2)
add_body(doc, 'The Client Portal is now a secure, authenticated Supabase-backed portal. Access is limited to authorized users and data is protected by Row Level Security. The public site does not offer open account registration.')
add_table(doc, ['Portal area', 'Current status'], [
('Authentication and account access','Live through Supabase Auth; accounts are administered, not openly self-registered.'),('Account-specific records','Protected using role and account membership rules.'),('Testimonials moderation','Admin-only review controls are provided in the secure portal.'),('Online checkout and payments','Not implemented; do not advertise as available.')
])
add_note(doc, 'Security warning', 'Do not put passwords, service-role keys, private API keys or client records in browser-delivered files or public assets. Preserve Supabase Auth and Row Level Security; do not create a fake client-side login.', 'danger')

page_break(doc)

# 12 POLICIES
add_heading(doc, '12. Legal and Policy Pages', 1)
add_body(doc, 'The policy pages are in enhancements.js. They are written as practical general website policies and should be reviewed whenever the business model changes materially.')
policy_rows = [
('Privacy Policy','#/privacy','Information collected through enquiries, email/WhatsApp, sharing, retention and visitor choices.'),
('Website & Service Terms','#/terms','General website information, confirmations, pricing, responsibilities, IP, third-party services.'),
('Booking & Cancellation','#/bookingpolicy','Booking confirmation, rescheduling, cancellation, lateness, bridal/events and Academy.'),
('Store & Returns','#/returnspolicy','Product enquiries, custom/hygiene products, damaged items, order changes, delivery and refunds.')
]
add_table(doc, ['Policy', 'Route', 'Covers'], policy_rows)
add_heading(doc, '12.1 When to update policies', 2)
add_bullets(doc, [
    'If analytics/cookies are enabled.',
    'If a real web form or database starts storing personal data.',
    'If online payments or e-commerce checkout are introduced.',
    'If deposit, cancellation or refund rules become fixed business policies.',
    'If delivery/returns procedures become standardised.',
    'If the business expands into a new legal jurisdiction or uses new third-party processors.'
])
add_body(doc, 'When policy wording changes, also change policyUpdated at the top of enhancements.js to the new date.')
add_note(doc, 'Legal review', 'These website policies are operational website text, not a substitute for advice from a qualified lawyer. As transactions, training, staff, e-commerce or data processing grow, have the policies reviewed professionally.', 'warn')

page_break(doc)

# 13 SEO
add_heading(doc, '13. Search Engine and Social Sharing (SEO)', 1)
add_body(doc, 'SEO means helping search engines and social platforms understand what each page is about. Elyra Suite currently has a basic SEO layer without paid tools.')
add_heading(doc, '13.1 Where SEO information lives', 2)
add_table(doc, ['File', 'Purpose'], [
('seo.js','Different page titles/descriptions for each route.'),('index.html','General description, social-share image, canonical URL and structured business data.'),('robots.txt','Allows crawling and points to the sitemap.'),('sitemap.xml','Lists the main website address for crawlers.')
])
add_heading(doc, '13.2 To change a page’s search title or description', 2)
add_steps(doc, [
    'Open seo.js.',
    'Find the route name, for example beauty, academy or contact.',
    'Edit the title and description text only.',
    'Keep titles clear and descriptions natural; do not stuff the same keyword repeatedly.',
    'Commit and test the browser tab title after deployment.'
])
add_heading(doc, '13.3 If the website moves to a custom domain', 2)
add_bullets(doc, [
    'Update SEO_BASE in seo.js.',
    'Update canonical URL, og:url, social image URL, Organization url/logo/image in index.html.',
    'Update sitemap.xml and robots.txt.',
    'Configure the domain in GitHub Pages and at the domain registrar.',
    'Retest every page, email link, social preview and partnership link.'
])

page_break(doc)

# 14 ANALYTICS SOCIAL DOMAIN
add_heading(doc, '14. Analytics, Social Media, Custom Domain and Professional Email', 1)
add_heading(doc, '14.1 Google Analytics', 2)
add_body(doc, 'analytics.js is ready but inactive. The current line is:')
add_code(doc, "const ELYRA_ANALYTICS_ID='';")
add_body(doc, 'When a real Google Analytics measurement ID is created, paste the value between the quotation marks, for example G-XXXXXXXXXX. Then update the Privacy Policy to explain analytics and any cookies/identifiers that are actually used.')
add_note(doc, 'Do not invent an analytics ID', 'Only use the ID from the business’s real analytics property. Until then, keeping the value blank means no Google Analytics script loads.', 'safe')
add_heading(doc, '14.2 Adding official social media links', 2)
add_steps(doc, [
    'Confirm the official Instagram, Facebook, TikTok, LinkedIn or YouTube URLs.',
    'Add the links to the footer/contact area in core.js or the relevant page.',
    'Optionally add a sameAs list in the Organization structured data inside index.html so search systems can associate the profiles with Elyra Suite.',
    'Test every link from the live website.'
])
add_heading(doc, '14.3 Moving to a custom domain', 2)
add_body(doc, 'A custom domain is optional. The current GitHub Pages address is fully functional. When ready, a domain such as elyrasuite.com or a suitable Ghana domain can be purchased from a domain registrar.')
add_steps(doc, [
    'Buy the domain from a reputable registrar.',
    'In GitHub repository Settings → Pages, add the custom domain.',
    'At the domain registrar, add the DNS records GitHub provides/requires.',
    'Wait for DNS verification and HTTPS activation.',
    'Update the SEO locations listed in Section 13.3.'
])
add_heading(doc, '14.4 Professional domain email', 2)
add_body(doc, 'After a custom domain exists, the business may create addresses such as hello@elyrasuite.com or bookings@elyrasuite.com using Google Workspace, Microsoft 365, Zoho Mail or another provider. Keep the current Gmail active during transition, then update BRAND.email and index.html once the new address is fully tested.')

page_break(doc)

# 15 NEW PAGE FEATURE
add_heading(doc, '15. How to Add a New Page, Service, Product or Article', 1)
add_heading(doc, '15.1 Adding a small service', 2)
add_body(doc, 'For a service that belongs to an existing division, do not create a new page. Add the service to the correct list in core.js. This is the safest and simplest change.')
add_heading(doc, '15.2 Adding a completely new page', 2)
add_steps(doc, [
    'Create a new page function in the most logical page JavaScript file.',
    'Add the function to the pages object in pages-connect.js so the router knows the page exists.',
    'Add the visible link to nav or more in core.js.',
    'Add a matching title/description entry in seo.js.',
    'Add any required images to assets/ and MEDIA in core.js.',
    'If the page needs special styling, add only the necessary styles to styles.css/media.css.',
    'Deploy and test every route, especially the mobile menu.'
])
add_note(doc, 'This is an AMBER change', 'Adding a page crosses several files. A non-technical owner can plan the content, but it is safer to have the code update reviewed if the route or script logic is unfamiliar.', 'warn')
add_heading(doc, '15.3 Adding a new Store category', 2)
add_body(doc, 'Edit the products list inside the shop() function in pages-business.js. Add the display name, short description and a brand-art filename. The email and WhatsApp enquiry buttons are generated for each category.')
add_heading(doc, '15.4 Adding a new Resource article', 2)
add_body(doc, 'Edit the articles list inside resources() in pages-connect.js. Use the same four-part pattern: category, article title, first paragraph, second paragraph.')

page_break(doc)

# 16 GITHUB UI
add_heading(doc, '16. Editing the Website in GitHub — Non-Technical Steps', 1)
add_heading(doc, '16.1 Editing text in a file', 2)
add_steps(doc, [
    'Open the repository: github.com/Edward-Wonder-Mordey/elyra-suite-website.',
    'Click the file named in this handbook.',
    'Click the pencil/Edit button.',
    'Use the browser Find command (Ctrl+F) to find the exact phrase you want to change.',
    'Change only the intended text.',
    'Click Commit changes.',
    'Write a short, clear message describing what changed.',
    'Commit to the main branch for routine approved updates.',
    'Open the Actions tab and wait for “Deploy Elyra Suite Website” to complete successfully.',
    'Open the live site and verify the result.'
])
add_heading(doc, '16.2 Uploading a new image', 2)
add_steps(doc, [
    'Open the assets folder in GitHub.',
    'Choose Add file → Upload files.',
    'Upload the image with a clear filename.',
    'Commit the upload.',
    'Then edit core.js MEDIA so the website points to the new filename.',
    'Commit again and test.'
])
add_heading(doc, '16.3 Updating this Word handbook', 2)
add_steps(doc, [
    'Open the docs folder in the repository.',
    'Download Elyra_Suite_Website_Owners_Handbook.docx.',
    'Edit it in Microsoft Word.',
    'Update the version/date and change log near the end of the document.',
    'Save the file with the same filename.',
    'Upload the updated file to docs/ as the replacement version and commit it with a message such as “Update website owner handbook”.'
])
add_note(doc, 'Why this Word file is different', 'GitHub can display many text files directly, but a .docx is a binary Word file. It is normally edited in Word and uploaded back, not edited inside GitHub’s text editor.', 'info')

page_break(doc)

# 17 DEPLOYMENT
add_heading(doc, '17. Deployment, Cache and Troubleshooting', 1)
add_heading(doc, '17.1 What publishes the website', 2)
add_body(doc, 'Every commit to the main branch triggers .github/workflows/deploy-pages.yml. The workflow checks out the repository, prepares GitHub Pages, uploads the site and deploys it to the public URL.')
add_bullets(doc, [
    'Green success in Actions = GitHub completed the deployment.',
    'A queued/in-progress status means wait; the site may still show the previous version.',
    'If a newer commit is pushed quickly, an older deployment may be cancelled because the workflow intentionally keeps only the newest Pages deployment.'
])
add_heading(doc, '17.2 If the site does not show the change', 2)
add_steps(doc, [
    'Confirm the latest GitHub Actions run succeeded.',
    'Hard-refresh the browser: Ctrl+F5 on Windows.',
    'Try a private/incognito window.',
    'Check that the filename and route were typed exactly, including capitalisation and spaces.',
    'If JavaScript/CSS is still cached, update the version query in index.html, for example ?v=20261012-2208 to a newer unique value. Use the same version on all CSS and JS script lines.',
    'If the site breaks, restore the previous file from GitHub History.'
])
add_heading(doc, '17.3 If an image does not appear', 2)
add_bullets(doc, [
    'Confirm it is actually inside assets/.',
    'Confirm core.js MEDIA points to the exact filename.',
    'Check spaces, commas, underscores, capital letters and file extension.',
    'Check whether unity.js overrides the homepage visual.',
    'Hard-refresh after deployment.'
])
add_heading(doc, '17.4 If the whole site stops loading', 2)
add_bullets(doc, [
    'The most common cause is a JavaScript syntax error: a missing quote, bracket, comma or backtick.',
    'Restore the last working file version from GitHub History before making additional edits.',
    'Do not keep stacking new changes on top of a broken version.'
])

page_break(doc)

# 18 SAFETY/MAINTENANCE
add_heading(doc, '18. Safe Maintenance and Future Growth', 1)
add_heading(doc, '18.1 Things that are safe to manage routinely', 2)
add_bullets(doc, [
    'Text wording, spelling and service descriptions.',
    'Contact details when updated in all required locations.',
    'Images and portfolio categories.',
    'Resource article content.',
    'Academy programme wording and confirmed dates.',
    'Policy text after business/legal review.',
    'SEO titles and descriptions.'
])
add_heading(doc, '18.2 Things that should be treated as technical projects', 2)
add_bullets(doc, [
    'Real user login/client portal.',
    'Online payments, Mobile Money or card checkout.',
    'Private database and document storage.',
    'Automated invoice/account system.',
    'Password reset, roles and permissions.',
    'Custom API integrations.',
    'Changing hosting/deployment architecture.',
    'Moving from hash routes to a different framework/router.'
])
add_note(doc, 'Security rule', 'Never store passwords, secret API keys, payment keys, private client documents, ID documents or confidential records in this public repository.', 'danger')
add_heading(doc, '18.3 Recommended monthly website check', 2)
add_bullets(doc, [
    'Open every main navigation page once.',
    'Test the email button and one WhatsApp button.',
    'Check mobile layout on a real phone.',
    'Confirm contact details are current.',
    'Confirm Store/Academy information is still accurate.',
    'Replace outdated promotions or dates.',
    'Check that partner links work.',
    'Check the latest GitHub deployment status.',
    'Add genuine portfolio/testimonial content when permission is available.'
])
add_heading(doc, '18.4 Recommended quarterly check', 2)
add_bullets(doc, [
    'Review all policy pages.',
    'Review SEO titles/descriptions.',
    'Review Analytics setup if enabled.',
    'Download a repository ZIP as an extra backup before major changes.',
    'Review whether the current static Store/Portal still fits the business volume.'
])

page_break(doc)

# APPENDIX A SERVICE CATALOG
add_heading(doc, 'Appendix A — Current Service Catalog Snapshot', 1)
add_heading(doc, 'A.1 Beauty & Personal Care', 2)
add_body(doc, 'Hair: Custom Wig Creation; Luxury Wig Sales; Wig Revamp & Restoration; Hair Installations; Hair Colouring; Bridal Hair Styling; Protective Styling; Treatment Services.')
add_body(doc, 'Makeup: Bridal Makeup; Event Makeup; Photoshoot Makeup; Fashion Makeup; Graduation Makeup; Corporate Makeup.')
add_body(doc, 'Nails: Luxury Manicures; Spa Pedicures; Acrylic Nails; Gel Nails; BIAB Nails; Nail Art; Press-On Nail Collections.')
add_heading(doc, 'A.2 Beauty Products Store', 2)
add_body(doc, 'Collections: Wigs; Hair Extensions; Hair Care Products; Nail Care Products; Beauty Accessories; Cosmetics; Makeup Tools.')
add_body(doc, 'Signature Product Lines: Elyra Hair Oil; Elyra Edge Control; Elyra Lash Collection; Elyra Press-On Nail Collection; Elyra Beauty Kits.')
add_heading(doc, 'A.3 Bridal & Events', 2)
add_body(doc, 'Services: Bridal Packages; Wedding Beauty Coordination; Bridal Team Services; Engagement Beauty Packages; Traditional Marriage Packages; Corporate Event Makeup.')
add_body(doc, 'VIP: Wedding Day Glam Team; Destination Weddings; Celebrity Styling; Executive Beauty Services. This list describes offered capability; it does not claim celebrity clients.')
add_heading(doc, 'A.4 Administrative Support', 2)
add_body(doc, 'Virtual Assistant Services; Email Management; Calendar Management; Data Entry; Appointment Scheduling; Customer Service Support; Document Preparation; Microsoft Office Services. Target sectors currently include Small Businesses, Churches, NGOs, Entrepreneurs and Consultants.')
add_heading(doc, 'A.5 Business Support Services', 2)
add_body(doc, 'Business Registration Guidance; Business Documentation; Company Profiles; Business Plans; Proposal Writing; Quotations & Invoices; Policy Documentation; Administrative Systems Setup.')
add_heading(doc, 'A.6 Social Media Management', 2)
add_body(doc, 'Content Creation; Page Management; Facebook Marketing; Instagram Marketing; TikTok Management; Customer Engagement; Brand Strategy. Target sectors currently include Beauty Brands, Startups, Restaurants, Churches and SMEs.')
add_heading(doc, 'A.7 Elyra Academy', 2)
add_body(doc, 'Beauty Training: Wig Making; Wig Installation; Makeup Artistry; Nail Technology.')
add_body(doc, 'Business Training: Office Administration; Customer Service; Business Management Basics; Entrepreneurship.')
add_body(doc, 'Delivery: Physical Classes; Online Courses; Video Tutorials; Certification Programmes. Use careful wording around accreditation and certificates.')
add_heading(doc, 'A.8 Corporate Consulting', 2)
add_body(doc, 'Operations Consulting; Administrative Systems; Organisational Planning; Business Process Improvement; Customer Experience Consulting.')

page_break(doc)

# APPENDIX B CURRENT STATUS
add_heading(doc, 'Appendix B — Current Functional Status', 1)
status_rows = [
('Email enquiries','LIVE','Primary contact method; mailto-based.'),('WhatsApp enquiries','LIVE','Secondary option.'),('GitHub Pages hosting','LIVE','Automatic deployment from main.'),('Responsive/mobile layout','LIVE','Controlled by styles.css and media.css.'),('Policies','LIVE','Privacy, Terms, Booking/Cancellation, Store/Returns.'),('SEO metadata','LIVE','Base metadata + route-specific titles/descriptions.'),('Analytics','READY, NOT ACTIVE','analytics.js contains no measurement ID yet.'),('Portfolio structure','LIVE','Representative brand visuals + framework for genuine work.'),('Testimonials','LIVE — MODERATED','Portfolio form submits to Supabase; public page shows only approved submissions with consent.'),('Store','ENQUIRY-BASED','No cart, checkout or payment system.'),('Academy registration','ENQUIRY-BASED','Email-first registration request; no student database.'),('Client / admin portal','LIVE — AUTHENTICATED','Supabase Auth, role/account access and Row Level Security; testimonial moderation is admin-only.'),('Online checkout/payments','NOT IMPLEMENTED','Store is enquiry-led; no online payment processor.'),('Custom domain','NOT YET CONNECTED','Current GitHub Pages URL remains live.'),('Professional domain email','NOT YET CONNECTED','Current Gmail remains primary.'),('Official social links','ADD WHEN CONFIRMED','Only add verified official accounts.'),
]
add_table(doc, ['Feature', 'Status', 'Meaning'], status_rows, widths=[Cm(4.6),Cm(3.7),Cm(8.8)], small=True)

page_break(doc)

# APPENDIX C CHANGE LOG
add_heading(doc, 'Appendix C — Website and Handbook Change Log', 1)
add_body(doc, 'Use this table whenever an important website or handbook update is made. Keeping a simple log helps future owners understand why something changed.')
change_rows = [
('12 Oct 2026','1.0','Initial owner handbook created after public website completion, partnership integration, email-first contact, image expansion, policies, SEO and analytics readiness.','Website team'),
('','','','',''),('','','','',''),('','','','',''),('','','','',''),('','','','','')
]
add_table(doc, ['Date', 'Version', 'Change made', 'Updated by'], [r[:4] for r in change_rows], widths=[Cm(3.0),Cm(2.2),Cm(9.0),Cm(3.0)], small=True)
add_heading(doc, 'C.1 Version naming suggestion', 2)
add_body(doc, 'Use simple version numbers. For example: 1.1 for a small handbook update, 1.2 for another small update, and 2.0 if the website architecture changes significantly (for example, moving to e-commerce or a real client portal).')
add_heading(doc, 'C.2 Final owner checklist before publishing any major change', 2)
add_bullets(doc, [
    'Is the information true and current?',
    'Does the change accidentally imply clients, staff, awards, accreditation or results that have not been verified?',
    'Have email, phone, links and dates been tested?',
    'Does the page still look good on a phone?',
    'Did the latest GitHub Pages deployment succeed?',
    'If personal data, payments or logins are involved, has the privacy/security impact been reviewed?',
    'Does this handbook also need updating?'
])
add_note(doc, 'Keep this handbook with the website', 'The goal is that a future owner, assistant, designer or developer can understand the Elyra Suite website without having to rediscover how it was built.', 'brand')


# 16 CURRENT CLIENT REVIEW AND ADMIN PORTAL
add_heading(doc, '16. Client Reviews and the Secure Admin Portal', 1)
add_body(doc, 'The Portfolio page includes a real client-feedback form. Submissions go to Elyra Suite for review. The public page displays only submissions that have been approved and have publication consent. The form is not a promise of instant publication.')
add_table(doc, ['Area', 'Current file / system', 'Owner guidance'], [
('Portfolio review section','pages-connect.js','Contains the Portfolio route, approved feedback display and submission form. Keep it truthful and test it after edits.'),
('Secure owner portal','portal-secure.js, loaded by the portal route','Uses Supabase Auth and role-based access. The Testimonials tab is for the admin role.'),
('Database moderation rules','supabase/migrations/20261020170457_create_elyra_testimonial_moderation.sql','Defines the testimonials data and Row Level Security. Apply backend changes through a reviewed migration; do not hand-edit production data as a workaround.'),
('Public configuration','site-config.js','Contains only browser-safe project URL and publishable key values. Never put a service-role key or password in a public file.')
], widths=[Cm(3.6), Cm(5.5), Cm(8.4)], small=True)
add_heading(doc, '16.1 Review, approve or remove feedback', 2)
add_steps(doc, [
'Sign in to the Elyra Suite admin portal using an authorized admin account.',
'Open the Testimonials tab and inspect each submission.',
'Approve only genuine client feedback when the client agreed that it can be published. Reject unsuitable submissions.',
'Use unpublish or return-to-review controls if a published item must be hidden or reviewed again.',
'Check the public Portfolio page after approval. Only approved feedback with publication consent should appear.'
])
add_note(doc, 'Evidence and consent', 'Never invent testimonials, clients, outcomes, before-and-after results or review screenshots. Keep submissions private until approval. If a client withdraws permission, unpublish the feedback promptly.', 'safe')
add_heading(doc, '16.2 Current system status', 2)
add_body(doc, 'The owner/client portal is now backed by Supabase authentication, account records and Row Level Security. The admin portal contains a review queue for client feedback. The site does not provide a public account-registration path. Product checkout and online payment processing are still not implemented.')
add_table(doc, ['Feature', 'Current status', 'Meaning'], [
('Email and WhatsApp enquiries','LIVE','Email is primary; WhatsApp is secondary.'),
('GitHub Pages hosting','LIVE','Changes on main trigger a GitHub Actions deployment.'),
('Responsive layout and policy pages','LIVE','Test service and policy page changes on mobile.'),
('SEO metadata','LIVE','Route-specific metadata is generated from the current SEO configuration.'),
('Analytics','READY, NOT ACTIVE','Only enter a real measurement ID after one is created.'),
('Portfolio feedback','LIVE — MODERATED','Public form; only approved, consented feedback is visible. No fabricated review content.'),
('Admin/client portal','LIVE — AUTHENTICATED','Supabase Auth and Row Level Security; access depends on assigned role/account.'),
('Store checkout / online payments','NOT IMPLEMENTED','The store is enquiry-led; do not promise online checkout or payment processing.'),
('Academy enrolment','ENQUIRY-BASED','No public student account system is documented.'),
('Custom domain and professional email','NOT CONNECTED','Use the current GitHub Pages URL and Gmail.')
], widths=[Cm(4.1), Cm(3.8), Cm(9.6)], small=True)
add_body(doc, 'Backend project ref: kqpbdagawllgonzoloao. Keep the Elyra database and its credentials separate from Eragonova. The GitHub Pages workflow uses the existing checked-in guide PDF if temporary guide decoding is not available.')

# Header after content - section first page remains different
header = doc.sections[0].header
p = header.paragraphs[0]
p.text = 'ELYRA SUITE  |  WEBSITE OWNER’S HANDBOOK'
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
style_paragraph_runs(p, color=PLUM, size=7.5, bold=True)

# Make first page footer minimal
fp = doc.sections[0].first_page_footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r=fp.add_run('Elyra Suite • Beauty • Business • Excellence')
set_run_font(r); r.font.size=Pt(8); r.font.color.rgb=RGBColor.from_string(ROSE)

# Basic metadata
props = doc.core_properties
props.title = 'Elyra Suite Website Owner’s Handbook'
props.subject = 'Plain-language guide to updating and maintaining the Elyra Suite website'
props.author = 'Elyra Suite'
props.keywords = 'Elyra Suite, website handbook, GitHub Pages, maintenance, owner guide'

# Avoid orphan headings by setting headings already; save
for _tbl in doc.tables:
    for _ri, _row in enumerate(_tbl.rows):
        _trpr=_row._tr.get_or_add_trPr()
        _cant=OxmlElement('w:cantSplit')
        _trpr.append(_cant)
        if _ri==0:
            _hdr=OxmlElement('w:tblHeader'); _hdr.set(qn('w:val'),'true'); _trpr.append(_hdr)
doc.save(OUT)
print(OUT)
