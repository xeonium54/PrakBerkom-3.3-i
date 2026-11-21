# NIM/Nama : muhammad rizky wibowo
# Tanggal : 11/11/26
# Deskripsi : praktikum berkom 4 nomor 3

n = float(input("Masukkan waktu sebelum UAS: "))

t1 = float(input("Waktu modul 1: "))
t2 = float(input("Waktu modul 2: "))
t3 = float(input("Waktu modul 3: "))
t4 = float(input("Waktu modul 4: "))

T1 = 0
T2 = 0
T3 = 0
T4 = 0

energi = 100
sisa = n

while sisa > 0:
    print("1. Belajar")
    print("2. Tidur")

    pilih = int(input("Pilih kegiatan: "))
    if pilih == 1:
        modul = int(input("Pilih modul (1-4): "))
        jam = float(input("Lama belajar: "))

        if jam > sisa:
            print("Waktu tidak cukup")
        elif jam * 5 > energi:
            print("Energi tidak cukup")
        else:
            if modul == 1:
                T1 += jam
            elif modul == 2:
                T2 += jam
            elif modul == 3:
                T3 += jam
            elif modul == 4:
                T4 += jam

                elif pilih == 2:
        energi = energi + (sisa * 12.5)

        if energi > 100:
            energi = 100

        sisa = 0
