# NIM/Nama  : 15626018 / Chantal Carissa Zuleika
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung biaya listrik akibat lampu yang menyala

# Kamus
# w      : daya lampu (watt)
# j      : lama lampu menyala (jam)
# r      : tarif listrik (rupiah per kWh)
# energi : energi listrik yang digunakan (kWh)
# biaya  : total biaya listrik (rupiah)

w = float(input("Masukkan daya lampu (watt): "))
j = float(input("Masukkan lama lampu menyala (jam): "))
r = float(input("Masukkan tarif listrik (rupiah per kWh): "))

energi = (w * j) / 1000
biaya = energi * r

print("Biaya listrik yang terbuang adalah Rp", biaya)
