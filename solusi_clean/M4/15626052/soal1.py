# NIM/Nama : 15626052/Nu'man Hanania Fawwaz
# Tanggal : 11/11/2026
# Deskripsi : Modul 4

# Kamus
# lebar foto : int
# tinggi foto : int
# fpb : int
# ratio : str

# Algoritma
import math
def R(l,t):
    fpb = math.gcd(l,t)
    l= l // fpb
    t = t // fpb
    return f"{l}/{t}"

l = int(input("Masukkan lebar foto : "))
t = int(input("Masukkan tinggi foto : "))
print(f"Ratio : {R(l,t)}")