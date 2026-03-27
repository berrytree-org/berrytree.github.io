# Broken Links Inventory — Berrytree.org

*Compiled by Martha Chen (Staff Genealogist) and Pam (Project Admin) — 2026-03-27*
*Status: **Document only — fixes deferred per Richard's direction.***

---

## Summary

| Category | Count | Description |
|---|---|---|
| WordPress `?page_id=N` | 50 | WordPress internal page ID links — all broken, no equivalent Hugo URL |
| Slug-style internal | 259 | WordPress slug-style links (e.g. `http://maryberry/`) — need mapping to Hugo paths |
| External `http://` | 28 | External sites using http:// — may work but should be upgraded to https:// |
| **Total** | **337** | |

**Martha's note:** The slug-style links are the most significant issue for usability — they make up the bulk of the index pages (alphabetical, name index, family tree index). Many of these pages likely exist in Hugo form; we just need a URL mapping table. The `?page_id` links are definitively dead and need to be replaced with correct Hugo paths or removed.

---

## Category 1 — WordPress Page ID Links (50 occurrences)

These are WordPress-generated internal links of the form `http://?page_id=N`. They will never resolve in the Hugo site. Each needs to be replaced with the correct Hugo path once we build the URL mapping.

| File | Broken Link |
|---|---|
| `ancestors/ira-berry-nc.md` | `http://?page_id=51` |
| `ancestors/john-berry-tx.md` | `http://?page_id=149` |
| `ancestors/john-berry-tx.md` | `http://?page_id=8` |
| `ancestors/joshua-berry-ohio.md` | `http://?page_id=97` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=107` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=124` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=135` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=155` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=183` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=41` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=63` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=72` |
| `ancestors/robert-berry-oc.md` | `http://?page_id=87` |
| `ancestors/robert-berry-pac.md` | `http://?page_id=126` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=107` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=108` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=109` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=135` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=137` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=140` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=148` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=155` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=161` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=183` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=21` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=29` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=31` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=39` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=41` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=43` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=58` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=63` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=72` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=74` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=81` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=87` (×2) |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=89` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=90` |
| `ancestors/robert-elizabeth-berrys-children.md` | `http://?page_id=96` |
| `ancestors/sarah-cate.md` | `http://?page_id=39` |
| `ancestors/william-clarence-berry-nc.md` | `http://?page_id=131` |
| `ancestors/william-clarence-berry-nc.md` | `http://?page_id=59` |
| `dna/dna-page-two.md` | `http://?page_id=37` |

---

## Category 2 — Slug-Style Internal Links (259 occurrences)

These are WordPress-style relative URLs (e.g. `http://maryberry/`) that were site-relative links in WordPress but are meaningless in Hugo. They need to be mapped to current Hugo content paths.

**Most-needed URL mappings** (appear most frequently):

| WordPress Slug | Likely Hugo Path | Occurrences |
|---|---|---|
| `http://maryberry/` | `/ancestors/mary-berry/` (needs page) | 13 |
| `http://joshuaberry/` | `/ancestors/joshua-berry-ohio/` | 15 |
| `http://catherineberrync/` | `/ancestors/catherine-berry-nc/` (needs page) | 16+ |
| `http://enoch-m-berry-page/` | needs page | 9 |
| `http://david-j-berry-sr/` | `/ancestors/david-j-berry-sr/` | several |
| `http://johnberrytx/` | `/ancestors/john-berry-tx/` | 12 |
| `http://thomaspersonberry/` | needs page | 4 |
| `http://robertberrypac/` | `/ancestors/robert-berry-pac/` | several |

### Full slug-style link inventory by file:

**`ancestors/aldridge-berry-farquhar-connection.md`**
- `http://georgerufusberrync/`
- `http://martha-m-lockley/`
- `http://mary-jane-berry-daughter-of-wc-massa-tompkins-berry/`
- `http://maryberry/`
- `http://roannfrances/`
- `http://williamclarenceberrync/`

**`ancestors/david-j-berry-sr.md`**
- `http://davidsodavid/`
- `http://elizabetheathersberrync/`
- `http://henrysodavid/`
- `http://joshuaberryga/`
- `http://maryberrybartonga/`
- `http://robertdjberry/`
- `http://sarahberrycatesga/`
- `http://thomassodavid/`
- `http://williamgsodavid/`
- `http://winiifredncga/`

**`ancestors/ira-berry-nc.md`**
- `http://ira-berry-census-page/`

**`ancestors/john-berry.md`**
- `http://robertberrypac/`

