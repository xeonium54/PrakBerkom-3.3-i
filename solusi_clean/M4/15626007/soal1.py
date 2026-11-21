# NIM/Nama : 15626007 / Ryssad Sabralnair
# Tanggal : 11 November 2026
# Deskripsi : Mensederhanakan Aspect Ratio Foto

lebar = int(input("Masukkan lebar foto (pixel): "))
tinggi = int(input("Masukkan tinggi foto (pixel): "))

#Subprogram untuk menghitung FPB
def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Menghitung aspect ratio yang tersederhana
fpb = fpb(lebar, tinggi)
aspect_ratio_lebar = lebar // fpb
aspect_ratio_tinggi = tinggi // fpb

print("Aspect ratio foto yang tersederhana:", aspect_ratio_lebar, ":", aspect_ratio_tinggi)