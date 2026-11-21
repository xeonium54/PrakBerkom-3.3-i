# 15626048_Siti Nawa Aulia
# 30 September 2026
# Menghitung konsentrasi akhir dari larutan campuran Tuan Mik

# Kamus
# K1 = Konsentrasi larutan pertama (persen)
# V1 = Volume larutan pertama (ml)
# K2 = Konsentrasi larutan kedua (persen)
# V2 = Volume larutan kedua (ml)
# K3 = Konsentrasi larutan ketiga (persen)
# V3 = Volume larutan ketiga (ml)
# K = Konsentrasi total

# Algoritma
K1 = float(input("Konsentrasi larutan pertama:"))
V1 = float(input("Volume larutan pertama:"))
K2 = float(input("Konsentrasi larutan kedua:"))
V2 = float(input("Volume larutan kedua:"))
K3 = float(input("Konsentrasi larutan ketiga"))
V3 = float(input("Volume larutan ketiga"))

# Total konsentrasi
K = (K1*V1+K2*V2+K3*V3)/(V1+V2+V3)
print(K)