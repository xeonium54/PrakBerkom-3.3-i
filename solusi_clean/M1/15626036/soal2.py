# NIM/ Nama : Aghneo Amar Ahsan
# Tanggal : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir larutan dengan memanfaatkan 3 inputan konsentrasi dan 3 inputan volume

# Kamus : 
# c1, c2, c3, v1, v2, v3 : integer
# C_akhir : float
c1 = int(input("Masukkan konsentrasi larutan pertama (persen) : "))
v1 = int(input("Masukkan volume larutan pertama (ml) : "))
c2 = int(input("Masukkan konsentrasi larutan kedua (persen) : "))
v2 = int(input("Masukkan volume larutan kedua (ml) : "))
c3 = int(input("Masukkan konsentrasi larutan ketiga (persen) : "))
v3 = int(input("Masukkan volume larutan ketiga (ml) : "))

C_akhir = float(((c1*v1)+(c2*v2)+(c3*v3))/(v1+v2+v3))

print("Konsentrasi akhir larutan campuran adalah :", C_akhir, "persen")