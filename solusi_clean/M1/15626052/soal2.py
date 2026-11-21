# NIM/Nama : 15626052 / Nu'man Hanania Fawwaz
# Tanggal : 30 September 2026
# Deskripsi : Soal Praktikum #1 Struktur Dasar Program

# Program menghitung konsentrasi larutan

# Kamus
# C1 (%)
# V1 (ml)
# C2 (%)
# V2 (ml)
# C3 (%)
# V3 (ml)

# Algoritma
C1 = float(input("Masukkan konsentrasi larutan pertama (%): "))
V1 = float(input("Masukkan volume larutan pertama (ml): "))
C2 = float(input('Masukkan konsentrasi larutan kedua (%): '))
V2 = float(input("Masukkan volume larutan kedua (ml): "))
C3 = float(input('Masukkan konsentrasi larutan ketiga (%): '))
V3 = float(input('Masukkan volume larutan ketiga (ml): '))

Cakhir = (( C1 * V1 ) + ( C2 * V2 ) + ( C3 * V3 )) / ( V1 + V2 + V3 )

print(f"Hasil konsentrasi akhir {Cakhir}")
