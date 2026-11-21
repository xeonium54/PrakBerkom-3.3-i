"""Parse testcase/tc_raw_<m>.md + testcase/pick.md -> testcase/M<m>/soal{1,2,3}.json.

Usage: python scripts/build_tc.py M1 [M2 ...]   (or "all")
soal1 = Easy, soal2 = Medium, soal3 = Hard, nomor soal dari pick.md.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TC = ROOT / "testcase"
LEVELS = ["Easy", "Medium", "Hard"]


def read_pick():
    """{modul: [easy, medium, hard]} dari pick.md."""
    pick, cur = {}, None
    for line in (TC / "pick.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"#\s*Modul\s*(\d+)", line)
        if m:
            cur = int(m.group(1))
            continue
        nums = re.findall(r"\|\s*(\d+)\s*(?=\|)", line)
        if cur and len(nums) == 3:
            pick[cur] = [int(n) for n in nums]
            cur = None
    return pick


def unescape(s):
    return re.sub(r"\\(.)", r"\1", s)


BOLD = re.compile(r"\*{2,3}(.+?)\*{2,3}")
GENERIC = r"Masukkan[^:*]*?:"
NUM = re.compile(r"-?\d+(\.\d+)?$")


def learn_prompts(rows):
    """Pola prompt dari baris yang input-nya bold: <=3 kata terakhir sebelum nilai bold, angka digeneralisasi."""
    pats = set()
    for text in rows:
        prev = 0
        for b in BOLD.finditer(text):
            words = text[prev: b.start()].split()[-3:]
            prev = b.end()
            if words:
                pats.add(r"\s+".join(re.sub(r"\\?\d+", r"\\d+", re.escape(w)) for w in words))
    return sorted(pats, key=len, reverse=True)


def parse_row(text, pats=()):
    """Satu baris tabel -> (inputs, prompts, expected, warnings).

    Prompt = 'Masukkan ...:' atau pola hasil learn_prompts. Nilai = isi bold kalau ada;
    kalau tidak, token pertama, atau semua token sampai prompt berikutnya bila semuanya angka (input array).
    """
    text = unescape(text).strip()
    found = sorted((m.start(), -m.end(), m.end()) for p in [GENERIC, *pats] for m in re.finditer(p, text))
    hits, last_end = [], -1
    for s, _, e in found:
        if s >= last_end:
            hits.append((s, e))
            last_end = e
    inputs, prompts, warns, expected = [], [], [], ""
    if not hits:
        return inputs, prompts, text.replace("*", ""), ["tidak ada prompt input"]
    for i, (s, e) in enumerate(hits):
        seg = text[e: hits[i + 1][0] if i + 1 < len(hits) else len(text)]
        b = BOLD.match(seg.lstrip())
        if b:
            val, rest = b.group(1), seg.lstrip()[b.end():]
        else:
            toks = seg.replace("*", "").split()
            if i + 1 < len(hits) and toks and all(NUM.match(t) for t in toks):
                val, rest = " ".join(toks), ""
            else:
                val, rest = (toks[0] if toks else ""), " ".join(toks[1:])
        if not val:
            warns.append(f"nilai kosong setelah prompt {text[s:e]!r}")
        inputs.append(val.replace("*", "").strip())
        prompts.append(text[s:e].strip())
        expected = rest.replace("*", "").strip()  # teks setelah input terakhir = output akhir
    return inputs, prompts, expected, warns


def parse_md(m):
    """{level: {nomor: [ {tc, inputs, prompts, expected, warnings} ]}}"""
    out, level, nomor = {}, None, None
    for line in (TC / f"tc_raw_{m}.md").read_text(encoding="utf-8").splitlines():
        lv = re.match(r"##\s*\*\*(\w+)\*\*", line)
        if lv:
            level, nomor = lv.group(1), None
            out.setdefault(level, {})
            continue
        so = re.match(r"###\s*Soal\s*(\d+)", line)
        if so:
            nomor = int(so.group(1))
            out[level].setdefault(nomor, [])
            continue
        row = re.match(r"^\|\s*(\d+)\s*\|(.*)\|\s*$", line)
        if row and level and nomor:
            out[level][nomor].append((int(row.group(1)), unescape(row.group(2)).strip()))
    for level in out.values():
        for nomor, rows in level.items():
            pats = learn_prompts([t for _, t in rows])
            level[nomor] = []
            for tc, text in rows:
                inputs, prompts, expected, warns = parse_row(text, pats)
                level[nomor].append({"tc": tc, "inputs": inputs, "prompts": prompts, "expected": expected,
                                     "full": text.replace("*", ""), "warnings": warns})
    return out


def build(m):
    pick = read_pick()[m]
    data = parse_md(m)
    dest = TC / f"M{m}"
    dest.mkdir(exist_ok=True)
    for k, (level, nomor) in enumerate(zip(LEVELS, pick), start=1):
        tcs = data[level][nomor]
        (dest / f"soal{k}.json").write_text(json.dumps(
            {"modul": m, "soal": k, "level": level, "nomor": nomor, "tcs": tcs},
            ensure_ascii=False, indent=2), encoding="utf-8")
        for t in tcs:
            for w in t["warnings"]:
                print(f"PERINGATAN M{m} soal{k} ({level} {nomor}) TC{t['tc']}: {w}")
        print(f"M{m} soal{k} = {level} no {nomor}: {len(tcs)} TC")


def _selfcheck():
    t = parse_md(1)["Easy"][3][0]
    assert t["inputs"] == ["75", "10", "1600"], t
    assert t["expected"] == "Biaya listrik yang terbuang adalah Rp1200", t
    inp, _, exp, _ = parse_row("Masukkan tahun: 2023 2023 bukan tahun kabisat.")
    assert inp == ["2023"] and exp == "2023 bukan tahun kabisat.", (inp, exp)
    t = parse_md(3)["Hard"][9][0]  # input array tanpa bold
    assert t["inputs"] == ["7", "8 1 4 2 5 1 8", "25"], t
    t = parse_md(4)["Hard"][8][0]  # menu interaktif tanpa bold
    assert t["inputs"][4:9] == ["1", "3", "0", "1", "5"], t


if __name__ == "__main__":
    _selfcheck()
    args = sys.argv[1:] or ["all"]
    mods = [1, 2, 3, 4] if args == ["all"] else [int(a.lstrip("Mm")) for a in args]
    for mod in mods:
        build(mod)
