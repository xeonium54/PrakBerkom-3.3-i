# NIM/Nama :
# Tanggal : 30 September 2026
# Deskripsi : Menghitung konsentrasi akhir dari tiga larutan yang dicampurkan.

# Input larutan pertama
C1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
V1 = float(input("Masukkan volume larutan pertama (ml): "))

# Input larutan kedua
C2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
V2 = float(input("Masukkan volume larutan kedua (ml): "))

# Input larutan ketiga
C3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
V3 = float(input("Masukkan volume larutan ketiga (ml): "))

# Menghitung konsentrasi akhir
Cakhir = (C1 * V1 + C2 * V2 + C3 * V3) / (V1 + V2 + V3)

# Menampilkan hasil
print(f"Konsentrasi akhir larutan campuran adalah {Cakhir:g} persen")
