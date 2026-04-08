# Meeting Notes — 2026-04-08

**Attendees:** Aaron, Lila, Pam, Martha, Terry, Rebecca (full core staff)
**Location:** Conference Room A
**Meeting Weather (Rebecca):** Sunny with a light breeze

---

## Agenda

### Session 1 (Morning)
1. Mobile gold hamburger menu icon
2. DNA Research Center section improvements
3. Wheel of Time category filter toggles
4. Documents Explorer filter toggles
5. W.P. Berry image cleanup
6. Mobile landing page menu fix
7. Addendum review for "Our Berrys in Frontier America"
8. About Us page portrait redesign

### Session 2 (Afternoon — Full Staff Meeting)
9. Action items board audit and refresh

---

## Work Completed

### 1. Mobile Gold Hamburger Menu Icon
Lila added a CSS filter to render the hamburger icon in gold on non-landing mobile pages, maintaining visual consistency with the site's forest/gold palette.

**Commit:** `b448807` — Mobile: gold hamburger menu icon on subpages

### 2. DNA Research Center — Collapsed Sections and Clickable Headers
Collapsed the "Understanding Y-DNA Testing" and "The Berry Y-DNA Project" sections by default to reduce scroll fatigue. Made full section headers clickable for expand/collapse, not just the small arrow icons.

**Commit:** `505e3b3` — DNA Research Center: collapse training sections by default, make headers clickable

### 3. Wheel of Time — All/None Category Filter Toggles
Added All/None buttons for the category filter toggles, making it easier to quickly select or deselect all categories at once.

**Commit:** `d1fe908`

### 4. Documents Explorer — All/None Type Filter Toggles
Applied the same All/None toggle pattern to the Documents Explorer's type filters. Recommended as an additional improvement under the new Page Name Reference directive.

**Commit:** `d1fe908`

### 5. W.P. Berry Image Removed from Robert Berry (OC) Page
Removed the W.P. Berry image from the Robert Berry (OC) page since it already exists on the Wiley P. Berry Sr. page. No need for duplication.

**Commit:** `d1fe908`

### 6. Mobile Landing Page — Hamburger Close Button Fix
Fixed the hamburger close (X) button overlapping the panel logo on mobile by adding left padding to `.hb-panel__logo`.

**Commit:** `d1fe908`

### 7. Addendum Review — "Our Berrys in Frontier America"
Martha reviewed the 10-page addendum PDF. All corrections (William Clarence Berry parentage, Y-DNA chart, census analysis, deed transcriptions) were confirmed as already incorporated into the 2015 revised edition. Added a note to the book reader Table of Contents clarifying the addendum's status.

**Commit:** `70a91c4` — About Us: thumbnail portraits with text wrap; book TOC: addendum note

### 8. About Us — Thumbnail Portraits with Text Wrap
Converted the About Us page's full-width portraits to 200px floated thumbnails with text wrap and click-to-enlarge links, improving layout and readability.

**Commit:** `70a91c4`

---

## Decisions Made

1. Addendum does not need its own chapter in the book reader. It is a 1st Edition correction document already absorbed into the 2015 revision.
2. All/None toggle added to Documents Explorer as well, since the same UX improvement applied (per new Page Name Reference directive).
3. Martha's addendum note wording approved by Aaron for the book TOC.

---

## Directives Added

- **Page Name Reference** — Added to CLAUDE.md. Match actual page titles as rendered on site, not internal descriptions. Recommend additional pages if applicable.

---

## Commits Summary

| Hash | Description |
|------|-------------|
| `b448807` | Mobile: gold hamburger menu icon on subpages |
| `505e3b3` | DNA Research Center: collapse training sections by default, make headers clickable |
| `d1fe908` | All/None category toggles, WP Berry image move, mobile menu logo fix |
| `70a91c4` | About Us: thumbnail portraits with text wrap; book TOC: addendum note |

---

## Session 2 — Action Items Board Audit

Pam conducted a full audit of the action items list (`Project/notes/action-items.txt`) against the current codebase. Findings:

### Items Confirmed COMPLETE (to move to Completed section)
- **Family-line tree pages** — All four (Joshua Sr., Thomas, William, Elizabeth) exist in `content/docs/family-lines/`. Elizabeth is lightweight (769 bytes) but present.
- **Page tagging system** — Fully deployed. Three taxonomies (tags, families, periods) across 254 pages with custom layout templates and landing pages.

