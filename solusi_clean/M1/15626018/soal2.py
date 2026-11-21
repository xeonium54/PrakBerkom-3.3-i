# NIM / Nama : 15626018 / Chantal Carissa Zuleika
# Tanggal    : 30 September 2026
# Deskripsi  : Menghitung konsentrasi akhir campuran tiga larutan

# Kamus
# C1     : konsentrasi larutan pertama (persen)
# V1     : volume larutan pertama (ml)
# C2     : konsentrasi larutan kedua (persen)
# V2     : volume larutan kedua (ml)
# C3     : konsentrasi larutan ketiga (persen)
# V3     : volume larutan ketiga (ml)
# Cakhir : konsentrasi akhir campuran (persen)

C1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
V1 = float(input("Masukkan volume larutan pertama (ml): "))

C2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
V2 = float(input("Masukkan volume larutan kedua (ml): "))

C3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
V3 = float(input("masukkan volume larutan ketiga (ml): "))

Cakhir = (C1 * V1 + C2 * V2 + C3 * V3) / (V1 + V2 + V3)

print("Konsentrasi akhir larutan campuran adalah", Cakhir, "persen")
