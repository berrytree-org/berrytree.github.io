# Berrytree.org Change Log

---

## 2026-04-08 (Session 4) — PLAN List Complete: All 24 Items Resolved

### Summary
Full staff session to close out the remaining 10 PLAN items from the April 2nd bug hunt (A5 deferred by Aaron). Completed 9 fixes spanning Schema.org structured data, accessibility alt text, CSS compatibility, external link repair, timeline cross-linking, genealogical content corrections, and page expansion. Aaron manually audited all fixes via localhost. Seven pages stamped with qc_owner. The PLAN list is now 24/24 complete.

### Technical Fixes
- **R19** — Ancestor-profile image alt text now reads "Portrait of [Name]" instead of just the name
- **R22** — Breadcrumb shortcode now emits Schema.org BreadcrumbList JSON-LD structured data on every page
- **V15** — Leaf divider `✦` (U+2726) given explicit font-family fallback stack for older systems
- **A14** — "Explore in the Berry Family Timeline" link auto-renders on ancestor pages with `families` front matter; timeline already links back via ancestor badges

### External Link Fixes (S23/S37)
- All 5 cemeterycensus.com references upgraded from HTTP to HTTPS
- Fixed `.html` extension to `.htm` in ch01 (was returning 404)
- Fixed `/nc/org/` typo to `/nc/orng/` in ch02 (was returning 404)
- Site confirmed alive with proper 301 redirects; no Wayback Machine archives exist

### Content Fixes
- **M6** — Removed unsupported "worldwide flu epidemic of 1858" claim from joshua-berry-sr.md; kept death year; added Martha's editorial comment in HTML
- **M7** — Expanded elizabeth-berry.md from 65 to ~90 lines: added bastardy bond (Aug 1791), will probate (May 1815, Person County), daughter Mary's marriage to Thomas Berry, grandson Josiah, Key Documents section, Notable Descendants section. Updated birth year to c. 1768 and death info per Chapter 8.
- **M8** — Added cross-reference notes on both Elizabeth Berry and Elizabeth Leathers Berry pages identifying the same William Riley as father of children by both women

### Additional Fixes
- Linked Ira Berry from Lewis Berry entry on joshua-berry-sr.md
- Bolded Elizabeth Leathers Berry name/link on elizabeth-berry.md

### QC Stamps
Seven pages stamped `qc_owner: 2026-04-08` after Aaron's manual audit:
robert-berry-oc, joshua-berry-sr, elizabeth-berry, elizabetheathersberrync, fiddletoncemetery, ch01, ch02

### Files Modified
- `layouts/_shortcodes/ancestor-profile.html` — R19 alt text, A14 timeline link
- `layouts/_shortcodes/breadcrumb.html` — R22 Schema.org JSON-LD
- `assets/_custom.scss` — V15 font fallback, A14 timeline link style
- `content/ancestors/joshua-berry-sr.md` — M6 correction, Ira Berry link, qc_owner stamp
- `content/ancestors/elizabeth-berry.md` — M7 expansion, M8 cross-ref, bold link, qc_owner stamp
- `content/ancestors/elizabetheathersberrync.md` — M8 cross-ref, qc_owner stamp
- `content/ancestors/robert-berry-oc.md` — qc_owner stamp
- `content/ancestors/fiddletoncemetery.md` — S37 HTTPS, qc_owner stamp
- `content/indexes/extended-site-map.md` — S37 HTTPS
- `content/books/frontier-america/ch01-williamsons-fosters-berrys-kemps.md` — S23 .html→.htm, S37 HTTPS, qc_owner stamp
- `content/books/frontier-america/ch02-robert-berry.md` — S23 /org/→/orng/, S37 HTTPS, qc_owner stamp

### Decisions Made
1. A5 (Open Graph/Twitter Cards) deferred by Aaron — dropped from this session
2. M6 flu epidemic: remove unsupported claim, preserve death year, add editorial comment
3. M7 Elizabeth Berry: source expansion content from Chapter 8 of the book
4. M8 William Riley: confirmed same person, cross-referenced both pages
5. S23/S37: site alive, HTTPS works, fix broken URLs rather than add Wayback fallbacks

---

## 2026-04-08 (Session 3) — Genealogy Source Review, PLAN List Audit & Fixes, Font Size Improvements

### Summary
Full team session focused on completing Martha's qc_genealogy source verification pass across all 194 ancestor and family-lines pages. Reviewed every page for source citations, stamped 72 as passing, logged 122 failures to a CSV for future remediation. Then audited the 24-item PLAN list from the April 2nd bug hunt, found 10 already fixed or partially fixed, and knocked out 8 more in-session. Closed with font-size improvements for elderly visitors.

### qc_genealogy Source Review
- **194 pages reviewed** (183 ancestors + 11 family-lines, after 11 Bucket 1 index pages stamped immediately)
- **72 pages passed** and stamped with `qc_genealogy: 2026-04-08`
- **122 pages failed** — logged to `Project/testing/qc-genealogy-failures.csv` with file, section, issue type, severity, and notes
- **Severity breakdown:** ~35 HIGH, ~65 MEDIUM, ~22 LOW
- **Key finding:** Ben's direct NC line is well-sourced; GA/AL branch pages are weakest; many pages have evidence on-page (census images, headstones) but don't formally cite it in the narrative

### PLAN List Audit
Verified all 24 items from the April 2nd bug hunt against current codebase:
- **Previously fixed (4):** S42 (Shelby DNA consent), V10 (chapter nav), V16 (back-to-top), A20 (documents section)
- **Fixed this session (8):** V18 (will-change on book covers), V8 (book TOC :visited state), R14 (semantic header for book-banner), A24 (lastmod mapping in hugo.toml), M13/M14 (missing _index.md child links), T1 (flexbox gap closed as acceptable risk), R10 (hero subtitle font 0.78→0.85rem), R17 (table font 0.9→0.95rem)
- **Still open (11):** R19, R22, S23/S37, V15, A5, A14, M6, M7, M8

### Files Modified
- `assets/_custom.scss` — will-change on book covers, :visited state on book TOC links, hero-sub font 0.78→0.85rem, table font 0.9→0.95rem
- `layouts/_shortcodes/book-banner.html` — `<div>` changed to `<header role="banner">`
- `hugo.toml` — Added `[frontmatter] lastmod = ['last_updated', ':fileModTime']`
- `content/ancestors/_index.md` — Added 7 missing child page links (M13/M14)
- `Project/tools/update-frontmatter.py` — Fixed YAML spacing bug in `apply_update` (was writing `key:value` instead of `key: value` for blank fields)
- `Project/testing/qc-genealogy-failures.csv` — Created, 122 entries
- `Project/notes/action-items.txt` — Moved sources_verified pass to completed
- `Project/notes/mac-shortcuts.md` — Created, Safari responsive design mode shortcut

### Decisions Made
1. Three-bucket approach for qc_genealogy review: index pages stamped immediately, source pages get light review, biography pages get full review
2. Failures tracked in CSV at Project/testing/ per audit report conventions
3. T1 (flexbox gap) closed as acceptable risk — Safari 14.1 is 5+ years old
4. Font-size bumps approved by Aaron after visual inspection on desktop and mobile

---

## 2026-04-08 (Session 2) — QC System Overhaul, Front Matter Tooling, Action Items Refresh

### Summary
Full staff meeting session focused on QC infrastructure. Built the QC report script, designed and implemented a three-lane QC review system (owner/webteam/genealogy), built a generic YAML/TOML front matter updater tool, migrated all 254 pages from old QC fields to the new system, and refreshed the full action items board.

### New Tools
- **`Project/tools/qc-report.py`** — QC status report generator. Reads front matter, reports by lane/section/structural issues. Flags: `--detail`, `--section`, `--flagged`, `--stale`.
- **`Project/tools/update-frontmatter.py`** — Generic front matter updater. Supports YAML and TOML. Operations: add, remove, rename, update. Dry-run by default, `--write` to apply. Filters by section, field presence, content source, filename glob. Portable to any Hugo site via `--content-dir` and `--format`.

### QC System Changes
- **Removed fields:** `qc_status` (string enum), `qc_date` (date), `sources_verified` (boolean)
- **Added fields:** `qc_owner` (date), `qc_webteam` (date), `qc_genealogy` (date)
- **Logic:** Blank = not reviewed or not yet clean. Date = cleared as of that date. Stale = `last_updated` newer than QC date. Fully cleared = all three dates present and none stale.
- **Migration:** All 254 pages updated via `update-frontmatter.py` in 5 steps, zero errors.
- **Front matter definitions** (`Project/docs/front-matter-definitions.md`) updated with new field specs, rules, and examples.

### Action Items Board
- Refreshed `Project/notes/action-items.txt` — confirmed completed items, closed missing images (no longer referenced), reclassified US Conflicts as QC review (already converted), moved QC report script and US Conflicts to completed.
- **No active HIGH items** for the first time in the project.

### Team
- Adopted team motto: **"We all make each other's lives better."** Added to team interaction map.
- Rebecca's meeting weather: Sunny with a light breeze, upgraded to sunny with zero cloud cover.

---

## 2026-04-08 — Mobile Polish, DNA Collapsible Sections, Explorer Toggles, About Us Portraits

### Summary
A UI refinement session focused on mobile experience, interactive improvements to data-driven pages, and visual upgrades to the About Us page. Also confirmed the book reader addendum is already incorporated into the 2015 revised edition.

### Commits
- `b448807` — Mobile gold hamburger menu icon on subpages (CSS filter in `_custom.scss`)
- `505e3b3` — DNA Research Center: collapsed "Understanding Y-DNA Testing" and "Berry Y-DNA Project" sections by default, made section headers clickable to toggle
- `d1fe908` — All/None category toggles on Wheel of Time and Documents Explorer, removed W.P. Berry image from Robert Berry (OC) page (already displayed on Wiley P. Berry page), fixed mobile landing page hamburger X overlapping panel logo
- `70a91c4` — About Us portraits converted to 200px floated thumbnails with text wrap and click-to-enlarge, added addendum note to book reader Table of Contents

### Other Changes
- **CLAUDE.md** — Added "Page Name Reference" directive under Standing Team Directives
- **Martha's addendum review** — Reviewed the 10-page addendum PDF and confirmed all corrections were already incorporated into the 2015 revised edition in the book reader. No content changes needed.

---

## 2026-04-07 (Session 4) — Children List Markup Cleanup

