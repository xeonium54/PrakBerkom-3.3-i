# Nama: Kirani Rizky Aulia Khairunissa
# NIM: 15426129
# Tanggal: Rabu, 11 November 2026

# PROGRAM MenghitungAspectRatioFoto
# Deskripsi: User memasukkan lebar dan tinggi foto dalam piksel, lalu sistem menghitung aspek rasio yang paling sederhana

# KAMUS
# lebar : int
# tinggi : int
# r_lebar : int
# r_tinggi : int

# ALGORITMA
print("PROGRAM MenghitungAspectRatioFoto")
print()

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

def HitungRasio(lebar, tinggi):
    while lebar % 5 == 0 and tinggi % 5 == 0:
        lebar = lebar / 5
        tinggi = tinggi / 5
    while lebar % 4 == 0 and tinggi % 4 == 0:
        lebar = lebar / 4
        tinggi = tinggi / 4 
    while lebar % 3 == 0 and tinggi % 3 == 0:
        lebar = lebar / 3
        tinggi = tinggi / 3
    while lebar % 2 == 0 and tinggi % 2 == 0:
        lebar = lebar / 2
        tinggi = tinggi / 2
        return lebar and tinggi

HitungRasio(lebar, tinggi)
r_lebar = lebar
r_tinggi = tinggi

print("Aspect ratio yang disederhanakan menjadi " + str(r_lebar) + ":" + str(r_tinggi))