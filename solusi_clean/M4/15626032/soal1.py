# NIM/Nama : 15626032/Muhamad Faiz Abdul Aziz
# Tanggal : 11/11/2026
# Deskripsi :

def fpb(a, b):
  while b > 0:
        sisa = a % b
        a = b
        b = sisa
        return a

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

pembagi = fpb(lebar, tinggi)

rasio_lebar = lebar // pembagi
rasio_tinggi = tinggi // pembagi

print("Aspect ratio disederhanakan menjadi " + str(rasio_lebar) + ":" + str(rasio_tinggi))
