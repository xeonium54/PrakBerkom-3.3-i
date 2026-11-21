#Nama : Febrian Yaif Hakim
#NIM : 15626042
#Tanggal: 11 Nov 2026

#Problem 1
def cari_fpb(a, b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

lebar= int(input("Masukin lebar foto (pixel): "))
tinggi= int(input("Masukkan tinggi foto (pixel): "))

fpb = cari_fpb(lebar, tinggi)

rasio_lebar = lebar//fpb
rasio_tinggi = tinggi//fpb

print(f"aspect rasio dosederhanakan menjadi {rasio_lebar}:{rasio_tinggi}")