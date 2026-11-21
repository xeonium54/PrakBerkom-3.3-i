# Pilah `_unsorted` M4

Soal kelas ini: soal1 = aspect ratio foto dengan subprogram FPB (Easy no 4), soal2 = skor dan kategori N kandidat PIN (Medium no 11), soal3 = Tuan Ky Sistem Kebut Semalam (Hard no 8).
`_orig/`, `_unsorted/` dan `solusi_raw/` tidak disentuh. Salinan pakai `cp` atau potongan baris persis (`sed -n a,bp`, tanpa mengubah isi).
**Nama file = 0** untuk setiap slot hasil pilah, yaitu slot yang ditandai (pilah) di tabel.

Bagian NIM 15626007, 15626020, 15626028, 15626029, 15626033.

| NIM | file | ditaruh ke | alasan |
|---|---|---|---|
| 15626007 | `soal1.py` (dari `Praktikum 4/P04_15626007_01/..._01_Case 1.py`) | tetap soal1.py | Isinya aspect ratio dengan `def fpb`. Folder `_01`/`_02`/`_03` = nomor soal, `Case 1..3` = salinan per testcase. Case 2 dan 3 folder `_01` isinya sama (md5 sama), beda dari Case 1 hanya baris kosong di awal. |
| 15626007 | `_unsorted/..._02__P04_15626007_02_Case 1.py` | soal2.py (pilah) | Slot soal2 sebelumnya berisi `_01_Case 2` (aspect ratio lagi, soal salah). Ditukar dengan isi folder `_02` = skor PIN dan rekap kategori. Case 1 dipakai agar sejalan dengan soal1; Case 2 dan 3 sama persis satu sama lain dan hanya beda komentar dengan Case 1. |
| 15626007 | `_unsorted/..._03__P04_15626007_03_Case 1.py` | soal3.py (pilah) | Slot soal3 sebelumnya berisi `_01_Case 3` (aspect ratio). Diganti dengan isi folder `_03`: header "Simulasi Tuan MIk ... H-1 UAS" dan komentar "Jujur Bingung Kak", tanpa kode. |
| 15626020 | `_unsorted/15626020-P04_15626020.ZIP__p04_15626020_zip.py` baris 1-75 | soal1.py (pilah) | Aspect ratio dengan `def fpb`. Termasuk docstring Colab dan header (baris 1-12). Kode diulang 3 kali (header "Problem 1", "Tes Case 2", "Test Case 3"), ketiga salinan identik. |
| 15626020 | file yang sama, baris 76-279 | soal2.py (pilah) | Skor PIN dan rekap, mulai dari header "Problem 2". Kode diulang 3 kali, identik. |
| 15626020 | file yang sama, baris 280-akhir (595) | soal3.py (pilah) | Tuan Ky (sisa waktu, 4 modul, belajar/tidur, prediksi UAS), mulai dari header "Problem 3". Kode diulang 3 kali. Baris terakhir (595) tidak berakhiran newline, ikut terpotong. |
| 15626028 | `_unsorted/15626028-P04_15626028.zip__untitled9.py` baris 1-34 | soal1.py (pilah) | Aspect ratio dengan `def hitung_fpb`. Termasuk docstring Colab, penanda "Problem 1" ada di dalam docstring. |
| 15626028 | file yang sama, baris 35-110 | soal2.py (pilah) | Skor PIN dan rekap, mulai dari `"""Problem 2"""`. |
| 15626028 | file yang sama, baris 111-203 | soal3.py (pilah) | Tuan Ky, mulai dari `"""Problem 3"""`. |
| 15626029 | `soal1.py` (dari `#P04_15626029_01.py`) | tetap soal1.py | Header "aspect ratio foto", isinya hanya 2 baris `input(int())`. Slot sudah benar. |
| 15626029 | `soal2.py` (dari `#P04_15626029_02.py`) | tetap soal2.py | Header "skor pin", kode belum selesai. Slot sudah benar. |
| 15626029 | `_unsorted/15626029-#P04_15626029_02__#P04_15626209.py` | soal3.py (pilah) | Nama file salah ketik NIM (`15626209`), tapi baris 1 `#P04_15626209_03` dan komentar "Tuan Ky ikut UP aja" menunjuk soal3. Isinya hanya komentar, tanpa kode. Di-`cp` utuh. |
| 15626033 | `soal1.py`, `soal2.py` | tetap | soal1 = aspect ratio dengan `hitung_fpb`, soal2 = skor PIN. Slot sudah benar. |
| 15626033 | `_unsorted/15626033-P04_15626033_01  (2)__P04_15626033_03(2).py` | soal3.py (pilah) | Deskripsi "pendekatan simulasi SKS", fungsi tidur/belajar/prediksi nilai UAS = soal3. Di extract masuk `_unsorted` karena bentrok dengan `_02`. Di-`cp` utuh. |

## Ragu / catatan
- 15626020 soal1, soal2, soal3: kode diulang 3 kali (tiap sel Colab satu case), sama dengan pola M3 NIM ini. Program meminta input 3 set; TC yang memberi 1 set kemungkinan berakhir EOFError di salinan kedua. Dipotong utuh. Kalau asisten mau menilai satu salinan saja: soal1 baris 10-31, soal2 baris 76-142, soal3 baris 280-385 file `_unsorted`.
- 15626020 soal3: salinan ketiga (baris 492-595) tidak punya baris kosong + `print("Prediksi ...")` di tempat yang sama; `print` terakhirnya menempel di baris 595 tanpa newline. Dibiarkan apa adanya.
- 15626028 soal2: `jalankan_program()` tidak pernah dipanggil (baris 109 hanya komentar "# Pemanggilan subprogram utama"), jadi soal2.py tidak meminta input dan tidak mencetak apa pun. Bukan salah potong; di file asli memang begitu.
- 15626007 soal2: Case 1 dan Case 2/3 hanya beda teks komentar, kodenya sama. Pilihan Case 1 tidak mengubah hasil TC.
- 15626033 soal3: file hanya berisi 3 fungsi, tanpa program utama, jadi tidak ada input/output (TC FAIL dengan output kosong). Tidak ada versi lain di `_orig`.
- 15626007 dan 15626029 soal3: hanya header/komentar, tidak ada kode jawaban. Dinilai sebagai kosong/tidak mencoba, kecuali asisten menemukan versi lain.
- Setelah pilah, TC untuk 5 NIM ini dijalankan ulang: `python -I scripts/run_tc.py M4 15626007 15626020 15626028 15626029 15626033`.
