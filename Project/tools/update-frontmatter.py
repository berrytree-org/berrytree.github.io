#!/usr/bin/env python3
"""
update-frontmatter.py — Generic front matter updater for Hugo content pages

Supports both YAML (---) and TOML (+++) front matter formats.
Auto-detects format per file, or use --format to force one.
Dry-run by default. Pass --write to apply changes.

Operations:
  add       Add a field (skips pages that already have it)
  remove    Remove a field
  rename    Rename a field (preserves value)
  update    Update an existing field's value (skips pages that don't have it)

Filters (combine any):
  --section       Filter by content section (e.g., ancestors, books)
  --has-field     Only pages that have this field
  --missing-field Only pages missing this field
  --source        Filter by content_source value (e.g., wp-export)
  --file          Filter by filename glob pattern (e.g., "*berry*")

Usage:
  # Preview adding qc_owner to all ancestor pages (YAML site)
  python3 update-frontmatter.py add qc_owner --section ancestors

  # Remove a field from a TOML-based site
  python3 update-frontmatter.py remove draft --format toml --write

  # Rename a field (auto-detects format per file)
  python3 update-frontmatter.py rename sources_verified qc_genealogy --write

  # Update a field value on pages that have it
  python3 update-frontmatter.py update last_updated 2026-04-08 --section books --write

  # Add a field only to pages missing it
  python3 update-frontmatter.py add qc_webteam --missing-field qc_webteam --write

  # Point at a different content directory
  python3 update-frontmatter.py add draft true --content-dir /path/to/site/content --write

Owner: Lila (Chief Web Designer & Architect)
Assistant: Terry (Associate Web Developer)
"""

import os
import re
import sys
import argparse
import fnmatch

# Default content dir (relative to this script's location in a Hugo project)
DEFAULT_CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'content')

# Front matter delimiter patterns
YAML_PATTERN = re.compile(r'^(---\n)(.*?)\n(---)', re.DOTALL)
TOML_PATTERN = re.compile(r'^(\+\+\+\n)(.*?)\n(\+\+\+)', re.DOTALL)


# ---------------------------------------------------------------------------
#  Format detection and extraction
# ---------------------------------------------------------------------------

def detect_format(content):
    """Detect front matter format. Returns 'yaml', 'toml', or None."""
    if content.startswith('---\n'):
        return 'yaml'
    if content.startswith('+++\n'):
        return 'toml'
    return None


def extract_fm_text(content, fmt):
    """Extract front matter lines and body. Returns (fm_lines, after, fmt) or None."""
    pattern = YAML_PATTERN if fmt == 'yaml' else TOML_PATTERN
    match = pattern.match(content)
    if not match:
        return None
    fm_text = match.group(2)
    fm_lines = fm_text.split('\n')
    after = content[match.end():]
    return fm_lines, after


def rebuild_content(fm_lines, after, fmt):
    """Rebuild file content from front matter lines and body."""
    delimiter = '---' if fmt == 'yaml' else '+++'
    fm_text = '\n'.join(fm_lines)
    return f"{delimiter}\n{fm_text}\n{delimiter}{after}"


# ---------------------------------------------------------------------------
#  Field patterns — YAML uses "key: value", TOML uses "key = value"
# ---------------------------------------------------------------------------

def field_pattern(field_name, fmt):
    """Return a compiled regex to match a field line."""
    if fmt == 'yaml':
        return re.compile(r'^' + re.escape(field_name) + r'\s*:')
    else:
        return re.compile(r'^' + re.escape(field_name) + r'\s*=')


def field_value_pattern(field_name, fmt):
    """Return a compiled regex to match a field line and capture its value."""
    if fmt == 'yaml':
        return re.compile(r'^' + re.escape(field_name) + r'\s*:\s*(.*)')
    else:
        return re.compile(r'^' + re.escape(field_name) + r'\s*=\s*(.*)')


def field_split_pattern(field_name, fmt):
    """Return a compiled regex that captures the separator and value."""
    if fmt == 'yaml':
        return re.compile(r'^' + re.escape(field_name) + r'(\s*:\s*)(.*)')
    else:
        return re.compile(r'^' + re.escape(field_name) + r'(\s*=\s*)(.*)')


