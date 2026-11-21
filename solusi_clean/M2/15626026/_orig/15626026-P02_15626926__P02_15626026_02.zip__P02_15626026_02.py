# NIM / NAMA : 15626026 / MUTHIAH AZKA NIAMILLAH
# TANGGAL : RABU, 14/10/2026
# DESKRIPSI : PROBLEM 2

# input
durasi_parkir = int(input("masukkan durasi parkir (jam): "))
mobil_listrik = input("apakah mobil listrik? (y/n): ")
akhir_pekan = input("apakah akhir pekan? (y/n): ")

# proses
if durasi_parkir <= 2:
    tarif = 5000
elif durasi_parkir <= 6:
    tarif = 5000 + (durasi_parkir - 2) * 3000
else:
    tarif = 17000 + (durasi_parkir - 6) * 2000

if mobil_listrik == 'y' and durasi_parkir > 2:
    tarif -5000
if akhir_pekan == 'y':
    tarif *= 1.2

# output
print("total tarif parkir adalah Rp{tarif}")