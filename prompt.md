# Repository Penilaian Praktikum Berpikir Komputasional

Prompt siap tempel ke Claude Code di root repo ini. Ganti `M1` / NIM sesuai kebutuhan.

## A. Periksa satu modul penuh
```
Periksa modul M1 mengikuti alur_periksa.md dari langkah 1 sampai 6.
- Langkah 2 (pilah _unsorted) dan 5 (penilaian) kerjakan dengan sub-agent, sekitar 15 NIM per sub-agent, sesuai aturan di CLAUDE.md.
- Kalau extract atau rekap init sudah pernah dijalankan untuk modul ini, jangan pakai --force. Lanjutkan dari hasil yang ada.
- Berhenti dan tanya saya kalau ada keputusan yang tidak tercakup di rules/rules_penilaian.md.
Di akhir, berikan laporan sesuai langkah 6.
```

## A2. Uji coba dulu dengan sedikit NIM
```
Jalankan alur_periksa.md untuk modul M1, tapi langkah 5 hanya untuk NIM 15426125, 15426126, 15426129, tanpa sub-agent.
Tunjukkan baris nilai.csv dan catatan/<NIM>.md mereka. Jangan isi NIM lain.
```

## B. Periksa ulang satu praktikan
```
Praktikan NIM 15626008 modul M1 keberatan dengan nilainya. Baca rekap/M1/catatan/15626008.md, cek ulang kodenya
(solusi_clean/M1/15626008/, termasuk _orig dan _unsorted) dan hasil TC-nya. Jalankan ulang TC kalau perlu.
Jelaskan setiap perubahan nilai beserta alasannya, lalu update nilai.csv dan catatannya. Terakhir jalankan rekap.py M1 check.
```

## C. Bangun karakteristik AI dari solusi referensi
Siapkan dulu solusi buatan AI: tiap model (gemini, claude, chatgpt) mengerjakan soal yang sama dengan prompt "kamu mahasiswa
semester 1, kerjakan soal ini dengan Python" (atau variasinya). Simpan di `ref/M#/<model>/soalK.py`.
```
Baca semua solusi di ref/ dan bandingkan dengan solusi praktikan di solusi_clean/ untuk modul yang sama.
Cari pola yang sering muncul di solusi AI tapi jarang di solusi praktikan: gaya komentar, penamaan, struktur,
fitur Python, cara format output. Perbarui rules/karakteristik_ai.md: tambah atau ubah tanda, beri contoh cuplikan
dari ref/, dan pindahkan tanda yang ternyata umum di solusi praktikan ke bagian "Bukan tanda AI".
Jangan mengubah bagian level dan aturan bukti.
```

## D. Sanity check rekap
```
Baca rekap/M1/nilai.csv dan hasil_tc.csv. Cari yang janggal: TC PASS tapi nilai TC < 0.6, nilai penguasaan 0.6 padahal
semua TC gagal, flag AI tanpa bukti, praktikan tidak mengumpulkan tapi nilainya > 0, comments kosong padahal nilai
di bawah maksimum. Laporkan dalam tabel, jangan mengubah apa pun.
```

## E. Tambah modul / kelas baru
```
Ada modul baru M5: soal di soal_praktikum/M5.pdf, zip di solusi_raw/M5, testcase di testcase/tc_raw_5.md,
template di rekap/M5. Tambahkan pick untuk Modul 5 ke pick.md (tanya saya nomornya), konversi PDF dengan doc2md,
jalankan build_tc.py M5, lalu cek apakah ada PERINGATAN parse. Tambahkan batasan soal M5 ke tabel Penguasaan Modul
di rules/rules_penilaian.md sebagai usulan yang saya review.
```
