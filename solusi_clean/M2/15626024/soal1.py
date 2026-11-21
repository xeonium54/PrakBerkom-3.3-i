# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 14 October 2026
# Deskripsi : Program yang mengecek nilai yang diinput apakah valid atau tidak

# Kamus
# S (int) = merupakan skor yang akan diinput

# Algoritma
S = int(input("Masukkan skor: "))

if 0 <= S <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")