### Summary
Fixed 9 ancestor pages where children lists used broken formatting — plain text and markdown links inside HTML `<ol class="children-list">` blocks. Hugo doesn't render markdown inside raw HTML, so linked children names were displaying as literal `[text](url)` instead of clickable links. All entries converted to the standard `child-name`/`child-dates`/`child-details` div structure matching the pattern established on John Robert Berry's page.

### Pages Fixed
1. `thomas-person-berry.md` — 2 children lists (first and second marriage)
2. `wiley-p-berry.md` — 8 children
3. `robert-berry-pac.md` — 3 children
4. `robert-berry-oc.md` — 10 children (also converted inline markdown links to HTML `<a>` tags in child-details)
5. `john-cate.md` — 5 children
6. `sarah-cate.md` — 2 children
7. `ira-berry-nc.md` — 6 children
8. `hannahcateberry.md` — 3 children (also fixed garbled UTF-8 replacement characters on a dash)
9. `eleanor-reed.md` — 4 children

### Detection Method
Diffed files containing `class="children-list"` (65) against files containing `class="child-name"` (58) to identify the 7 remaining broken pages. Thomas Person Berry and Wiley P. Berry were caught by visual inspection first.

---

## 2026-04-07 (Session 3) — Project Folder Reorganization

### Summary
Reorganized the `Project/` directory to follow standard project development conventions. Consolidated overlapping directories, moved misplaced files, and codified the folder structure in CLAUDE.md with a standing directive for Pam to enforce correct file placement.

### Changes
- **Deleted:** `OLLAMA.md` (unused), `notes/timeline_data.json` (stale duplicate of `data/timeline_data.json`), all `.DS_Store` files, `tools/__pycache__/`
- **Merged `scripts/` → `tools/`:** Moved `add_unlinked_pills.py` and `link_events.py`, removed empty `scripts/` directory
- **Meeting notes consolidated:** 8 dated files moved from `notes/` → `meetings/`
- **Misplaced files corrected:** `design_criteria.md` → `design/`, `top-20-mistakes-of-amateur-genealogists.md` → `research/`
- **Renamed:** `action_Items.txt` → `action-items.txt` (kebab-case convention)
- **CLAUDE.md updated:** Folder structure reference table added, all paths corrected, Pam's filing enforcement directive added, timestamp updated
- **CSV inventory refreshed** by Tom (254 pages, 0 unconverted)
- **Pre-reorganization backup** created at `Project/backup/berrytree-project-folder-backup.tz` (412 MB)

### Contractors Active
- Tom (CSV inventory)
- Kate (backup creation)

### Files Modified
- `CLAUDE.md` — Folder structure section, path references, Pam's checklist, timestamp
- `Project/notes/change-log.md` — This entry
- `Project/meetings/2026-04-07-session3-meeting-notes.md` — Session notes

---

## 2026-04-07 — Lightbox: Full-Resolution Image Viewer + 30 Image Upgrades

### Summary
Built a pure CSS/JS lightbox system and recovered 30 full-resolution images from Ben Henderson's genealogy archive. Images that have a full-res version in `static/images/full/` are now automatically clickable with a zoom overlay. No external libraries.

### Image Recovery
- Queried WordPress database (MariaDB) to extract 813 image records with page context
- Cross-referenced against Ben Henderson's archive (6,427 images)
- Identified 30 images where Ben's original was significantly larger than the site version
- Highlight: John Robert Berry portrait upgraded from 117KB to 5.2MB (4,396% increase)

### Lightbox Implementation
- Pure CSS overlay + minimal JS (no library dependencies)
- `img-float` shortcode: auto-detects full-res version in `/images/full/` via Hugo `fileExists`
- `ancestor-profile` shortcode: same auto-detection added
- Hover shows magnifying glass icon, click opens dark overlay, Escape/click-outside to close
- 8 raw HTML/markdown image references updated manually for pages not using shortcodes

### Files Modified
- `assets/_custom.scss` — lightbox CSS (overlay, close button, caption, zoom cursor)
- `layouts/baseof.html` — lightbox overlay HTML + JS
- `layouts/_shortcodes/img-float.html` — auto-detect full-res, add lightbox-trigger class
- `layouts/_shortcodes/ancestor-profile.html` — same auto-detect for profile images
- `content/ancestors/john-robert-berry.md` — manual lightbox links for church deed + census
- `content/ancestors/lookalikes.md` — manual lightbox links (2 images)
- `content/ancestors/fiddletoncemetery.md` — manual lightbox link
- `content/ancestors/whowellberrytx.md` — manual lightbox link
- `content/ancestors/william-clarence-berry-nc.md` — manual lightbox link
- `content/ancestors/joshua-berry-ohio-detail.md` — manual lightbox link
- `content/ancestors/joshua-berry-ohio.md` — manual lightbox link

