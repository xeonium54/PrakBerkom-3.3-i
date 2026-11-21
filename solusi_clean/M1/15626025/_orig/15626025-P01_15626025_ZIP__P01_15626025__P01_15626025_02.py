# NIM/Nama : Maria Amatussyafee Nurjaman
# Tanggal : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir dari larutan

#PROGRAM : Problem 2

#KAMUS
# k_larutan_1, v_larutan_1, k_larutan_2, v_larutan_2, k_larutan_3, v_larutan_3 : integer
# konsentrasi_akhir : integer


#ALGORITMA
k_larutan_1 = int(input("Masukan konsentrasi larutan pertama (persen): "))
v_larutan_1 = int(input("Masukan volume larutan pertama (ml): "))
k_larutan_2 = int(input("Masukan konsentrasi larutan pertama (persen): "))
v_larutan_2 = int(input("Masukan volume larutan kedua (ml): "))
k_larutan_3 = int(input("Masukan konsentrasi larutan ketiga (persen): "))
v_larutan_3 = int(input("Masukan volume larutan ketiga (ml): "))

konsentrasi_akhir = ((k_larutan_1 * v_larutan_1) + (k_larutan_2 * v_larutan_2) + (k_larutan_3 * v_larutan_3)) / (v_larutan_1 + v_larutan_2 + v_larutan_3)

print(f"Konsentrasi akhir dari larutan adalah {konsentrasi_akhir}.")
