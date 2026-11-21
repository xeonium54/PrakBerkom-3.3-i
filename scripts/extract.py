"""Extract solusi_raw/M<m>/*.zip -> solusi_clean/M<m>/<NIM>/soal{1,2,3}.py + log.

Usage: python scripts/extract.py M1 [--force]
Output per modul:
  solusi_clean/M<m>/<NIM>/soalK.py      file terpilih untuk soal K (1=Easy, 2=Medium, 3=Hard)
  solusi_clean/M<m>/<NIM>/_orig/...     semua file asli (nama asli, path di-flatten dengan '__')
  solusi_clean/M<m>/<NIM>/_unsorted/... file .py yang nomor soalnya tidak jelas / bentrok -> dipilah agent
  solusi_clean/M<m>/_log.csv            satu baris per file di dalam zip
  solusi_clean/M<m>/_missing.csv        NIM roster tanpa kiriman / soal yang kurang / NIM di luar roster
Zip dibaca di memori; tidak ada path dari zip yang dipakai untuk menulis (aman dari zip-slip).
"""
import csv
import io
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = re.compile(r"(^|/)(__MACOSX|\.)")


def roster(m):
    """[(StudentID, NIM)] dari kolom A,B sheet NILAI di rekap/M<m>/*.xlsx (baris >= 5), urut baris."""
    xlsx = next((ROOT / "rekap" / f"M{m}").glob("*.xlsx"))
    z = zipfile.ZipFile(xlsx)
    wb = z.read("xl/workbook.xml").decode()
    rid = re.search(r'<sheet name="NILAI"[^>]*r:id="(\w+)"', wb).group(1)
    rels = z.read("xl/_rels/workbook.xml.rels").decode()
    target = re.search(rf'Id="{rid}"[^>]*Target="([^"]+)"|Target="([^"]+)"[^>]*Id="{rid}"', rels)
    target = (target.group(1) or target.group(2)).lstrip("/")
    sheet = z.read(target if target.startswith("xl/") else "xl/" + target).decode()
    ss = [re.sub("<[^>]+>", "", s) for s in re.findall(r"<si>(.*?)</si>", z.read("xl/sharedStrings.xml").decode(), re.S)]
    cells = {}
    for col, r, attrs, inner in re.findall(r'<c r="([AB])(\d+)"([^>]*)>(.*?)</c>', sheet, re.S):
        v = re.search(r"<v>(.*?)</v>", inner)
        if int(r) >= 5 and v:
            cells[(col, int(r))] = ss[int(v.group(1))] if 't="s"' in attrs else v.group(1)
    rows = sorted({r for _, r in cells})
    return [(cells.get(("A", r), ""), cells[("B", r)]) for r in rows if ("B", r) in cells]


def nim_of(zipname):
    m = re.match(r"(\d{8})-", zipname) or re.search(r"(\d{8})", zipname)
    return m.group(1) if m else None


def soal_of(stem, nim):
    """Nomor soal 1-3 dari nama file, atau None kalau tidak jelas."""
    s = re.sub(r"^\s*#?\s*p[oy]?\s*0?[1-9]", "", stem, flags=re.I)  # buang prefix P01/PO1/PY03/p1
    s = re.sub(r"\d{8}", "", s)                                     # buang NIM (juga NIM typo)
    nums = re.findall(r"\d+", s)
    return int(nums[-1]) if nums and 1 <= int(nums[-1]) <= 3 else None


