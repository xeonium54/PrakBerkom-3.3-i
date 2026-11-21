# NIM/Nama : 15626038 / Keysha Hana Putri
# Tanggal : Rabu, 14 Oktober 2026
# Deskripsi : Porgram ini digunakan untuk memvalidasi skor ujian peserta sebelum diinput ke sistem.

#KAMUS
# skor : int

skor = int(input("Masukkan skor: "))
if skor > 0 and skor <100:
    print("Skor valid , dapat diinput ke sistem.")
else:
    print("Skor tidak valid , perlu diperiksa ulang.")