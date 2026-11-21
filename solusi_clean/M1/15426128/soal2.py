#Kamus
#c1, c2, c3 :float (Konsentrasi volume larutan dalam persen)
#v1, v2, v3 :float (Volume larutan dalam Militer)
# c_akhir = ((c1*v1) + (c2*v2) + (c3*v3)) / (c1 + c2 + c3) {Rumus untuk mencari c akhir}

v1 = float(input("Masukkan volume larutan 1 (persen): "))
c1 = float(input("Masukkan konsentrasi larutan 1 (ml): "))

v2 = float(input("Masukkan volume larutan 2 (persen): "))
c2 = float(input("Masukkan konsentrasi larutan 2 (ml): "))

v3 = float(input("Masukkan volume larutan 3 (persen): "))
c3 = float(input("Masukkan konsentrasi larutan 3 (ml): "))

c_akhir = ((c1*v1) + (c2*v2) + (c3*v3)) / (c1 + c2 + c3)

print(f"Konsentrasi akhir larutan campuran adalah: {c_akhir: .2f} %")
