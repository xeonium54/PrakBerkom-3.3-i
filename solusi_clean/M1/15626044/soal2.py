# NIM/Nama : 15626044/Saliha Mahira Al-kwarismy
# Tanggal : 2023-03-30
# Deskripsi : Problem 2

# Masukkan volume dan konsentrasi larutan pertama, kedua, dan ketiga
# V1 = volume larutan pertama (mL)
# C1 = konsentrasi larutan pertama (%)
# V2 = volume larutan kedua (mL)
# C2 = konsentrasi larutan kedua (%)
# V3 = volume larutan ketiga (mL)
# C3 = konsentrasi larutan ketiga (%)

# Input larutan pertama
C1 = int(input("Masukkan konsentrasi larutan pertama (%): "))
V1 = int(input("Masukkan volume larutan pertama (mL): "))

# Input larutan kedua
C2 = int(input("Masukkan konsentrasi larutan kedua (%): "))
V2 = int(input("Masukkan volume larutan kedua (mL): "))

#Input larutan ketiga
C3 = int(input("Masukkan konsentrasi larutan ketiga (%): "))
V3 = int(input("Masukkan volume larutan ketiga (mL): "))

# Rumus konsentrasi akhir larutan campuran
total_campuran = ((C1 * V1) + (C2 * V2) + (C3 * V3)) 
total_volume = V1 + V2 + V3
hasil_akhir = total_campuran / total_volume

# Menampilkan hasil konsentrasi akhir larutan campuran
print(f"Konsentrasi akhir larutan campuran adalah {hasil_akhir} persen")