# NIM/Nama : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal : 30 September 2026
# Deskripsi : Mencari konsentrasi akhir dari campuran 3 larutan

# Kamus
# C1 (int) = Konsentrasi larutan pertama (persen)
# C2 (int) = Konsentrasi larutan kedua (persen)
# C3 (int) = Konsentrasi larutan ketiga (persen)
# V1 (int) = Volume larutan pertama (ml)
# V2 (int) = Volume larutan kedua (ml)
# V3 (int) = Volume larutan ketiga (ml)
# C  (int) = Kons. larutan akhir (persen)

# Algoritma
C1 = int(input("Masukkan konsentrasi larutan pertama (persen): "))
V1 = int(input("Masukkan konsentrasi larutan pertama (ml): "))
C2 = int(input("Masukkan konsentrasi larutan kedua (persen): "))
V2 = int(input("Masukkan konsentrasi larutan kedua (ml): "))
C3 = int(input("Masukkan konsentrasi larutan ketiga (persen): "))
V3 = int(input("Masukkan konsentrasi larutan ketiga (ml): "))

C = float(((C1*V1)+(C2*V2)+(C3*V3))/(V1+V2+V3))

print(f"Konsentrasi akhir larutan campuran adalah {C} persen")
