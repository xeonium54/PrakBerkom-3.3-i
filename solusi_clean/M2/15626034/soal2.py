#NIM/NAMA : 15626034/Ahmad Zaky 
#Tanggal : 14/10/2026
#Deskripsi : Program penghitung tarif parkir

#kamus
    #durasi_parkir : integer
    #mobil_listrik : boolean
    #akhir_pekan : boolean

#algoritma
durasi_parkir = int(input("Masukkan durasi parkir (jam): "))
kelebihan = 0
if durasi_parkir <=2 :
    tarif_dasar = 5000
elif durasi_parkir <= 6:
    kelebihan = durasi_parkir - 2
    tarif_dasar = 5000 + (kelebihan * 3000)
else:
    kelebihan = durasi_parkir - 6
    tarif_dasar = 5000 + (4 * 3000) + (kelebihan * 2000)

tarif_setelah_diskon = tarif_dasar
mobil_listrik = input("Apakah mobil listrik? (y/n): ").lower() == "ya"
if mobil_listrik and durasi_parkir > 2:
    tarif_setelah_diskon = max(0, tarif_dasar - 5000)

total_tarif = tarif_setelah_diskon
akhir_pekan = input("Apakah akhir pekan? (y/n): ").lower() == "ya"
if akhir_pekan:
    total_tarif = total_tarif * 1.2

print("Total tarif parkir: Rp", total_tarif)

