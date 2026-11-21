# NIM/Nama : 15626012 / Muhammad Dzaky Nouvaldi
# Tanggal: 30 September 2026
# Deskripsi: Menghitung konsentrasi akhir larutan


# KAMUS
# v : float
# c : float

# Input larutan pertama
c1 = float(input("Masukkan konsentrasi pertama (persen): "))
v1 = float(input("Masukkan volume pertama (ml): "))

# Input larutan kedua
c2 = float(input("Masukkan konsentrasi kedua (persen): "))
v2 = float(input("Masukkan volume kedua (ml): "))

# Input larutan ketiga
c3 = float(input("Masukkan konsentrasi ketiga (persen): "))
v3 = float(input("Masukkan volume ketiga (ml): "))


# Menghitung konsentrasi akhir 
c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)

# output konsentrasi akhir
print("Konsentrasi dari larutan campuran tersebut adalah: ", c_akhir)