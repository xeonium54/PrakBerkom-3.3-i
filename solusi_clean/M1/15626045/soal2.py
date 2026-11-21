# Program Menghitung Konsentrasi Larutan Campuran
# Deskripsi: Menghitung konsentrasi akhir dari larutan campuran dari tiga larutan berdasarkan volume (v) dalam ml dan konsentrasi (c) dalam persen

# KAMUS
# c1 : int
# v1 : int
# c2 : int
# v2 : int
# c3 : int
# v3 : int
# konsentrasi_akhir : float

# ALGORITMA
c1 = int(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = int(input("Masukkan volume larutan pertama (ml): "))
c2 = int(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = int(input("Masukkan volume larutan kedua (ml): "))
c3 = int(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = int(input("Masukkan volume larutan ketiga (ml): "))

konsentrasi_akhir = ((c1*v1)+(c2*v2)+(c3*v3))/(v1+v2+v3)

print("Konsentrasi akhir larutan campuran adalah", konsentrasi_akhir, "persen")
