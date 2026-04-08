#!/usr/bin/env python3
"""
qc-report.py — Generate a QC status report from front matter fields

Three independent QC lanes, each tracked by a date field:
  - qc_owner:     Aaron's review sign-off
  - qc_webteam:   Structural/visual QC (Terry/Malcolm)
  - qc_genealogy: Source verification (Martha)

A blank date means not yet cleared. A date means cleared as of that date.
A QC date older than last_updated means the reviewer needs another pass (stale).

Usage:
  python3 Project/tools/qc-report.py              # Summary report
  python3 Project/tools/qc-report.py --detail      # Include per-page detail
  python3 Project/tools/qc-report.py --section ancestors  # Filter by section
  python3 Project/tools/qc-report.py --flagged     # Show only pages with issues
  python3 Project/tools/qc-report.py --stale       # Show only stale reviews

Owner: Terry (Associate Web Developer)
"""

import os
import re
import sys
import argparse
from collections import defaultdict

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'content')

# Front matter extraction patterns
FM_PATTERN = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
FIELD_PATTERNS = {
    'qc_owner': re.compile(r'^qc_owner:\s*["\']?([\d-]+)["\']?', re.MULTILINE),
    'qc_webteam': re.compile(r'^qc_webteam:\s*["\']?([\d-]+)["\']?', re.MULTILINE),
    'qc_genealogy': re.compile(r'^qc_genealogy:\s*["\']?([\d-]+)["\']?', re.MULTILINE),
    'last_updated': re.compile(r'^last_updated:\s*["\']?([\d-]+)["\']?', re.MULTILINE),
    'content_source': re.compile(r'^content_source:\s*["\']?([\w-]+)["\']?', re.MULTILINE),
}

# Structural QC patterns (applied to body content, not front matter)
STRUCTURAL_CHECKS = {
    'raw_html_divs': re.compile(r'<div[\s>]', re.IGNORECASE),
    'raw_html_spans': re.compile(r'<span[\s>]', re.IGNORECASE),
    'raw_html_strong': re.compile(r'<strong[\s>]', re.IGNORECASE),
    'raw_html_em': re.compile(r'<em[\s>]', re.IGNORECASE),
    'script_tags': re.compile(r'<script[\s>]', re.IGNORECASE),
    'nbsp': re.compile(r'&nbsp;'),
    'bare_h2': re.compile(r'^## (?!\*\*)(?!<)(.+)$', re.MULTILINE),
    'bare_h3': re.compile(r'^### (?!\*\*)(?!<)(.+)$', re.MULTILINE),
    'missing_alt': re.compile(r'<img[^>]+alt\s*=\s*["\']["\']', re.IGNORECASE),
    'inline_style': re.compile(r'<(?:img|div|span|p)[^>]+style\s*=', re.IGNORECASE),
}

QC_LANES = [
    ('qc_owner', 'Owner (Aaron)'),
    ('qc_webteam', 'Web Team (Terry/Malcolm)'),
    ('qc_genealogy', 'Genealogy (Martha)'),
]


def get_section(rel_path):
    """Extract the top-level section from the relative path."""
    parts = rel_path.split(os.sep)
    return parts[0] if len(parts) > 1 else '(root)'


def extract_front_matter(content):
    """Extract front matter fields into a dict."""
    fm_match = FM_PATTERN.match(content)
    if not fm_match:
        return {}
    fm_text = fm_match.group(1)
    fields = {}
    for name, pattern in FIELD_PATTERNS.items():
        match = pattern.search(fm_text)
        fields[name] = match.group(1) if match else None
    return fields


def get_body(content):
    """Return content after front matter."""
    fm_match = FM_PATTERN.match(content)
    if fm_match:
        return content[fm_match.end():]
    return content


def run_structural_checks(body):
    """Run structural QC checks on the body content. Returns list of issue names."""
    issues = []
    for name, pattern in STRUCTURAL_CHECKS.items():
        if pattern.search(body):
            issues.append(name)
    return issues


def is_stale(qc_date, last_updated):
    """Check if a QC date is stale (older than last_updated)."""
    if not qc_date or not last_updated:
        return False
    return qc_date < last_updated


