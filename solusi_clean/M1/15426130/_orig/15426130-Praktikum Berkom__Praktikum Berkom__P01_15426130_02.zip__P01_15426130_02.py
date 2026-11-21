#NIM/Nama  : 15426130/ Yudha Putra
#Tanggal   : 30 September 2027
#Deskripsi : Menghitung Konsentrasi Akhir Campuran Larutan

c1 = float(input("Masukkan Konsentrasi Larutan Pertama (persen): "))
v1 = float(input("Masukkan volume larutan pertama (ml): "))
c2 = float(input("Masukkan Konsentrasi Larutan Kedua (persen): "))
v2 = float(input("Masukkan volume larutan Kedua (ml): "))
c3 = float(input("Masukkan Konsentrasi Larutan Ketiga (persen): "))
v3 = float(input("Masukkan volume larutan Kedua (ml): "))

c_akhir = (c1*v1+c2*v2+c3*v3)/(v1+v2+v3)

print(f"Konsentrasi akhir larutan campuran adalah {c_akhir:.2f} persen")