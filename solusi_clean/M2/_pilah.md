# Pilah `_unsorted` M2

Soal kelas ini: soal1 = validasi skor 0..100 (Problem 1, no 6), soal2 = tarif parkir (Problem 2, no 10), soal3 = jalur kereta A/B (Problem 3, no 5).
`_orig/`, `_unsorted/` dan `solusi_raw/` tidak disentuh. Salinan pakai `cp` atau potongan baris persis (`sed -n a,bp`, tanpa mengubah isi).
**Nama file = 0** untuk setiap slot hasil pilah, yaitu slot yang ditandai (pilah) di tabel.

Bagian NIM 15626007, 15626009, 15626022, 15626043, 15626044. Pengecekan tanpa hasil: 15626030, 15626032, 15626038.

| NIM | file | ditaruh ke | alasan |
|---|---|---|---|
| 15626007 | `_unsorted/...p02_15626007__ryssad_sabralnair_py.py` baris 1-62 | soal1.py (pilah) | Problem 1: validasi skor 0..100, 3 blok Case berulang. Termasuk header docstring Colab di baris 1-11. |
| 15626007 | file yang sama, baris 63-168 | soal2.py (pilah) | Problem 2: tarif parkir (durasi, mobil listrik, akhir pekan), 3 blok Case. Mulai dari `"""**Problem 2**`. |
| 15626007 | file yang sama, baris 169-420 | soal3.py (pilah) | Problem 3: jalur kereta A/B, 3 blok Case. Mulai dari `"""**Problem 3**`. Gabungan soal1+2+3 sama persis dengan file asli (cmp). |
| 15626009 | `soal1.py` lama (`welcome_to_colab (1).py`, 247 baris) baris 214-226 | soal1.py (pilah, ditimpa) | Slot berisi notebook "Welcome to Colab" (415 KB) dan jawaban ketiga soal ada di baris 214-247. Jawaban soal1 (skor, `N > 0` saja) dipotong. Baris `NAMA : ARDINA` dst. bukan komentar (tidak diberi `#` oleh praktikan), dibiarkan apa adanya. File asli utuh di `_orig/`. |
| 15626009 | file yang sama, baris 228-242 | soal2.py (pilah) | Jawaban soal2 (tarif parkir), tidak lengkap: hanya cek `N > 0` / `N < 0`, tidak ada hitungan tarif. |
| 15626009 | file yang sama, baris 244-247 | soal3.py (pilah) | Soal3 (kereta) hanya 4 baris `print` prompt, tanpa input/logika. Praktis kosong, lihat Ragu. |
| 15626022 | `_unsorted/...p02_15626022_02_py (1).py` | soal2.py (pilah) | Tarif parkir (durasi, mobil listrik, hari). Bentrok nama dengan `_01` yang sudah di soal1 (skor). Format input beda dari soal (mobil listrik dan hari pakai angka 1/2 dan hari 6-7, bukan y/n). |
| 15626043 | `_unsorted/...P02_15626043_02py (1).zip__P02_15626043_02py (1).py` | soal2.py (pilah) | Tarif parkir; header "Problem 2". |
| 15626043 | `_unsorted/...P02_15626043_03 (1).zip__P02_15626043_03 (1).py` | soal3.py (pilah) | Jalur kereta; header "Problem 3". |
| 15626044 | `solusi_raw/M2/15626044-P02.15626044.zip` entri `P02.15626044.01.zip` | soal1.py (pilah) | Zip-nya sebenarnya berisi 3 file teks Python bernama `.zip` (bukan zip bersarang), jadi extract.py melapor "zip rusak". Dibaca langsung dengan zipfile, ditulis tanpa diubah (byte sama). Isi: skor 0..100. |
| 15626044 | entri `P02.15626044.02.zip` | soal2.py (pilah) | Tarif parkir. |
| 15626044 | entri `P03.15626044.03.zip` | soal3.py (pilah) | Jalur kereta. Ada `else:` diikuti komentar lalu `print` tidak menjorok (kemungkinan IndentationError). Dibiarkan. |
| 15626030 | `_orig/...po2_15626030_1_py_.py` | tidak ada tambahan | Hanya satu file (skor), sudah di soal1. Zip mentah juga hanya berisi satu file. Soal2, soal3: tidak ditemukan. |
| 15626032 | `_orig/...P02_15626032_01.py` | tidak ada tambahan | Hanya satu file (skor), sudah di soal1. Soal2, soal3: tidak ditemukan. |
| 15626038 | `_orig/` (`_01`, `_02`) | tidak ada tambahan | soal1 = skor, soal2 = parkir, sudah benar. Soal3: tidak ditemukan (zip mentah hanya 2 file). |
| 15626022 | zip mentah | soal3 tidak ada | Zip hanya berisi `_01` dan `_02`. Soal3: tidak ditemukan. |

## Ragu / catatan
- 15626009: soal3.py hanya 4 baris print, soal2.py tidak menghitung tarif. Dinilai sebagai jawaban yang sangat tidak lengkap, bukan kosong.
- 15626009: soal1.py sebelumnya berisi seluruh notebook Colab. Sekarang diganti potongan jawaban saja, jadi TC dan kolom otomatis perlu dihitung ulang.
- 15626044: NIM di header file tertulis 15662044 (angka tertukar), nama zip 15626044. Dianggap salah ketik praktikan.
