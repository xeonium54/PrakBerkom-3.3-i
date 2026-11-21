# NIM/Nama  : 15626047/Jeremia Arista Matthew Sugiarto
# Tanggal   : 11 November 2026
# Deskripsi : Program menyederhanakan aspek ratio foto

#Kamus
lebar=int
tinggi=int

#Bikin fpb
def fpb(a,b):
    while b !=0:
        a, b = b, a % b
    return a

#Algoritma Utama
lebar=int(input("Masukkan lebar foto (piksel):"))
tinggi=int(input("Masukkan tinggi foto (piksel):"))
faktor=fpb(lebar, tinggi)
r_lebar=lebar//faktor
r_tinggi=tinggi//faktor

print (f"Aspect ratio disederhanakan menjadi {r_lebar}:{r_tinggi}")