# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 14 Oktober 2026
# Deskripsi : Menghitung jumlah tarif parkir berdasarkan 
#             lama waktu parkir, jenis kendaraan, dan hari

# KAMUS
# durasi : int : lama waktu parkir dalam jam
# listrik : str : jenis kendaraan listrik/tidak
# hari : str : apakah hari parkir saat akhir pekan/tidak

# ALGORITMA
# Memasukkan durasi, jenis kendaraan, dan hari parkir
durasi = int(input("Masukkan durasi parkir (jam) : "))
listrik = input("Apakah mobil listrik? (y/n) : ")
hari = input("Apakah akhir pekan (y/n) : ")

# Jika durasi lebih dari atau sama dengan 2 jam
# Maka dikenakan tarif 5000
if (durasi <= 2) :
    tarif = 5000
# Jika durasi lebih dari 2 jam dan kurang dari sama dengan 6 jam
# dikenakan tarif parkir 5000 di awal 2 jam dan sisanya dikenakan 3000 per jamnya
elif (durasi > 2 and durasi <= 6) :
    tarif = 5000 + (durasi - 2) * 3000
# Jika durasi lebih dari 6 jam
# dikenakan tarif 5000 untuk 2 jam pertama
# tarif 3000 untuk 4 jam, mengikuti aturan sebelumnya
# tarif sisanya dikenakan 2000 per jamnya
elif (durasi > 6) :
    tarif = 5000 + 4 * 3000 + (durasi - 6) * 2000

# Potongan tarif mobil listrik
# jika mobil adalah listrik (y) 
# maka tarif dasar dikurangi 5000
if (listrik == "y" and durasi > 2) :
    tarif = tarif - 5000

# Akhir pekan 
# Jika mobil diparkir pada saat akhir pekan
# tarif dasar dikalikan dengan 1.2 karena volume parkir lebih padat
if (hari == "y") :
    tarif = tarif * 1.2

# Menghitung tarif akhir yang didapat
print("Total tarif parkir adalah Rp." , tarif)