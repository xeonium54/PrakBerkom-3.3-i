# NIM/Nama : Arya Satya Anggara
# Tanggal : 11 November 2026
# Deskripsi : Program ini untuk menyederhanakan aspect ratio foto dengan menghitung fpb dari lebar dan tinggi foto, kemudian membagi keduanya dengan nilai fpb tersebut

def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a


lebar = int(input("masukan lebar foto (piksel): "))
tinggi = int(input("masukan tinggi foto (piksel): "))

fpb = fpb(lebar, tinggi)

lebar = lebar // fpb
tinggi = tinggi // fpb

print("aspect ratio disederhanakan menjadi", str(lebar) + ":" + str(tinggi))
