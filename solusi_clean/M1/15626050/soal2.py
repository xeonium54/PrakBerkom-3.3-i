# NIM/Nama = 15626050/Yohanes Yoel Christopher Naibaho
# Tanggal  = 30-9-2026
# Deskripsi = Menghitung Konsentrasi Akhir Dari Suatu Larutan Campuran

# KAMUS
# C1,V1,C2,V2,C3,V3, = float
# KonsentrasiAkhir = float

# ALGORITMA
C1 = float(input("input Konsentrasi Larutan 1(persen): "))
V1 = float(input("input Volume Larutan 1(ml): "))
C2 = float(input("input Konsentrasi Larutan 2(persen): "))
V2 = float(input("input Volume Larutan 2(ml): "))
C3 = float(input("input Konsentrasi Larutan 3(persen): "))
V3 = float(input("input Volume Larutan 3(ml): "))
KonsentrasiAkhir = (((C1*V1)+(C2*V2)+(C3*V3))/(V1+V2+V3))
print("Konsentrasi Akhir Dari Larutan Campuran adalah", KonsentrasiAkhir ,"persen")