def walk(data, prefix):
    """Yield (path_dalam_zip, bytes) untuk semua file, masuk ke zip bersarang."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for info in z.infolist():
            name = info.filename
            if info.is_dir() or SKIP.search(name):
                continue
            body = z.read(info)
            if name.lower().endswith(".zip"):
                yield from walk(body, f"{prefix}{name}!/")
            else:
                yield prefix + name, body


def ipynb_to_py(body):
    nb = json.loads(body.decode("utf-8", "replace"))
    cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
    return "\n\n".join("".join(c.get("source", "")) for c in cells).encode("utf-8")


def flat(path):
    return re.sub(r"[\\/:!*?\"<>|]+", "__", path)


def run(m, force=False):
    raw, clean = ROOT / "solusi_raw" / f"M{m}", ROOT / "solusi_clean" / f"M{m}"
    old = [p for p in clean.iterdir() if p.is_dir()] if clean.exists() else []
    if old and not force:
        sys.exit(f"{clean} sudah berisi {len(old)} folder NIM (mungkin sudah dipilah manual). Pakai --force untuk menimpa.")
    for p in old:
        shutil.rmtree(p)
    clean.mkdir(parents=True, exist_ok=True)

    names = [nim for _, nim in roster(m)]
    log, got = [], {}
    zip_ok_re = re.compile(rf"P0{m}_(\d{{8}})\.zip")
    for zp in sorted(raw.glob("*.zip")):
        nim = nim_of(zp.name)
        if not nim:
            log.append([None, zp.name, "", "", "", "", "NIM tidak terbaca dari nama zip"])
            continue
        base = re.sub(r"^\d{8}-", "", zp.name)  # prefix NIM- ditambahkan Teams
        zm = zip_ok_re.fullmatch(base)
        zip_ok = bool(zm and zm.group(1) == nim)
        dest = clean / nim
        (dest / "_orig").mkdir(parents=True, exist_ok=True)
        slots = got.setdefault(nim, {})
        try:
            files = list(walk(zp.read_bytes(), ""))
        except zipfile.BadZipFile:
            log.append([nim, zp.name, "", "", zip_ok, "", "zip rusak / bukan zip"])
            continue
        if not files:
            log.append([nim, zp.name, "", "", zip_ok, "", "zip kosong"])
        for path, body in files:
            fname = path.split("/")[-1].split("!")[-1]
            (dest / "_orig" / flat(f"{zp.stem}__{path}")).write_bytes(body)
            note = "dalam folder/zip bersarang" if "/" in path or "!" in path else ""
            low = fname.lower()
            if low.endswith(".ipynb"):
                body, note = ipynb_to_py(body), (note + "; ipynb->py").strip("; ")
            elif low.endswith(".txt") or "." not in fname:
                note = (note + "; bukan .py (txt/tanpa ekstensi), cek apakah isinya kode").strip("; ")
            elif not low.endswith(".py"):
                log.append([nim, zp.name, path, "diabaikan", zip_ok, "", note or "bukan .py"])
                continue
            stem = Path(fname).stem
            k = soal_of(stem, nim)
            pm = re.match(r"\s*#?\s*p[oy]?\s*0?([1-9])", stem, re.I)
            name_ok = bool(re.fullmatch(rf"P0{m}_{nim}_0[1-3]\.py", fname))
            if pm and int(pm.group(1)) != m:
                k, note = None, (note + f"; prefix modul lain (P0{pm.group(1)})").strip("; ")
            if k and k in slots and slots[k][1] == body:
                log.append([nim, zp.name, path, "duplikat", zip_ok, name_ok, f"identik dgn {slots[k][0]}"])
                continue
            if k and k not in slots:
                slots[k] = (path, body)
                (dest / f"soal{k}.py").write_bytes(body)
                where = f"soal{k}"
            else:
                (dest / "_unsorted").mkdir(exist_ok=True)
                (dest / "_unsorted" / flat(f"{zp.stem}__{path}")).write_bytes(body)
                where = "_unsorted"
                if k:
                    note += "; bentrok (isi beda) dgn " + slots[k][0]
                elif "prefix modul lain" not in note:
                    note += "; nomor soal tidak jelas"
                note = note.strip("; ")
            log.append([nim, zp.name, path, where, zip_ok, name_ok, note])

    with open(clean / "_log.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["nim", "zip", "file_dalam_zip", "ditaruh_di", "nama_zip_ok", "nama_file_ok", "catatan"])
        w.writerows(log)
    with open(clean / "_missing.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["nim", "masalah"])
        for nim in names:
            if nim not in got:
                w.writerow([nim, "tidak mengumpulkan"])
            else:
                lack = [f"soal{k}" for k in (1, 2, 3) if k not in got[nim]]
                if lack:
                    unsorted = (clean / nim / "_unsorted").exists()
                    w.writerow([nim, "belum ada " + ",".join(lack) + (" (cek _unsorted)" if unsorted else "")])
        for nim in sorted(set(got) - set(names)):
            w.writerow([nim, "NIM tidak ada di roster rekap"])
    print(f"M{m}: {len(list(raw.glob('*.zip')))} zip, {len(got)} NIM, roster {len(names)}. "
          f"Lihat {clean / '_log.csv'} dan _missing.csv")


def _selfcheck():
    n = "15426125"
    assert soal_of("P01_15426125_01", n) == 1
    assert soal_of("P04-15426126.02", "15426126") == 2
    assert soal_of("po2_15626030_1_py_", "15626030") == 1
    assert soal_of("p03_15626020", "15626020") is None
    assert soal_of("Problem 2", n) == 2
    assert soal_of("PY03 15626009", "15626009") is None
    assert soal_of("P0_15626013_02", "15626013") == 2
    assert nim_of("15626026-P02_15626926.zip") == "15626026"
    assert nim_of("P01_15426126.zip") == "15426126"


if __name__ == "__main__":
    _selfcheck()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    for a in args:
        run(int(a.lstrip("Mm")), force="--force" in sys.argv)
