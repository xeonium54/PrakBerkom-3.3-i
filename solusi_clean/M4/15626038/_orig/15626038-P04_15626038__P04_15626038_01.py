# NIM/Nama : 15626038/Keysha Hana Putri
# Tanggal : Rabu, 11/11/2026
# Deskripsi : Program ini digunakan untuk menyederhanakan aspect ratio foto.

#KAMUS
# l,t,rasio : int

#ALGORITMA
def fpb(l, t):
    #Masukkan fungsi untuk menghitung FPB

l = int(input("Masukkan lebar foto (piksel): "))
t = int(input("Masukkan tinggi foto (piksel): "))
fpb_l = fpb(l)
fpb_t = fpb(t)

print("Aspect ratio disederhanakan menjadi " + str(fpb_l) + ":" + str(fpb_t))