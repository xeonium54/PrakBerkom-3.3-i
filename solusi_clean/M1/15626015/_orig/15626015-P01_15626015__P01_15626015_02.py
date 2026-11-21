# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 30 September 2026
# Deskripsi : Permasalahan 02, menghitung konsentrasi akhir dari sebuah larutan

# kamus 
# c1 = float = konsentrasi larutan 1 dalam persen
# c2 = float = konsentrasi larutan 2 dalam persen
# c3 = float = konsentrasi larutan 3 dalam persen
# v1 = float = volume larutan 1 dalam mL
# v2 = float = volume larutan 2 dalam mL
# v3 = float = volume larutan 3 dalam mL
# C Akhir = float = konsentrasi akhir larutan dalam persen

c1 = float(input("masukkan konsentrasi larutan pertama (persen)"))
v1 = float(input("masukkan volume larutan pertama (ml)"))
c2 = float(input("masukkan konsentrasi larutan kedua (persen)"))
v2 = float(input("masukkan volume larutan kedua (ml)"))
c3 = float(input("masukkan konsentrasi larutan ketiga (persen)"))
v3 = float(input("masukkan volume larutan ketiga (ml)"))

C_akhir = ((c1 * v1) + (c2 * v2) + (c3 * v3)) / (v1 + v2 + v3)

print("Konsentrasi akhir larutan campuran adalah", C_akhir, "persen")