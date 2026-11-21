# NIM/Nama : 15616045 / Anindhita Ramya Rahmadani
# Tanggal  : Rabu, 14 Oktober 2026
# Deskripsi: Memvalidasi skor ujian peserta pada rentang 0 hingga 100.

# KAMUS
# skor : float

# ALGORITMA
skor = float(input("Masukkan skor: "))

if (0 <= skor <= 100):
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")
