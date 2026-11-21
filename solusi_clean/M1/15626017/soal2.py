# NIM/Nama  : 15626017 / Naura Vira Vania Ramadhani 
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir dari campuran tiga larutan

# KAMUS
# c1      : float (konsentrasi larutan pertama dalam persen)
# v1      : float (volume larutan pertama dalam ml)
# c2      : float (konsentrasi larutan kedua dalam persen)
# v2      : float (volume larutan kedua dalam ml)
# c3      : float (konsentrasi larutan ketiga dalam persen)
# v3      : float (volume larutan ketiga dalam ml)
# c_akhir : float (konsentrasi akhir larutan campuran)

# Input data 
c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukkan volume larutan pertama (ml): "))

c2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = float(input("Masukkan volume larutan kedua (ml): "))

c3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = float(input("Masukkan volume larutan ketiga (ml): "))

# Menghitung konsentrasi akhir sesuai rumus:
# C_akhir = (C1*V1 + C2*V2 + C3*V3) / (V1 + V2 + V3)
c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)

print(f"Konsentrasi akhir larutan campuran adalah {c_akhir:g} persen")