# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 14 Oktober 2026
# Deskripsi : Validasi Skor Ujian

# Masukkan skor
Skor = int(input("Masukkan skor: "))

# Validasi skor
if Skor >= 0 and Skor <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")