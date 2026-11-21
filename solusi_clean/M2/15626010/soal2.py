# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 14/10/2026
# Deskripsi : Program ini berfungsi untuk menghitung total tarif parkir kendaraan Kompeng Mall secara otomatis.

# Program Hitung Tarif Parkir

# Menerima input dari pengguna
durasi = int(input("Masukkan durasi parkir (jam): "))
apakah_mobil_listrik = input("Apakah mobil listrik (y/n): ").lower()
apakah_akhir_pekan = input("Apakah akhir pekan (y/n): ").lower()

# Hitung tarif dasar 
if durasi <= 2:
    tarif =  5000
elif durasi <= 6:
    tarif = 5000 + (durasi - 2) * 3000
else:
    tarif = 5000 + (4*3000)+(durasi - 6)*2000

# aturan diskon mobil listrik (kalau > 2 jam)
if apakah_mobil_listrik == 'y' and durasi > 2:
    tarif -=5000

# aturan pengali akhir pekan
if apakah_akhir_pekan == 'y':
    tarif *= 1.2

# menampilkan total tarif parkir
if tarif == int(tarif):
    print(f"Total tarif parkir adalah Rp{int(tarif)}")
else:
    print(f"Total tarif parkir adalah Rp{tarif}")