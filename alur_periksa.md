# Alur Periksa

Satu modul (`M#`, # = 1..4) diperiksa berurutan dari langkah 0 sampai 6. Semua perintah dijalankan dari root repo pakai Git Bash.
Aturan nilai ada di [rules/rules_penilaian.md](rules/rules_penilaian.md), ciri AI di [rules/karakteristik_ai.md](rules/karakteristik_ai.md).

## 0. Persiapan (sekali saja)
- Soal PDF sudah dikonversi ke `soal_praktikum/M#.pdf.md`. Kalau belum: `doc2md soal_praktikum/M#.pdf auto`. Teks hasil konversi memuat huruf watermark yang berserakan, abaikan saja.
- Testcase: `python -I scripts/build_tc.py all` menghasilkan `testcase/M#/soal{1,2,3}.json`. Baca PERINGATAN yang tercetak. Kalau ada, bandingkan JSON dengan `testcase/tc_raw_#.md` dan perbaiki JSON-nya secara manual.

## 1. Extract
```
python -I scripts/extract.py M#            # tambah --force untuk menimpa (hasil pilah manual hilang!)
```
Baca `solusi_clean/M#/_missing.csv` dan `_log.csv`. Arti kolom `ditaruh_di`:
- `soalK`: sudah ditempatkan otomatis.
- `_unsorted`: nomor soal tidak jelas, bentrok, atau prefix modul lain. Pilah di langkah 2.
- `duplikat`: isinya sama dengan file yang sudah dipakai, abaikan.
- `diabaikan`: bukan kode (pdf, gambar).

## 2. Pilah `_unsorted` (agent)
Untuk tiap `solusi_clean/M#/<NIM>/_unsorted/`:
1. Baca file dan cocokkan isinya dengan soal di `soal_praktikum/M#.pdf.md` (lihat prompt input dan rumusnya).
2. Salin file yang cocok ke `solusi_clean/M#/<NIM>/soalK.py` dengan `cp`. Jangan hapus `_unsorted`.
3. Satu file berisi beberapa soal: pecah ke beberapa `soalK.py`, potong kode apa adanya tanpa diperbaiki.
4. Kalau slot `soalK.py` sudah terisi tapi isinya ternyata jawaban soal lain: tukar.
5. File dengan prefix modul lain (mis. `P02_` di zip M1): pakai hanya kalau isinya memang soal modul ini.
6. Catat setiap tindakan di `solusi_clean/M#/_pilah.md` (NIM, file, ditaruh ke mana, alasan). Kolom nama file untuk soal itu = 0.

Setelah selesai, jalankan ulang TC untuk NIM yang dipilah (langkah 3 dengan daftar NIM).

## 3. Jalankan testcase
```
python -I scripts/run_tc.py M#             # semua NIM (sekitar 40 detik)
python -I scripts/run_tc.py M# NIM1 NIM2   # hanya NIM tertentu; baris NIM lain di hasil_tc.csv dibiarkan
```
Hasil di `rekap/M#/hasil_tc.csv`. Arti status ada di docstring `scripts/run_tc.py` dan tabel TC di rules_penilaian.
Kode praktikan hanya boleh dijalankan lewat script ini atau dengan `python -I` dari folder sementara, dengan input dari pipe.

## 4. Kemiripan antar praktikan
```
python -I scripts/similar.py M#            # rekap/M#/kemiripan.csv, pasangan dengan rasio >= 0.9
```

## 5. Nilai per praktikan (agent)
```
python -I scripts/rekap.py M# init         # draft rekap/M#/nilai.csv; kolom otomatis sudah terisi
```
Lalu untuk setiap NIM (bagi ke sub-agent, sekitar 15 NIM per sub-agent, lihat CLAUDE.md):
1. Baca `soal1.py`..`soal3.py` dan soalnya di `soal_praktikum/M#.pdf.md`.
2. Isi `header`, `indentasi`, `komentar` dan `penguasaan` sesuai rules_penilaian.
3. Untuk TC yang belum terisi (NUMOK/FAIL/ERROR/TIMEOUT): baca `expected` dan `stdout_tail` di `hasil_tc.csv`, beri nilai sesuai tabel TC. Kalau `stdout_tail` terpotong, jalankan manual: `printf 'a\nb\n' | python -I solusi_clean/M#/<NIM>/soalK.py`. Input-nya ambil dari `testcase/M#/soalK.json`.
4. Koreksi kolom otomatis kalau perlu (mis. file hasil pilah manual: nama file = 0).
5. Cek AI sesuai karakteristik_ai.md dan lihat `kemiripan.csv`.
6. Isi `penalti` (selama aturan penalti masih TODO: 0).
7. Isi `comments`, singkat, dipisah `; `. Contoh: `s1 TC4 pembulatan 13.333; s3 pakai if padahal dilarang; AI:Sedang (s2 type hints baris 5, try/except); MIRIP:15626017 s2 (0.99)`.
8. Tulis alasan per soal di `rekap/M#/catatan/<NIM>.md` (3–6 baris per soal). File ini dibaca asisten kalau ada keberatan dari praktikan.

Sub-agent tidak menulis langsung ke `nilai.csv`. Tiap sub-agent menulis `rekap/M#/nilai_part_<n>.csv` dengan header yang sama, lalu agent utama menggabungkannya ke `nilai.csv` dengan urutan baris tetap seperti draft.

## 6. Validasi dan laporan
```
python -I scripts/rekap.py M# check        # harus "OK"; kalau tidak, perbaiki sel yang disebut
```
Laporkan ke asisten:
- jumlah yang tidak mengumpulkan / soal kurang;
- daftar flag AI level Sedang/Tinggi dan pasangan MIRIP rasio 1.0;
- kasus yang perlu keputusan manusia (TC yang mungkin salah, aturan TODO yang terpakai, hasil pilah yang ragu);
- 5 nilai total tertinggi dan terendah sebagai sanity check.

Nilai di `nilai.csv` disalin asisten ke xlsx secara manual. Urutan kolom C..AH sama persis dengan kolom `penalti`..`comments`.
