''''15626033_Farah Ghiza Humairoh'''
'''30 sepetember 2026'''
'''praktikum berkom'''



'''PROBLEM 2'''
c1 = int(input("masukkan konsentrasi larutan pertama (persen): "))
v1 = int(input("masukkan volume larutan pertama (ml): "))
c2 = int(input("masukkan konsentrasi larutan kedua (persen): "))
v2 = int(input("masukkan volume larutan kedua (ml): "))
c3 = int(input("masukkan konsentrasi larutan ketiga (persen): "))
v3 = int(input("masukkan volume larutan ketiga (ml): "))
c_akhir = (c1 * v1 * c2 * v2 * c3 * v3) / (v1 + v2 + v3)
c_akhir_rounded = round(c_akhir, 2)
print(f"konsentrasi akhir larutan campuran adalah {c_akhir_rounded} persen")



