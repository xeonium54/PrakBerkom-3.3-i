Nama / NIM : Muthi'ah Azka Niamillah / 15626026
Tanggal : Rabu, 11 November 2026
Deskripsi : Soal 1

def hitung_fpb(a, b):
    while b ! = 0:
        sisa = a % b
        a = b
        b = sisa

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masaukkan tinggi foto (piksel): "))

fpb = hitung_fpb(lebar, tinggi)

rasio_lebar = lebar // fpb
rasio_tinggi = tinggi // fpb

print("Aspect ratio disederhanakan menjadi", rasio_lebar, ":", rasio_tinggi, ")