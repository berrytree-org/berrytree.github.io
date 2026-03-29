# Internal Link Audit & Fix Report

**Audited by:** Tom, Terry, Lila
**Date:** 2026-03-29
**Scope:** All internal links to `/documents/`, `/images/`, `/census/` across all content files
**Build result before:** 99 pages, 496 static files, 0 Hugo errors
**Build result after:** 99 pages, 507 static files, 0 Hugo errors

---

## Summary

| Category | Links Checked | Valid Before | Broken Before | Fixed | Remaining |
|----------|--------------|--------------|---------------|-------|-----------|
| `/documents/` content pages | 6 | 6 | 0 | — | 0 |
| `/documents/` static PDFs | 18 | 11 | 7 | 7 | 0 |
| `/census/` | 2 | 2 | 0 | — | 0 |
| `/images/` | ~420 | ~405 | 16 | 16 | 0 |
| **Total** | **~446** | **~424** | **23** | **23** | **0** |

---

## Files Added to Static

### Images added to `static/images/` (4 files)
All sourced from `/Volumes/Starfish_Backup/Berrytree_Archive/`:

| File | Archive Source |
|------|---------------|
| `maryblalockbond.jpg` | `wp-content/uploads/2015/01/` |
| `voucher1509.jpg` | `wp-content/uploads/2012/03/` |
| `robertberry1755taxlist.jpg` | `wp-content/uploads/2012/03/` |
| `Front-Cover-for-INDEX-Bk-e1443292129249.jpg` | `wp-content/uploads/2015/01/` |

### PDFs added to `static/documents/` (7 files)

| File | Archive Source | Referenced In |
|------|---------------|---------------|
| `berrybrothers.pdf` | `Projects/incoming/` | `family-lines/david-j-berry-family-tree.md` |
| `ednahannahfamily.pdf` | `wp-content/uploads/2012/09/` | `ancestors/thomas-person-berry.md` |
| `marthaberrywrenn.pdf` | `wp-content/uploads/2012/09/` | `ancestors/thomas-person-berry.md` |
| `ettaemmaberryandchildren.pdf` | `wp-content/uploads/2012/09/` | `ancestors/thomas-person-berry.md` |
| `dtcateskids.pdf` | `wp-content/uploads/2012/09/` | `ancestors/thomas-person-berry.md` |
| `danrberryfamily.pdf` | `wp-content/uploads/2012/09/` | `ancestors/thomas-person-berry.md` |
| `thomasandlucysgrandchildren.pdf` | `wp-content/uploads/2012/09/` | `ancestors/thomas-person-berry.md` |

---

## Link Fixes by File

### `content/family-lines/david-j-berry-family-tree.md` (2 links fixed)

| Line | Before | After | Notes |
|------|--------|-------|-------|
| 926 | `/images/02/berrybrothers.pdf` | `/documents/berrybrothers.pdf` | Wrong directory; PDF added |
| 928 | `/images/02/berrybrothers.pdf` | `/documents/berrybrothers.pdf` | Wrong directory; PDF added |

---

### `content/ancestors/robert-berry-jr.md` (4 links fixed)

Census images were in `static/census/` but referenced as `/images/`.

| Line | Before | After |
|------|--------|-------|
| 128 | `/images/robertjr1830ala.jpg` | `/census/robertjr1830ala.jpg` |
| 130 | `/images/robertjrslavepage1830ala.jpg` | `/census/robertjrslavepage1830ala.jpg` |
| 132 | `/images/robertjr1840ala.jpg` | `/census/robertjr1840ala.jpg` |
| 134 | `/images/robertjrslavpage1840ala.jpg` | `/census/robertjrslavpage1840ala.jpg` |

---

### `content/ancestors/robert-berry-jr-detail.md` (4 links fixed)

Same census images referenced via `/images/08/` subdirectory (never existed).

