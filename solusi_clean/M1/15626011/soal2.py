# NIM/Nama  : Vidia Nurafifa
# Tanggal   : Rabu, 30/09/2026
# Deskripsi : Menghitung konsentrasi akhir larutan campuran

# C1,C2,C3 = konsesntrasi larutan ke-n
# V1,V2,V3 = Volume larutan ke-n 

C1 = float(input("Masukkan Konsentrasi larutan pertama (persen): "))
V1 = float(input("Masukkan volume k=larutan pertama (ml): "))

C2 = float(input("Masukkan Konsentrasi larutan kedua (persen): "))
V2 = float(input("Masukkan volume k=larutan pertama (ml): "))

C3 = float(input("Masukkan Konsentrasi larutan ketiga (persen): "))
V3 = float(input("Masukkan volume k=larutan pertama (ml): "))

C_akhir = (C1*V1+C2*V2+C3*V3)/(V1+V2+V3)

print(f'Konsentrasi akhir larutan campuran adalah {C_akhir:.1f} persen')