**`ancestors/joshua-berry-ohio.md`**
- `http://joshua-jr-census/`

**`ancestors/robert-berry-jr.md`**
- `http://catherineberrync/`
- `http://davidmiddletonberryala/`
- `http://deed-book-page-331/`
- `http://deed-book-page-421/`
- `http://georgeberrytx/`
- `http://land-grant-to-robert-berry-jr/` (×2)
- `http://robert-berry-jr-census-page/`
- `http://thompsonberryala/`

**`ancestors/robert-berry-oc.md`**
- `http://1790censusindex/`
- `http://1800-orange-county-nc-census/`
- `http://1810-hannah-cate-census/`
- `http://annfosterpac/`
- `http://david-j-berry-sr/`
- `http://fiddletoncemetery/`
- `http://marykempepac/`
- `http://rb2sourcelist/`
- `http://richardwilliamsonpac/`
- `http://robert-berry-oc-will/`
- `http://robert-berrys-oc-pay-vouchers/`
- `http://rogerwilliamsonpac/`

**`ancestors/robert-berry-pac.md`**
- `http://richardwilliamsonpac/`
- `http://robertberrypac/`
- `http://rogerwilliamsonpac/`
- `http://samuel-hollowell/`

**`ancestors/robert-elizabeth-berrys-children.md`**
- `http://david-j-berry-sr/` (×2)
- `http://henryberry/`
- `http://isaacberry/`
- `http://robert-berry-joshuas-son-nc/`
- `http://robertberrypac/`

**`ancestors/shelby-dale-berry.md`**
- `http://ken-berry/`

**`ancestors/william-clarence-berry-nc.md`**
- `http://martha-m-lockley/`
- `http://mary-jane-berry-daughter-of-wc-massa-tompkins-berry/`

**`dna/dna-page-three.md`**
- `http://dnapage/`
- `http://ydna-matching-william-berry-ydna/`

**`dna/overview.md`**
- `http://dnapage/`
- `http://dnapagetwo/`

**`family-lines/_index.md`**
- `http://djbtree/`
- `http://elizabeth/`
- `http://isaac-berry-family-tree/`
- `http://joshberrytree/`
- `http://mary-berry-family-line/` (×2)
- `http://robert-berry-family-line/`
- `http://tberrytree/`

**`indexes/alphabetical.md`** (high volume — 60+ links, sample):
- `http://1810-hannah-cate-census/`
- `http://adaleeberrync/`
- `http://addie-lena-berry/`
- `http://albertedgar/`
- `http://by-family-line/`
- `http://catherineberrync/`
- `http://census-page-for-thomas-p-berry/`
- `http://cora-berry-mcvicker/`
- `http://david-crockett-berry-5/`
- `http://david-j-berry-sr/`
- `http://davidleeberryohio/`
- `http://djbtree/`
- `http://doraellenturleyga/`
- `http://eli-berry-nc/`
- `http://elizabeth/`
- `http://emmanuel-patten-berry/`
- `http://enoch-m-berry-page/`
- `http://georgerufusberrync/`
- `http://hannahcateberry/`
- `http://horacepratherberryga/`
- `http://ira-berry-census-page/`
- `http://iraberrync/`
- `http://jamesberrytenn/`
- `http://jesseleeberry/`
- `http://john-h-berry-ala-tx/`
- `http://joshua-berry-census-page/`
- `http://joshua-berry-oc-document-page/`
- `http://joshua-jr-census/`
- `http://joshuaberry/`
- `http://maryberry/`
- `http://maryelizabethsdaughternc/`
- `http://mattielstricklandala/`
- `http://nancy-berry-spinster-joshuas-daughter/` (×2)
- `http://orange-county-nc-marriage-bonds-a-c/`
- `http://picturedirectoryt/`
- `http://rb2sourcelist/`
- `http://robert-berry-jr-census-page/`
- `http://robert-berry-oc-will/`
- `http://robertberrypac/`
- `http://robertdjberry/`
- `http://robertpicklenc/`
- `http://sallymalenaberrync/` (×2)
- `http://sarah-frances-berry-kelly-ga/`
- `http://tberrytree/`
- `http://tennesseepicturealbum/`
- `http://thomaspersonberry/` (×2)
- `http://walterglenberryga/`
- `http://whowellberryjrtx/`
- `http://whowellberrytx/`
- `http://wileyharoldberrync/`
- `http://wileypberryjrnc/`
- `http://william-cates-estate-sale/`
- `http://william-edgar-berry-alabama/`
- `http://william-henry-berry-ga/`
- `http://william-oscar-berry-ga/` (×2)
- `http://william-thomas-maners/`
- `http://williamaaronturleyga/`
- `http://williamclarenceberrync/`
- `http://williameugeneberrync/`
- `http://williamgsodavid/`
- `http://williamhberrync/`
- `http://williamlamar/`
- `http://williamson-deeds-and-wills-1691-to-1755-pac/`
- `http://williamtberryjrala/`
- `http://williamtberrysrala/`
- `http://willieadolphysberrync/`
- `http://winiifredncga/`
- `http://woodrowwilsonberrync/`

