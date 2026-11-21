# NIM/Nama : 15426128/Fathir Sulihansyah 
# Tanggal  : 14 Oktober 2026
# Deskripsi: Program untuk menghitung total tarif parkir

# Kamus koding :
# durasi : (Interger)Menyatakan lama waktu parkir dalam satuan jam
# apkh_ev : (String)Menyatakan apakah kendaraan tersebut mobil listrik
# weekend : (String)Menyatakan apakah hari tersebut merupakan akhir pekan 
# tarif_dasar : (Float)Menyimpan perhitungan tarif parkir awal sebelum atau sesudah potongan mobil ev
# total_tarif : (Float)Menyimpan hasil akhir tarif parkir setelah memperhitungkan seluruh aturan

durasi = int(input("Masukkan durasi parkir (jam): "))
apkh_ev = input("Apakah mobil listrik? (y/n) : ").strip().lower()
weekend = input("Apakah akhir pekan? (y/n) : ").strip().lower()

if durasi <= 2:
    tarif_dasar = 5000
elif durasi <= 6:
    tarif_dasar = 5000 + (durasi - 2) * 3000
else :
    tarif_dasar = 5000 + (4*3000) + (durasi - 6) * 2000
    
if apkh_ev == 'y' and durasi > 2:
    tarif_dasar -= 5000
    if tarif_dasar < 0:
        tarif_dasar = 0
        
if weekend == 'y' :
    total_tarif = tarif_dasar*1.2
else:
    total_tarif = tarif_dasar

print(f"Total tarif parkir adalah Rp{total_tarif}")
    

