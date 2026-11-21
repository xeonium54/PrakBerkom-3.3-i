# NIM/Nama: 15626040/Frizka Yunisaf
# Tanggal: 11 November 2026
# Deskripsi: Menyederhanakan aspek rasio foto.

def FPB(a,b):
    while (b !=0):
        sisa = a % b
        a = b
        b = sisa
    return a

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggai foto (piksel): "))
f = FPB(lebar, tinggi)

print ("Aspect ratio disederhanakan menjadi " + str(lebar//f) + ":" + str(tinggi//f))
