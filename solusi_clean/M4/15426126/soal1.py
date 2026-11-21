# NIM/Nama : 15426126/Zhahiran Kayyis
# Tanggal  : 11 November 2026
# Deskripsi: Program untuk menyederhanakan aspect ratio foto menggunakan FPB.

def hitung_fpb(a, b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a


# Program utama
lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

fpb = hitung_fpb(lebar, tinggi)

rasio_lebar = lebar // fpb
rasio_tinggi = tinggi // fpb

print("Aspect ratio disederhanakan menjadi", str(rasio_lebar) + ":" + str(rasio_tinggi))