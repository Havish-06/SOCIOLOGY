"""Convert YouTube .vtt captions into readable text with a [mm:ss] stamp about every 20 seconds.

Usage: python vtt2txt.py <raw_dir> <out_dir>
"""
import os, re, sys, glob

raw, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
TS = re.compile(r'^(\d+):(\d+):(\d+)\.\d+ -->')
for path in sorted(glob.glob(os.path.join(raw, '*.vtt'))):
    base = os.path.basename(path)
    case_vid, lang = base.rsplit('.', 2)[0], base.rsplit('.', 2)[1]
    lines, seen, cur, last_stamp = [], set(), 0, -999
    for ln in open(path, encoding='utf-8', errors='replace'):
        ln = ln.strip()
        m = TS.match(ln)
        if m:
            h, mi, s = map(int, m.groups()); cur = h * 3600 + mi * 60 + s
            continue
        if not ln or ln.startswith(('WEBVTT', 'Kind:', 'Language:', 'NOTE')) or '-->' in ln:
            continue
        txt = re.sub(r'<[^>]+>', '', ln).strip()
        if not txt or txt in seen:
            continue
        seen.add(txt)
        if cur - last_stamp >= 20:
            lines.append(f'\n[{cur // 60:02d}:{cur % 60:02d}] ')
            last_stamp = cur
        lines.append(txt + ' ')
    vid = case_vid.split('__', 1)[1]
    header = f'# {case_vid}  (caption language: {lang}; https://www.youtube.com/watch?v={vid})\n'
    open(os.path.join(out, case_vid + '.txt'), 'w', encoding='utf-8').write(header + ''.join(lines).strip() + '\n')
    print(case_vid, lang)
