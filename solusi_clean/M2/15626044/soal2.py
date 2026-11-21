# P02.15626044.02
# NIM : 15662044
# Tanggal : 14 Oktober
# Deskripsi : Problem 2

# Menghitung tarif awal berdasarkan durasi
durasi = int(input("Masukkan durasi parkir: "))
if durasi <= 2:
    tarif_uang = 5000
elif 2 < durasi <= 6:
    tarif_uang = 5000 + (durasi - 2) * 3000
else:
    tarif_uang = 5000 + (4 * 3000) + (durasi - 6) * 2000

# Menghitung tarif untuk mobil listrik
mobil_listrik = str(input("Apakah mobil lisrik? (y/n): "))
if mobil_listrik == "y" and durasi > 2:
    tarif_uang -= 5000
else:
    tarif_uang = tarif_uang

# Saat akhir pekan
akhir_pekan = str(input("Apakah akhir pekan? (y/n): "))
if akhir_pekan == "y":
    tarif_total = tarif_uang * 1.2
else: 
    tarif_total = tarif_uang

# Hasil tarif total parkir
print(f"Total tarif parkir adalah Rp{tarif_total}")

