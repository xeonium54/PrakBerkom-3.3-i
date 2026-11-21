# NIM/Nama  : Vidia Nurafifa
# Tanggal   : Rabu, 30/09/2026
# Deskripsi : Membuat program untuk menentukan total biaya listrik yang terbuang

# daya lampu (w)
# lama lampu menyala (t) satuannya per jam
# tarif = 1500 rupiah/kwh


w = float(input("Masukkan daya lampu (watt):"))
t = float(input("Masukan lama lampu menyala (jam):"))
tarif = float(input("Masukkan tarif l/istrik (rupiah/kwh):"))

energi = w * t / 1000
biaya = energi * tarif 
print("Biaya yang terbuang adalah Rp", biaya)