# NIM/Nama : 15626051/Rafa Davlin Ginting Suka
# Tanggal  : 14 Oktober 2026
# Deskripsi: menghitung tarif parkir di mall

durasi = int(input("masukan durasi parkir dalam jam: "))
listrik = input("apakah mobil listrik? (y/n): ")
akhirpekan = input("apakah di akhir pekan? (y/n)")

if (durasi <= 2):
    tarif = 5000
elif (durasi <= 6):
    tarif = 5000 + (durasi - 2) * 3000
else:
    tarif = 5000 + 12000 + (durasi - 6) * 2000

if (listrik == "y" and durasi > 2):
    tarif = tarif - 5000

if (akhirpekan == "y"):
    tarif = tarif * 1.2

print("total tarif parkir" + str(tarif))