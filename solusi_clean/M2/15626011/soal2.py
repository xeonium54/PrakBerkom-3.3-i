# NIM/Nama  : Vidia Nurafifa
# Tanggal   : Rabu, 14/10/2026
# Deskripsi : Menghitung total tarif parkir

# durasi <= 2 jam, tarif = Rp.5.000
# 2 jam < durasi <= 6 jam, tarif = Rp.5000 + ((n-2)*Rp.3.000)
# durasi > 6 jam, tarif = (Rp.5000 + ((n-2)*Rp.3.000)) + ((n-6)*Rp.2.000)
# jika kendaraan mobil listrik, tarif -Rp.5.000 namun tidak berlaku untuk <= 2 jam
# jika akhir pekan, tarif (klo kena potongan mobil listrik) dikali 1,2

# durasi = d
# mobil listrik = mbl 
# akhir pekan = akp

d = int(input("Masukkan durasi parkir (jam): "))
mbl = input("Apakah mobil listrik? (y/n) ")
akp = input("Apakah akhir pekan? (y/n) ")

if d <= 2:
    tarif = 5000
elif d <=6:
    tarif = 5000 + ((d-2)*3000)
else:
    tarif = 5000 + (4*3000) + ((d-6)*2000)

if mbl == "y" and d > 2:
    tarif = tarif - 5000
    
if akp == "y":
    tarif = tarif*1.2 
    
print("Total tarif parkir adalah Rp", tarif)