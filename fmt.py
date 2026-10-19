#!/usr/bin/env python3
"""Re-align Markdown table columns in src/.

Only two-column tables, i.e. bidding tables, are touched.  Wider tables keep
their hand alignment.

Column width is the widest body cell.  Header cells are exempt and overhang,
keeping the first column narrow under long auction headers.  A last column
that no body row supplies (body rows ending without a pipe) gets a fixed
`---`, having nothing to align to, or `-` under an empty header cell.  Alignment colons in the separator are
preserved and applied to the body.

Whitespace only, and idempotent.  Run it by hand after editing tables.
"""
import glob, sys

def cells(line):
    """(cells, closed) -- closed means the row ends with a pipe."""
    p = line.split('|')
    return (p[1:-1], True) if line.endswith('|') else (p[1:], False)

def align(raw):
    t = raw.strip()
    return t.startswith(':'), t.endswith(':')

def sep_cell(raw, w):
    l, r = align(raw)
    w = max(w, 3 if (l or r) else 1)
    return (':' if l else '') + '-' * (w - l - r) + (':' if r else '')

def pad(s, w, raw):
    l, r = align(raw)
    return s.center(w) if l and r else s.rjust(w) if r else s.ljust(w)

def fmt(path):
    lines = open(path).read().split('\n')
    out, i, fence = [], 0, False
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            fence = not fence
        if fence or not l.startswith('|-') or not out:
            out.append(l); i += 1; continue

        sep, _ = cells(l)
        n = len(sep)
        if n != 2:
            out.append(l); i += 1; continue
        body = []
        j = i + 1
        while j < len(lines) and lines[j].startswith('|') and not lines[j].startswith('|-'):
            body.append(cells(lines[j])); j += 1

        # width = widest plain body cell; headers are exempt
        w = [0] * n
        for k in range(n):
            for c, closed in body:
                if k < len(c) - (0 if closed else 1) and '<br>' not in c[k]:
                    w[k] = max(w[k], len(c[k].strip()) + 2)
        # a last column no body row supplies has nothing to align to;
        # an empty header cell above it collapses to a single dash
        if not any(closed for _, closed in body) and body:
            hdr, _ = cells(out[-1])
            w[n - 1] = 1 if n - 1 < len(hdr) and not hdr[n - 1].strip() else 3

        out.append('|' + '|'.join(sep_cell(sep[k], w[k]) for k in range(n)) + '|')
        for c, closed in body:
            end = len(c) if closed else len(c) - 1
            r = ['' if k >= len(c) else
                 c[k] if '<br>' in c[k] or k >= end else
                 ' ' + pad(c[k].strip(), w[k] - 1, sep[k]) for k in range(max(n, len(c)))]
            if not closed:
                r[end] = ' ' + c[end].strip()
            out.append('|' + '|'.join(r) + ('|' if closed else ''))
        i = j
    return '\n'.join(out)

for f in sorted(glob.glob('src/**/*.md', recursive=True)):
    new = fmt(f)
    if new != open(f).read():
        open(f, 'w').write(new)
        print('fmt', f)