| Line | Before | After |
|------|--------|-------|
| 145 | `/images/08/robertjr1830ala.jpg` | `/census/robertjr1830ala.jpg` |
| 147 | `/images/08/robertjrslavepage1830ala.jpg` | `/census/robertjrslavepage1830ala.jpg` |
| 149 | `/images/08/robertjr1840ala.jpg` | `/census/robertjr1840ala.jpg` |
| 151 | `/images/08/robertjrslavpage1840ala.jpg` | `/census/robertjrslavpage1840ala.jpg` |

---

### `content/ancestors/thomas-person-berry.md` (12 links fixed)

Original site stored both PDFs and full-size images under `/images/09/` — that subdirectory was never created. PDFs moved to `/documents/`; JPGs corrected to flat `/images/` path (files already existed there).

| Line | Before | After | Type |
|------|--------|-------|------|
| 16 | `/images/09/tp-berry-family-bible-page-3-enhanced.jpg` | `/images/tp-berry-family-bible-page-3-enhanced.jpg` | Image |
| 84 | `/images/09/ednahannahfamily.pdf` | `/documents/ednahannahfamily.pdf` | PDF added |
| 87 | `/images/09/marthaberrywrenn.pdf` | `/documents/marthaberrywrenn.pdf` | PDF added |
| 90 | `/images/09/ettaemmaberryandchildren.pdf` | `/documents/ettaemmaberryandchildren.pdf` | PDF added |
| 90 | `/images/09/emmaberryclayton.jpg` | `/images/emmaberryclayton.jpg` | Image |
| 93 | `/images/09/dtcateskids.pdf` | `/documents/dtcateskids.pdf` | PDF added |
| 99 | `/images/09/danrberryfamily.pdf` | `/documents/danrberryfamily.pdf` | PDF added |
| 105 | `/images/09/danrberryfamily.pdf` | `/documents/danrberryfamily.pdf` | PDF added |
| 105 | `/images/09/maggieturner.jpg` | `/images/maggieturner.jpg` | Image |
| 114 | `/images/09/Thomas-Person-Berry-Picture-and-youngest-grand-daughter-Audrie-Schull.jpg` | `/images/Thomas-Person-Berry-Picture-and-youngest-grand-daughter-Audrie-Schull.jpg` | Image |
| 120 | `/images/09/Nancy-Clayton-Whitfield.jpg` | `/images/Nancy-Clayton-Whitfield.jpg` | Image |
| 123 | `/images/09/thomasandlucysgrandchildren.pdf` | `/documents/thomasandlucysgrandchildren.pdf` | PDF added |
| 125 | `/images/09/Lucy-B-Berry-headstone.jpg` | `/images/Lucy-B-Berry-headstone.jpg` | Image |

---

### `content/ancestors/william-aaron-turley-ga.md` (1 link fixed)

| Line | Before | After |
|------|--------|-------|
| 24 | `/images/09/Fred-Turley-Martha-Mattie-Starke.jpg` | `/images/Fred-Turley-Martha-Mattie-Starke.jpg` | Image |

---

## Confirmed Valid (Not Broken)

The following links were flagged by the initial automated scan but are valid Hugo content pages — not static files:

| Link | Hugo Page |
|------|-----------|
| `/documents/camp-power-of-attorney/` | `content/documents/camp-power-of-attorney.md` ✓ |
| `/documents/land-grant-robert-berry-jr/` | `content/documents/land-grant-robert-berry-jr.md` ✓ |

---

## Root Cause

The WordPress source site organized uploads into year/month subdirectories (`/wp-content/uploads/2012/09/`) and census images into a separate `/census/` path. During migration, census images were correctly placed in `static/census/` but some content links were not updated to match. Additionally, the WordPress theme used numbered subdirectories (`/images/09/`) as a lightbox convention — these subdirectories were never part of the Hugo static layout.

---

*Audit and fixes recorded by Pam — 2026-03-29*
