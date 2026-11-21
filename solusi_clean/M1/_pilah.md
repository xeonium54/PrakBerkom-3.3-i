# Pilah `_unsorted` M1

Soal kelas ini: soal1 = biaya listrik lampu (Problem 1), soal2 = konsentrasi larutan campuran (Problem 2), soal3 = upah shift dan lembur Tuan Joji (Problem 3).
Semua file disalin dengan `cp` atau dipotong per baris tanpa mengubah isi. `_orig/` dan `_unsorted/` tidak disentuh.
**Nama file = 0** untuk setiap slot yang terisi dari hasil pilah, yaitu slot yang ditandai (pilah) di tabel.

Bagian NIM 15626004, 15626005, 15626007, 15626008, 15626013, 15626020, 15626031, 15626033, 15626035, 15626046, 15626052.

| NIM | file | ditaruh ke | alasan |
|---|---|---|---|
| 15626004 | `15626004-P01_15626004__P02_15626004_02.py` | soal2.py (pilah) | Prefix P02, tapi isinya konsentrasi larutan C1..C3/V1..V3, jadi soal2 M1. |
| 15626005 | `soal1.py` lama (`P01_15626005_02.py.zip!/konsentrasi_uprak1.py`) | soal2.py (pilah, tukar) | Isinya konsentrasi larutan, bukan biaya listrik. Dipindah ke slot soal2. |
| 15626005 | `..._P01_NIM_01,py.zip__biaya listrik.py` | soal1.py (pilah) | Biaya listrik lampu (daya, lama, tarif). |
| 15626005 | `..._P01_15626003_03_REVISI.py.zip__uprak01_upah.py` | soal3.py (pilah) | Upah lembur (jam/menit masuk-keluar, batas shift, tunjangan). Nama zip memuat NIM 15626003, tapi header file 15626005. Lihat Ragu. |
| 15626007 | `soal1.py` lama (`p01_15626007_py (1).py`) | soal3.py (pilah, tukar) | Isinya upah shift/lembur, ditulis 3 kali (Case 1-3). |
| 15626007 | `P01_15626007__p01_15626007_ipy.py` | soal1.py (pilah) | Biaya listrik (3 blok case berulang). |
| 15626007 | `P01_15626007__p01_15626007_py.py` | soal2.py (pilah) | Konsentrasi larutan (3 blok case berulang). |
| 15626008 | `P01_15626008__P02_15626008_02.py` | soal2.py (pilah) | Prefix P02, isinya konsentrasi larutan. Bentuknya salinan sesi REPL (`...`, output ikut). Deskripsi header keliru menyebut biaya listrik. |
| 15626008 | `15626008-P02_15626008_02__P02_15626008_02.py` | tidak dipakai (duplikat) | Identik (cmp) dengan file P02 di dalam P01_15626008.zip. Dikirim juga sebagai zip terpisah. |
| 15626008 | `P01_15626008__P03_15626008_03.py` | soal3.py (pilah) | Prefix P03, isinya upah shift/lembur M1. Salinan REPL, baris input j1/m1 tidak ada di kodenya. |
| 15626013 | `P01_15626013__berkom__Untitled-1.txt` | tidak dipakai | Isinya hanya header dan kamus biaya listrik (6 baris komentar, tanpa kode). soal1.py yang ada sudah lengkap. |
| 15626020 | `P01_15626020__Rudianto 15626020 30 September.ipynb` (sudah dikonversi ke kode oleh extract) | soal1.py (pilah, dipotong) | 3 sel pertama berisi percobaan biaya listrik (pseudo-kode, bukan Python valid). 2 sel terakhir dibuang: contoh bawaan Colab (`google.colab ai`, plot matplotlib), bukan jawaban soal. Lihat Ragu. |
| 15626031 | `..._p02_15626031__p02_15626031_1.py` | soal2.py (pilah, tukar) | Folder p02 = problem 2: konsentrasi larutan. soal2.py lama (`p01_15625031_02.py`) ternyata kode biaya listrik yang sama dengan soal1 (hanya konstanta testcase beda), jadi ditimpa. |
| 15626031 | `..._p03_15626031__p03_15626031_1.py` | soal3.py (pilah, tukar) | Folder p03 = problem 3: upah lembur. soal3.py lama (`p01_15626031_03.py`) juga salinan biaya listrik, jadi ditimpa. |
| 15626031 | `..._p02_..._1.py` dalam `p02_15626031.zip`, `..._p03_..._1.py` dalam `p03_15626031.zip` | tidak dipakai (duplikat) | Identik (md5) dengan versi folder. |
| 15626031 | `..._p03_15626031_2.py` (folder dan zip) | tidak dipakai | Kode sama dengan `_1`, hanya konstanta awal testcase 2 yang beda (konstanta ditimpa input). |
| 15626031 | `..._p02_15626031_2.py`, `_3.py`, `..._p03_15626031_3.py` (folder dan zip) | tidak dipakai | File kosong (0 byte). |
| 15626033 | `15626033-P01_15626033.zip__praktikum berkom.py` | soal1.py, soal2.py, soal3.py (pilah, dipecah) | Satu file berisi `'''PROBLEM 1'''`..`'''PROBLEM 3'''`. Dipotong di penanda itu; 3 baris header identitas ikut ke tiap potongan. |
| 15626035 | `P01_15626035__P01_15626035__BIAYA LISTRIK.ipynb` (sudah dikonversi) | soal1.py (pilah) | Biaya listrik (daya, durasi, tarif). |
| 15626035 | `P01_15626035__P03_15626035.ipynb` (sudah dikonversi) | soal3.py (pilah) | Prefix P03, isinya awal soal upah (dict jam_masuk, batas_normal, pengali_lembur, ...). Terpotong di `"tunjangan_makan":`; notebook asli di `_orig` juga terpotong di situ. Lihat Ragu. |
| 15626046 | `P01_15626046__P1_15626046__P1_15626046.txt` | soal1.py (pilah) | Salinan sesi IDLE biaya listrik (ada `>>>` dan output). Format sama dengan soal2/soal3 yang sudah ada. |
| 15626052 | `..._P01_15626052.01.zip__P01_15626052.01__P01_15626052.01.py` | soal1.py (pilah, ganti) | Kode biaya listrik. soal1.py lama adalah `(HASIL) P01_15626052.01.py`, yaitu log jalan IDLE (output saja, bukan kode). Versi kode dipilih; file HASIL tetap di `_orig`. |
| 15626052 | `..._P01_15626052_02.zip__P01_15626052_02__P01_15626052_02.py` | soal2.py (pilah, ganti) | Kode konsentrasi. soal2.py lama `(HASIL)P01_15626052_02.py` = log output IDLE. |
| 15626052 | `..._P01_15626052.01.zip__P01_15626052_02.zip__..._02.py` | tidak dipakai (duplikat) | Identik (md5) dengan yang dipakai untuk soal2. |

