# NIM       : 15426129
# Nama      : Kirani Rizky Aulia Khairunissa
# Tanggal   : Rabu, 30 September 2026
# Deskripsi : Praktikum 1 Berpikir Komputasional (Problem 2)

# PROGRAM Penghitungan Konsentrasi Campuran
# Deskripsi:
# User memasukkan persen konsentrasi dan volume dari larutan pertama, kedua, dan ketiga.
# Sistem melakukan penghitungan konsentrasi akhir yang dihasilkan. 

# KAMUS
# c(i) dengan i = [1, 2, 3] sebagai variabel dari persen konsentrasi larutan pertama, kedua, dan ketiga berturut-turut
# v(i) dengan i = [1, 2, 3] sebagai variabel dari volume larutan pertama, kedua, dan ketiga berturut-turut
# c1: float
# v1 : float
# c2: float
# v2 : float
# c3: float
# v3 : float
# c_akhir = float

# ALGORITMA
print("PROGRAM Penghitungan Konsentrasi Campuran")
print()

c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukkan volume larutan pertama (ml): "))
c2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = float(input("Masukkan volume larutan kedua (ml): "))
c3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = float(input("Masukkan volume larutan ketiga (ml): "))

c_akhir = ((c1 * v1) + (c2 * v2) + (c3 * v3)) / (v1 + v2 + v3)
print("Konsentrasi akhir larutan campuran adalah", c_akhir, "persen.")
print()