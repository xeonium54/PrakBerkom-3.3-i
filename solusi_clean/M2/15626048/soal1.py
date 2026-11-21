# Nim: 15626048
# Tanggal: 14 Oktober 2026
# Deskripsi: Program Analisis Kasus Percabangan

# Program memvalidasi skor ujian

# Kamus
# n: int

# Algoritma
skor = int(input("Masukan n:"))

if 1<= skor <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")


