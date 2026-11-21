# Keputusan asisten M4 (2026-11-21)

Keputusan umum dari `rekap/M1/_keputusan_asisten.md` (no 1, 3, 4, 6) dan `rekap/M2/_keputusan_asisten.md` (no 1, 2, 3, 5, 6, 7, 8) juga berlaku untuk M4, atas keputusan asisten.

1. **Soal1 wajib subprogram FPB.** FPB dari `math.gcd` (di dalam `def` atau tidak) dianggap tidak menghitung FPB sendiri: penguasaan 0.2 (15626045, 15626052).
2. **Materi belum diajarkan** di M4: `dict`, `lambda`, `sorted(key=...)`: penguasaan 0.2. `def`/subprogram wajib, loop, list, rekursi dan `import` lain boleh.
3. **Wajib subprogram tidak dipenuhi** (tanpa `def`, atau soal3 tidak membuat subprogram untuk tiap tindakan dan prediksi nilai): melanggar batasan soal, penguasaan 0.2 (aturan rules_penilaian, bukan aturan baru).
4. **Kode diulang beberapa kali dalam satu file** (satu blok per case, 15626020): TC dinilai dari output blok pertama, sama seperti preseden M2 15626013 dan M3 15626020.
5. **File tanpa kode** (hanya header/komentar, bukan file 0 byte): compile 0.2 karena file bisa dijalankan tanpa error, ikut M2/M3 (15626007, 011, 016, 019, 029, 037, 048 soal3). File 0 byte tetap compile 0.
