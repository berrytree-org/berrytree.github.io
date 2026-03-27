# Berrytree.org Change Log

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

## Outstanding Items

| Item | Owner | Status |
|---|---|---|
| 324 legacy `http://?page_id=N` broken links in content | Martha / Andrew | Open |
| 3 missing images on Roger Williamson PAC page | Richard / research | Open |
| GitHub repo push / go-live | Richard | Awaiting approval |
| DNS pointed to GitHub Pages? | Richard | Unconfirmed |
| SSH key for push access | Richard | Unconfirmed |
| DNA pages restructuring decision | Richard | Deferred |
| GEDCOM/genthree data files migration plan | Martha | Open |
| Contact form (replace static email) | Terry / Lila | Future |
| `usaconflicts`, `page-updates`, `announcements` pages | Richard | Parked |
