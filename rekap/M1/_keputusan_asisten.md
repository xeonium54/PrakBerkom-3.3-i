# Keputusan asisten M1 (2026-11-21)

Keputusan untuk kasus yang tidak tercakup di rules/rules_penilaian.md. Berlaku untuk modul M1.

1. **Kiriman berupa salinan sesi IDLE/REPL** (ada `>>>`, `...` dan baris output; contoh 15626008 s1-s3, 15626046 s1-s3):
   - `compile` tetap 0 (file asli SyntaxError).
   - Untuk TC: buat salinan bersih di scratchpad (buang awalan `>>> ` / `... `, buang baris output dan banner), file praktikan tidak diubah. Jalankan `printf '<input>' | python -I <salinan>` dengan input dari `testcase/M1/soalK.json`, lalu nilai TC dari hasilnya sesuai tabel TC.
   - Catat di comments: `sK log REPL, TC dari salinan bersih (keputusan asisten)`.
2. **15626005 soal3** ada di zip `P01_15626003_03_REVISI` (NIM 15626003), header file menulis 15626005: dinilai sebagai milik 15626005, nama file 0. 15626003 tetap "tidak mengumpulkan".
3. **Penalti "File tanpa ekstensi .py" (1.5)**: kiriman `.txt` dan `.ipynb` juga kena 1.5. Dihitung sekali per praktikan. File `.py` yang isinya JSON notebook (15626049) juga kena. File `.txt` yang bukan jawaban (15626013 `Untitled-1.txt`) tidak kena.
4. **TC beda pembulatan sekaligus teks beda**: 0.4.
5. **`abs()` di soal Hard** dianggap fungsi bawaan yang dilarang: penguasaan 0.2.
6. **Total tidak boleh negatif**: penalti dipotong maksimal sebesar nilai (15626020: penalti 0.2, total 0).
