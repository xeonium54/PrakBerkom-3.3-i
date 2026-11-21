# NIM/Nama :
# Tanggal  :
# Deskripsi:

def fpb(a, b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

lebar = int(input("masukan lebar foto (piksel): "))
tinggi = int(input("masukan tinggi foto (piksel): "))

f = fpb(lebar, tinggi)
hasil_lebar = lebar // f
hasil_tinggi = tinggi // f

print("aspect ratio disederhanakan menjadi" + str(hasil_lebar) + ":"+ str(hasil_tinggi))