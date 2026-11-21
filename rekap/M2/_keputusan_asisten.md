# Keputusan asisten M2 (2026-11-21)

Keputusan umum dari `rekap/M1/_keputusan_asisten.md` (no 1, 3, 4, 5, 6) juga berlaku untuk M2, atas keputusan asisten. No 2 di M1 khusus satu NIM, tidak dipakai.

1. **Kiriman berupa salinan sesi IDLE/REPL** (ada `>>>`, `...` dan baris output):
   - `compile` tetap 0 (file asli SyntaxError).
   - Untuk TC: buat salinan bersih di scratchpad (buang awalan `>>> ` / `... `, buang baris output dan banner), file praktikan tidak diubah. Jalankan `printf '<input>' | python -I <salinan>` dengan input dari `testcase/M2/soalK.json`, lalu nilai TC dari hasilnya sesuai tabel TC.
   - Catat di comments: `sK log REPL, TC dari salinan bersih (keputusan asisten)`.
2. **Penalti "File tanpa ekstensi .py" (1.5)**: kiriman `.txt` dan `.ipynb` juga kena 1.5. Dihitung sekali per praktikan. File `.py` yang isinya JSON notebook juga kena. File `.txt` yang bukan jawaban tidak kena.
3. **TC beda pembulatan sekaligus teks beda**: 0.4.
4. **`abs()` di soal Hard (soal3)**: dilarang oleh catatan soal ("Dilarang menggunakan fungsi abs()"), penguasaan 0.2. Soal 1 dan 2 M2 tidak melarang `abs()`.
5. **Total tidak boleh negatif**: penalti dipotong maksimal sebesar nilai.
6. **Output benar lalu crash** (hasil sudah tercetak, lalu NameError dsb.): TC dinilai dari output yang tercetak sesuai tabel TC (0.6 kalau persis, 0.4 kalau teks beda). Crash-nya mengurangi penguasaan.
7. **Penalti bertumpuk**: nama zip salah (0.5) dan file tanpa `.py` (1.5) dijumlah jadi 2.0 (15626035, 15626044, 15626052).
8. **Format input beda dari soal** (angka untuk y/n, `Ya/Tidak`, jenis kereta huruf kecil, urutan input beda): bukan cara input wajar, TC tetap 0 (15626022, 15626041, 15626048, 15626052).
9. **Materi belum diajarkan** (dict, `def`/`__main__`, `range`): penguasaan 0.2.
