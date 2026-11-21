# NIM/Nama : 15626005/Addien Maulana Bima
# Tanggal : 14 Oktober 2026
# Deskripsi : Program menghitung tarif parkir total

T = float(input("Masukkan Durasi Parkir (jam) : "))
L = input("Apakah mobil listrik? (y/n) : ")
W = input("Apakah hari ini hari libur? (y/n) ")

if T<=2:
    tarif_dasar = 5000
elif T<=6:
    tarif_dasar = 5000+(T-2)*3000
else :
    tarif_dasar = 5000+(4*3000)+(T-6)*2000

tarif_diskon = tarif_dasar
if L == "y" and T>2:
    tarif_diskon = tarif_dasar-5000
    if tarif_diskon<0:
        tarif_diskon = 0

tarif_total = tarif_diskon
if W == "y" :
    tarif_total = tarif_diskon*1.2

print(f"Total Parkir Adalah Rp.{int(tarif_total)}")

