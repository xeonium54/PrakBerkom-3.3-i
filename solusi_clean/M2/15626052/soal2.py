# Nama/NIM : Nu'man Hanania Fawwaz/15626052
# Tanggal : 14/10/2026
# Deskripsi : Praktikum #2 Analisi Kasus (Percabangan)

# Program pembayaran tarif parkir Kompeng Mall
# Kamus
# jam : int
# mobil listrik y/n : str
# akhir pekan y/n : str

# Algoritma
jam = int(input('Masukkan durasi parkir: '))
A = str(input('Apakah mobil listrik (y/n): '))
B = str(input('Apakah akhir pekan (y/n): '))

if jam in range(0,3):
  print('Tarif parkir adalah Rp 5000')

elif jam in range(3,7):
  if A == 'y':
    print(f'Tarif parkir adalah {3000 * (jam - 2)}')
  elif B == 'y':
    print(f'Tarif parkir adalah {(5000 + 3000 * (jam - 2)) * 1.2}')
    if A == 'y':
      print(f'Tarif parkir adalah {3000 * (jam - 2) * 1.2}')
  else:
      print(f'Tarif parkir adalah {5000 + 3000 * (jam - 2)}')

else:
  if A == 'y':
    print(f'Tarif parkir adalah {3000 * 4 + 2000 * (jam - 6)}')
  elif B == 'y':
    print(f'Tarif parkir adalah {(5000 + 3000 * 4 + 2000 * (jam - 6)) * 1.2}')
    if A == 'y':
      print(f'Tarif parkir adalah {(3000 * 4 + 2000 * (jam - 6)) * 1.2}')
  else :
    print(f'Tarif parkir adalah {5000 + 4 * 3000 + (jam - 6) * 2000}')