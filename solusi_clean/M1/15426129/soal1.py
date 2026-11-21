# NIM       :15426129
# Nama      : Kirani Rizky Aulia Khairunissa
# Tanggal   : Rabu, 30 September 2026
# Deskripsi : Praktikum 1 Berpikir Komputasional (Problem 1)

# PROGRAM Menghitung Biaya Listrik
# Deskripsi:
# User memasukkan daya lampu, lama lampu menyala, serta tarif listrik. Sistem akan menghitung biaya listrik yang terbuang.

# KAMUS
# w (daya dalam watt) : float
# j (lama lampu menyala dalam jam) : float
# r (tarif listrik per jam dalam rupiah) : float
# b (biaya total listrik yang terbuang) : float

# ALGORITMA
print("PROGRAM Penghitungan Biaya Listrik")
print()

w = float(input("Masukkan daya lampu (watt) : "))
j = float(input("Masukkan lama lampu menyala (jam) : "))
r = float(input("Masukkan tarif listrik (rupiah per kWh) : "))

b = float(((w * j) / 1000) * r)
print("Biaya listrik yang terbuang adalah Rp", b)
print()