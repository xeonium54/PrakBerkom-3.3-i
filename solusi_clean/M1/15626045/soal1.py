# Program Biaya Listrik
# Deskripsi: Menghitung biaya listrik yang terbuang akibat lampu yang menyala berdasarkan daya (w) watt, waktu (j) dalam jam, dan tarif listrik (r) Rupiah per kWh

# KAMUS
# w : float
# j : float
# r : float
# biaya : float

# ALGORITMA
w = float(input("Masukkan daya lampu (watt): "))
j = float(input("Masukkan lama waktu menyala (jam): "))
r = float(input("Masukkan tarif listrik (rupiah per kWh): "))

biaya = ((w * j)/ 1000) * r

print("Biaya listrik yang terbuang adalah Rp", biaya)
