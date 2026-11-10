"""Build the independent comparison table and the side-by-side table against the team's AI draft.

Reads the "Coding summary" block of every independent_analysis/cases/<case_id>.md and writes:
  independent_analysis/comparison.csv   one row per case (the independent coding)
  independent_analysis/side_by_side.csv  key fields, independent vs draft (analysis/comparison.csv)

Run from the repository root:  python independent_analysis/method/build_tables.py
"""
import csv, glob, os, re

ROOT = 'independent_analysis'
KEYS = ['case_id', 'comedian', 'performance_date', 'controversy_date', 'setting', 'form', 'language', 'clip_status',
        'joke_found_in_transcript', 'topic', 'sacred_object', 'genre', 'target', 'direction', 'collapse_type',
        'gap_months', 'first_spreader', 'objectors', 'objector_distance', 'norm_invoked', 'mobilising_actor',
        'actor_type', 'channel', 'legal_actions', 'extralegal_actions', 'outcome_type', 'highest_stigma_step',
        'courtesy_stigma', 'comedian_response', 'response_changed_course', 'audience_size_tier', 'election_period',
        'key_lenses', 'best_explanation', 'confidence']


def coding(path, section):
    text = open(path, encoding='utf-8').read()
    if section not in text:
        return None
    block = text.split(section, 1)[1]
    block = re.search(r'```\w*\n(.*?)```', block, flags=re.S).group(1)
    row = {}
    for line in block.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            if k.strip() in KEYS:
                row[k.strip()] = v.strip()
    return row


paths = sorted(glob.glob(os.path.join(ROOT, 'cases', '*.md')))
first = [coding(p, '## Coding summary') for p in paths]
final = [coding(p, '## Final coding') for p in paths]
missing = [os.path.basename(p) for p, r in zip(paths, final) if r is None]
if missing:
    print('no Final coding yet, using the first coding for:', ', '.join(missing))
rows = [f or c for f, c in zip(final, first)]

# how often the independent first coding matched the draft, per field (before settling)
draft_all = {r['case_id']: r for r in csv.DictReader(open('analysis/comparison.csv', encoding='utf-8'))}
AGREE = [('outcome_type', 'outcome_type'), ('direction', 'direction'), ('collapse_type', 'collapse_type'),
         ('form', 'form'), ('courtesy_stigma', 'courtesy_stigma'), ('highest_stigma_step', 'highest_stigma_step')]
with open(os.path.join(ROOT, 'agreement.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['field', 'cases', 'independent_equals_draft', 'final_equals_draft', 'final_equals_independent'])
    for ind, dr in AGREE:
        n = a = b = c = 0
        for c0, cf in zip(first, rows):
            d = draft_all.get(c0['case_id'])
            if not d:
                continue
            n += 1
            norm = lambda s: s.split('(')[0].strip().lower()
            a += norm(c0.get(ind, '')) == norm(d.get(dr, ''))
            b += norm(cf.get(ind, '')) == norm(d.get(dr, ''))
            c += norm(cf.get(ind, '')) == norm(c0.get(ind, ''))
        w.writerow([ind, n, a, b, c])

with open(os.path.join(ROOT, 'comparison.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=KEYS)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in KEYS})

# side by side with the draft, for the fields both tables share
draft = {r['case_id']: r for r in csv.DictReader(open('analysis/comparison.csv', encoding='utf-8'))}
PAIRS = [('topic', 'topic'), ('genre', 'genre'), ('direction', 'direction'), ('form', 'form'),
         ('collapse_type', 'collapse_type'), ('sacred_object', 'sacred_object'), ('outcome_type', 'outcome_type'),
         ('highest_stigma_step', 'highest_stigma_step'), ('courtesy_stigma', 'courtesy_stigma'),
         ('comedian_response', 'comedian_response'), ('gap_months', 'gap_months'),
         ('mobilising_actor', 'who_mobilised')]
with open(os.path.join(ROOT, 'side_by_side.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['case_id', 'field', 'independent', 'draft'])
    for r in rows:
        d = draft.get(r['case_id'], {})
        for ind, dr in PAIRS:
            w.writerow([r['case_id'], ind, r.get(ind, ''), d.get(dr, '')])
print(len(rows), 'cases')
