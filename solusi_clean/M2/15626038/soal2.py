# NIM/Nama : 15626038 / Keysha Hana Putri
# Tanggal : Rabu, 14 Oktober 2026
# Deskripsi : Program ini digunakan untuk menghitung tarif biaya parkir

#KAMUS
# durasi : int
# mobilListrik : string
# akhirPekan : string


durasi = int(input("Masukkan durasi parkir (jam): "))
mobilListrik = str(input("Apakah mobil listrik? (y/n): "))
akhirPekan = str(input("Apakah akhir pekan? (y/n): "))

if (durasi >= 0):
    tarif = 5000
    if (durasi > 2 and durasi <=6):
        durasiTambahan1 = durasi - 2
        tarif += 3000 * durasiTambahan1
        if (durasi > 6):
            durasiTambahan2 = durasi - 6
            tarif += 2000 * durasiTambahan2

if (mobilListrik == 'y'):
    if (durasi > 2):
        tarif -= 5000

if (akhirPekan == 'y'):
    tarif *= 1.2
else:
    tarif *= 1

print("Total tarif parkir adalah Rp", tarif)