def list_continuation_pattern(fmt):
    """Pattern for YAML list continuation lines (indented - items). TOML doesn't have these."""
    if fmt == 'yaml':
        return re.compile(r'^\s+-\s')
    return None


# ---------------------------------------------------------------------------
#  Field operations (format-aware)
# ---------------------------------------------------------------------------

def field_exists(fm_lines, field_name, fmt):
    """Check if a field exists in front matter lines."""
    pat = field_pattern(field_name, fmt)
    return any(pat.match(line) for line in fm_lines)


def get_field_value(fm_lines, field_name, fmt):
    """Get the raw value string of a field."""
    pat = field_value_pattern(field_name, fmt)
    for line in fm_lines:
        m = pat.match(line)
        if m:
            return m.group(1).strip()
    return None


def find_field_index(fm_lines, field_name, fmt):
    """Find the line index of a field."""
    pat = field_pattern(field_name, fmt)
    for i, line in enumerate(fm_lines):
        if pat.match(line):
            return i
    return -1


def format_value(value, fmt):
    """Format a value for the target front matter format."""
    if value is None:
        return ''
    # Booleans
    if value.lower() in ('true', 'false'):
        return value.lower()
    # Dates (YYYY-MM-DD)
    if re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        if fmt == 'toml':
            return value  # TOML dates are bare
        return value  # YAML dates are also bare
    # Numbers
    try:
        int(value)
        return value
    except (ValueError, TypeError):
        pass
    try:
        float(value)
        return value
    except (ValueError, TypeError):
        pass
    # Lists (already formatted)
    if value.startswith('['):
        return value
    # Strings
    if fmt == 'toml':
        # TOML always uses double quotes for strings
        return f'"{value}"'
    else:
        # YAML — quote if needed
        if '"' not in value:
            return f'"{value}"'
        if "'" not in value:
            return f"'{value}'"
        return f'"{value}"'


def format_field_line(field, value, fmt):
    """Format a complete field line."""
    sep = ': ' if fmt == 'yaml' else ' = '
    formatted = format_value(value, fmt) if value else ''
    if formatted:
        return f"{field}{sep}{formatted}"
    else:
        if fmt == 'yaml':
            return f"{field}:"
        else:
            return f'{field} = ""'


def apply_add(fm_lines, field, value, fmt, after_field=None, before_field=None):
    """Add a field to front matter. Returns modified lines or None if skipped."""
    if field_exists(fm_lines, field, fmt):
        return None

    new_line = format_field_line(field, value, fmt)
    cont_pat = list_continuation_pattern(fmt)

    if after_field:
        idx = find_field_index(fm_lines, after_field, fmt)
        if idx >= 0:
            insert_at = idx + 1
            if cont_pat:
                while insert_at < len(fm_lines) and cont_pat.match(fm_lines[insert_at]):
                    insert_at += 1
            fm_lines.insert(insert_at, new_line)
            return fm_lines
    if before_field:
        idx = find_field_index(fm_lines, before_field, fmt)
        if idx >= 0:
            fm_lines.insert(idx, new_line)
            return fm_lines

    fm_lines.append(new_line)
    return fm_lines


def apply_remove(fm_lines, field, fmt):
    """Remove a field from front matter. Returns modified lines or None if not found."""
    idx = find_field_index(fm_lines, field, fmt)
    if idx < 0:
        return None

    fm_lines.pop(idx)
    cont_pat = list_continuation_pattern(fmt)
    if cont_pat:
        while idx < len(fm_lines) and cont_pat.match(fm_lines[idx]):
            fm_lines.pop(idx)

    return fm_lines


def apply_rename(fm_lines, old_field, new_field, fmt):
    """Rename a field. Returns modified lines or None if not found."""
    if not field_exists(fm_lines, old_field, fmt):
        return None
    if field_exists(fm_lines, new_field, fmt):
        return None

    pat = field_split_pattern(old_field, fmt)
    for i, line in enumerate(fm_lines):
        m = pat.match(line)
        if m:
            fm_lines[i] = f"{new_field}{m.group(1)}{m.group(2)}"
            return fm_lines
    return None


