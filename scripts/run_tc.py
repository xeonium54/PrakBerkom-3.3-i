"""Jalankan testcase ke solusi_clean/M<m>/<NIM>/soal{1,2,3}.py -> rekap/M<m>/hasil_tc.csv.

Usage: python scripts/run_tc.py M1 [NIM ...]
Butuh: scripts/extract.py dan scripts/build_tc.py sudah dijalankan.

Status per TC:
  PASS     semua token output yang diharapkan muncul berurutan di stdout (prompt/teks lain boleh menyela)
  NUMOK    teks beda, tapi semua angka yang diharapkan muncul berurutan -> agent cek untuk nilai parsial
  FAIL     output salah
  ERROR    program crash (lihat stderr), dan output tidak PASS
  TIMEOUT  lebih dari 5 detik (biasanya minta input lebih banyak / loop tak berhenti)
  NOFILE   soalK.py tidak ada
Kolom compile: OK / SyntaxError / File kosong (dicek dengan compile(), tanpa menjalankan kode).
"""
import csv
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NUMS = re.compile(r"(?:(?<!\w)-)?\d+(?:[.,]\d+)?")  # 'ke-1' -> 1, bukan -1
TIMEOUT = 5


def in_order(needles, hay):
    it = iter(hay)
    return all(n in it for n in needles)  # subsequence check


def tokens_in_order(expected, stdout):
    """Tiap token expected dicari berurutan di stdout (boleh menempel ke prompt), tapi angka tidak boleh
    jadi potongan angka lain (Rp1200 tidak cocok dengan Rp12000 / Rp1200.5)."""
    pos = 0
    for tok in expected.split():
        pat = re.escape(tok)
        if tok[0].isdigit():
            pat = r"(?<![\d.])" + pat
        if tok[-1].isdigit():
            pat += r"(?!\d|[.,]\d)"
        m = re.compile(pat).search(stdout, pos)
        if not m:
            return False
        pos = m.end()
    return True


def judge(expected, stdout):
    if tokens_in_order(expected, stdout):
        return "PASS"
    def nums(s):
        return [float(x.replace(",", ".")) for x in NUMS.findall(s)]
    if in_order(nums(expected), nums(stdout)):
        return "NUMOK"
    return "FAIL"


def compile_status(path):
    src = path.read_bytes()
    if not src.strip():
        return "File kosong"
    try:
        compile(src, str(path), "exec")
        return "OK"
    except SyntaxError as e:
        return f"SyntaxError baris {e.lineno}: {e.msg}"
    except ValueError as e:  # mis. null byte
        return f"Error: {e}"


def run_one(path, inputs, cwd):
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    try:
        p = subprocess.run([sys.executable, "-I", str(path)], input="\n".join(inputs) + "\n",
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=TIMEOUT, cwd=cwd, env=env)
        return p.stdout, p.stderr, p.returncode, False
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return out, "", None, True


def main(m, only):
    clean = ROOT / "solusi_clean" / f"M{m}"
    tcs = {k: json.loads((ROOT / "testcase" / f"M{m}" / f"soal{k}.json").read_text(encoding="utf-8"))["tcs"]
           for k in (1, 2, 3)}
    nims = sorted(p.name for p in clean.iterdir() if p.is_dir() and re.fullmatch(r"\d{8}", p.name))
    if only:
        nims = [n for n in nims if n in only]
    rows, summary = [], {}
    with tempfile.TemporaryDirectory() as cwd:
        for nim in nims:
            for k in (1, 2, 3):
                f = clean / nim / f"soal{k}.py"
                if not f.exists():
                    rows += [[nim, k, t["tc"], "NOFILE", "", t["expected"], "", ""] for t in tcs[k]]
                    continue
                comp = compile_status(f)
                for t in tcs[k]:
                    if not comp.startswith("OK"):
                        rows.append([nim, k, t["tc"], "ERROR", comp, t["expected"], "", comp])
                        continue
                    out, err, rc, to = run_one(f, t["inputs"], cwd)
                    st = judge(t["expected"], out)
                    if st != "PASS":
                        st = "TIMEOUT" if to else ("ERROR" if rc else st)
                    rows.append([nim, k, t["tc"], st, comp, t["expected"],
                                 " ".join(out.split())[-400:], err.strip().splitlines()[-1][:200] if err.strip() else ""])
    for r in rows:
        summary[r[3]] = summary.get(r[3], 0) + 1
    out = ROOT / "rekap" / f"M{m}" / "hasil_tc.csv"
    header = ["nim", "soal", "tc", "status", "compile", "expected", "stdout_tail", "stderr_last"]
    if only and out.exists():  # jalankan ulang sebagian NIM: ganti baris NIM itu saja
        with open(out, encoding="utf-8-sig", newline="") as fh:
            old = [r for r in list(csv.reader(fh))[1:] if r[0] not in only]
        rows = sorted(old + [[str(c) for c in r] for r in rows], key=lambda r: (r[0], int(r[1]), int(r[2])))
    with open(out, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"M{m}: {len(nims)} NIM dijalankan, {summary} -> {out}")


def _selfcheck():
    assert judge("Biaya listrik yang terbuang adalah Rp1200",
                 "Masukkan daya: Masukkan lama: Biaya listrik yang terbuang adalah Rp1200\n") == "PASS"
    assert judge("Saldo ke-1: Rp5. Saldo ke-2: Rp7.", "Saldo ke-1: Rp5. Masukkan x: Saldo ke-2: Rp7.") == "PASS"
    assert judge("adalah Rp1200", "hasilnya Rp 1200") == "NUMOK"
    assert judge("Biaya adalah Rp1200", "(kWh):Biaya adalah Rp1200") == "PASS"
    assert judge("adalah Rp1200", "adalah Rp12000") == "FAIL"
    assert judge("adalah Rp1200", "adalah Rp1200.0") == "NUMOK"
    assert judge("adalah Rp1200", "adalah Rp1300") == "FAIL"
    assert judge("transaksi ke-1: Rp5", "transaksi ke1: Rp5") == "NUMOK"
    assert judge("saldo -5", "saldo 5") == "FAIL"


if __name__ == "__main__":
    _selfcheck()
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(int(sys.argv[1].lstrip("Mm")), set(sys.argv[2:]))
