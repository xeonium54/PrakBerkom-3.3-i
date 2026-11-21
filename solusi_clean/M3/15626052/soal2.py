# NIM/Nama : Nu'man Hanania Fawwaz 15626052
# Tanggal : 28/10/2026
# Deskripsi : Pengulangan & Array

# Problem 2
# Simulasi trailing stop dan menghitung untung atau rugi

# Kamus
# Persentase trailing stop : int
# Harga saham : int
# BatasJual : Puncak * (1 - Persen/100)

# Algoritma
Persen = int(input('Masukkan persentase trailing stop: '))
i = 0
Puncak = 0
BatasJual = Puncak * (1 - Persen/100)
while (i < BatasJual):
  Harga = int(input(f'Masukkan harga saham hari ke-{i+1}: '))
  if Harga > Puncak:
    Puncak = Harga

