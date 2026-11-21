# NIM/Nama  : 15626017 / Naura Vira Vania Ramadhani
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung total biaya listrik yang terbuang akibat lampu menyala

# KAMUS
# daya        : float (daya lampu dalam watt)
# lama        : float (lama lampu menyala dalam jam)
# tarif       : float (tarif listrik per kWh dalam rupiah)
# energi_kwh  : float (energi listrik terpakai dalam kWh)
# total_biaya : float (total biaya listrik yang terbuang)

# Input data
daya = float(input("Masukkan daya lampu (watt): "))
lama = float(input("Masukkan lama lampu menyala (jam): "))
tarif = float(input("Masukkan tarif listrik (rupiah per kWh): "))

# Perhitungan
# Energi dalam kWh = (daya * lama) / 1000
energi_kwh = (daya * lama) / 1000
total_biaya = energi_kwh * tarif

print(f"Biaya listrik yang terbuang adalah Rp{total_biaya:g}")