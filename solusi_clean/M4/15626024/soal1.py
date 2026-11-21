# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 11 November 2026
# Deskripsi : 

def FPB(a, b):
    # Kamus Lokal
    # sisa (float)

    # Algoritma
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

# Algoritma program utama
lebar = int(input("Masukkan lebar foto (pixel): "))
tinggi = int(input("Masukka  tinggi foto (pixel): "))
hitungFPB = FPB(lebar, tinggi)
rasio_lebar = lebar // hitungFPB
rasio_tinggi = tinggi // hitungFPB

print(f"Aspect ratio disederhanakan menjadi {rasio_lebar}:{rasio_tinggi}")