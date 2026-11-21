 
# NIM/Nama : 15626001 / Muhamad Naufal Al Fajri
# Tanggal : 11 November  2026
# Deskripsi :

a = int(input("Masukkan lebar foto (piksel):"))
b = int(input("Masukkan tinggi foto (piksel):"))
def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("Aspect ratio disederhanakan mejadi ", fpb)