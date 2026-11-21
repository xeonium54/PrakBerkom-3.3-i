# NIM/Nama : 15626004
# Tanggal : 10/14/2026
# Deskripsi : Program lama durasi tarif parkir 

# KAMUS
# A : float

# Algoritma
durasi = float((input)("durasi tarif parkir (jam): "))
listrik = input("apakah durasi mobil listrik? (ya/tidak): ")
akhir_pekan = input("apakah akhir pekan? (ya/tidak): ")

if durasi <= 2:
    tarif_dasar = 5000
elif durasi <= 6:
    tarif_dasar = 5000 + (durasi - 2) * 3000 
else: 
    tarif_dasar = 5000 + (4 * 3000) + (durasi - 6) * 2000 

if listrik and durasi > 2:
    arif_setelah_potongan = tarif_dasar - 5000
else:
    tarif_setelah_potongan = tarif_dasar

if akhir_pekan:
    total_tarif = int(tarif_setelah_potongan * 1.2) 
else:
    total_tarif = tarif_setelah_potongan

print("Total tarif parkir akhir: Rp", total_tarif)