# NIM = 15626033
# Nama = Farah Ghiza HUmairoh 
# Tanggal = 11 nov 2026
# Deskripsi = faktor persekutuan terbesar (FPB)
# Kamus = 1. a : integer, b : integer, lebar : integer, tinggi : integer, f : integer


def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a
lebar = int(input("masukkan lebar foto (piksel): "))
tinggi = int(input("masukkan tinggi foto (piksel): "))
f = hitung_fpb(lebar, tinggi)

lebar_rasio = lebar // f
tinggi_rasio = tinggi // f

print(f"Aspect ratio foto tersebut adalah {lebar_rasio}:{tinggi_rasio}")