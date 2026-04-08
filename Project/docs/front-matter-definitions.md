# Front Matter Definitions & Taxonomy Reference

**Status:** Active
**Created:** 2026-04-07
**Owner:** Lila (structure), Martha (genealogical values), Terry (QC fields)
**Approved by:** Aaron
**See also:** `Project/notes/tag-strategy.md` (strategy rationale and implementation phases)

---

## Overview

Every content page in berrytree.org uses YAML front matter to define metadata. This document is the authoritative reference for all front matter fields, their types, allowed values, and usage rules.

Front matter serves two purposes:
1. **Public taxonomies** — visitor-facing navigation and discovery (`families`, `periods`, `tags`)
2. **Internal tracking** — team-only quality control and provenance fields (`qc_status`, `qc_date`, `last_updated`, `content_source`, `sources_verified`)

---

## Standard Hugo Fields

These are built-in Hugo fields used across the site.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Page title displayed in browser and navigation |
| `weight` | integer | Recommended | Sort order within section (lower = first) |
| `bookToc` | boolean | Recommended | Enable/disable table of contents (Hugo Book theme) |
| `description` | string | Optional | SEO meta description; used on section index pages |
| `aliases` | list of strings | As needed | URL redirects from old paths to this page |

---

## Public Taxonomies

These fields generate visitor-facing taxonomy pages. Hugo builds listing pages at `/families/`, `/periods/`, and `/tags/`.

### `families` — Family Line Affiliation

**Type:** List of strings
**Required on:** All ancestor pages, family-line pages, book chapters
**Optional on:** Documents, pictures, resources
**Hugo taxonomy key:** `family = "families"` (defined in `hugo.toml`)

#### Allowed Values

| Value | Gen 3 Ancestor | Primary Locations |
|-------|---------------|-------------------|
| `Joshua Berry` | Joshua Berry × Nancy Ellison | Orange County NC, GA, OH |
| `John Berry` | John Berry × Martha Stepp | Person County NC, Jackson County GA |
| `Thomas Berry` | Thomas Berry × Sarah Cate | Orange County NC, Wayne County TN |
| `Isaac Berry` | Isaac Berry × Lydia Berry | Orange County NC |
| `Mary Berry` | Mary Berry × George Waggoner / James Camp | Orange County NC, Rutherford County NC, SC |
| `William Berry` | William Berry × Hannah Cate | Orange County NC, Wayne County TN |
| `Henry Berry` | Henry Berry × Fanny Ashley | Orange County NC |
| `Elizabeth Berry` | Elizabeth Berry (unwed) × William Riley | Orange County NC |
| `David J Berry` | David J. Berry × Mary Blalock | Orange County NC, Fayette County GA |
| `Robert Berry Jr` | Robert Berry Jr. × Mary Waggoner | Orange County NC, Fayette County AL |

#### Rules

- Use exact values as listed above (title case, no periods in "David J Berry" and "Robert Berry Jr")
- Pages may have multiple families (e.g., cross-line marriages)
- Gen 1–2 pages (Robert Berry PAC, Robert Berry OC, Elizabeth Cate, John Cate, Mary Kempe, Roger Williamson) receive ALL 10 family values
- Reference/utility pages (indexes, census compilations, site pages) receive no family assignment

#### Example

```yaml
families: ["Joshua Berry"]
families: ["Robert Berry Jr", "Mary Berry"]           # cross-line page
families: ["Joshua Berry", "John Berry", "Thomas Berry", "Isaac Berry", "Mary Berry", "William Berry", "Henry Berry", "Elizabeth Berry", "David J Berry", "Robert Berry Jr"]  # Gen 1-2 page
```

---

### `periods` — Historical Era

**Type:** List of strings
**Required on:** Ancestor pages, book chapters
**Optional on:** Documents, pictures
**Hugo taxonomy key:** `period = "periods"` (defined in `hugo.toml`)

#### Allowed Values

| Value | Date Range | Context |
|-------|------------|---------|
| `Colonial` | pre-1776 | PAC/VA origins, earliest Berry records |
| `Revolutionary` | 1776–1800 | War service, early land grants, OC establishment |
| `Early Settlement` | 1800–1840 | Berry migration south/west from NC |
| `Antebellum` | 1840–1861 | Established families, pre-war era |
| `Civil War` | 1861–1865 | Military service, disruption |
| `Reconstruction` | 1865–1900 | Post-war recovery, westward expansion |
| `Modern` | 1900+ | 20th century and beyond |

#### Rules

- Assign based on the person's primary active adult period
- Pages may have multiple periods if the person's life spanned eras significantly
- Census pages get the period of the census year
- Document pages get the period of the document date
- Limit to 2 periods per page

#### Example

```yaml
periods: ["Revolutionary", "Early Settlement"]
periods: ["Civil War", "Reconstruction"]
```

---

### `tags` — General-Purpose Discovery Tags

**Type:** List of strings
**Optional on:** All content pages
**Hugo taxonomy key:** `tag = "tags"` (defined in `hugo.toml`)
**New tags require Aaron's approval before use.**

#### Record Type Tags

| Tag | Use For |
|-----|---------|
| `census` | Pages featuring census data or analysis |
| `will` | Wills, probate records |
| `deed` | Land deeds, property transfers |
| `land-grant` | Original land grants |
| `marriage-bond` | Marriage bonds, licenses |
| `military` | Military service, pension records |
| `obituary` | Death notices, obituaries |
| `cemetery` | Cemetery records, burial information |
| `estate` | Estate sales, inventories |
| `power-of-attorney` | POA documents |

#### Content Type Tags

