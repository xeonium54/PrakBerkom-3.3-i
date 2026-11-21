# Pilah `_unsorted` M3

Soal kelas ini: soal1 = saldo transaksi Tuan Mik (Easy no 9), soal2 = trailing stop saham (Medium no 12), soal3 = volume genangan air / kaktus Tuan Ky (Hard no 9).
`_orig/`, `_unsorted/` dan `solusi_raw/` tidak disentuh. Salinan pakai `cp` atau potongan baris persis (`sed -n a,bp`, tanpa mengubah isi).
**Nama file = 0** untuk setiap slot hasil pilah, yaitu slot yang ditandai (pilah) di tabel.

Bagian NIM 15626020, 15626028, 15626030, 15626043.

| NIM | file | ditaruh ke | alasan |
|---|---|---|---|
| 15626020 | `_unsorted/15626020-iLoveZIP_Create__p03_15626020.py` baris 1-129 | soal1.py (pilah) | Saldo transaksi. Termasuk docstring Colab dan header (baris 1-12). Kode diulang 3 kali, di sela-selanya ada output dan penjelasan yang ditempel tanpa `#` (baris 44-58, 90-99). Lihat Ragu. |
| 15626020 | file yang sama, baris 131-229 | soal2.py (pilah) | Trailing stop, mulai dari header `# NIM/Nama` kedua. Kode diulang 3 kali. |
| 15626020 | file yang sama, baris 231-336 | soal3.py (pilah) | Genangan air, mulai dari header ketiga. Kode diulang 3 kali. |
| 15626028 | `_unsorted/15626028-P03_15626028.zip__untitled7.py` baris 1-62 | soal1.py (pilah) | Saldo transaksi. Nama/NIM ada di docstring Colab baris 1-11. |
| 15626028 | file yang sama, baris 63-116 | soal2.py (pilah) | Trailing stop, mulai dari docstring `"""Nama: ...` kedua. |
| 15626028 | file yang sama, baris 117-184 | soal3.py (pilah) | Genangan air, mulai dari docstring `"""Nama: ...` ketiga. |
| 15626030 | `soal1.py` (dari `p03_15626030_01_.py`) | tetap soal1.py | Isinya saldo transaksi, slot sudah benar. |
| 15626030 | `_unsorted/..._p03_15626030_02_ (1).py` | soal2.py (pilah) | Isinya trailing stop (meminta persentase dan harga saham per hari). Di-`cp` utuh. Di extract masuk `_unsorted` karena bentrok nama dengan `_01_`. |
| 15626030 | - | soal3 tidak ada | Kiriman hanya berisi `_01_` dan `_02_`. Soal3: tidak ditemukan. |
| 15626043 | `_unsorted/...p02_15626043_01.zip__p02_15626043_01.py` | soal1.py (pilah) | Prefix P02, tapi isinya soal1 M3 (saldo awal, transaksi, "Saldo Tuan Mik"). Ada 3 salinan di `_unsorted` (zip bersarang) dengan md5 sama persis; yang dipakai salinan pertama, dua lainnya duplikat. |
| 15626043 | `soal2.py` (dari `p03_15626043_02.py`) | tetap soal2.py | Isinya hanya docstring Colab dan header (12 baris), tanpa kode. Deskripsi header tertulis "Menghitung saldo transaksi" (salin dari soal1). Tidak ada versi lain, slot dibiarkan. |
| 15626043 | `soal3.py` (dari `p03_15626043_03ynb.py`) | tetap soal3.py | Hanya docstring dan header "Perhitungan Volume Genangan Air", tanpa kode. Salinan di `_orig` md5-nya sama. |

## Ragu / catatan
- 15626020 soal1: output dan penjelasan yang ditempel tanpa `#` ikut terpotong apa adanya, jadi file kena SyntaxError (karakter `−` U+2212 dan baris output). Kalau asisten mau menilai hanya kodenya, salinan pertama yang bersih ada di baris 10-42 file `_unsorted`.
- 15626020 soal2, soal3 (dan soal1): kode diulang 3 kali (tiap sel Colab satu case). Waktu dijalankan, program meminta input 3 set; TC yang hanya memberi 1 set kemungkinan berakhir EOFError di salinan kedua. Sama seperti pola "3 blok case berulang" di M1/M2, dipotong utuh.
- 15626028 soal2: baris `Input persentase trailing stop` (baris 6 di soal2.py) tidak diberi `#` oleh praktikan, jadi SyntaxError. Dibiarkan apa adanya.
- 15626043 soal2 dan soal3: hanya header, tidak ada kode jawaban. Dinilai sebagai kosong/tidak mencoba, kecuali asisten menemukan versi lain.
- Setelah pilah, TC untuk 4 NIM ini perlu dijalankan ulang: `python -I scripts/run_tc.py M3 15626020 15626028 15626030 15626043`.
