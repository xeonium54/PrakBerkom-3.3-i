# NIM/Nama : 15626032/Muhamad Faiz Abdul Aziz
# Tanggal : 30 September 2026
# Deskripsi : Membantu Tuan Mik menghitung konsentrasi akhir dari larutan

# Kamus
C1 = int(input("Masukan konsentrasi larutan pertama (persen): "))
V1 = int(input("Masukan volume larutan pertama (ml): "))
C2 = int(input("Masukan konsentrasi larutan kedua (persen): "))
V2 = int(input("Masukan volume larutan kedua (ml):  "))
C3 = int(input("Masukan konsentrasi larutan ketiga (persen): "))
V3 = int(input("Masukan volume larutan ketiga (ml): "))

# Logaritma
C_akhir = (C1*V1 + C2*V2 + C3*V3) / (V1 + V2 + V3)

# Hasil 
print(f"Konsentrasi akhir larutan campuran adalah: {C_akhir}persen")