| Tag | Use For |
|-----|---------|
| `biography` | Narrative life story pages |
| `family-tree` | Tree/lineage pages |
| `source-list` | Source compilation pages |
| `census-page` | Dedicated census data pages |
| `book-chapter` | Chapters from Ben's books |
| `document` | Primary source document pages |
| `photograph` | Photo collections or pages with significant photography |
| `index-page` | Site indexes and finding aids |

#### Location Tags

| Tag | Use For |
|-----|---------|
| `prince-anne-county-va` | PAC Virginia origins |
| `orange-county-nc` | Orange County NC (primary Berry homeland) |
| `georgia` | Georgia lines |
| `alabama` | Alabama lines |
| `texas` | Texas lines |
| `tennessee` | Tennessee lines |
| `ohio` | Ohio lines |
| `iowa` | Iowa lines |
| `kentucky` | Kentucky lines |

#### Topic Tags

| Tag | Use For |
|-----|---------|
| `migration` | Pages discussing family movement/relocation |
| `dna` | DNA testing, genetic genealogy |
| `unresolved` | Open questions, unconfirmed connections |
| `pac-to-oc` | The PAC-to-OC connection investigation |

#### Rules

- All tags use lowercase-hyphenated slugs
- No freeform tagging; use only approved values
- New tags require Aaron's approval and must be added to this document
- Content type tag is typically first in the list

#### Example

```yaml
tags: ["biography", "census", "land-grant", "orange-county-nc", "georgia"]
tags: ["census-page", "census"]
tags: ["index-page"]
```

---

## Internal Tracking Fields

These fields are for team use only. Hugo does not build pages for them. They are invisible to visitors.

| Field | Type | Allowed Values | Purpose |
|-------|------|---------------|---------|
| `qc_owner` | date | YYYY-MM-DD or blank | Aaron's review sign-off date |
| `qc_webteam` | date | YYYY-MM-DD or blank | Structural/visual QC sign-off date (Terry/Malcolm) |
| `qc_genealogy` | date | YYYY-MM-DD or blank | Genealogical source verification date (Martha) |
| `last_updated` | date | YYYY-MM-DD | Date of last substantive content change |
| `content_source` | string | `wp-export`, `original`, `book`, `new` | Content provenance |

### QC Date Fields — How They Work

Three independent review lanes, each tracked by a single date field:

| Field | Reviewer | What's Checked |
|-------|----------|----------------|
| `qc_owner` | Aaron | Content approval, presentation, ready for public |
| `qc_webteam` | Terry/Malcolm | Structure, formatting, HTML cleanup, heading conventions, links |
| `qc_genealogy` | Martha | Source citations, genealogical accuracy, unsourced claims |

### Rules

- **Blank = not yet reviewed** (or reviewed and found issues — reviewer does not stamp until the page is clean)
- **Has a date = cleared** as of that date by that reviewer
- **Stale = `last_updated` is newer than a QC date** — that reviewer needs another pass
- **Fully cleared = all three QC dates are present and none are stale**
- Each reviewer only updates their own field. Never overwrite another reviewer's date.
- `last_updated` updates on substantive content edits, not cosmetic fixes
- `content_source` is set once at page creation and does not change
- New pages start with all three QC fields blank

---

## Complete Front Matter Example

### Ancestor (Person) Page — Fully Cleared

```yaml
---
title: "Joshua Berry Sr."
weight: 4
bookToc: true
aliases:
  - /ancestors/joshuaberry/
families: ["Joshua Berry"]
periods: ["Revolutionary", "Early Settlement"]
tags: ["biography", "census", "land-grant", "orange-county-nc"]
qc_owner: 2026-04-08
qc_webteam: 2026-04-08
qc_genealogy: 2026-04-08
last_updated: 2026-04-07
content_source: "wp-export"
---
```

### Ancestor Page — Partially Reviewed

```yaml
---
title: "Joshua Berry Family Tree"
aliases:
  - /ancestors/joshberrytree/
families: ["Joshua Berry"]
periods: ["Revolutionary", "Early Settlement"]
tags: ["family-tree", "orange-county-nc"]
qc_webteam: 2026-04-08
last_updated: 2026-04-07
content_source: "wp-export"
---
```

### Reference/Utility Page — Not Yet Reviewed

```yaml
---
title: "Generation Three"
tags: ["index-page"]
last_updated: 2026-04-07
content_source: "wp-export"
---
```

### Gen 1-2 Ancestor Page — Fully Cleared

```yaml
---
title: "Robert Berry — Orange County, NC"
bookToc: true
families: ["Joshua Berry", "John Berry", "Thomas Berry", "Isaac Berry", "Mary Berry", "William Berry", "Henry Berry", "Elizabeth Berry", "David J Berry", "Robert Berry Jr"]
periods: ["Colonial", "Revolutionary"]
tags: ["biography", "orange-county-nc", "will", "land-grant"]
qc_owner: 2026-04-08
qc_webteam: 2026-04-08
qc_genealogy: 2026-04-08
last_updated: 2026-04-07
content_source: "wp-export"
---
```

---

## Taxonomy Limits

| Rule | Limit |
|------|-------|
| Max taxonomy values per page (all three combined) | 10 (exception: Gen 1-2 pages with all families) |
| Minimum pages per tag (orphan threshold) | 2 |
| Slug format | lowercase-hyphenated (tags), title case (families) |

---

## Governance

- New taxonomy values require Aaron's approval
- Quarterly audit for orphan tags (fewer than 2 pages)
- This document must be updated whenever new values are approved
- Design criteria (`Project/design_criteria.md`) governs visual presentation of taxonomy pages

---

*Created 2026-04-07 by Lila, Martha, Terry, and Pam*
