# NIM/Nama : 15626035/Naila Rahmah Zhafirah
# Tanggal : 14 Oktober 2016
# Deskripsi : Menghitung tarif parkir apabila mobil listrik atau akhir pekan

# Kamus
durasi = 0
mobil_listrik = ""
akhir_pekan = ""
tarif = 0

# Input
durasi = int(input("Masukkan durasi parkir (jam): "))
mobil_listrik = input("Apakah moil listrik (y/n): ")
akhir_pekan = input("Apakah akhir pekan? (y/n): ")

# Mengitung tarif parkir
if durasi <= 2:
    tarif = 5000
elif durasi <= 6:
    tarif = (5000 + durasi - 2) * 3000
else:
    tarif = 17000 + (durasi - 6) * 2000

# Potongan tarif mobil listrik
if mobil_listrik == "y" and durasi > 2:
    tarif = tarif - 5000

# Pengali alhir pekan
if akhir_pekan == "y":
    tarif = tarif * 1.2

print("Total tarif parkir adalah Rp", int(tarif))