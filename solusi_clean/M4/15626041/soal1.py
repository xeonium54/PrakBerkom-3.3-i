# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 11 November 2026
# Deskripsi : Menyederhanakan rasio foto

def fpb(a,b):
    while b!=0:
        sisa  = a % b 
        a = b 
        b = sisa
    return a

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

pembagi = fpb(lebar, tinggi)
print(f"Aspect ratio foto adalah {str(lebar//pembagi)} : {str(tinggi//pembagi)} ")