# NIM = 15626033
# Tanggal = 14 oktober 2026
# deskripsi = memvalidasi skor ujian

skor = int(input("masukkan skor: "))
if 0 <= 100:
    print("skor valid, dapat diinput ke sistem.")
else:
    print("skor tidak valid, perlu diperiksa ulang.")