**`indexes/family-tree.md`**
- `http://djbtree/`
- `http://henry-berry-tree/`
- `http://isaac-berry-family-tree/`
- `http://john-berry-family-tree/`
- `http://joshberrytree/`
- `http://mary-berry-family-line/`
- `http://robert-berry-juniors-family-tree/`
- `http://tberrytree/`
- `http://wbfamilytree/`

**`indexes/name-index.md`** (high volume — 100+ links):
- `http://catherineberrync/` (×16)
- `http://david-j-berry-sr/` (×3)
- `http://davidmiddletonberryala/` (×2)
- `http://davidsonoftom/`
- `http://eleanorreed/` (×2)
- `http://elizaberryfranklin/` (×2)
- `http://elizabeth/`
- `http://enoch-m-berry-page/` (×9)
- `http://georgeberrytx/` (×4)
- `http://henryberry/`
- `http://henrybradfordberryala/` (×2)
- `http://isaacberry/` (×2)
- `http://jamesberrytenn/`
- `http://johnberrytx/` (×12)
- `http://joshuaberry/` (×15)
- `http://ken-berry/`
- `http://maryberry/` (×12)
- `http://nancy-berry-spinster-joshuas-daughter/`
- `http://robertberrypac/`
- `http://robertcberryalabama/` (×2)
- `http://robertdjberry/`
- `http://robertpicklenc/` (×2)
- `http://sallymalenaberrync/`
- `http://sarahberrycatesga/`
- `http://thomasberrync/`
- `http://thomaspersonberry/` (×4)
- `http://thompsonberryala/` (×2)
- `http://william-berry/` (×2)
- `http://williamclarenceberrync/` (×3)
- `http://winiifredncga/`

**`pictures/_index.md`**
- `http://picturedirectoryt/`

**`timelines/1700s.md`**
- `http://1700-1799-timeline/` (×4)

---

## Category 3 — External http:// Links (28 occurrences)

These are links to external sites still using `http://`. They may work but should be upgraded to `https://` when possible. FindAGrave links in particular are likely still valid — just the scheme needs updating.

| File | Link |
|---|---|
| `ancestors/aldridge-berry-farquhar-connection.md` | `http://www.tomcamp.org/` |
| `ancestors/john-berry-tx.md` | `http://johnberrytx/francis-marion-berry/` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=26117641` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=28339491` (×4) |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=42194340` (×3) |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=42227040` (×3) |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=42227343` (×2) |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=47103218` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=48920424` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=48920526` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=49919695` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=49919734` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=49919744` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=52801146` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=62957167` |
| `ancestors/john-berry.md` | `http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=74168917` |
| `indexes/extended-site-map.md` | `http://cemeterycensus.com/nc/orng/cem233.htm` |
| `resources/_index.md` | `http://vagenweb.org/princess_anne/` |
| `resources/_index.md` | `http://www.ncgenweb.us/` |

---

## Recommended Fix Strategy (for future session)

1. **Phase 1 — URL mapping table:** Build a `Projects/notes/url-mapping.md` that maps each WordPress slug/page_id to its Hugo equivalent path. Many of these pages already exist in Hugo; they just need to be identified.

2. **Phase 2 — Automated replacement:** Once the mapping table is complete, a short Python script can do a find-and-replace pass across all content files.

3. **Phase 3 — Missing pages:** Some slugs (e.g. `http://maryberry/`, `http://isaacberry/`) point to pages that have not yet been migrated. These need content migration before links can be fixed.

4. **Phase 4 — External https upgrade:** A simple `sed` or Python pass to update `findagrave.com` and other external links to `https://`.

*Martha's note: The index pages (alphabetical, name-index) are the most link-dense and will have the highest user impact when fixed. I recommend prioritizing those after the ancestor pages are confirmed complete.*

---

*Document created: 2026-03-27 | Next review: when Richard gives the go-ahead to fix links*
