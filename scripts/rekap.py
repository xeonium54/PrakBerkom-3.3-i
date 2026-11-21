"""Draft dan validasi rekap/M<m>/nilai.csv (urutan kolom = sheet NILAI di xlsx).

Usage:
  python scripts/rekap.py M1 init [--force]   buat draft: kolom otomatis terisi, kolom penilaian agent kosong
  python scripts/rekap.py M1 check            cek: tidak ada sel kosong, 0 <= nilai <= max, NIM & urutan = xlsx

Kolom otomatis di draft (agent tetap boleh mengoreksi):
  nama_file = 0.2 kalau nama_file_ok di _log.csv, selain itu 0
  compile   = 0.2 kalau compile OK di hasil_tc.csv, selain itu 0
  tcN       = 0.6 kalau PASS, 0 kalau NOFILE, kosong kalau NUMOK/FAIL/ERROR/TIMEOUT (agent menilai)
  soal tidak ada (NOFILE) -> semua kolom soal itu 0
Kosong = harus diisi agent: penalti, header, indentasi, komentar, penguasaan, TC non-PASS, comments.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # python -I tidak menambah folder script
from extract import roster  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PARTS = [("header", 0.2), ("nama_file", 0.2), ("indentasi", 0.2), ("komentar", 0.2), ("compile", 0.2),
         ("penguasaan", 0.6), ("tc2", 0.6), ("tc3", 0.6), ("tc4", 0.6), ("tc5", 0.6)]
COLS = ["StudentID", "NIM", "penalti"] + [f"s{k}_{p}" for k in (1, 2, 3) for p, _ in PARTS] + ["comments"]
MAX = {"penalti": 4.0, **{f"s{k}_{p}": mx for k in (1, 2, 3) for p, mx in PARTS}}


def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def init(m, force):
    out = ROOT / "rekap" / f"M{m}" / "nilai.csv"
    if out.exists() and not force:
        sys.exit(f"{out} sudah ada (mungkin sudah dinilai). Pakai --force untuk menimpa.")
    log = read(ROOT / "solusi_clean" / f"M{m}" / "_log.csv")
    tc = read(ROOT / "rekap" / f"M{m}" / "hasil_tc.csv")
    name_ok = {(r["nim"], r["ditaruh_di"]): r["nama_file_ok"] == "True" for r in log}
    tcs = {(r["nim"], r["soal"], r["tc"]): r for r in tc}
    rows = []
    for sid, nim in roster(m):
        row = {c: "" for c in COLS}
        row.update(StudentID=sid, NIM=nim)
        for k in (1, 2, 3):
            first = tcs.get((nim, str(k), "2"))
            if not first or first["status"] == "NOFILE":
                row.update({f"s{k}_{p}": 0 for p, _ in PARTS})
                continue
            row[f"s{k}_nama_file"] = 0.2 if name_ok.get((nim, f"soal{k}")) else 0
            row[f"s{k}_compile"] = 0.2 if first["compile"] == "OK" else 0
            for n in (2, 3, 4, 5):
                t = tcs.get((nim, str(k), str(n)))
                if t and t["status"] == "PASS":
                    row[f"s{k}_tc{n}"] = 0.6
        rows.append(row)
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, COLS)
        w.writeheader()
        w.writerows(rows)
    blanks = sum(1 for r in rows for c in MAX if r[c] == "")
    print(f"Draft {out}: {len(rows)} baris, {blanks} sel kosong untuk agent.")


def check(m):
    path = ROOT / "rekap" / f"M{m}" / "nilai.csv"
    rows, errs = read(path), []
    if list(rows[0].keys()) != COLS:
        errs.append(f"header kolom beda dari format: {list(rows[0].keys())}")
    want = roster(m)
    got = [(r["StudentID"], r["NIM"]) for r in rows]
    if got != want:
        errs.append(f"StudentID/NIM/urutan beda dari xlsx (xlsx {len(want)} baris, csv {len(got)} baris)")
    for i, r in enumerate(rows, start=2):
        for c, mx in MAX.items():
            v = r.get(c, "")
            try:
                x = float(v)
            except ValueError:
                errs.append(f"baris {i} NIM {r['NIM']} kolom {c}: {'kosong' if v == '' else repr(v)}")
                continue
            if not 0 <= x <= mx + 1e-9:
                errs.append(f"baris {i} NIM {r['NIM']} kolom {c}: {x} di luar 0..{mx}")
    print("\n".join(errs) if errs else f"OK: {path} lengkap dan valid ({len(rows)} baris).")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    assert len(COLS) == 34 and sum(MAX.values()) - 4.0 == 12.0  # 34 kolom A..AH, 3 soal x 4.0
    if len(sys.argv) < 3 or sys.argv[2] not in ("init", "check"):
        sys.exit(__doc__)
    m = int(sys.argv[1].lstrip("Mm"))
    init(m, "--force" in sys.argv) if sys.argv[2] == "init" else check(m)
