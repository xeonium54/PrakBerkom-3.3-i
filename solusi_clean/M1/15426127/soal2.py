# NIM/Nama : Luna Febryvazrya
# Tanggal : 30 September 2026
# Deskripsi : Mencari konsentrasi akhir dari suatu larutan

a = int(input("Masukkan konsentasi larutan pertama (a): "))
b = int(input("Masukkan volume larutan pertama (b): "))
c = int(input("Masukkan konsentrasi larutan kedua (c): "))
d = int(input("Masukkan volume larutan kedua (d): "))
e = int(input("Masukka konsentrasi larutan ketiga (e): "))
f = int(input("Masukkan volume larutan ketiga (f): "))

campuran_larutan = (a*b) + (c*d) + (e*f) 
jumlah_volume = b + d + f
Konsentrasi_akhir = campuran_larutan // jumlah_volume

print(f"Konsentrasi akhir: {Konsentrasi_akhir}")