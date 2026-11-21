def hitung_fpb(a, b):
    fpb = 1
    if a < b:
        terkecil = a
    else:
        terkceil = b
    for i in range(1, terkecil + 1):
        if (a % i == 0) and (b % i == 0):
            fpb = i
    return fpb
lebar = int(input("Masukkan lebar foto (piksel):"))
tinggi = int(input("Masukkan tinggi foto (piksel):"))
fpb = hitung_fpb(lebar, tinggi)

rasio_lebar = lebar // fpb
rasio_tinggi = tinggi // fpb
print(f"Aspect ratio disederhanakan menjadi {rasio_lebar}:{rasio_tinggi}")