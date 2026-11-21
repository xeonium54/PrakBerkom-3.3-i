# Nama/NIM : Nu'man Hanania Fawwaz/15626052
# Tanggal : 14/10/2026
# Deskripsi : Praktikum #2 Analisis Kasus (Percabangan)

# Program menentukan prioritas kereta yang lewat serta waktu tunggu bagi kereta lain
# Kamus
# Jenis A = str
# Jenis B = str
# Jarak A = int
# Jarak B = int
# Kecepatan A = int
# Kecepatan B = int

# Algoritma
A = str(input("Jenis kereta A: "))
B = str(input("Jenis kereta B: "))
xA = int(input("Jarak kereta A: "))
xB = int(input("Jarak kereta B: "))
vA = int(input("Kecepatan kereta A: "))
vB = int(input("Kecepatan kereta B: "))

t_A = xA / vA
t_B = xB / vB
selisih_waktu_tiba = (t_A - t_B)

if 0 <= selisih_waktu_tiba <= 30:
  if A == 'Bisnis':
    if B == 'Eksekutif':
      print('Konflik terdeteksi ! Kereta B diprioritaskan melintas')
      print(f'Kereta A harus berhenti dan menunggu selama {(t_B + 40.0) - t_A}')
    else:
      print('Konflik terdeteksi ! Kereta A diprioritaskan melintas')
      print(f'Kereta B harus berhenti dan menunggu selama {(t_A + 40.0) - t_B}')

  elif A == 'Bisnis' and B == 'Kargo':
    print('Konflik terdeteksi ! Kereta A diprioritaskan melintas')
    print(f'Kereta B harus berhenti dan menunggu selama {(t_A + 40.0) - t_B}')

  elif A == 'Eksekutif' and B == 'Kargo':
    print('Konflik terdeteksi ! Kereta A diprioritaskan melintas')
    print(f'Kereta B harus berhenti dan menunggu selama {(t_A + 40.0) - t_B}')

  else:
    print('Konflik terdeteksi ! Kereta B diprioritaskan melintas')
    print(f'Kereta A harus berhenti dan menunggu selama {(t_B + 40.0) - t_A}')

else:
  if A == 'Eksekutif' and B == 'Eksekutif':
    if t_A > t_B:
      print('Jalur aman. Kereta A melintas duluan tanpa henti')
    else:
      print('Jalur aman. Kereta B melintas duluan tanpa henti')
  elif A == 'Bisnis' and B == 'Bisnis':
    if t_A > t_B:
      print('Jalur aman. Kereta A melintas duluan tanpa henti')
    else:
      print('Jalur aman. Kereta B melintas duluan tanpa henti')
  elif A == 'Kargo' and B == 'Kargo':
    if t_A > t_B:
      print('Jalur aman. Kereta A melintas duluan tanpa henti')
    else:
      print('Jalur aman. Kereta B melintas duluan tanpa henti')