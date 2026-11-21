# NIM/NAMA : 15626029/HANIF MAHIB YN
# TGL : 30 SEPT 2026
# DESC : Program buat ngitung konstentrasi larutan

# KAMUS
# c1, c2, c3, v1, v2, v3, CT : float

# CODE
c1 = float(input(" Konsentrasi larutan 1(persen) : "))
v1 = float(input("volume larutan 1(ml) : "))
c2 = float(input(" Konsentrasi larutan 2(persen) : "))
v2 = float(input("volume larutan 2(ml) : "))
c3 = float(input(" Konsentrasi larutan 3(persen) : "))
v3 = float(input("volume larutan 3(ml) : "))

CT = ((c1 * v1)+(c2 * v2)+(c3 * v3))/(v1 + v2 +v3)

print("Konsentrasi total larutan :",CT)