def scan_pages(content_dir, section_filter=None):
    """Scan all .md files and return page data."""
    pages = []
    content_dir = os.path.abspath(content_dir)

    for root, dirs, files in os.walk(content_dir):
        for f in files:
            if not f.endswith('.md'):
                continue

            file_path = os.path.join(root, f)
            rel_path = os.path.relpath(file_path, content_dir)
            section = get_section(rel_path)

            if section_filter and section != section_filter:
                continue

            with open(file_path, 'r', encoding='utf-8') as fh:
                content = fh.read()

            fields = extract_front_matter(content)
            body = get_body(content)
            structural_issues = run_structural_checks(body)

            # Compute stale flags
            last_updated = fields.get('last_updated')
            stale = {}
            for field_key, _ in QC_LANES:
                qc_val = fields.get(field_key)
                stale[field_key] = is_stale(qc_val, last_updated)

            pages.append({
                'file': rel_path,
                'section': section,
                'fields': fields,
                'structural_issues': structural_issues,
                'stale': stale,
            })

    pages.sort(key=lambda p: p['file'])
    return pages


def print_header(title):
    """Print a section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")


def print_summary(pages):
    """Print the summary report."""
    total = len(pages)

    print_header("QC STATUS REPORT")
    print(f"\n  Total pages scanned: {total}")

    # --- Three QC Lanes ---
    print_header("QC REVIEW LANES")
    print(f"\n  {'Lane':<30} {'Cleared':>8} {'Blank':>8} {'Stale':>8} {'% Done':>8}")
    print(f"  {'-' * 30} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 8}")

    for field_key, label in QC_LANES:
        cleared = sum(1 for p in pages if p['fields'].get(field_key) and not p['stale'][field_key])
        blank = sum(1 for p in pages if not p['fields'].get(field_key))
        stale = sum(1 for p in pages if p['stale'][field_key])
        pct = (cleared / total * 100) if total else 0
        print(f"  {label:<30} {cleared:>8} {blank:>8} {stale:>8} {pct:>7.1f}%")

    # Fully cleared (all three lanes have non-stale dates)
    fully_cleared = sum(
        1 for p in pages
        if all(
            p['fields'].get(fk) and not p['stale'][fk]
            for fk, _ in QC_LANES
        )
    )
    pct_full = (fully_cleared / total * 100) if total else 0
    print(f"\n  Fully cleared (all 3 lanes):  {fully_cleared} of {total}  ({pct_full:.1f}%)")

    # --- Content Source ---
    print_header("CONTENT SOURCE")
    source_counts = defaultdict(int)
    for p in pages:
        src = p['fields'].get('content_source', '(missing)')
        source_counts[src] += 1
    for src in sorted(source_counts.keys()):
        count = source_counts[src]
        pct = (count / total * 100) if total else 0
        print(f"  {src:<15} {count:>4}  ({pct:5.1f}%)")

    # --- By Section ---
    print_header("BY SECTION")
    section_data = defaultdict(lambda: {
        'total': 0, 'owner': 0, 'webteam': 0, 'genealogy': 0,
        'fully_cleared': 0, 'issues': 0,
    })
    for p in pages:
        sec = p['section']
        section_data[sec]['total'] += 1
        for field_key, short in [('qc_owner', 'owner'), ('qc_webteam', 'webteam'), ('qc_genealogy', 'genealogy')]:
            if p['fields'].get(field_key) and not p['stale'][field_key]:
                section_data[sec][short] += 1
        if all(p['fields'].get(fk) and not p['stale'][fk] for fk, _ in QC_LANES):
            section_data[sec]['fully_cleared'] += 1
        if p['structural_issues']:
            section_data[sec]['issues'] += 1

    print(f"  {'Section':<20} {'Total':>5} {'Owner':>6} {'Web':>5} {'Gen':>5} {'Full':>6} {'Issues':>7}")
    print(f"  {'-' * 20} {'-' * 5} {'-' * 6} {'-' * 5} {'-' * 5} {'-' * 6} {'-' * 7}")
    for sec in sorted(section_data.keys()):
        d = section_data[sec]
        print(f"  {sec:<20} {d['total']:>5} {d['owner']:>6} {d['webteam']:>5} {d['genealogy']:>5} {d['fully_cleared']:>6} {d['issues']:>7}")

    # --- Structural Issues Summary ---
    print_header("STRUCTURAL ISSUES")
    issue_counts = defaultdict(int)
    pages_with_issues = 0
    for p in pages:
        if p['structural_issues']:
            pages_with_issues += 1
            for issue in p['structural_issues']:
                issue_counts[issue] += 1

    if issue_counts:
        print(f"\n  Pages with issues: {pages_with_issues} of {total}")
        print()
        issue_labels = {
            'raw_html_divs': 'Raw <div> tags',
            'raw_html_spans': 'Raw <span> tags',
            'raw_html_strong': 'Raw <strong> tags',
            'raw_html_em': 'Raw <em> tags',
            'script_tags': '<script> tags',
            'nbsp': '&nbsp; entities',
            'bare_h2': 'Bare ## headings (not bold)',
            'bare_h3': 'Bare ### headings (not bold)',
            'missing_alt': 'Empty alt text on images',
            'inline_style': 'Inline style attributes',
        }
        for issue in sorted(issue_counts.keys()):
            label = issue_labels.get(issue, issue)
            print(f"  {label:<35} {issue_counts[issue]:>4} pages")
    else:
        print("\n  No structural issues detected.")


def print_detail(pages):
    """Print per-page detail."""
    print_header("PER-PAGE DETAIL")
    for p in pages:
        fm = p['fields']
        owner = fm.get('qc_owner', '-')
        webteam = fm.get('qc_webteam', '-')
        genealogy = fm.get('qc_genealogy', '-')
        source = fm.get('content_source', '-')
        last = fm.get('last_updated', '-')
        issues = ', '.join(p['structural_issues']) if p['structural_issues'] else 'clean'

        # Mark stale dates
        owner_display = f"{owner} (STALE)" if p['stale']['qc_owner'] else owner
        webteam_display = f"{webteam} (STALE)" if p['stale']['qc_webteam'] else webteam
        genealogy_display = f"{genealogy} (STALE)" if p['stale']['qc_genealogy'] else genealogy

        print(f"\n  {p['file']}")
        print(f"    owner: {owner_display}  |  webteam: {webteam_display}  |  genealogy: {genealogy_display}")
        print(f"    last_updated: {last}  |  source: {source}  |  structural: {issues}")


def print_flagged(pages):
    """Print only pages with structural issues."""
    print_header("PAGES WITH STRUCTURAL ISSUES")
    found = False
    for p in pages:
        if p['structural_issues']:
            found = True
            print(f"\n  {p['file']}")
            print(f"    -> {', '.join(p['structural_issues'])}")

    if not found:
        print("\n  No structural issues found.")


def print_stale(pages):
    """Print pages where a QC date is stale (older than last_updated)."""
    print_header("STALE QC REVIEWS")
    found = False
    for p in pages:
        stale_lanes = []
        for field_key, label in QC_LANES:
            if p['stale'][field_key]:
                stale_lanes.append(f"{label}: {p['fields'][field_key]} < last_updated {p['fields']['last_updated']}")
        if stale_lanes:
            found = True
            print(f"\n  {p['file']}")
            for s in stale_lanes:
                print(f"    -> {s}")

    if not found:
        print("\n  No stale reviews found.")


def main():
    parser = argparse.ArgumentParser(description='Generate QC status report from front matter fields')
    parser.add_argument('--detail', action='store_true', help='Include per-page detail')
    parser.add_argument('--section', type=str, help='Filter by content section (e.g., ancestors, books)')
    parser.add_argument('--flagged', action='store_true', help='Show only pages with structural issues')
    parser.add_argument('--stale', action='store_true', help='Show only pages with stale QC reviews')
    args = parser.parse_args()

    content_dir = os.path.abspath(CONTENT_DIR)
    pages = scan_pages(content_dir, section_filter=args.section)

    if not pages:
        print("No pages found.")
        sys.exit(1)

    print_summary(pages)

    if args.flagged:
        print_flagged(pages)

    if args.stale:
        print_stale(pages)

    if args.detail:
        print_detail(pages)

    # Final line
    print(f"\n{'=' * 70}")
    filter_note = f" (section: {args.section})" if args.section else ""
    print(f"  Report complete. {len(pages)} pages scanned{filter_note}.")
    print(f"{'=' * 70}\n")


if __name__ == '__main__':
    main()
