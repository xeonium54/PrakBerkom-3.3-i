# NIM/Nama: Nirmala Rahma Maulida
# Tanggal : 30 September 2026
# Deksripsi : Pada program ini dituju untuk membantu tuan mik menghitung konsentrasi akhir pada praktikum kimianya

#Praktikum kimia 

# KAMUS 
# C1, C2, C3, V1, V2, V3 : int

#proses
C1 = int(input("masukkan konsentrasi larutan pertama (persen): "))
V1 = int(input("masukkan volume larutan pertama (ml): "))
C2 = int(input("masukkan konsentrasi larutan kedua (persen): "))
V2 = int(input("masukkan volume larutan kedua (ml): "))
C3 = int(input("masukkan konsentrasi larutan ketiga (persen): "))
V3 = int(input("masukkan volume larutan ketiga (ml): "))

C_akhir = (C1 * V1 + C2 * V2 + C3 * V3) / (V1 + V2 + V3)

#output
print("konsentrasi akhir larutan campuran", C_akhir) 