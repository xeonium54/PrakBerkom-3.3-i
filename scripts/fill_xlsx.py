"""Salin nilai.csv ke salinan xlsx template (template asli tidak disentuh).

Usage:
  python -I scripts/fill_xlsx.py M1 [M2 ...]   tulis rekap/final/<nama template>.xlsx
Kolom C..AH sheet NILAI = kolom penalti..comments di nilai.csv. Baris dicocokkan lewat NIM di kolom B.
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))  # python -I tidak menambah folder script
from extract import roster  # noqa: E402
from rekap import COLS, read  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def col_name(i):  # 0 -> A
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def sheet_path(z):
    wb = z.read("xl/workbook.xml").decode()
    rid = re.search(r'<sheet name="NILAI"[^>]*r:id="(\w+)"', wb).group(1)
    rels = z.read("xl/_rels/workbook.xml.rels").decode()
    t = re.search(rf'Id="{rid}"[^>]*Target="([^"]+)"|Target="([^"]+)"[^>]*Id="{rid}"', rels)
    t = (t.group(1) or t.group(2)).lstrip("/")
    return t if t.startswith("xl/") else "xl/" + t


def fill(m):
    src = next((ROOT / "rekap" / f"M{m}").glob("*.xlsx"))
    rows = read(ROOT / "rekap" / f"M{m}" / "nilai.csv")
    assert [(r["StudentID"], r["NIM"]) for r in rows] == roster(m), f"M{m}: urutan nilai.csv beda dari xlsx, jalankan rekap.py check"
    z = zipfile.ZipFile(src)
    name = sheet_path(z)
    sheet = z.read(name).decode()
    for i, r in enumerate(rows):
        rn = 5 + i  # roster() mulai baris 5 dan urut baris
        assert re.search(rf'<c r="B{rn}"[^>]*><v>{r["NIM"]}</v>', sheet), f"M{m}: NIM {r['NIM']} tidak di B{rn}"
        for j, c in enumerate(COLS[2:], start=2):
            ref, v = f"{col_name(j)}{rn}", r[c]
            if c == "comments":
                body = f' t="inlineStr"><is><t xml:space="preserve">{escape(v)}</t></is></c>' if v else "></c>"
            else:
                body = f"><v>{float(v):g}</v></c>"
            sheet, n = re.subn(rf'<c r="{ref}"( s="\d+")?[^>]*?(?:/>|>.*?</c>)', lambda mt: f'<c r="{ref}"{mt.group(1) or ""}{body}', sheet, count=1)
            assert n == 1, f"M{m}: sel {ref} tidak ada di template"
    out = ROOT / "rekap" / "final" / src.name
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as o:
        for item in z.infolist():
            o.writestr(item, sheet if item.filename == name else z.read(item))
    verify(out, name, rows)
    print(f"OK: {out} ({len(rows)} baris)")


def verify(out, name, rows):
    """Baca ulang hasil dan bandingkan tiap sel dengan nilai.csv."""
    s = zipfile.ZipFile(out).read(name).decode()
    for i, r in enumerate(rows):
        for j, c in enumerate(COLS[2:], start=2):
            cell = re.search(rf'<c r="{col_name(j)}{5 + i}"[^>]*>(.*?)</c>', s, re.S).group(1)
            got = re.sub("<[^>]+>", "", cell)
            want = escape(r[c]) if c == "comments" else f"{float(r[c]):g}"
            assert got == want, f"{col_name(j)}{5 + i}: {got!r} != {want!r}"


if __name__ == "__main__":
    assert col_name(0) == "A" and col_name(25) == "Z" and col_name(33) == "AH"
    for a in sys.argv[1:] or sys.exit(__doc__):
        fill(int(a.lstrip("Mm")))
