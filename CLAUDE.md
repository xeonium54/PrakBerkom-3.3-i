# Penilaian Praktikum Berpikir Komputasional (Python)

Repo untuk asisten menilai praktikum kelas 3.3-i: 4 modul (M1–M4), 60 praktikan, 3 soal per modul (Easy/Medium/Hard).
Agent mengerjakan bagian yang butuh penilaian manusia. Bagian yang deterministik dikerjakan script di `scripts/`.
Alur lengkap: **[alur_periksa.md](alur_periksa.md)**. Ikuti urutannya, jangan loncat langkah.

## Direktori
| Path | Isi | Boleh diubah? |
|---|---|---|
| `soal_praktikum/M#.pdf` | soal asli | tidak |
| `soal_praktikum/M#.pdf.md` | soal hasil doc2md (ada huruf watermark berserakan) | jangan diedit |
| `solusi_raw/M#/*.zip` | kiriman praktikan apa adanya (`<NIM>-<nama asli>.zip` dari Teams, atau `P0#_NIM.zip`) | **tidak pernah** |
| `solusi_clean/M#/<NIM>/soal{1,2,3}.py` | hasil `extract.py` + pilah manual | ya (langkah 2) |
| `solusi_clean/M#/<NIM>/_orig/`, `_unsorted/` | semua file asli / yang belum jelas soalnya | jangan dihapus |
| `solusi_clean/M#/_log.csv`, `_missing.csv`, `_pilah.md` | log extract, yang kurang, catatan pilah | log: dibuat ulang script |
| `testcase/tc_raw_#.md`, `pick.md` | testcase mentah semua soal + nomor soal kelas ini | tidak |
| `testcase/M#/soal{1,2,3}.json` | testcase terpilih hasil `build_tc.py` | hanya untuk koreksi parse |
| `rekap/M#/*.xlsx` | template nilai resmi | **tidak pernah** |
| `rekap/M#/hasil_tc.csv`, `kemiripan.csv` | hasil script | dibuat ulang script |
| `rekap/M#/nilai.csv`, `catatan/<NIM>.md` | nilai akhir + alasan | ya (agent) |
| `rules/` | aturan penilaian, ciri AI | aturan diubah hanya oleh asisten |
| `ref/M#/<model>/soalK.py` | solusi referensi buatan AI | ya |
| `scripts/` | extract, build_tc, run_tc, similar, rekap | ya, tapi selftest (`assert`) harus tetap lolos |

Soal 1 = Easy, Soal 2 = Medium, Soal 3 = Hard. Nomornya ada di `testcase/pick.md`.

## Rules
- Bahasa: Indonesia untuk comments, catatan dan laporan.
- Jalankan Python dengan `python -I`. Kode praktikan hanya dijalankan lewat `scripts/run_tc.py` atau `printf ... | python -I <file>`. Jangan `import` file praktikan, jangan jalankan kode praktikan yang membaca/menulis file atau memakai jaringan; catat saja di comments.
- Jangan memperbaiki kode praktikan. Pilah dan potong boleh, edit isi tidak.
- `extract.py --force` dan `rekap.py init --force` menimpa hasil kerja manual. Jangan dipakai tanpa izin asisten.
- Nilai mengikuti `rules/rules_penilaian.md`. Kalau aturannya masih TODO, pakai nilai usulan dan tulis itu di comments. Jangan mengarang aturan baru.
- Indikasi AI tidak mengubah nilai. Flag di `comments` dan wajib disertai bukti.
- Setiap nilai di bawah maksimum harus punya alasan di `catatan/<NIM>.md`.
- Jangan baca PDF/xlsx langsung. Untuk soal pakai `.pdf.md`, untuk roster pakai `scripts/extract.py:roster`.
- Data praktikan (nama, NIM, kode) tidak boleh dikirim ke layanan luar.
- Sub-agent: bagi per sekitar 15 NIM. Brief harus menyebut modul, daftar NIM, file output `rekap/M#/nilai_part_<n>.csv`, dan larangan: tidak mengubah `nilai.csv`, `solusi_raw/`, xlsx, dan tidak menjalankan `git stash`, `checkout` atau `reset`.
- Selesai satu modul: `python -I scripts/rekap.py M# check` harus OK sebelum melapor.

## Perintah cepat
```
python -I scripts/build_tc.py all
python -I scripts/extract.py M1
python -I scripts/run_tc.py M1 [NIM ...]
python -I scripts/similar.py M1
python -I scripts/rekap.py M1 init | check
```
Prompt siap pakai ada di [prompt.md](prompt.md).
