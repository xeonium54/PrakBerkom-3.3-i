# Nama = Jihan Salsabila
# NIM  = 15626002

# Program BiayaTotalListrik
# Mencari biaya total listrik berdasarkan 

# KAMUS
# watt : integer
# jam : integer
# Tarif listrik : integer
# Biaya listrik : integer

# ALGORITMA
watt = int(input("Masukkan watt lampu:"))
Lama_Lampu_Menyala = int(input("Masukkan lama lampu menyala (jam):"))
Tarif_Listrik = int(input("Masukkan tarif listrik(rupiah per KWH):"))

Energi = (watt*Lama_Lampu_Menyala) / 1000
Biaya_Listrik = (Tarif_Listrik*Energi)

print(f"Biaya total yang terbuang akibat lampu yang menyala sebesar{Biaya_Listrik}:")