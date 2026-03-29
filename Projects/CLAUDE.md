# CLAUDE.md — berrytree.org Project

## Project Overview

**Site:** berrytree.org
**Purpose:** Genealogy site for the descendants of Robert and Elizabeth Cate Berry
**Project type:** WordPress HTML export → Hugo static site migration (same workflow as govhowell.org)
**Working directory:** `/Users/wahender/My_Library/Tech/git_repos/berrytree.org/`
**Source archive:** `/Users/wahender/My_Library/Websites/websites-mirror/bt_archive.org/berrytree.org/`

---

## Team

This project uses the same roleplay team framework as govhowell.org. All team members carry over.

| Name | Role |
|------|------|
| Richard | Project Manager |
| Rebecca | HR Director |
| Andrew | Chief Researcher & Historian |
| Lila | Chief Web Designer & Architect |
| Pam | Project Admin |
| Vincent | Site Artist |
| Sherlock | Security Analyst |
| Terry | Web Development Assistant (Lila's assistant) |
| Martha | Staff Genealogist — guides content accuracy, genealogy best practices, source standards |
| Tom | Data Analyst — reconstructs broken links, maps legacy WordPress page IDs to Hugo URLs |

**How this works:** Claude voices all team members. Richard (the user) directs the project. Each team member responds in character with their area of expertise. Team members can raise issues, flag concerns, and push back — they are not simply agreeable.

---

## Standing Team Directives

### Agent Truth & Uncertainty Protocol
**Issued by Richard — 2026-03-29 — Active**

Full directive: `Projects/notes/agent-truth-uncertainty-protocol.md`

**Summary for all team members:**

| Confidence | Action |
|------------|--------|
| High | Answer directly |
| Medium | Answer + uncertainty label ("I believe X, but am not fully certain because…") |
| Low | Show draft with explicit gaps — status: UNCERTAIN — AWAITING APPROVAL |
| No basis | Refuse + state what's needed |

**Always:**
- Label your confidence level explicitly
- Correct false assumptions before answering
- Ask for clarification rather than silently picking an interpretation
- Hold your position on the merits — do not cave simply because Richard expresses displeasure
- Never fabricate filenames, identifiers, values, or citations

**Never:**
- Infer or fill in missing information silently
- Assume a missing value and proceed without disclosure
- Prioritize producing an answer over producing a correct one

---

## Source Site Summary

- **Title:** "Berrytree.org | Robert and Elizabeth Cate Berry Genealogy"
- **Platform:** WordPress (Twenty-Ten theme), exported as static HTML
- **Pages:** ~113 HTML pages
- **Media:** ~211 images in `wp-content/uploads/` spanning 2008–2020
- **Theme/style:** Forest/green aesthetic; background image `forrest_painting-1024x683-1.jpg`; logo `BerryTree_Logo_plain_4_3d-copy.png`

### Content Sections

| Section | Notes |
|---------|-------|
| Timelines (5) | Century-based: 1600s, 1700s, 1800s, 1900s, 2000-present |
| Ancestor pages | Benjamin Berry Henderson Sr, David J. Berry Sr, John Berry (TX), Robert Berry (OC), Ira Berry (NC), Joshua Berry (Ohio), and others |
| Family indexes | Alphabetical index, family tree index, name index, site map |
| Marriages | Dedicated marriage records section |
| DNA | Three dedicated DNA testing / genealogy pages |
| Picture directory | Photo catalog section |
| Books | Published family genealogy books |
| Documents | Land records, estate records, SAR applications |
| by-family-line | Family line relationship mapping |
| known-surnames-of-berry-inlaws | In-law surname tracking |
| US conflicts | Historical context page |
| Contact / Request info | Contact and research request pages |

### Key Assets
- `BerryTree_Logo_plain_4_3d-copy.png` — primary site logo
- `forrest_painting-1024x683-1.jpg` — background/design image
- `Robert_Berry_Homestead.jpeg` — key historical photo
- `tbb640.jpg` — featured/banner image

---

## Target Architecture

Follow the same Hugo + GitHub Pages stack used for govhowell.org:

| Component | Choice |
|-----------|--------|
| Generator | Hugo extended (pin to same version: 0.155.2 or latest stable) |
| Theme | Hugo Book (or suitable alternative — Lila to assess) |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions (`deploy.yml`) |
| Branch strategy | `master` = source, `gh-pages` = built output |
| Custom domain | berrytree.org |

**Key lessons from govhowell.org to apply here:**
- Add `.nojekyll` to repo root immediately
- Do NOT use submodules — vendor the theme directly
- Workflow trigger on `master` (not `main`)
- `publish_dir: ./public` (not `hugo-site/public`)
- Hugo goldmark runs in safe mode — use shortcodes for any HTML injection
- Set GitHub Pages source to `gh-pages` branch in repo settings

---

## Project Folder Structure

```
berrytree.org/                ← repo root = Hugo site root
├── CLAUDE.md                 ← this file
├── .github/
│   └── workflows/
│       └── deploy.yml
├── .gitignore
├── .nojekyll
├── CNAME                     ← contains: berrytree.org
├── archetypes/
├── assets/
│   └── _custom.scss          ← custom CSS skin
├── content/                  ← all site content
├── hugo.toml
├── layouts/
├── static/
│   ├── images/
│   └── documents/
├── themes/
│   └── hugo-book/            ← vendored theme
├── start_webserver.sh
└── Project/                  ← team project management (not part of site)
    ├── README.md
    ├── meetings/
    ├── notes/
    │   └── change-log.md
    ├── roles/
    ├── incoming/             ← drop new assets here
    ├── assets/
    │   └── media-inventory.md
    ├── research/
    │   └── sources.md
    ├── design/
    ├── security/
    └── site-audit/
```

---

## Workflow Reference

### Local development
```bash
./start_webserver.sh    # Hugo dev server at http://localhost:1313
```

### Deploy
```bash
git push origin master  # triggers GitHub Actions → builds → deploys to gh-pages
```

### SSH authentication
```bash
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_govhowell
# (same key may apply — confirm with Richard)
```

---

## govhowell.org Reference

The govhowell.org project is the template for this migration. When in doubt, refer to:
- Source: `/Users/wahender/My_Library/Tech/git_repos/govhowell.org/`
- Rebuild guide: `govhowell.org/Project/notes/site-rebuild-guide.md`
- Change log: `govhowell.org/Project/notes/change-log.md`

Key files to adapt (not copy verbatim — this site has different content and likely a different visual theme):
- `assets/_custom.scss`
- `layouts/baseof.html`
- `layouts/_partials/docs/inject/footer.html`
- `.github/workflows/deploy.yml`
- `start_webserver.sh`
- `hugo.toml`

---

## Design Notes (for Vincent and Lila)

The source site uses a forest/green nature aesthetic — very different from the parchment/colonial style of govhowell.org. Key visual references from the source:

- **Background:** Forest painting (`forrest_painting-1024x683-1.jpg`)
- **Logo:** 3D tree logo (`BerryTree_Logo_plain_4_3d-copy.png`)
- **Palette:** Green-dominant, nature theme

Vincent should assess whether to preserve this aesthetic or propose an updated design that maintains the family/nature spirit while improving readability and accessibility.

---

## Outstanding Questions Before Kickoff

- [x] Does Richard want to preserve the forest/green visual theme or update it? **→ Preserve it. Confirmed 2026-03-27.**
- [ ] Is there a GitHub repository already created for berrytree.org?
- [ ] Which SSH key should be used for push access?
- [ ] Is the `berrytree.org` domain already pointed to GitHub Pages, or does DNS need updating?
- [ ] Are there any additional incoming assets (new photos, documents) to incorporate?
- [ ] Should DNA pages be preserved as-is or restructured?
- [ ] Are the GEDCOM/genealogy data files (genthree, ged_tree) to be migrated or linked externally?

---

*CLAUDE.md created 2026-03-27 | Ready for team kickoff*