## Ringkasan slot setelah pilah

| NIM | soal1 | soal2 | soal3 | masih kurang |
|---|---|---|---|---|
| 15626004 | ada | pilah | ada | - |
| 15626005 | pilah | pilah (tukar) | pilah | - |
| 15626007 | pilah | pilah | pilah (tukar) | - |
| 15626008 | ada | pilah | pilah | - |
| 15626013 | ada | ada | ada | - |
| 15626020 | pilah | - | - | soal2, soal3 |
| 15626031 | ada | pilah (tukar) | pilah (tukar) | - |
| 15626033 | pilah | pilah | pilah | - |
| 15626035 | pilah | ada | pilah (tidak selesai) | - |
| 15626046 | pilah | ada | ada | - |
| 15626052 | pilah (ganti) | pilah (ganti) | - | soal3 |

## Ragu

- **15626005 soal3**: file upah ada di zip `P01_15626003_03_REVISI.py.zip`, NIM di nama zip 15626003 (praktikan itu tercatat tidak mengumpulkan), header file 15626005. Saya anggap salah ketik nama dan milik 15626005. Asisten perlu konfirmasi. Tidak ada versi non-REVISI.
- **15626008 soal2/soal3** (dan soal1 yang sudah ada): ketiganya salinan sesi REPL (`... ` di depan baris, output ikut), jadi tidak bisa dijalankan sebagai .py. Perlu keputusan apakah dinilai manual dari kodenya.
- **15626046 soal1** (juga soal2/soal3): salinan sesi IDLE dengan `>>>`, kasusnya sama dengan 15626008.
- **15626052 soal1/soal2**: slot awal berisi file `(HASIL)` (log output). Saya ganti dengan file kodenya. Kalau asisten mau menilai output HASIL, file itu masih ada di `_orig`. soal3 tidak ada di kiriman mana pun.
- **15626020 soal1**: notebook berisi pseudo-kode biaya listrik yang bukan Python valid. Dua sel contoh Colab dibuang saat memotong; salah satunya memanggil `google.colab.ai` (jaringan). soal2 dan soal3 tidak ada.
- **15626031 soal2/soal3**: struktur kiriman `pNN_NIM/pNN_NIM_k.py` saya baca sebagai problem NN, testcase k (folder p01 berisi 3 salinan kode listrik dengan konstanta TC1-3). Prefix p02/p03 di sini berarti problem 2/3 M1, bukan modul 2/3. Isinya cocok dengan soal M1. soal2.py/soal3.py lama (salinan listrik) ditimpa, aslinya tetap di `_orig`.
- **15626035 soal3**: isinya hanya awal program dan terpotong (sudah begitu di notebook aslinya). Dipakai karena memang soal3 M1; hasilnya pasti error.
