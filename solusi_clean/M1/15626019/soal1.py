# NIM/Nama : 15626019/Naura Nur Aprilia
# Tanggal : 30-09-2026
# Deskripsi : Menentukan Total Biaya Listrik yang Terbuang Akibat Lampu yang Menyala

# KAMUS
# x : int
# y : float
# z : int
# Biaya : float

# ALGORITMA
x = int(input("Masukkan daya lampu (watt): "))
y = float(input("Masukkan lama lampu menyala (jam): "))
z = int(input("Masukkan tarif listrik (rupiah per kWh): "))

Biaya = ((x * y)/1000) * z

print("Rp", Biaya)