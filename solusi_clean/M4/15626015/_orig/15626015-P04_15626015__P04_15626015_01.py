# NIM/Nama : Ken Btari Syahidah
# Tanggal : 11 November 2026
# Deskripsi : Menghitung aspek rasio foto dalam bentuk sederhana.

# KAMUS
# Lebar = int 
# Tinggi = int

# ALGORITMA
def fpb(a, b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

# Program utama
lebar = int(input("Masukkan lebar foto (piksel) : "))
tinggi = int(input("Masukkan tinggi foto (piksel) : "))

hasilfpb = fpb(lebar, tinggi)

rasioL = lebar // hasilfpb
rasioT = tinggi // hasilfpb

print("Aspect ratio disederhanakan menjadi" , str(rasioL) , ":" , str(rasioT) )
    