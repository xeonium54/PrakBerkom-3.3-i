# Nama: Reyza Aulia Rahman
# NIM: 15426131
# Deskripsi: Rasio paling sederhana layar

# lebar

def fpb(x, y):
    while y !=0:
        sisa = x%y
        x = y
        y = sisa
    return x

lebar = int(input("Masukkan lebar foto (piksel):"))
tinggi = int(input("Masukkan tinggi foto (piksel):"))


final = fpb(lebar, tinggi)

leras = lebar // final
tiras = tinggi // final


print(f"Aspect rasio disederhanakan menjadi {leras}:{tiras}")

      