def apply_update(fm_lines, field, value, fmt):
    """Update a field's value. Returns modified lines or None if field not found."""
    idx = find_field_index(fm_lines, field, fmt)
    if idx < 0:
        return None

    formatted = format_value(value, fmt)
    pat = field_split_pattern(field, fmt)
    m = pat.match(fm_lines[idx])
    sep = ': ' if fmt == 'yaml' else ' = '
    if m:
        # Normalize separator to ensure valid YAML/TOML spacing
        raw_sep = m.group(1)
        if fmt == 'yaml' and ':' in raw_sep and not raw_sep.endswith(' '):
            raw_sep = ': '
        fm_lines[idx] = f"{field}{raw_sep}{formatted}"
    else:
        fm_lines[idx] = f"{field}{sep}{formatted}"
    return fm_lines


# ---------------------------------------------------------------------------
#  Filters
# ---------------------------------------------------------------------------

def get_section(rel_path):
    """Extract the top-level section from the relative path."""
    parts = rel_path.split(os.sep)
    return parts[0] if len(parts) > 1 else '(root)'


def strip_quotes(val):
    """Remove surrounding quotes from a value string."""
    if val and len(val) >= 2 and val[0] in ('"', "'") and val[-1] == val[0]:
        return val[1:-1]
    return val


def matches_filters(rel_path, fm_lines, fmt, args):
    """Check if a file matches all specified filters."""
    if args.section:
        if get_section(rel_path) != args.section:
            return False
    if args.has_field:
        if not field_exists(fm_lines, args.has_field, fmt):
            return False
    if args.missing_field:
        if field_exists(fm_lines, args.missing_field, fmt):
            return False
    if args.source:
        source_val = get_field_value(fm_lines, 'content_source', fmt)
        if source_val:
            source_val = strip_quotes(source_val)
        if source_val != args.source:
            return False
    if args.file_pattern:
        filename = os.path.basename(rel_path)
        if not fnmatch.fnmatch(filename, args.file_pattern):
            return False
    return True


# ---------------------------------------------------------------------------
#  CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description='Generic front matter updater for Hugo content pages (YAML & TOML)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Formats:
  Auto-detects per file (--- = YAML, +++ = TOML).
  Use --format yaml or --format toml to force one format.

Operations:
  add FIELD [VALUE]           Add a field (skips if already present)
  remove FIELD                Remove a field
  rename OLD_FIELD NEW_FIELD  Rename a field, preserve value
  update FIELD VALUE          Update value (skips if field missing)

Examples:
  %(prog)s add qc_owner --section ancestors
  %(prog)s remove draft --format toml --write
  %(prog)s rename sources_verified old_sources_verified --write
  %(prog)s update last_updated 2026-04-08 --section books --write
  %(prog)s add weight 10 --content-dir /other/site/content --write
