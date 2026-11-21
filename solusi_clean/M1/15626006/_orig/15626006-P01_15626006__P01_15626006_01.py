# NIM / Nama : 15626006 / Maria Zeysta Kamelia Rumanti
# Tanggal : 30 September 2026
# Deskripsi : Program menghitung biaya listrik yang terbuang akibat lampu yang lupa dimatikan. Program ini menghitung total biaya berdasarkan daya lampu (watt), durasi menyala, tarif listrik (per kWh).
print("Problem 1")

#KAMUS
w = float
j = float
r = float
energi_kwh = float
biaya = float

#Algoritma
w = float(input("Masukkan daya lampu (watt): "))
j = float(input("Masukkan lama lampu menyala (jam): "))
r = float(input("Masukkan tarif listrik (rupiah per kWh): "))

#Menghitung energi listrik dalam satuan kWh
energi_kwh = (w * j)

#Menghitung total biaya listrik
biaya = energi_kwh * r

print("Biaya listrik yang terbuang adalah Rp ", biaya)