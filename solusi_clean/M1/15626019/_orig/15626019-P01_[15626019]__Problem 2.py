# NIM/Nama : 15626019/Naura Nur Aprilia
# Tanggal : 30-09-2026
# Deskripsi : Menghitung Konsentrasi Akhir dari Larutan Campuran

# KAMUS
# C1 : int
# V1 : int
# C2 : int
# V2 : int
# C3 : int
# V3 : int
# Cakhir : float

# ALGORITMA
C1 = int(input("Masukkan konsentrasi larutan pertama (persen): "))
V1 = int(input("Masukkan volume larutan pertama (ml): "))
C2 = int(input("Masukkan konsentrasi larutan kedua (peresn): "))
V2 = int(input("Masukkan volume larutan kedua (ml): "))
C3 = int(input("Masukkan konsentrasi larutan ketiga (persen): "))
V3 = int(input("Masukkan volume larutan ketiga (ml): "))

Cakhir = ((C1 * V1) + (C2 * V2) + (C3 * V3)) / (V1 + V2 + V3)

print("Konsentrasi akhir larutan campuran adalah", Cakhir, "persen")