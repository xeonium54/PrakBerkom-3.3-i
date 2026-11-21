# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 30 September 2026
# Deskripsi: Menentukan total biaya listrik akibat lampu menyala 

# KAMUS
# daya_lampu : float
# lama_pemakaian : float
# tarif : float

# Input
daya_lampu = float(input("Masukkan daya lampu (watt): "))
lama_pemakaian = float(input("Masukkan lama pemakaian (jam): "))
tarif = float(input("Masukkan tarif listrik (Rp/kWh): "))

# Menghitung energi yang terpakai dalam kWh (1 kWh = 1000 watt * 1 jam)
energi_kWh = (daya_lampu * lama_pemakaian) / 1000

# Menghitung total biaya listrik yang terpakai
total_biaya = energi_kWh * tarif

# Output
print("Total biaya listrik yang terpakai: Rp", total_biaya)