"""
    )

    parser.add_argument('operation', choices=['add', 'remove', 'rename', 'update'],
                        help='Operation to perform')
    parser.add_argument('field', help='Field name to operate on')
    parser.add_argument('value', nargs='?', default=None,
                        help='Value for add/update, or new field name for rename')

    # Format
    parser.add_argument('--format', choices=['yaml', 'toml'], default=None,
                        dest='fm_format',
                        help='Force front matter format (default: auto-detect per file)')

    # Content directory
    parser.add_argument('--content-dir', type=str, default=None,
                        help='Path to content directory (default: ../../content relative to script)')

    # Filters
    parser.add_argument('--section', type=str, help='Filter by content section')
    parser.add_argument('--has-field', type=str, help='Only pages that have this field')
    parser.add_argument('--missing-field', type=str, help='Only pages missing this field')
    parser.add_argument('--source', type=str, help='Filter by content_source value')
    parser.add_argument('--file', type=str, dest='file_pattern', help='Filter by filename glob')

    # Behavior
    parser.add_argument('--write', action='store_true',
                        help='Apply changes (default is dry-run)')
    parser.add_argument('--after', type=str, default=None,
                        help='Insert new field after this existing field (for add operation)')
    parser.add_argument('--before', type=str, default=None,
                        help='Insert new field before this existing field (for add operation)')

    args = parser.parse_args()

    if args.operation == 'rename' and not args.value:
        parser.error('rename requires a new field name: rename OLD_FIELD NEW_FIELD')
    if args.operation == 'update' and args.value is None:
        parser.error('update requires a value: update FIELD VALUE')

    return args


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    content_dir = os.path.abspath(args.content_dir or DEFAULT_CONTENT_DIR)

    if not os.path.isdir(content_dir):
        print(f"  ERROR: Content directory not found: {content_dir}")
        sys.exit(1)

    mode = "DRY RUN" if not args.write else "WRITING"
    fmt_label = args.fm_format or "auto-detect"
    print(f"\n  update-frontmatter.py — {mode}  (format: {fmt_label})")
    print(f"  Content dir: {content_dir}")
    print(f"  Operation: {args.operation} {args.field}" +
          (f" {args.value}" if args.value else ""))

    filters = []
    if args.section:
        filters.append(f"section={args.section}")
    if args.has_field:
        filters.append(f"has={args.has_field}")
    if args.missing_field:
        filters.append(f"missing={args.missing_field}")
    if args.source:
        filters.append(f"source={args.source}")
    if args.file_pattern:
        filters.append(f"file={args.file_pattern}")
    if filters:
        print(f"  Filters: {', '.join(filters)}")
    print()

    modified = 0
    skipped = 0
    errors = 0
    yaml_count = 0
    toml_count = 0

    for root, dirs, files in sorted(os.walk(content_dir)):
        for f in sorted(files):
            if not f.endswith('.md'):
                continue

            file_path = os.path.join(root, f)
            rel_path = os.path.relpath(file_path, content_dir)

            with open(file_path, 'r', encoding='utf-8') as fh:
                content = fh.read()

            # Determine format
            if args.fm_format:
                fmt = args.fm_format
            else:
                fmt = detect_format(content)
                if not fmt:
                    continue  # No front matter detected

            result = extract_fm_text(content, fmt)
            if not result:
                continue

            fm_lines, after = result

            if fmt == 'yaml':
                yaml_count += 1
            else:
                toml_count += 1

            # Check filters
            if not matches_filters(rel_path, fm_lines, fmt, args):
                continue

            # Apply operation on a copy
            fm_copy = fm_lines[:]

            if args.operation == 'add':
                new_lines = apply_add(fm_copy, args.field, args.value, fmt,
                                      after_field=args.after, before_field=args.before)
            elif args.operation == 'remove':
                new_lines = apply_remove(fm_copy, args.field, fmt)
            elif args.operation == 'rename':
                new_lines = apply_rename(fm_copy, args.field, args.value, fmt)
            elif args.operation == 'update':
                new_lines = apply_update(fm_copy, args.field, args.value, fmt)

            if new_lines is None:
                skipped += 1
                continue

            new_content = rebuild_content(new_lines, after, fmt)

            if new_content == content:
                skipped += 1
                continue

            modified += 1
            fmt_tag = f" [{fmt}]" if not args.fm_format else ""
            print(f"  {'WRITE' if args.write else 'WOULD'}: {rel_path}{fmt_tag}")

            if args.write:
                try:
                    with open(file_path, 'w', encoding='utf-8') as fh:
                        fh.write(new_content)
                except Exception as e:
                    print(f"  ERROR writing {rel_path}: {e}")
                    errors += 1

    # Summary
    print(f"\n  {'=' * 50}")
    print(f"  {mode} complete.")
    print(f"  Modified: {modified}  |  Skipped: {skipped}  |  Errors: {errors}")
    if yaml_count or toml_count:
        print(f"  Files scanned: {yaml_count} YAML, {toml_count} TOML")
    if not args.write and modified > 0:
        print(f"\n  Re-run with --write to apply these changes.")
    print(f"  {'=' * 50}\n")


if __name__ == '__main__':
    main()
