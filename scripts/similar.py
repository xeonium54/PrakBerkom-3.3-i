"""Cari pasangan solusi yang mirip antar praktikan -> rekap/M<m>/kemiripan.csv.

Usage: python scripts/similar.py M1 [ambang=0.9]
Kode dinormalisasi dulu (komentar dan spasi dibuang). Kemiripan tinggi = bahan pertimbangan
(sumber sama / AI sama), bukan bukti.
"""
import csv
import io
import itertools
import re
import sys
import tokenize
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize(src):
    out = []
    try:
        for t in tokenize.generate_tokens(io.StringIO(src).readline):
            # nama variabel & string dipertahankan: soal M1 kecil, tanpa itu semua solusi terlihat identik
            if t.type in (tokenize.NAME, tokenize.OP, tokenize.NUMBER):
                out.append(t.string)
            elif t.type == tokenize.STRING:
                out.append(" ".join(t.string.split()))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return re.sub(r"\s+", " ", re.sub(r"#.*", "", src))
    return " ".join(out)


def main(m, thr):
    clean = ROOT / "solusi_clean" / f"M{m}"
    rows = []
    for k in (1, 2, 3):
        code = {p.parent.name: normalize(p.read_text(encoding="utf-8", errors="replace"))
                for p in clean.glob(f"*/soal{k}.py")}
        for a, b in itertools.combinations(sorted(code), 2):
            r = SequenceMatcher(None, code[a].split(), code[b].split(), autojunk=False).ratio()
            if r >= thr:
                rows.append([k, a, b, round(r, 3)])
    rows.sort(key=lambda r: -r[3])
    with open(ROOT / "rekap" / f"M{m}" / "kemiripan.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["soal", "nim_a", "nim_b", "rasio"])
        w.writerows(rows)
    print(f"M{m}: {len(rows)} pasangan >= {thr} -> rekap/M{m}/kemiripan.csv")


if __name__ == "__main__":
    a = normalize("x = int(input('a'))  # k\nprint(x)")
    assert a == normalize("x  =  int(input('a'))\n\n\nprint(x)  # lain"), a
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(int(sys.argv[1].lstrip("Mm")), float(sys.argv[2]) if len(sys.argv) > 2 else 0.9)