### New Files
- `static/images/full/` — 30 full-resolution images (copied from Ben's archive)
- `Project/incoming/berrytree_image_manifest.json` — 813 WP images mapped to pages
- `Project/incoming/image_upgrade_manifest.json` — 30 upgradeable images with page context
- `Project/docs/Genealogy_FileSystem_Design_v6.md` — Aaron's file system design (reference)

### Stats
- 28 lightbox triggers across 22 pages
- 30 full-res images in `static/images/full/`
- Zero code changes needed to add future images (drop in `/images/full/`, shortcode auto-detects)

---

## 2026-04-07 — Homepage: Restore Pictures Card + Add Browse by Topic Card

### Summary
Expanded the homepage explore card grid from 6 to 8 cards. Restored the Pictures card that was removed during the taxonomy rollout, and added a new Browse by Topic card linking to `/tags/`.

### Changes
- Restored Pictures card (position 6) with original photo-frame SVG icon → `/pictures/`
- Added Browse by Topic card (position 7) with tag SVG icon → `/tags/`
- Family Lines card moved to position 8
- Extended stagger animation delays for cards 7 and 8

### Files Modified
- `layouts/index.html` (explore card grid + animation CSS)

### Commit
- `eab6f39` — Homepage: restore Pictures card, add Browse by Topic card (8-card grid)

---

## 2026-04-07 — Taxonomy System: Full Site Tagging + Navigation

### Summary
Designed and implemented a complete taxonomy system across all 254 content pages. Three public taxonomies (families, periods, tags), five internal QC fields, custom landing pages, and navigation integration. Zero unconverted, zero untagged.

### Strategy & Vocabulary
- 10 family values (Gen 3 lines), 7 historical periods (Colonial through Modern), 30 controlled tags
- 5 internal front matter fields: qc_status, qc_date, last_updated, content_source, sources_verified
- Strategy doc: `Project/notes/tag-strategy.md`
- Front matter reference: `Project/docs/front-matter-definitions.md`

### Tagging (254 pages, 100% coverage)
- 13 family-line pages tagged (Phase 2 pilot)
- 10 Gen 3 ancestor pages tagged (Phase 2 pilot)
- 183 ancestor pages tagged (Phase 3, batch scripts + research agents)
- 48 remaining pages tagged: books, documents, pictures, DNA, timelines, indexes, etc. (Phase 4)

### Custom Taxonomy Landing Pages (Phase 5)
- `layouts/_default/terms.html` — taxonomy index template (card grid, intros, page counts)
- `layouts/_default/taxonomy.html` — individual term template (section-grouped page lists)
- SCSS added to `assets/_custom.scss` — forest/cream aesthetic, card hover states, discovery banner

### Navigation Updates
- Sidebar (`hugo.toml`): Added "Family Lines" (/families/) and "Browse by Topic" (/tags/)
- Hamburger menu (`layouts/index.html`): Same two entries added
- Homepage explore cards: Pictures card replaced with Family Lines card (new SVG branching tree icon)
- Periods discovery banner added to /tags/ page linking to /periods/

### Tools Created
- `Project/tools/add-tags.py` — Batch tagging script
- `Project/tools/apply-families.py` — Family line assignment script

### Files Modified
- 254 content .md files (front matter updated)
- `hugo.toml` (menu entries + weights)
- `layouts/index.html` (hamburger menu + explore card)
- `layouts/_default/terms.html` (new)
- `layouts/_default/taxonomy.html` (new)
- `assets/_custom.scss` (taxonomy styles)
- `Project/notes/tag-strategy.md` (new)
- `Project/docs/front-matter-definitions.md` (new)

---

## 2026-04-07 — WP-to-Markdown Conversion COMPLETE

### Summary
Completed all remaining page conversions across the entire site. Every triage category from Martha's Phase 3A spreadsheet is at zero remaining. All 229 triaged pages plus 27 additional pages across documents, indexes, books, galleries, and family lines are now converted. Zero unconverted pages remain.

### REFERENCE Pages (17 → 0 remaining)
- familyhouses.md — Full conversion with photo-gallery layout, 7 themed sections
- genfour.md — Raw HTML to markdown, 10 family line sections
- genfive.md — Raw HTML to markdown, family line sections
- fiddletoncemetery.md — Photo gallery, burial list, cemetery location with aerial photo
- marriages.md — 21 missing bonds added to timeline JSON, page now redirects to /timeline/
- undevelopedlines.md — Raw HTML to markdown
- fiddleton-1891.md — Stripped WP comments, structured source metadata
- georgialand.md — Clean sections, formatted source citations
- proofpage.md — Added preamble, formatted evidence list
- usaconflicts.md — Raw HTML to markdown, cross-linked to veterans page
- new-veteran-page.md — 80+ portraits organized into family line sections
- berrylist.md, berrylistpage2.md — Archived (redundant with familynamelist)
- known-surnames-of-berry-inlaws.md — Confirmed at /indexes/berry-inlaw-surnames/

### CHILDREN-LIST Pages (8 → 0 remaining)
All folded into parent GEN pages and archived. Unique data merged before archiving:
- joshuachildren.md: 8 birth years + DNA Donor Line label merged into joshua-berry-sr.md
- jesseleechildren.md: birth dates/locations for 6 children merged into jesseleeberry.md
- wpbsrchildren.md: marriage dates and spouse info for 5 children merged into wiley-p-berry.md
- davidjchildren.md, jrbchildren.md, djbrbchildren.md, rbjchildren.md: parent already had all data
- robert-elizabeth-berrys-children.md: already gone from prior session

### SPECIAL CONTENT Pages (19 → 0 remaining)
- ahberrystory.md — Full conversion with photo-feature, 4 narrative sections
- lookalikes.md — Photo gallery with family line comparisons
- robert-berry-oc-character.md — Archived (content already on robert-berry-oc.md)
- john-berry-tx-detail.md — Archived (duplicate of john-berry-tx.md)
- location-fiddleton-cemetery.md — Merged into fiddletoncemetery.md
- aldridge-berry-farquhar-connection.md — Already converted
- 13 other pages: already gone from prior sessions

### Legacy Duplicates Archived (11 pages)
elizabeth.md, henryberry.md, isaacberry.md, maryberry.md, robertberryjr.md, thomasberrync.md, johnrobertberry.md, john-robert-berrys-family-history.md, john-robert-berry-family-history.md, robert-berry-jr-detail.md, joshuaberryohio.md. All targets received proper aliases.

### 12 Unconverted Ancestor Pages — Converted
Added info-banners to: george-rufus-berry-nc, joshua-berry-ohio, roger-williamson-pac, marykempepac, sarahberrycatesga, robert-berry-joshuas-son-nc, william-aaron-turley-ga, frederickmberryiowa, harrisonberryiowa, james-thomas-wilson. Full HTML conversion for thomasyoungberrync.md.

### 14 Biographical Documents — Converted and Moved to /ancestors/
Full HTML-to-markdown conversion, info-banners added, moved from /documents/ to /ancestors/ with aliases: lelawillievirginiaguthrie, william-edgar-berry-alabama, william-henry-berry-ga, william-oscar-berry-ga, william-thomas-maners, williamaaronturleyga, williamclarenceberrync, williameugeneberrync, williamgsodavid, williamhberrync, williamlamar, williamtberryjrala, williamtberrysrala, willieadolphysberrync.

### 27 Remaining Pages — All Converted
12 document pages, 5 index pages, 4 book pages, 2 galleries, 2 family lines, 2 other. All received info-banners and HTML cleanup.

### Document Merges
- documents/william-berry.md → merged into ancestors/william-berry.md (5 census images, Cate family, Y-DNA link)
- documents/williamchildren.md → archived (redundant)
- documents/joshua-berry-oc-document-page.md → merged into ancestors/joshua-berry-sr.md (4 document images)
- documents/richardwilliamsonpac.md → merged into ancestors/roger-williamson-pac.md (will image, children list)

### Duplicate Consolidations
- familytreeindex.md → archived (duplicate of family-tree.md)
- alphabetical.md → archived (broken duplicate of alphabetical-pages-index.md)
- robert-berry-family-line.md → archived (subset of robert-berry-juniors-family-tree.md)
- alphabetical-pages-index.md rebuilt with 229 pages from CSV inventory

### Prototype Pages
12 Phase 2 GEN format prototypes moved to Project/archived/prototypes/ for design reference.

### Timeline Data
21 marriage bonds from the Grooms Book added to timeline_events.json (308 total entries).

### Tools Created
- Project/tools/update-csv-inventory.py — Regenerates Project/docs/all_site_pages.csv
- Project/docs/all_site_pages.csv — Complete site inventory (254 pages)

### Action Items Added
- Tags system discussion (LOW priority, next meeting agenda)

### Files Modified
~120+ files touched across content/, data/, indexes/, and Project/.

---

## 2026-04-06 — Stub Retirement, Merge Completion, Census Formatting, Shortcode Updates

### Summary
Cleared three full triage categories (RETIRE, MERGE, STUB) and formatted all census companion pages. Extended img-float shortcode with size parameter. Total pages remaining: ~34.

### Retired Pages (11 WordPress leftovers)
Archived to `Project/archived/retired-2026-04-06/`:
no-access, forum, announcements, contact-us, about-us, home, bens-blog, history-of-the-cover-pages-2015, crest, three-brothers-oc, berry-martin-shipman-family-connections.
`page-updates.md` kept as active converted page.

### Merged Duplicates (4 remaining from 8)
4 already retired in prior phases. Completed remaining 4:
- roannfrances.md → roann-frances-berry.md (alias added)
- emmagberrync.md → emma-g-berry-nc.md (alias added)
- georgerufusberrync.md → george-rufus-berry-nc.md (alias added)
- thomaseuartberrync.md → thomas-euart-berry-nc.md (alias added)

### Stubs Folded (12 pages)
Images folded into parent pages with 50% size + click-for-full-size links:
| Stub | Folded Into |
|------|------------|
| catecrest | john-cate.md |
| locateplantation | robert-berry-oc.md (already present) |
| robert-berry-oc-9798 | robert-berry-oc.md (already present) |
| robert-h-breezes-headstone | coradberrync.md (already present) |
| thomas-berry-land-sale | thomas-berry.md |
| cora-and-frank-headstone | coradberrync.md (already present) |
| 9798-2 | robert-berry-oc.md (already present) |
| samuel-hollowell | robert-berry-pac.md |
| servicewahendersonnc | Archived only (Aaron's preference) |
| david-crockett-berrt | Archived (empty typo page) |
| annfosterpac | roger-williamson-pac.md (content already present) |
| dora-ellen-turley-home | doraellenturleyga.md |

### Census Pages Formatted (9 pages)
Light formatting pass: info-banner shortcode, descriptions, bold headings, HTML stripping, cross-links, UNSOURCED flags, image alt text.

### Shortcode Updates
- `img-float.html` — added `size` parameter for max-width control (e.g., `size="50%"`)

### Triage Status
| Category | Status |
|----------|--------|
| RETIRE | **Done** (0 remaining) |
| MERGE | **Done** (0 remaining) |
| STUB | **Done** (0 remaining) |
| CENSUS | **Done** (0 remaining) |
| CHILDREN-LIST | 3 remaining |
| REFERENCE | ~10 remaining |
| SPECIAL CONTENT | 19 remaining |
| **Total remaining** | **~34 pages** |

---

## 2026-04-06 — WP-to-Markdown Conversion: 110 Files + Design Criteria Upgrade

### Summary
Massive conversion run: 110 ancestor pages converted through the full WP-to-Markdown pipeline, then 76 upgraded to the full design criteria format (ancestor-chain shortcode, ancestor-profile card, breadcrumb, ancestor-page wrapper). Created info-banner shortcode (#19), fixed banner h2 semantics (#29), extended ancestor-chain shortcode to support Gen 3-9.

### Info-Banner Shortcode (#19 + #29)
- Created `layouts/_shortcodes/info-banner.html` — two params (title, subtitle)
- Added `.info-banner` CSS to `assets/_custom.scss`
- Uses `<p>` not `<h2>` for title (Jim's #29 heading hierarchy fix)
- Replaced inline HTML banners across 12 info pages
- Items #19 and #29 closed

### Ancestor-Chain Shortcode Extended
- `layouts/_shortcodes/ancestor-chain.html` now supports Gen 3 through Gen 9
- Previously only supported Gen 1-3 (Gen 1+2 hardcoded)
- Enables deep lineage chains (e.g., Ruby Alyene Hunt at Gen 8)

### WP-to-Markdown Conversion (110 files)
Tool pass (`wp-to-markdown.py` + `fix-nested-images.py`) followed by manual cleanup:
- Bold headings (`## **Text**` / `### **Text**`)
- Front matter `description` fields added
- `<!-- UNSOURCED -->` flags on uncited claims
- Cross-links to named ancestor pages
- Image alt text filled in
- HTML artifacts stripped

### Design Criteria Upgrade (76 files)
Full format applied per `Project/design_criteria.md`:
- `<div class="ancestor-page">` wrapper
- `{{< breadcrumb >}}` shortcode
- `{{< ancestor-chain >}}` with full lineage (Gen 3-9)
- `{{< ancestor-profile >}}` vital statistics card
- `<h2 class="ancestor-section">` for Children/Census sections
- `{{< census-summary >}}` shortcode where applicable
- Tree-link footer to family line pages
- `bookToc: true` in front matter

### Duplicate Merged
- `mary-jane-berry-daughter-of-wc-massa-tompkins-berry.md` deleted
- `mary-jane-berry-wc.md` is canonical with alias redirect

### Ancestor-Chain Parameter Fix (16 files)
- Stripped inline Markdown links and bold from shortcode parameters
- Extracted URLs to proper `linkN` parameters
- Standardized `&` to `×` between spouses

### Files Modified
110 ancestor pages + 1 SCSS + 2 shortcodes + 1 deleted duplicate = 114 files total

### Deferred
- TX branch (10 files) needs Martha's UNSOURCED review pass
- documents.json entries for pages with uncatalogued source material (Tom)

---

## 2026-04-06 — Retroactive QC Pass: All 25 Batch Files

### Summary
Full team audit and retroactive quality pass across all 25 converted files (Batches 1 + 2A). All contractors brought in for migration review. Nine High Priority items identified, approved, and applied.

### Team Migration Review
All 10 team members (6 core staff + 7 contractors) submitted observations compiled into `Project/notes/team_migration_suggestions.md`. 30 suggestions categorized into 4 tiers: High (roll into workflow), Before Next Batch, Medium, Defer.

### Retroactive Fixes Applied
| Item | What | Count |
|------|------|-------|
| #1 | `description` added to front matter | 23 files |
| #6 | Missing image alt text fixed | 3 files (elizaberryfranklin, joshuaberry, proofpage) |
| #7 | `<!-- UNSOURCED -->` comments on unflagged claims | ~90 comments across 15 files |
| #14 | Cross-links to ancestor pages in narrative text | 28 links across 11 files |
| #28 | Heading hierarchy fixes | 4 files (familynamelist, jesseleeberry, genthree, pictures/_index) |

### Tool Updates (Kate)
| Item | What |
|------|------|
| #16 | Expanded image pattern detection: non-self-closing `<img>` tags, inline style/width/height stripping |
| #17 | Script tag detection with warnings (does not silently strip) |

### Process Improvements
| Item | What | Location |
|------|------|----------|
| #22 | Formal per-page QC checklist (12 items, 4 categories) | `Project/notes/conversion-qc-checklist.md` |
| #30 | Banner contrast verified: cream 10.7:1, gold 6.3:1 (both pass WCAG AA) | Closed |

### Deferred to Next Session
- documents.json entries for 10 pages with uncatalogued source material (Tom)
- 7 data errors (date typos, conflicting birth year) found by Martha
- Banner shortcode (#19) and semantic h2 fix (#29)

### Audit Highlights
- **Martha:** 85 unsourced claims flagged; genthree.md worst offender (19 claims); 7 date typos spotted
- **Andrew:** 43 unlinked ancestor names found; Robert Berry Jr. unlinked across 5 pages
- **Tom:** 10 pages with primary sources not in documents.json; 0 broken JSON links
- **Jim:** Banner colors pass WCAG AA (10.7:1 cream, 6.3:1 gold)

---

## 2026-04-06 — Batch 2A Commit, Bold Headings, Duplicate Merge, Override Archived

### Summary
Committed Batch 2A (15 pages, ~43K artifacts). Established bold heading convention (`## **Text**` / `### **Text**`). Merged duplicate surname page. Added A-Z section dividers. Archived an untracked Hugo theme override.

### Bold Heading Convention
- All `##` and `###` headings now wrap text in `**bold**` across all batch files
- Extended site map: 257 headings converted to `### **Text**` format
- Rule added to `Project/design_criteria.md` Section 5

### Duplicate Page Merged
- `ancestors/known-surnames-of-berry-inlaws.md` merged into `indexes/berry-inlaw-surnames.md`
- Alias added so old URL still resolves
- 6 cross-references updated (extended-site-map, site-map, page-updates, home, books/books, design_criteria)

### A-Z Section Dividers
- `indexes/berry-inlaw-surnames.md` — A through Z letter groupings applied
- `ancestors/orange-county-nc-marriage-bonds-a-c.md` — A, B, C dividers inserted

### Hugo Theme Override Archived
- **File:** `layouts/_partials/docs/html-head.html` (origin unknown)
- **What it did:** Overrode the Hugo Book theme's meta description fallback. Theme uses `.Summary` (~70 words auto-generated); override used `.Plain | truncate 200` (full plain text, truncated at 200 chars). One-line difference on line 8.
- **Why archived:** Minor improvement not worth the maintenance burden of tracking a theme override. Most pages should have explicit `description` front matter anyway.
- **Archived to:** `Project/archived/html-head-override-2026-04-06.html`
- **If meta descriptions look wrong later:** Check this file first. It's in archived, laughing at us.

---

## 2026-04-06 — Design Criteria Established & Applied

### Summary
Established formal design criteria for the site (Project/design_criteria.md). Defined three page types: Ancestor pages, Family Line pages, and Info/Reference pages. Applied the standard retroactively to all 25 converted pages across Batches 1 and 2.

### Design Criteria Created
- Kate authored `Project/design_criteria.md` as the site's design bible
- Three page types defined with full structural templates
- Info page banner standard: forest/gold gradient with headline and subtitle
- Ancestor page standard: Gen chain format, ancestor-profile, book references
- Book reference section added mapping all 18 chapters of *Our Berrys in Frontier America*
- Deviation policy: Aaron must approve any departures from the standard
- Added as standing directive in CLAUDE.md

### Design Applied — Batch 1 (10 files)
| Type | Files | Treatment |
|------|-------|-----------|
| Info pages | genthree, aldridge-berry-farquhar-connection, familynamelist, william-cates-estate-sale | Forest/gold banners |
| Ancestor pages | jamesberrytenn, george-rufus-berry-nc, jesseleeberry, johnberry, john-berry-detail, robert-clark-berry-ga | Gen chains + book refs where applicable |

### Design Applied — Batch 2 Track A (15 files)
| Type | Files | Treatment |
|------|-------|-----------|
| Info pages | orange-county-nc-marriage-bonds, williamson-deeds, page-updates, berry-wills-deeds, proofpage, berry-inlaw-surnames, pictures/_index, extended-site-map | Forest/gold banners |
| Ancestor pages | enoch-m-berry, georgerufusberrync, francis-marion-berry, elizaberryfranklin, albertedgar, joshuaberry | Gen chains + book refs where applicable |

### Content Improvements
| Page | Change |
|------|--------|
| known-surnames-of-berry-inlaws | Alphabetical sections, preamble, contact invite, forest/gold banner |
| page-updates | Banner, toned-down contact language |
| francis-marion-berry | Gen convention applied |
| robert-clark-berry-ga | Descendant tree expanded from run-on line |
| william-cates-estate-sale | Estate items as indented sub-lists |
| johnberry | Census records formatted, table tags removed |

### Standing Directives Added to CLAUDE.md
- Visitor-facing contact language: warm but no commitments on Aaron's time
- Design criteria reference: all pages must conform to Project/design_criteria.md

### Data Integrity (Tom)
- All 15 Berry marriages in OC bonds file verified present in marriages page
- 2 minor date discrepancies flagged (bond vs. ceremony dates)
- Williamson deeds collection properly indexed in documents.json

---

## 2026-04-06 — WordPress-to-Markdown Conversion: Batches 1 & 2

### Summary
Began site-wide WordPress HTML cleanup. Built conversion tooling, converted 25 ancestor and document pages across two batches, and resolved multiple rendering issues discovered during visual review.

### Batch 1 (10 files, ~9,200 artifacts eliminated)
| File | Artifacts | Result |
|------|-----------|--------|
| `jamesberrytenn.md` | 2,408 | Clean (manual census cleanup) |
| `genthree.md` | 1,202 | Clean |
| `george-rufus-berry-nc.md` | 289 | Clean |
| `jesseleeberry.md` | 213 | Clean |
| `johnberry.md` | 1,166 | Clean (manual table + Gen labels) |
| `aldridge-berry-farquhar-connection.md` | 910 | Clean |
| `john-berry-detail.md` | 859 | Clean |
| `robert-clark-berry-ga.md` | 707 | Clean (manual descendant tree) |
| `familynamelist.md` | 1,298 | Clean |
| `william-cates-estate-sale.md` | 442 | Clean (manual sub-list formatting) |

### Batch 2 — Track A (15 files, ~43,431 artifacts eliminated)
| File | Artifacts | Result |
|------|-----------|--------|
| `orange-county-nc-marriage-bonds-a-c.md` | 37,353 | Clean |
| `williamson-deeds-and-wills-1691-to-1755-pac.md` | 1,642 | Clean |
| `page-updates.md` | 493 | Clean |
| `enoch-m-berry-page.md` | 441 | Clean |
| `berry-wills-and-deeds-from-pac-1691-to-1755.md` | 440 | Clean |
| `georgerufusberrync.md` | 426 | Clean |
| `francis-marion-berry.md` | 340 | Clean |
| `known-surnames-of-berry-inlaws.md` | 313 | Clean |
| `proofpage.md` | 307 | Clean |
| `berry-inlaw-surnames.md` | 291 | Clean |
| `elizaberryfranklin.md` | 261 | Clean |
| `pictures/_index.md` | 254 | Clean |
| `albertedgar.md` | 235 | Clean |
| `joshuaberry.md` | 234 | Clean |
| `extended-site-map.md` | 401 | Clean |

### Tooling Created
| File | Purpose |
|------|---------|
| `layouts/_shortcodes/img-float.html` | Hugo shortcode replacing WordPress image alignment |
| `assets/_custom.scss` | `.img-float` responsive float styles |
| `Project/tools/wp-to-markdown.py` | Main conversion tool (bold fix, space collapsing, household detection) |
| `Project/tools/fix-nested-images.py` | Fixes nested `[![]()]()`patterns → `img-float` shortcodes |
| `layouts/_partials/docs/html-head.html` | Override to bypass Hugo `.Summary` slice overflow bug |

### Bug Fixes During Conversion
| Bug | Fix |
|-----|-----|
| Bold markers stripped (`**name**` → `name`) | Empty italic cleanup regex `\*\s*\*` was eating `**`; fixed with lookbehind |
| `1940Georgia` missing space | Empty bold cleanup `\*\*\s*\*\*` ate spaces; now preserves them |
| Census household data as wall of text | Added `collapse_space_padding()` with household detection and comma formatting |
| Hugo `.Summary` slice overflow on large pages | Overrode `html-head.html` partial to use `.Plain \| truncate 200` instead of `.Summary` |
| `summaryLength` not set | Added `summaryLength = 40` to `hugo.toml` |

### Content Improvements (during review)
| Page | Change |
|------|--------|
| `page-updates.md` | Added 2026 entries for James Thomas Wilson and Gen 3 tree pages |
| `francis-marion-berry.md` | Standardized ancestor chain to Gen convention |
| `known-surnames-of-berry-inlaws.md` | Alphabetical sections, preamble, contact invite, forest/gold banner |
| `robert-clark-berry-ga.md` | Expanded run-on descendant tree into nested list |
| `william-cates-estate-sale.md` | Indented sub-lists for estate items |
| `johnberry.md` | Census records formatted with list markers and proper bold |

### Workflow Established
1. Run `wp-to-markdown.py` (HTML → Markdown)
2. Run `fix-nested-images.py` (nested image-link cleanup)
3. Martha verifies content accuracy
4. Visual check in browser (source + rendered)
5. Aaron approves
6. Commit in batches

### Data Integrity (Tom)
- All 15 Berry marriages in OC bonds file verified present in marriages page
- 2 minor date discrepancies flagged (bond vs. ceremony dates)
- Williamson deeds collection properly indexed in `documents.json`

---

## 2026-04-06 — Homepage Landing Page Redesign

### Summary
Redesigned the homepage layout to restore the Hugo Book sidebar on desktop while preserving the full-bleed cinematic hero experience. The sidebar and hamburger nav are now responsive: sidebar on desktop, hamburger on mobile.

### Changes
| Change | Detail |
|--------|--------|
| Hamburger nav | Now mobile-only (hidden above 56rem breakpoint) |
| Sidebar restored | Desktop shows the Book theme sidebar with search |
| Hero full-bleed | Hero image fills entire viewport width; sidebar floats over it |
| Homepage sidebar theme | Dark forest green (`#0e1e0e`) background, gold (`#c8a84b`) nav links, cream search bar |
| Subpage transition | Subpages retain cream sidebar, creating a welcome-to-workspace visual shift |
| Sidebar height | Fixed positioning ensures full-viewport coverage on homepage |
| Content sections | Stats, cards, homestead band, and footer clear sidebar with left margin |

### Files Modified
| File | Notes |
|------|-------|
| `layouts/index.html` | Mobile/desktop media queries, full-bleed hero breakout, homepage sidebar styling |

### Additional Changes (second commit: `c44b65d`)
| Change | Detail |
|--------|--------|
| Forest background image | Removed on homepage; replaced with solid `#1a2e1a` |
| Cream bleed | `.book-page` cream background stripped on homepage |
| Home nav link | Disabled and darkened on landing page (`pointer-events: none`) |

### Research & Documentation
- **Martha:** Formal PAC-to-OC connection research assessment (`Project/research/pac-oc-connection-assessment.md`)
- **Martha:** Publishable evidence review for site (`Project/testing/pac-oc-evidence-review.md`)
- **Martha:** Email draft to Berry Henderson re: PAC-OC research collaboration (`Project/notes/email-draft-berry-pac-oc.md`) — sent by Aaron
- **Pam:** Changelog updated

---

## 2026-04-05 — WordPress → Markdown Conversion Tooling

### The Big Picture
Built the complete toolchain to eliminate all WordPress HTML from the site. Conversion tool, img-float shortcode, CSS, and workflow are ready. Test conversion of jamesberrytenn.md (2,408 artifacts → 0) passed visual review. Batch conversion of remaining 292 files begins 2026-04-06.

### Files Created
| File | Purpose |
|------|---------|
| `layouts/_shortcodes/img-float.html` | Hugo shortcode replacing all WordPress image alignment classes. Params: src, alt, side (left/right/center/none), caption, link |
| `Project/tools/wp-to-markdown.py` | Conversion tool: images → img-float shortcodes, headings, bold/italic, lists, blockquotes, links, paragraph tags, WP comments, divs/spans, nbsp cleanup |

### CSS Added
| File | Notes |
|------|-------|
| `assets/_custom.scss` | `.img-float` styles mirroring WordPress alignment CSS: float left/right, center, responsive stacking at 600px, figcaption styling |

### Conversion Audit
| Metric | Value |
|--------|-------|
| Total files with WP artifacts | 292 / 323 |
| Total artifacts before conversion | 82,741 |
| Automated reduction | 92% (to 6,760) |
| Remaining 8% | Mostly HTML tables in family-tree pages |

### Severity Tiers (conversion order)
| Tier | Artifacts | Files |
|------|-----------|-------|
| S (30,000+) | 1 | orange-county-nc-marriage-bonds |
| A (500-2,500) | ~10 | jamesberrytenn, williamson-deeds, family-line trees |
| B (100-500) | ~30 | ancestor pages, book chapters |
| C (10-99) | ~120 | Bulk ancestor/document pages |
| D (1-9) | ~38 | Light touch, nearly clean |

### Workflow
1. Run `python3 Project/tools/wp-to-markdown.py <file>` (preview)
2. Review diff, visual check in browser
3. Martha verifies content accuracy
4. Aaron approves
5. Commit in batches of 10

### Tool Refinements During Testing
- Images inside heading tags now extracted before the heading
- Empty headings (`<h2></h2>`) stripped
- `<h3><strong>text</strong></h3>` detected as WordPress bold-faking, converted to `**text**` not `### text`
- Bare `<h3>` prose (non-label text) also converted to bold; only short labels ending in `:` kept as headings
- Blank line inserted before converted bold text to ensure Markdown rendering

---

## 2026-04-05 — Image Text-Wrap Cleanup (Site-Wide)

### The Big Picture
Site-wide fix for WordPress image alignment classes that had no CSS support, causing chaotic text wrapping on legacy ancestor pages. Lila added float/margin/clear-fix/responsive CSS rules, then the web team (Lila, Kate, Terry) audited all 102 affected pages and performed HTML surgery on the 14 worst offenders.

### CSS Changes
| File | Action | Notes |
|------|--------|-------|
| `assets/_custom.scss` | Enhanced | Added `.alignleft`, `.alignright`, `.alignnone`, `.aligncenter` float rules with margins, max-width 45%, responsive stacking at 600px. Added `clear: both` on headings, lists, blockquotes, tables, figures. |

### Pages Updated (HTML Cleanup)
| Page | Action | Notes |
|------|--------|-------|
| `sallymalenaberrync.md` | Major fix | 5 mid-word/mid-sentence images extracted ("we[img]nt", "Hender[img]son", "Civil [img]War", "VI[img]EW", "[img]great depression") |
| `jesseleeberry.md` | Major fix | Mid-sentence image, death certificate pulled out of `<h2>`, adjacent images separated |
| `francis-marion-berry.md` | Fix | 4 images extracted from `<li>` items, mid-sentence image separated |
| `horacepratherberryga.md` | Fix | Image extracted from `<strong>/<li>`, spacer blocks cleaned |
| `enoch-m-berry-page.md` | Fix | Spacer blocks between floated images cleaned |
| `albertedgar.md` | Fix | Adjacent draft card images separated |
| `home.md` | Fix | Float class removed from table cell image |
| `unknown-pictures-page-1.md` | Fix | Adjacent images on same line separated |
| `cora-berry-mcvicker.md` | Fix | Image separated from text-wrapping anchor |
| `elizabeth.md` | Fix | Spacer blocks cleaned |
| `johnrobertberry.md` | Fix | Broken anchor tag fixed, alt text added |
| `walterglenberryga.md` | Fix | Image extracted from `<h3>`, spacers cleaned |
| `sarah-frances-berry-kelly-ga.md` | Fix | Adjacent images separated, spacers cleaned |
| `frederickmberryiowa.md` | Fix | "la[img]rge" mid-word split fixed |
| `wileyharoldberrync.md` | Fix | "h[img]is" mid-word split fixed |
| `john-robert-berrys-family-history.md` | Fix | "B[img]e" mid-word split fixed |

### Scope
- 102 pages affected by WordPress alignment classes (379 total occurrences)
- CSS fix covers all 102 pages automatically
- 14 pages required per-page HTML cleanup (structural issues CSS can't fix)
- Zero mid-word images remain site-wide after cleanup

### Commits
- `ee4130f` — Initial CSS alignment rules
- `ab63c6a` — CSS clearing enhancement + HTML cleanup across 14 pages

---

## 2026-04-05 — Pattie Swiney Berry Page Update & James Thomas Wilson Page

### The Big Picture
Major research session driven by new source data Aaron brought in. Updated Pattie Berry Wilson's page with corrected biographical details, created a new page for her father-in-law James Thomas Wilson, and resolved a birth-year discrepancy using the 1900 US Federal Census.

### Pages Created
| Page | Action | Notes |
|------|--------|-------|
| `ancestors/james-thomas-wilson.md` | New page | Father-in-law of Pattie Berry; full Wilson family documented with sourced citations |

### Pages Updated
| Page | Action | Notes |
|------|--------|-------|
| `ancestors/pattiesberrync.md` | Major update | Middle name (Swiney), birth/death locations, wedding date, spouse details, FindAGrave links, cross-link to James Thomas Wilson page |
| `indexes/site-map.md` | Entry added | James Thomas Wilson NC listed alphabetically |

### Research Findings
- **Pattie's middle name** confirmed as Swiney (family surname)
- **Death location** confirmed as Red Springs, Robeson County, NC via FindAGrave memorial #37475565, backed by NC Death Certificate (Ancestry). Ben's original "living in Sanford" refers to residence, not place of death.
- **Wedding date** corrected from "sometime around 1911" to December 20, 1910
- **Felix Curry "Bob" Wilson** fully documented: birth, death, military service (CPL Signal Corps), burial at Buffalo Cemetery, parents
- **James Thomas Wilson birth year** — Headstone and FindAGrave say 1859; 1900 Census (FamilySearch ark:/61903/1:1:MSB8-SVG) says January 1857. Census is authoritative (recorded during lifetime). Headstone believed in error.
- **Mystery URL resolved** — Original FindAGrave GRid=25895150 was for James Thomas Wilson, not Pattie
- **Wilson-Berry connection** — Wilson and Berry families did business in Orange County as early as 1833 (land deeds on William Clarence Berry's page)

### Sources Processed (in Project/incoming/)
- `Pattie_S_Berry_Wilson_1886-1915-FindaGrave_Memorial.html`
- `James_Thomas_Wilson_1859-1929-FindaGrave_Memorial.html`
- `Felix_G_Wilson_1831-1896-FindaGrave_Memorial.html`
- `Thomas_Wilson_United_States_Census_1900.txt`

### FindAGrave Memorials Referenced
| Person | Memorial ID |
|--------|-------------|
| Pattie S. Berry Wilson | #37475565 |
| Felix Curry "Bob" Wilson | (pending — not on FindAGrave under that name) |
| James Thomas Wilson | #25895150 |
| Clara Parker Wilson | #25895133 |
| Felix G. Wilson Sr. | #54107844 |

---

## 2026-04-05 — Family-Line Tree Pages: Joshua Sr., Thomas, William, Elizabeth

### The Big Picture
Created the four missing family-line tree pages, closing the last visible gap in the family-lines section. All ten Gen 3 siblings now have both an anchor page (biography) in `ancestors/` and a descendant tree page in `family-lines/`. Legacy pages were moved and reformatted rather than duplicated.

### Pages Created/Moved

| Page | Action | Source | Depth | Lines |
|------|--------|--------|-------|-------|
| `joshua-berry-family-tree.md` | Moved from `ancestors/joshberrytree.md` | Already gen-tree div format | Gen 9 | 268 |
| `thomas-berry-family-tree.md` | Moved from `ancestors/tberrytree.md` | Already gen-tree div format | Gen 10 | 651 |
| `william-berry-family-tree.md` | Converted from `ancestors/wbfamilytree.md` | Hybrid markdown → gen-tree divs | Gen 8 | 567 |
| `elizabeth-berry-family-tree.md` | New page | Anchor page data (1 child) | Gen 4 | 16 |

### What Changed
- All four pages live in `content/family-lines/` alongside the other six tree pages
- Hugo aliases preserve old URLs (`/ancestors/joshberrytree/`, `/ancestors/tberrytree/`, `/ancestors/wbfamilytree/`, `/ancestors/elizabeth/`)
- Gen 3 root entries link back to their anchor pages in `ancestors/`
- `by-family-line.md` hub updated: Joshua, Thomas, Elizabeth links pointed to new locations; William line (previously plain text, no link) now linked
- Old source files removed from `ancestors/`

### Martha's Verification Pass
- **Thomas tree:** 3 malformed HTML lines fixed (stray commas and missing div wrappers inherited from original data)
- **William tree:** Elizabeth Berry (half-sister, b. 1812, daughter of Hannah Cate and John Berry) was missing from the original `wbfamilytree.md`, added with own section
- **Joshua tree:** 2 inherited gen-class mismatches flagged for future cleanup (Lewis Berry spouse tagged gen-6 instead of gen-4, Roy Felts tagged gen-6 instead of gen-7) — rendering unaffected
- **Elizabeth tree:** Clean, minimal, verified against anchor page

### Hub Link Cleanup
- Fixed 2 non-breaking space characters in `by-family-line.md` (Unicode `\xc2\xa0` before Thomas and between "Cate" and "Berry" on William line)

### Team
- **Lila** — Page creation, format conversion, alias setup, hub link updates
- **Martha** — Four-page verification pass, data gap identification (Elizabeth half-sister), flagged inherited issues
- **Pam** — Changelog, action item tracking

---

## 2026-04-05 — Phase 3B Complete: All 10 Gen 3 Pages Converted

### The Big Picture
Phase 3B is done. All 10 Gen 3 ancestor pages are now in GEN format. The second session converted the remaining 5 pages, added Aaron's 1950 census find for Wiley P. Berry, and fixed 4 broken links in documents.json that were left over from earlier satellite archiving. Commit `96cca9c`.

### Pages Converted This Session

| # | Page | Satellites Archived | Key Notes |
|---|------|---------------------|-----------|
| 6 | `thomas-person-berry.md` | 2 (thomaspersonberry.md, census-page-for-thomas-p-berry.md) | 3 marriages, 9 children across 2 families, 17 images, 6 PDF links. Census data from 1810–1880 folded in. |
| 7 | `wiley-p-berry.md` | 0 (child pages are standalone) | Ben's personal grandparent memories. 1950 census added (FamilySearch, ED 68-24). |
| 8 | `john-cate.md` | 0 | Simple page — father-in-law of Robert Berry OC. Will image preserved. |
| 9 | `hannahcateberry.md` | 1 (1810-hannah-cate-census.md) | Alias added for widely-linked 1810 census page (8+ inbound links preserved). |
| 10 | `elizabethcate.md` | 0 | Short character sketch. Census links updated to new hannahcateberry anchor. |

### documents.json Fixes
4 broken links repaired — all pointed to archived satellites:

| Old Link | New Target |
|----------|------------|
| `/ancestors/census-page-for-thomas-p-berry/` | `/ancestors/thomas-person-berry/#census-records` |
| `/ancestors/ira-berry-census-page/` | `/ancestors/ira-berry-nc/#census-records` |
| `/ancestors/robert-berrys-oc-pay-vouchers/` | `/ancestors/robert-berry-oc/#military-service-and-pay-vouchers` |
| `/ancestors/voucherpage/` | `/ancestors/robert-berry-oc/#revolutionary-war-vouchers` |

New entry added: `census-wiley-p-berry-1950` — 1950 federal census, Cheeks Township, Orange County, NC.

### New Workflow Rule
Going forward, every satellite archival includes a documents.json link check. Saved to team memory.

### Phase 3B Final Tally
- **10 pages converted** to GEN format
- **~22 satellites archived** (content folded, aliases preserve URLs)
- **0 broken links** remaining in documents.json
- **1 new census record** added (1950 Wiley P. Berry)
- All Hugo builds clean throughout

### What's Next
Gen 3 batch complete. Next batch TBD — likely Gen 4 or remaining unconverted pages from Phase 3A triage.

### Team
- **Martha** — Content verification, census research guidance, 1950 census intake
- **Lila** — GEN conversions, satellite archival, documents.json maintenance, memory updates
- **Pam** — Changelog, project tracking

---

## 2026-04-05 — Phase 3B: Gen 3 Batch — First 5 Conversions Complete

### The Big Picture
Phase 3B conversion work began and completed 5 of the 10 Gen 3 pages in a single session. Martha verified content, Lila built GEN conversions, satellites were folded in and archived. All builds clean. No files pushed.

### Pages Converted

| # | Page | Lines | Satellites Folded/Archived | Key Notes |
|---|------|-------|---------------------------|-----------|
| 1 | `robert-berry-oc.md` | 457 | 11 files (civic, political, traits, vouchers, pay vouchers, camp POA, children list, Richard Berry research, plantation location, 2× Berry Brothers stubs) | Gen 2 patriarch. 4 date corrections (all 100-year typos). Largest page on site. |
| 2 | `sarah-cate.md` | 188 | 2 files (sarah-cate-detail.md, sarahcate.md) | Date correction: Hannah's marriage 1789→1799. 7 census images preserved. |
| 3 | `ira-berry-nc.md` | 181 | 3 files (ira-berry-nc-detail.md, iraberrync.md, ira-berry-census-page.md) | Census page had unique research: Civil War death deduction, Nancy Waggoner childbirth death. Franklin link fixed. |
| 4 | `robert-berry-pac.md` | 165 | 2 files (robert-berry-pac-detail.md, robertberrypac.md) | Gen 1 root page. Added Sources section linking to rb2sourcelist and rbresourcelist. |
| 5 | `eleanor-reed.md` | 116 | 1 file (eleanorreed.md) | Removed WordPress template cruft. Restored correct 1810 census link. |

### Archived Satellites
All satellite files moved to `Project/archived/phase3b-satellites/` — 19 files total. These no longer render as live pages but are recoverable.

### Date Corrections Applied (Martha-verified)
- robert-berry-oc.md: "1857"→c.1759, "1892"→1792, "1881"→1781, "1712"→1812
- sarah-cate.md: Hannah's marriage "1789"→1799

### What Was Preserved
Every word of Ben Henderson's original prose across all 5 pages. Only formatting, structure, and confirmed date typos were changed.

### What's Next — Remaining Gen 3 Pages
- thomas-person-berry.md (+ thomaspersonberry.md merge)
- wiley-p-berry.md (+ wpbsrchildren.md fold-in)
- john-cate.md
- hannahcateberry.md
- elizabethcate.md

### Team
- **Martha** — Content verification, date corrections, source cross-referencing
- **Lila** — GEN format conversion, HTML structure, image verification, archival

---

## 2026-04-05 — Phase 3B Begins: Robert Berry (OC) Converted to GEN Format

### The Big Picture
First conversion of Phase 3B, and the biggest single page on the site. Robert Berry (Orange County) is the Gen 2 patriarch, the trunk of the entire Berry family tree. Martha verified all content, Lila built the GEN conversion, and all 10 satellite pages were consolidated into one authoritative page. Hugo builds clean.

### What Changed
- **`content/ancestors/robert-berry-oc.md`** — Full GEN conversion: ancestor-profile shortcode, breadcrumbs, ancestor-chain, standardized children list, structured sections. Grew from a loosely formatted 416-line legacy page to a properly structured 457-line GEN page.

### Satellite Pages Folded In
| Source File | Content | Destination Section |
|-------------|---------|-------------------|
| `civic.md` | Court records 1777–1791 | Civic Life |
| `political.md` | Regulator movement, Revolutionary War narrative | Roots of Rebellion |
| `roberts-traits.md` | Land holdings, character essay | Land Holdings + Marriage/Family |
| `voucherpage.md` | Military voucher list (6 vouchers) | Military Service and Pay Vouchers |
| `robert-berrys-oc-pay-vouchers.md` | Voucher images, beef purchase narrative | Military Service and Pay Vouchers |
| `camppowerofattorney.md` | 1815 power of attorney transcription | Children — Camp POA subsection |
| `robert-elizabeth-berrys-children.md` | Detailed children list, spouse info, migration map | Consolidated children list |
| `robert-berry-had-a-brother-named-richard-berry.md` | Richard Berry deed evidence, DNA ruling-out | Robert's Brother Richard |
| `locateplantation.md` | Fiddleton Plantation location image | Fiddleton Plantation |
| `robert-berry-oc-9798.md` / `9798-2.md` | Berry Brothers photo | Children section |

### Date Corrections (Martha-verified typos, all exactly 100 years off)
- "married Elizabeth Cate in 1857" → c. 1759
- "had daughter Mary in 1892" → 1792
- "battle of Guilford Courthouse in April 1881" → 1781
- "the will he wrote in 1712" → 1812

### Other Cleanup
- Removed empty WordPress table artifact (broken `<table>` with no data)
- Fixed self-referencing links that pointed back to the same page
- Removed broken markdown formatting (stray bold markers, double asterisks)
- All 20 referenced images verified present in `/static/images/`

### What Was Preserved
Every word of Ben Henderson's original prose. Narrative sections from `political.md`, `civic.md`, and `roberts-traits.md` are intact. Only formatting, structure, and the four date typos were changed.

### What's Next
- Remaining Gen 3 conversions: sarah-cate.md, ira-berry-nc.md, robert-berry-pac.md, eleanor-reed.md, thomas-person-berry.md, wiley-p-berry.md, john-cate.md, hannahcateberry.md, elizabethcate.md
- Satellite pages listed above are candidates for retirement once Aaron confirms the consolidated page

### Team
- **Martha** — Content verification, date correction, section mapping
- **Lila** — GEN format conversion, HTML structure, image verification

---

## 2026-04-05 — Phase 3A Triage: 229 Ancestor Pages Categorized

### The Big Picture
Martha completed the Phase 3A triage of every page in `/content/ancestors/`, categorizing all 229 files for the legacy ancestor page conversion project. This is the largest remaining workstream on the site. No files were modified; the triage is a decision document awaiting Aaron's approval before any conversion work begins.

### What Was Produced
- **`Project/notes/phase3a-triage.md`** — Full triage spreadsheet with every ancestor page categorized

### Triage Results

| Category | Count | Description |
|----------|-------|-------------|
| DONE | 23 | Already converted to GEN format |
| CONVERT | 113 | Substantial content, needs full GEN conversion |
| MERGE | 20 | Duplicates, fold into primary page and retire |
| STUB | 15 | Thin content, absorb into parent pages |
| RETIRE | 12 | WordPress artifacts, broken, no genealogical value |
| CENSUS | 11 | Census companions, light formatting pass |
| REFERENCE | 17 | Indexes and documentary pages (not biographies) |
| CHILDREN-LIST | 8 | Fold into parent GEN pages during conversion |
| SPECIAL | 19 | Need individual judgment calls |

### Key Findings
- **Duplicate pattern identified:** Nearly every Gen 3 child has both a legacy HTML version and a GEN-converted version (20 merge candidates)
- **Robert Berry OC is the largest conversion:** 415-line page plus 6–7 satellite pages (civic, political, character essay, vouchers, traits)
- **Detail pages** (sarah-cate-detail.md, ira-berry-nc-detail.md, etc.) are a WordPress split-content pattern; each folds back into its parent during conversion
- **113 pages need full GEN conversion**, organized by generation for Phase 3B batching: Gen 3 → Gen 4 → Gen 5+ → Census → Reference

### What's Next
- Aaron reviews and approves the triage
- Phase 3B conversion begins in generational order
- Phase 3C cleanup sweep follows

---

## 2026-04-05 — Contact Form: Formspree Replaces Email-Only Page

### The Big Picture
Replaced the static email-only contact page with a structured Formspree contact form, restoring the form submission capability lost during the WordPress-to-Hugo migration.

### What Changed
- **`content/contact/_index.md`** — New form with five fields: Name (required), Email (required), Family Line dropdown (8 sons + "Not sure"), Message (required), and a cousin-sharing privacy checkbox
- **`assets/_custom.scss`** — Form styles added: forest-palette labels, cream inputs, green submit button, accessible focus states, custom select dropdown arrow
- **Formspree endpoint** — `https://formspree.io/f/maqllvbp`, free tier (50 submissions/month), honeypot spam protection
- **Email fallback** — Obfuscated email link (`berrytree@thgnetworks.com`) preserved below the form for visitors who prefer direct contact

### Design Decisions
- **Family Line dropdown** replaces the old free-text approach, helps Aaron route inquiries by line
- **Privacy checkbox** replaces the old "include this magic phrase" system with a clear opt-in: checked = share with cousins, unchecked = stay private
- Ben Henderson's note and the James Berry research request carried over unchanged

### Also Committed
- **Em dash directive pass** — 13 files updated to replace casual em dashes with commas per standing team directive

---

## 2026-04-04 — DNA Research Center: 10 Scattered Pages → One Data-Driven Hub

### The Big Picture
Consolidated the entire DNA section — 10 legacy pages (many duplicates) with key data trapped in images — into a single, unified DNA Research Center at `/dna/`. Follows the same JSON + dynamic JS + filters pattern as the Documents Explorer and Wheel of Time pages.

### Infrastructure
- **`data/dna_participants.json`** — Structured dataset: 14 Y-DNA participants, 37-marker values, 8 family lines, modal values, Robert T Berry mystery case, resources. OCR'd from `ydnapicchart.jpg` (860x579) and cross-referenced with site text and Chapter 17.
- **`layouts/dna/list.html`** — Full-width dynamic page with collapsible educational sections, filterable participant table, marker viewer, compare tool, mystery case, origins, and resources.
- **`content/dna/_index.md`** — Updated to `type: dna` to use new layout.

### Content — 8 Sections
1. **Understanding Y-DNA Testing** — Collapsible primer: STR markers, matching levels (12/25/37/67), mutations, autosomal DNA for female-line descendants, how to get tested
2. **The Berry Y-DNA Project** — History: Cookie Paulson started it, first match July 20 2004, 239 total participants, 18 unrelated Berry families, 14 confirmed matches
3. **Family Lines** — 8 clickable cards (6 tested / 2 not possible), doubles as participant filter
4. **Y-DNA Participants** — Filterable by line and state, expandable marker viewer with mutation highlighting
5. **Compare Your DNA** — Paste your markers, see distance to each Berry line, marker-by-marker color-coded comparison
6. **Robert T Berry Mystery** — 66/67 marker match to William line, full vitals, census records, eight sons table
7. **Normandy Origins** — 20% of FTDNA matches trace to Jersey off Normandy coast
8. **Resources & Next Steps** — Links to FTDNA, ISOGG, Berry surname project

### Data Verification — Three-Phase Process

**Phase 1 — OCR from chart images:** Extracted marker data from `ydnapicchart.jpg` via `test.berrytree.org`. Got William line and Thomas line right but misread Thomas DYS19 as 14 (actually 16) and false-flagged Joshua line DYS437 mutation.

**Phase 2 — FTDNA project export:** Aaron downloaded full Berry Family DNA Project results (118K-line HTML, 732 members). Confirmed Thomas line corrections, identified 12 kit numbers in R-Z43 cluster, but couldn't map kits to names (export shows surname only).

**Phase 3 — Original chart text:** Aaron found and pasted the original marker chart data. Cross-referencing mutation patterns with FTDNA kit data matched 10 of 12 kits to specific participants.

### Final Data — All 14 Participants Verified

| Line | Participant(s) | Mutations | Status |
|------|---------------|-----------|--------|
| William (4) | Wiley P #18, Harold #123, George W #134, George D #218 | None — perfect modal | Verified |
| Robert Jr. | Billy Wayne #8 | CDYa=36 | Verified |
| Robert Jr. | David Lee #101 | DYS442=13 | Verified |
| John | Shelby Dale #236 | DYS390=25 (different lab, partial) | Verified |
| Joshua | Kenneth Ronald #83 | DYS570=19, CDYa=36, CDYb=38 | Verified |
| Joshua | Charles Thomas #116 | CDYb=38, DYS442=13 | Verified |
| David J. | Dane Eaton #35 | DYS607=16, CDYa=36 | Verified |
| David J. | Billy J. #122 | CDYa=36 | Verified |
| Thomas | John Allen #39 | DYS19=16, DYS458=18 | Verified |
| Thomas | Jeffery Bryon #44 | DYS19=16, DYS458=18, DYS570=19 | Verified |
| Thomas | Thomas Keith #180 | DYS458=18 only (different lab, missing markers 31-35) | Verified |

**Surprise:** Tom #180 does NOT have the DYS19=16 mutation — only John #39 and Jeff #44 do.

### FTDNA Kit Mapping
- 4 William line kits identified (individual assignment unknown): 130368, 139565, 214669, 19390
- 6 kits matched by mutation pattern: 80064→Ken #83, 106258→Dave #101, 118832→Charles #116, 28846→Dane #35, 37125→Jeff #44, 33728→John #39
- 2 kits unresolved (both CDYa=36 only): 12910 and 130331 → Billy W #8 or Billy J #122
- 2 participants tested at different labs (not in FTDNA): Shelby #236, Tom #180

### Project Metadata (from FTDNA export)
- Current admins: Geoff Blackburn OAM, Michelle Leonard
- Co-admins: Bill Rodgers, Patrick Berry
- Members: 732 (up from 239 in Ben's book)
- Haplogroup: R-U152 > Z56 > BY3548 > Z43 > Z145 > BY1823 > BY193088

### Cleanup
- 9 legacy pages removed from `content/dna/` and archived to `Project/archived/dna-legacy-pages.zip`
- Build notes saved to `Project/research/dna-research-center-build.md`
- FTDNA export saved to `Project/incoming/FamilyTreeDNA - Berry Family DNA Project test results annex.html`

---

## 2026-04-04 — Documents Page: From 2 Links to 65-Record Dynamic Explorer

### The Big Picture
Transformed the Documents page from a bare list of 2 links into a comprehensive, data-driven document archive with 65 records spanning three centuries, filterable by record type, family line, location, and generation.

### Infrastructure
- **`data/documents.json`** — Tom built complete structured dataset: 65 records, 9 record types, 77 locations, generations 0–8, full metadata (people, tags, image counts, date ranges)
- **`layouts/documents/list.html`** — Dynamic explorer layout modeled on Wheel of Time architecture; renders entirely from JSON
- **`layouts/_shortcodes/document-card.html`** — New shortcode for document cards (used in static page, preserved for reference)
- **`static/js/documents-nav.js`** — Kate's sticky jump-nav with scrollspy (used on static version)
- **`layouts/_partials/docs/inject/body.html`** — Conditional JS injection for documents page

### Content
- **Cataloged and added 65 document records** across 12 categories:
  - Wills & Probate (4), Deeds & Land Records (6), Document Collections (3), Estate Records (1), Legal Documents (1), Military Records (2), Marriage Records (5), Vital Records — Death Certificates (5), Family Record PDFs (8), Census Record Collections (10), Family Records with Census & Vital Documents (17), Cemetery & Headstone Records (4)
- **Merged duplicate** `land-grant-robert-berry-jr.md` into `land-grant-to-robert-berry-jr.md`; fixed 4 stale links across 3 files (Martha)
- **Added death certificates** (5): Alexander Cates, Jesse Lee Berry, Herman Fantom Maners, Ruby A. Berry, Elizabeth Berry
- **Added marriage certificates** (3): Jesse Waldo Maners, Martin Adolphus Maners, Herman F. Maners Jr.
- **Discovered and cataloged** 21 document-focused pages in `content/ancestors/` (census pages, military vouchers, marriage indexes, cemetery records, land documents)

### Design
- **Dynamic explorer** with four filter dropdowns (Record Type, Family Line, Location, Generation), type toggle pills with counts, sort options (date, alpha, by type), and Clear All
- **Tagline:** *"Families not forgotten. Records that preserve the past."* (Aaron + Andrew collaboration)
- **Intro copy:** Andrew's Variation 2 — "The Warm Guide"
- **Dark forest theme** matching Timelines page aesthetic
- **Color-coded cards** with type badges, family line badges, location badges, generation badges, image counts
- **Vincent:** Count badges on category headers, section separators
- **Kate:** Sticky category jump-nav with scrollspy (static version)
- **CSS:** Document card styles, tagline, intro, count badges, jump-nav, explorer layout

### Team
- **Hired:** Jim — Accessibility Consultant (Contract), 20 years Fortune 500 ADA compliance
- **Contractors active this session:** Andrew (copy/SEO), Vincent (design), Kate (JavaScript), Tom (data)

---

## 2026-03-27 — Full Site Kickoff & Migration

### Session 1 — Infrastructure
- Initialized Hugo site with Hugo Book theme (vendored)
- Forest/green SCSS skin created (Lila)
- GitHub Actions deploy workflow (master → gh-pages, Hugo 0.155.2 pinned)
- CNAME, .nojekyll, .gitignore, start_webserver.sh
- Content skeleton: all sections scaffolded
- Git repo initialized on `master` branch
- Remote: https://github.com/berrytree-org/berrytree.github.io.git *(do not push until Richard says go)*

### Session 2 — About Page
- Migrated `about-us` WordPress page → `content/about/_index.md`
- Copied Ben Henderson and William Henderson photos

### Session 3 — Full Content Migration
- Migrated all 38 WordPress pages to Hugo markdown
- 54 images copied to `static/images/`
- Marriages table rebuilt as proper markdown tables
- Contact form junk removed; email placeholder added
- `genthree` (Robert & Elizabeth's children) moved to `content/ancestors/`
- Build: 66 pages, 0 errors

### Session 4 — Team Expansion & Site Improvements
- **Hired:** Martha Chen, Staff Genealogist (2026-03-27)
- **Homepage:** Berry banner (`cropped-new_berry_banner2.png`) restored as full-width hero; homepage expanded with family overview
- **Mobile:** Hamburger menu — CSS slide-in sidebar, touch-friendly, forest-themed
- **Email security:** `berrytree@thgnetworks.com` obfuscated via base64+JS shortcode (`{{< email >}}`); no plain email in HTML source
- **Security:** Added `security.txt` per RFC 9116; goldmark `unsafe = true` for HTML in markdown; legacy broken http:// links flagged for future cleanup
- **Vincent's 3 improvements:**
  1. Decorative `✦` ornament dividers replacing plain `<hr>`
  2. Generation badge styling hook (`.gen-badge`)
  3. Enhanced table styling — left border accent, first-column emphasis
- **Resources section added** (Martha + Andrew): databases, NC/VA records, DNA project info, research standards (GPS/BCG), abbreviations, recommended reading
- **Hugo config:** `markup.goldmark.renderer.unsafe = true` (required for hero HTML block)

---

## 2026-03-28 — Full Site Reconstruction & Link Repair

- **Full site reconstruction** from Berrytree_Archive backup — 264 new pages + 587 media files recovered
- Processed `Projects/incoming` assets — missing images + Mary Berry content
- Fixed all 50 broken `?page_id=` internal links (Tom)
- Reintegrated all new pages into site navigation; fixed slug links
- QA checklist created for reintegrated pages
- Fixed all broken links found during QA pass

---

## 2026-03-29 — Deployment Fixes & Cleanup

- Fixed 23 broken document/image links; added 11 missing static assets
- Removed large PDFs from git tracking; added to `.gitignore`
- Excluded `Projects/` directory and `start_webserver.sh` from git tracking
- Updated deploy workflow: trigger on `main`, publish to `master`
- Fixed hamburger menu not showing on mobile

---

## 2026-03-30 — Image & Media Cleanup

- **Full WordPress migration complete:** 264 new pages + 587 media files
- Lowercased all mixed-case image filenames and fixed content references
- Fixed 574 mixed-case image references across 62 content files
- Fixed `j-c-henderson` thumbnail reference in `sallymalenaberrync.md`
- Fixed 53 WordPress thumbnail references across 21 content files
- **All broken image references resolved — 0 missing images remain**
- Replaced Wagons South / Wagons West PDF link with Google Drive URL

---

## 2026-03-31 — Wheel of Time & Homepage Redesign

- **Wheel of Time interactive feature** — replaced static timeline pages with animated, interactive timeline
- **Front page redesign** incorporating Wheel of Time component
- Homepage polish: hamburger nav, suppress sidebar, transparent menu button
- Standardized generation tree formatting across all ancestor and family-line pages

---

## 2026-04-01 — Book Reader & Phase 2 Completion

- **Phase 2 complete:** Ancestor page redesign, sidebar accessibility, and complete link audit
- Updated all records files to `main`
- **Book reader launched:**
  - Preface + 8 chapters, landing page
  - John Robert Berry page consolidation
  - Added link to dad's book on main page
  - Chapter 6 (Joshua Berry) + updated book TOC with Ch 5–8 links
  - Completed Ch 9–12, 14, 17 and Books page featured card
- Fixed deploy workflow: publish to `gh-pages` instead of `master`

---

## 2026-04-03 — QC Pass, Wheel of Time Enhancements & Timeline Consolidation

- **Site-wide QC sweep:** accessibility, SEO, cross-links, link fixes, and design polish (Malcolm)
- **Wheel of Time event cards:** added person pills and family line pills
- **Legacy timeline page retirement:**
  - Deleted `1800-1899-timeline.md`, `1900-1999-timeline.md`, and `1810-2.md` from `content/ancestors/` — all content now in Wheel of Time JSON
  - Added missing Josiah Berry (1810, Thomas Berry line) to `timeline_events.json`
  - Census detail pages retained: `1800-orange-county-nc-census.md`, `1810-hannah-cate-census.md`
- **Site map cleanup:**
  - Removed dead links to 1600s, 1700s, 2000-Present, and old Timelines hub from both `site-map.md` and `extended-site-map.md`
  - Removed orphaned Timeline 1–6, Timeline Index, and Timeline Number 2 entries from extended site map
  - Added single Wheel of Time entry (`/timelines/`) in both site maps
  - Zero broken timeline links remain across all content files

---

## 2026-04-03 — Orphaned Pages Audit & Cleanup

- **Lila conducted orphaned page audit** — identified 7 content pages with zero inbound links from anywhere on the site
- **Deleted 6 orphaned/duplicate files:**
  - `ancestors/abbreviations-used-in-berrytree-org.md` — redundant with Resources page abbreviations table
  - `ancestors/dedication-page.md` — HTML duplicate of `dedication.md`
  - `books/ben-henderson-releases-second-berry-book.md` — duplicate book announcement with broken link
  - `family-lines/relationships-across-family-lines.md` — duplicate of `relationships.md`
  - `pictures/picturedirectoryt.md` — duplicate picture directory (typo filename)
  - `pictures/picture-directory.md` — duplicate picture directory; `pictures/_index.md` already serves this content
- **Linked 2 previously orphaned pages:**
  - `books/ben-henderson-second-book.md` — added link from Books index under Family Tree Index section
  - `contact/request-for-information.md` — added "Research Request: James Berry of Smith County, Tennessee" section to Contact page
- **Fixed 4 stale links** pointing to deleted `/pictures/picturedirectoryt/` → `/pictures/`: site-map, extended-site-map, alphabetical-pages-index, page-updates
- Full report: `Project/testing/orphaned_pages.md`

---

## 2026-04-03 — GEN Format Standardization

- **Lila converted 11 legacy pages** from raw WordPress HTML with dot-leader generation indexing to the site's GEN format standard
- Each page received: front matter (`weight`, `bookToc`), `ancestor-page` wrapper, `breadcrumb` shortcode, `ancestor-chain` shortcode, `ancestor-profile` shortcode, and clean markdown with dash-leader generation indentation
- **Files converted:**
  - `ancestors/david-crockett-berry-5.md` — Gen 6 ancestor page
  - `ancestors/henry-berry-tree.md` — Gen 3 Henry Berry family tree
  - `ancestors/census-page-for-thomas-berry.md` — Gen 3 census page
  - `ancestors/mattielstricklandala.md` — Gen 6 ancestor page
  - `ancestors/rb2sourcelist.md` — Gen 1 Robert Berry (PAC) origins research
  - `ancestors/john-h-berry-ala-tx.md` — Gen 5 ancestor page
  - `ancestors/whowellberrytx.md` — Gen 7 ancestor page
  - `ancestors/robertclarkberryga.md` — Gen 6 ancestor page
  - `ancestors/rbresourcelist.md` — Gen 2 Robert Berry resource list
  - `ancestors/robertberryancestors.md` — Gen 2 ancestors tree
  - `ancestors/wbfamilytree.md` — Gen 3 William Berry family tree (330+ entries, massive inline `<strong>` block parsed and restructured)
  - `family-lines/mary-berrys-family-tree.md` — Gen 3 Mary Berry family tree
- **Data integrity note:** `wbfamilytree.md` contained duplicate data blocks (Thomas Jefferson Berry, Lenard Bradford Berry, others appeared twice with slightly different info); duplicates were merged, unique entries preserved
- **Skipped 2 files** from original list: `ch01-williamsons-fosters-berrys-kemps.md` (already GEN formatted), `extended-site-map.md` (index page, dots are truncation not generation indexing)
- Typo fix: `david-crockett-berry-5.md` had "Aug 26 18916" corrected to 1916

---

## 2026-04-04 — Light Theme & Giovanni's Celebration

- **Documents Explorer** (`layouts/documents/list.html`) — switched from dark forest theme to site-wide light cream palette (Lila)
- **Wheel of Time** (`layouts/timelines/list.html`) — switched from dark forest theme to site-wide light cream palette; wagon wheel SVG retains woody/golden aesthetic (Lila)
- **Dark theme values preserved** in `Project/design/dark-settings.md` for future light/dark toggle implementation
- **Credit competition officially closed** — Andrew wins with 65 points
- **Giovanni's Celebration** — Full team dinner at Giovanni's Restaurant. M5 MacBook Pros, $1,000 bonuses, $250 Apple gift cards for all 13 team members (staff and contractors). Trophy ceremony for credit competition winner. Full account: `Project/notes/giovannis-party.md`

---

## 2026-04-05 — Em Dash Cleanup (Terry)

- **Site-wide em dash audit and cleanup** per new Standing Team Directive: casual pause em dashes replaced with commas; attribution, title, and parenthetical em dashes preserved
- **30 replacements across 13 files:**
  - `content/_index.md` — 3 (prose pauses in intro and table)
  - `content/about/_index.md` — 4 (description + prose pauses)
  - `content/contact/_index.md` — 2 (description + Option 1 text)
  - `content/resources/_index.md` — 8 (table descriptions + GPS standards list)
  - `content/ancestors/david-j-berry-sr.md` — 5 (prose pauses in narrative)
  - `content/ancestors/robert-berry-jr.md` — 6 (prose pauses in narrative)
  - `content/ancestors/john-robert-berry.md` — 1 ("disease, most likely typhoid")
  - `content/ancestors/joshua-berry-sr.md` — 3 (prose pauses + child details)
  - `content/ancestors/thomas-berry.md` — 4 (prose pauses + census summary)
  - `content/ancestors/william-berry.md` — 2 (prose pauses)
  - `content/pictures/_index.md` — 1 (description meta)
  - `content/family-lines/_index.md` — 1 (description meta)
  - `layouts/index.html` — 2 (homepage card descriptions)
- **Preserved (not touched):** all "Born X — Died Y" date attributions, census year entries, title/subtitle separators, document references, spouse attributions, parenthetical inserts (double em dashes), and all code comments/technical documentation

---

## Outstanding Items

| Item | Owner | Status |
|---|---|---|
| ~~324 legacy `http://?page_id=N` broken links~~ | ~~Tom~~ | **Done** (2026-03-28) |
| ~~All broken image references~~ | ~~Team~~ | **Done** (2026-03-30) |
| ~~Phase 2: Ancestor redesign + link audit~~ | ~~Team~~ | **Done** (2026-04-01) |
| ~~Book reader: all chapters~~ | ~~Team~~ | **Done** (2026-04-01) |
| DNA pages restructuring decision | Aaron | Deferred |
| Contact form (replace static email) | Terry / Lila | Future |
| `usaconflicts`, `page-updates`, `announcements` pages | Aaron | Parked |
| ~~Family-line tree pages (Joshua Sr., Thomas, William, Elizabeth)~~ | ~~Lila / Martha~~ | **Done** (2026-04-05) |
| Joshua tree: fix 2 inherited gen-class mismatches (Lewis Berry spouse, Roy Felts) | Lila | LOW — rendering unaffected |
| Clean up `.old` backup files | Team | In .gitignore but still in repo |
| Missing images (`robertcberry1870ala.jpg`, `stone2large.jpg`) | Aaron | Still looking |
| ~~Giovanni's celebration dinner~~ | ~~Pam / Rebecca~~ | **Done** (2026-04-04) |
| Light/dark theme toggle | Lila | Future — dark values saved in `Project/design/dark-settings.md` |
