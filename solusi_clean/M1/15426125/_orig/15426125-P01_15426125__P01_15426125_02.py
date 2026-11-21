#menghitung konsentrasi akgir

#Input data larutan pertama
c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukkan volume larutan pertama (ml): "))
#Input data larutan kedua
c2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = float(input("Masukkan volume larutan kedua (ml): "))
#Input data larutan ketiga
c3 = float(input("Masukkan konsentrasi lautan ketiga (persen): "))
v3 = float(input("Masukkan volume larutan ketiga (ml): "))
#menghitung konsentrasi akhir
c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)
#Tampilan akhir
print(f"Konsentrasi akhir larutan campuran adalah {c_akhir}")