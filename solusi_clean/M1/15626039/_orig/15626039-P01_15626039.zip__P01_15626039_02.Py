# 15626039/Khalif Aufar Aufar Aridkhi
# 30 September 2026
# Praktikum Modul 1, Menghitung total tarif biaya yang dikeluarkan

# Masukan konsentrasi dari larutan 1,2, dan 3 
k1 = int(input("Masukkan konsentrasi larutan pertama dalam (persen): "))
k2 = int(input("Masukkan konsentrasi larutan kedua dalam (persen): "))
k3 = int(input("Masukkan konsentrasi larutan ketiga dalam (persen): "))

# Masukkan Volume larutan dari larutan 1,2, dan 3
l1 = int(input("Masukkan volume larutan pertama (ml): "))
l2 = int(input("Masukkan volume larutan kedua (ml): "))
l3 = int(input("Masukkan volume larutan ketiga (ml): "))

# Operasikan konsentrasi akhir dari larutan campuran tersebut
kl = k1*l1 + k2*l2 + k3*l3
total_l = l1+l2+l3
ka = kl / total_l

print(f"Konsentrasi akhir larutan yang tercampur adalah : {ka} persen")
