# Rules Penilaian

Sumber rubrik: sheet `NILAI` di `rekap/M#/*.xlsx`. Sumber aturan praktikum: bagian "Petunjuk" di `soal_praktikum/M#.pdf.md`.
Bagian bertanda **TODO(asisten)** wajib diisi asisten. Selama masih TODO, agent memakai nilai **usulan** yang tertulis, lalu mencatat "pakai aturan usulan" di kolom `comments`.

## Rubrik per soal (maks 4.0 per soal, 3 soal = 12.0)

| Kolom CSV | Kolom xlsx | Maks | Diisi oleh |
|---|---|---|---|
| `sK_header` | Header program | 0.2 | agent |
| `sK_nama_file` | Nama file sesuai format | 0.2 | script (`_log.csv`), agent koreksi |
| `sK_indentasi` | Penggunaan indentasi | 0.2 | agent |
| `sK_komentar` | Penggunaan komentar | 0.2 | agent |
| `sK_compile` | Compile | 0.2 | script (`hasil_tc.csv`) |
| `sK_penguasaan` | Penguasaan Modul | 0.6 | agent |
| `sK_tc2`..`sK_tc5` | TC 2..TC 5 | 0.6 masing-masing | script (PASS), agent (selain PASS) |
| `penalti` | Penalti | 4.0 | agent sesuai bagian Penalti |

Soal 1 = Easy, Soal 2 = Medium, Soal 3 = Hard. Nomor soal ada di `testcase/pick.md`. TC 1 adalah contoh di PDF dan tidak dinilai.

## Cara menilai tiap kolom

### Header (0.2)
Format wajib dari PDF:
```
# NIM/Nama :
# Tanggal :
# Deskripsi :
```
- 0.2: tiga baris ada dan terisi (format boleh sedikit beda, mis. docstring atau `#NIM :` dan `#Nama :` terpisah).
- 0.1: ada tapi kurang satu atau dua, atau ada yang kosong.
- 0: tidak ada header.
- header di docstring Colab dihitung kalau isinya lengkap

### Nama file (0.2)
Format: file `P0m_NIM_0k.py` di dalam `P0m_NIM.zip` (m = modul, k = nomor soal).
- 0.2: `nama_file_ok = True` di `solusi_clean/M#/_log.csv`.
- 0: selain itu.
- **TODO(asisten):** apakah nama zip yang salah ikut mengurangi nilai ini, atau masuk penalti? Apakah salah kecil (`PO1` pakai huruf O, `P01-NIM.01.py`) dapat 0.1? (usulan: zip salah tidak mengurangi; salah kecil 0.1)

### Indentasi (0.2)
Python menolak indentasi yang salah, jadi nilai ini soal kerapian.
- 0.2: konsisten (4 spasi atau tab, tidak campur), blok mudah dibaca.
- 0.1: tidak konsisten (campur 2/4/8 spasi), baris kosong berantakan.
- 0: file tidak bisa dibaca atau kosong.

### Komentar (0.2)
PDF minta komentar untuk kegunaan variabel, percabangan, pengulangan, fungsi dan prosedur.
- 0.2: bagian penting diberi komentar yang menjelaskan maksud.
- 0.1: komentar sedikit atau cuma mengulang kode (`# print hasil`).
- 0: tidak ada komentar selain header.

### Compile (0.2)
- 0.2: `compile = OK` di `hasil_tc.csv`.
- 0: SyntaxError atau file kosong.
- Runtime error (mis. `int("0.5")`) tidak mengurangi kolom ini; yang turun nilai TC-nya.

### Penguasaan Modul (0.6)
Baca soal dan "Catatan" di `soal_praktikum/M#.pdf.md`, lalu baca kodenya.

| Modul | Materi | Batasan yang sudah ada di soal kelas ini |
|---|---|---|
| M1 | Struktur Dasar Program | Hard: tanpa if-else, tanpa `max()`/`min()`, format `.2f` |
| M2 | Analisis Kasus (Percabangan) | dilarang `abs()` (cek soal yang relevan) |
| M3 | Pengulangan dan Array | dilarang `max()`/`min()`, input array dengan `input().split()` |
| M4 | Subprogram | wajib subprogram sesuai catatan soal, dilarang `max`/`min` |

- 0.6: logika benar, memakai materi modul, mematuhi batasan.
- 0.2: logika sebagian benar, atau melanggar satu batasan (mis. pakai `max()` padahal dilarang), atau pakai materi yang belum diajarkan.
- 0: tidak mencoba, kode tidak berhubungan dengan soal, atau hardcode output.

### TC 2–5 (0.6 per TC)
Status dari `rekap/M#/hasil_tc.csv`:

| Status | Usulan nilai | Catatan |
|---|---|---|
| PASS | 0.6 | sudah diisi script |
| NUMOK | 0.4 - 0.5 | angka benar, teks/format beda (kata kurang; spasi; kalau karena trailing zero jadi 0.5, misal `1200.0` vs `1200`) |
| FAIL | 0–0.5 | 0.4 kalau hanya beda pembulatan/jumlah desimal, 0.5 kalau beda pembulatan hanya karena repeating decimal (output 13.33333333334 tapi TC minta 13.33) ; 0 kalau nilainya salah |
| ERROR | 0 | crash; cek dulu apakah gara-gara format input TC (lihat di bawah) |
| TIMEOUT | 0 | biasanya meminta input lebih banyak dari TC atau loop tak berhenti |
| NOFILE | 0 | |

- Sebelum memberi 0 untuk ERROR/TIMEOUT, cek apakah penyebabnya cara input yang masih wajar (mis. soal array tapi praktikan input satu per satu). Kalau masih wajar, jalankan manual dengan input yang disesuaikan dan nilai dari hasilnya. Catat di `comments`.
- `int(input())` untuk input desimal (mis. TC berisi `0.5`) dihitung kesalahan praktikan: ERROR = 0.

## Penalti (maks 4.0, dikurangkan dari total)
- Terlambat tidak perlu ada penalti dulu
- Nama zip salah: 0.5
- File tanpa ekstensi `.py`: 1.5
- Plagiarisme: 2.0
- Indikasi AI: **tidak** memberi penalti. Cukup flag di `comments` (keputusan asisten).

## Kasus khusus
- Tidak mengumpulkan sama sekali: semua 0, `comments = "tidak mengumpulkan"`.
- Satu file berisi beberapa soal: pisahkan ke `soal1.py`..`soal3.py` saat memilah `_unsorted` (lihat alur). Nama file = 0.
- Soal tertukar (file `_02` berisi jawaban soal 3): pindahkan ke slot yang benar. Nama file = 0.
- File `.txt`, `.ipynb` atau tanpa ekstensi yang isinya kode: tetap dinilai. Catat di `comments`.
