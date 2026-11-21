# Nim/Nama = Siti Nawa Aulia
# Tanggal = 30 September 2026
# Deskripsi = Menyelesaikan permasalahan untuk menentukan biaya listrik yang terbuang

# Total Biaya Listrik yang Terbuang

# Kamus
# W = Daya Lampu (Watt)
# J = Lamanya lampu menyala (Jam)
# R = Tarif listrik (rupiah per Kwh)
# 1 Kwh = 1000 watt-jam

# Algoritma
W = int(input("Masukan daya lampu: "))
J = int(input("Masukan lamanya lampu menyala:"))
R = int(input("Masukan tarif listrik:"))

Energi = (W*J)/1000
print(Energi)

Biaya = (Energi*R)
print(Biaya)