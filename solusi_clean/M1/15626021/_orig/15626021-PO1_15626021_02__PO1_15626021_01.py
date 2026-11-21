# NIM/Nama  : 15626021 / Aufaa Fakhri Ibrahim Irahadi
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung total biaya listrik yang terbuang dari lampu yang menyala

# KAMUS VARIABEL
# daya        : float (daya lampu dalam watt)
# lama        : float (durasi menyala lampu dalam jam)
# tarif       : float (tarif listrik dalam rupiah/kWh)
# energi_kwh  : float (energi listrik yang dikonsumsu dalam kWh)
# total_biaya : float (total biaya listrik terbuang dalam rupiah)

# Input data dari user
daya = float(input("Masukkan daya lampu (watt): "))
lama = float(input("Masukkan lama lampu menyala (jam): "))
tarif = float(input("Masukkan tarif listrik (rupiah per kWh): "))

# Menghitung energi dalam kWh (watt * jam / 1000)
energi_kWh + (daya * lama) / 1000

# Menghitung total biaya
total_biaya + energi_kWh * tarif

# Menampilkan hasil (mengatur tampilan float/int sesuai test case)
if total_biaya.is_integer():
    print(f"Biaya listrik yang terbuah adalah Rp{int(total_biaya)}")
else:
    print(f"Biaya listik yang terbuang adalah Rp{total_biaya: .2f}".rstrip('0').rstrip('.'))
