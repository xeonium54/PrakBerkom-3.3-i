# NIM/Nama : 15626052 / Nu'man Hanania Fawwaz
# Tanggal : 30 September 2026
# Deskripsi : Soal Praktikum #1 Struktur Dasar Program

# Menghitung total biaya energi listrik yang terbuang

# Kamus
# daya lampu = watt
# lama lampu menyala = jam
# tarif listrik = rupiah per kWh
# 1 kWh = 1000 watt-jam

# Algoritma
dayalampu = float(input("Masukkan daya lampu (watt): "))
lamalampumenyala = float(input("masukkan lama lampu menyala (jam): "))
tariflistrik = float(input("Masukkan tarif listrik (rupiah per kWh): "))

Energi = dayalampu * lamalampumenyala / 1000
Biaya = Energi * tariflistrik

print(f"Energi yang dibutuhkan adalah {Energi} kWh")
print(f"Biaya yang dikeluarkan {Biaya} rupiah")
