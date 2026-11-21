# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 14 Oktober 2026
# Deskripsi : Menghitung Total Tarif Parkir

# Masukkan dari pengguna
Durasi = int(input("Masukkan durasi parkir (dalam jam): "))
Jenis_Mobil = input("Apakah mobil listrik (y/n): ")
Jenis_Hari = input("Apakah akhir pekan (y/n): ")

# Menghitung tarif dasar
if Durasi <= 2:
    tarif_dasar = 5000
elif Durasi <= 6:
    tarif_dasar = 5000 + (Durasi - 2) * 3000
else:
    tarif_dasar = 5000 + 12000 + (Durasi - 6) * 2000
    
# Aturan potongan Harga
if Jenis_Mobil == "y":
    if Durasi > 2:
        tarif_dasar = tarif_dasar - 5000
    else:
        tarif_dasar = tarif_dasar
else:
    tarif_dasar = tarif_dasar
    
# Aturan Akhir pekan
if Jenis_Hari == "y":
    total_tarif = tarif_dasar * 1.2
else:
    total_tarif = float(tarif_dasar)
    
# Hasil Tarif Totak
print(f"Total tarif parkir adalah Rp.{total_tarif}")