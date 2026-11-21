# NIM / Nama : 15626006/Maria Zeysta Kamelia Rumanti
# Tanggal : 11 November 2026
# Deskripsi : Program untuk menyederhanakan aspek rasio photo.

def hitung_FPB(a, b):
    while b != 0:
        a, b = b, a % b
    return a

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

FPB = hitung_FPB (lebar, tinggi)

rasio_lebar = lebar // FPB
rasio_tinggi = tinggi // FPB

print(f"Aspect rasio disederhanakan menjadi {rasio_lebar}:{rasio_tinggi}")