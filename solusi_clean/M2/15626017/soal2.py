# NIM/Nama : 15626017 / Naura Vira Vania Ramadhani 
# Tanggal : 14 Oktober 2026
# Deskripsi : Program untuk menghitung tarif parkir berdasarkan durasi, jenis kendaraan, dan hari.

# Membaca masukan dari user 
durasi = int(input("Masukkan durasi parkir (jam):"))
is_mobil_listrik = input("Apakah mobil listrik? (y/n): ")
is_akhir_pekan = input("Apakah akhir pekan? (y/n): ")

# Menghitung tarif dasar parkir 
if durasi <= 2:
    tarif_dasar = 5000
elif durasi <= 6:
    tarif_dasar = 5000 + (durasi-2) * 3000 
else:
    tarif_dasar = 5000 + (4*3000) + (durasi - 6) * 2000

# Aturan tambahan 1 : Potongan mobil listrik jika durasi lebih dari 2 jam 
if is_mobil_listrik == 'y' and durasi > 2:
    tarif_setelah_potongan = tarif_dasar - 5000
else:
    tarif_setelah_potongan = tarif_dasar 

#Aturan tambahan 2: Pengali akhir pekan 
if is_akhir_pekan == 'y':
    total_tarif = tarif_setelah_potongan * 1.2 
else:
    total_tarif = tarif_setelah_potongan 

# Menampilkan hasil total tarif parkir 
print(f"Total tarif parkir adalah Rp{total_tarif}")