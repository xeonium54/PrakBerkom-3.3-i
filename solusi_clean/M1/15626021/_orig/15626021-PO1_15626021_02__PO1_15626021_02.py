# NIM/Nama  : 15626021 / Aufaa Fakhri Ibrahim Irahadi
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir dari campuran tiga jenis larutan 

# KAMUS VARIABEL
# c1, c2, c3 : float (konsentrasi larutan 1, 2, dan 3 dalam persen)
# v1, v2, v3 : float (volume larutan 1, 2, dan 3 dalam ml)
# c_akhir    : float (konsentrasi akhir larutan campuran dalam persen)

# ALGORITMA
# Input larutan pertama
c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukkan volume larutan pertama (ml): "))

# Input larutan kedua
c2 = float(input("Masukkan konsentrasi laurtan kedua (persen): "))
v2 = float(input("Masukkan volume larutan kedua (ml): "))

# Input larutan ketiga
c3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = float(input("Masukkan volume larutan ketiga (ml): "))

# Perhitungan konsentrasi akhir
c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)

# Output
print(f"Konsentrasi akhir larutan campuran adalah {c_akhir:.1f} persen" if c_akhir * 10 % 10 == 0 else f"Konsentrasi akhir larutan campuran adalah {c_akhir: .2f} persen")