### Items Resolved (to close)
- **Missing images** (`robertcberry1870ala.jpg`, `stone2large.jpg`) — Neither file is referenced anywhere in site content. Searched both Ben Henderson archives (READ ONLY and Research). No exact match found. No broken image links. Clean close.

### Items Needing Status Update
- **US Conflicts page** — Already converted at `content/ancestors/usaconflicts.md`. Needs a QC pass, not a migration. Aaron confirmed complete.

### Directive Test
Aaron tested Pam's filing enforcement directive by requesting meeting notes be placed in `Project/testing/`. Pam flagged the incorrect location and redirected to `Project/meetings/`. Test passed.

---

## Session 2 — QC Report Script

Terry built `Project/tools/qc-report.py`, an automated QC status report that reads front matter fields and generates summary reports by section, content source, and structural issues. Supports `--detail`, `--section`, `--flagged`, and `--stale` flags.

Initial baseline report: 254 pages scanned, 159 with structural issues (150 raw divs, 84 raw spans, 55 bare h2 headings, 31 bare h3 headings, 25 raw strong tags).

Lila noted many raw divs are intentional (children lists, census tables). May need an allowlist in future.

---

## Session 2 — Three-Lane QC System

Aaron raised the need to separate team QC from owner QC to avoid losing review data. Discussion led to a streamlined three-date-field system:

| Field | Reviewer | Meaning |
|-------|----------|---------|
| `qc_owner` | Aaron | Owner review sign-off date |
| `qc_webteam` | Terry/Malcolm | Structural/visual QC sign-off date |
| `qc_genealogy` | Martha | Source verification sign-off date |

**Rules:** Blank = not yet cleared. Date = cleared. Stale = `last_updated` newer than QC date. Fully cleared = all three dates present, none stale.

**Replaced:** `qc_status` (enum), `qc_date` (date), `sources_verified` (boolean).

Front matter definitions updated at `Project/docs/front-matter-definitions.md`.

---

## Session 2 — Generic Front Matter Updater

Lila built `Project/tools/update-frontmatter.py`:
- **Operations:** add, remove, rename, update
- **Safety:** Dry-run by default, `--write` to apply
- **Filters:** `--section`, `--has-field`, `--missing-field`, `--source`, `--file`
- **Positioning:** `--after` / `--before` for field insertion
- **Format support:** Auto-detects YAML (`---`) and TOML (`+++`), or force with `--format`
- **Portable:** `--content-dir` to point at any Hugo site

Aaron's idea. Lila approved with guardrails. Built, tested, and immediately used for the QC migration.

---

## Session 2 — QC Field Migration

Migrated all 254 pages from old QC fields to new three-lane system using `update-frontmatter.py`:

1. `remove qc_status` — 254 modified
2. `remove sources_verified` — 254 modified
3. `add qc_owner --after last_updated` — 254 modified
4. `add qc_webteam --after qc_owner` — 254 modified
5. `add qc_genealogy --after qc_webteam` — 254 modified

Zero errors across all five steps. QC report script updated to read new fields. Spot-checked by Aaron.

---

## Session 2 — Team Motto

Aaron proposed a team motto. Team workshopped wording. Final version adopted:

> **"We all make each other's lives better."**

Added to the top of `Project/staff/team_interaction_map.md`.

---

## Decisions Made (Session 2)

1. Three-lane QC system adopted (qc_owner, qc_webteam, qc_genealogy) replacing single qc_status field
2. Blank-until-clean policy: QC date only stamped when page passes, not when reviewed
3. Missing images item closed (not referenced in content, not found in Ben's archives)
4. US Conflicts QC confirmed complete by Aaron
5. Team motto adopted: "We all make each other's lives better."

---

## Action Items (Updated)

- [x] Terry: Build QC report script — DONE
- [x] US Conflicts page QC — DONE (Aaron confirmed)
- [ ] Martha: Continue `qc_genealogy` pass on Gen 3 pages (carried over)
- [ ] Continue general QC review of recently converted pages
- [ ] PLAN list (24 items) — Cherry-pick session still pending
- [ ] WikiTree migration — Paused (LOW)
- [ ] Light/dark theme toggle — LOW
- [ ] External domain monitoring — LOW, Sherlock watching

---

*Notes by Pam — 2026-04-08*
