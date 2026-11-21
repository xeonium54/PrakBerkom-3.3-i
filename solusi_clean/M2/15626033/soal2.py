# NIM = 15626033
# Tanggal = 14 oktober 2026
# deskripsi = menghitung total tarif parkir

durasi = float(input("masukkan durasi parkir (jam): "))
is_listrik = input("apakah mobil listrik? (y/n): "). lower()
is_akhir_pekan = input("apakah akhir pekan? (y/n): "). lower()
if durasi <= 2:
    tarif_dasar = 5000
elif durasi <= 6:
    tarif_dasar = 5000 + (durasi - 2) * 3000
else:
    tarif_dasar = 5000 + (4 * 3000) + (durasi - 6) * 2000
if is_akhir_pekan == 'y':
    total_tarif = total_tarif * 1.2
print(f"Total tarif parkir yang harus dibayar: Rp{int(total_tarif)}")
