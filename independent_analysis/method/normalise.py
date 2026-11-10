"""Apply consistency_rules.md to the Final coding block of each case file (run once, from the repository root)."""
import re

CHANGES = {  # case_id: {key: new value}
    'agrima_2020': {'highest_stigma_step': '4'},
    'bharti_2022': {'highest_stigma_step': '3'},
    'virli_2026': {'highest_stigma_step': '3', 'audience_size_tier': 'medium'},
    'kamra_2018': {'audience_size_tier': 'medium'},
    'munawar_2021': {'audience_size_tier': 'medium'},
    'virdas_2021': {'audience_size_tier': 'medium (964K YouTube subscribers; larger Netflix and film fame)'},
}

for case, fields in CHANGES.items():
    path = f'independent_analysis/cases/{case}.md'
    text = open(path, encoding='utf-8').read()
    head, tail = text.split('## Final coding', 1)
    for key, value in fields.items():
        tail, n = re.subn(rf'^{key}:.*$', f'{key}: {value}', tail, count=1, flags=re.M)
        assert n == 1, (case, key)
    tail = tail.rstrip('\n') + '\n\n(Some values above were aligned across cases by `method/consistency_rules.md`.)\n'
    open(path, 'w', encoding='utf-8').write(head + '## Final coding' + tail)
    print(case, fields)
