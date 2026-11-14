"""Build the comparison table from the case files.

Reads the "Final coding" block (or, if missing, the "Coding summary" block) of every
independent_analysis/cases/<case_id>.md and writes independent_analysis/comparison.csv, one row per case.

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

with open(os.path.join(ROOT, 'comparison.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=KEYS)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in KEYS})
print(len(rows), 'cases')
