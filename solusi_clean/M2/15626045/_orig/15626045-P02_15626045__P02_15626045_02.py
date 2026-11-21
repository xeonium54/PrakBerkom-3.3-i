# NIM/Nama : 15626045/Anindhita Ramya Rahmadani
# Tanggal  : Rabu, 14 Oktober 2026
# Deskripsi: Menghitung tarif parkir dasar yang ditentukan oleh lama durasi parkir dalam jam dengan beberapa aturan dasar dan aturan tambahan.

# KAMUS
# durasi : int
# molis : str
# pekan : str
# tarif_d : int
# tarif_a : int
# tarif_b : int
# y : str
# n : str

# ALGORITMA
durasi = int(input("Masukkan durasi parkir (jam): "))
molis = str(input("Apakah mobil listrik? (y/n): "))
pekan = str(input("Apakah akhir pada akhir pekan? (y/n): "))

if (0 < durasi <= 2):
    tarif_d = 5000
elif (2 < durasi <= 6):
    tarif_d = 5000 + (durasi - 2) * 3000
else: # durasi > 6
    tarif_d = 5000 + 4 * 3000 + (durasi - 6) * 2000

if (molis == "y"):
    if (molis == "y") and (durasi > 2):
        tarif_a = tarif_d - 5000
    else: # (molis == "y") and (durasi <= 2)
        tarif_a = tarif_d
else:
    tarif_a = tarif_d

if (pekan == "y"):
    tarif_b = tarif_a * 1.2
else:
    tarif_b = tarif_a

print("Total tarif parkir adalah " + "Rp" + str(tarif_b))
