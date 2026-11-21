# NIM/Nama : Nu'man Hanania Fawwaz 15626052
# Tanggal : 28/10/2026
# Deskripsi : Pengulangan & Array

# Problem 1
# Mengetahui kapan saldo Pa Mik negatif serta total pemasukan & pengeluaran

# Kamus
# Saldo awal : int
# Jumlah transaksi (N) : int
# Nilai transaksi : int
# Saldo akhir : int
# Total pemasukan =

# Algoritma
S = int(input('Masukkan saldo awal (Rp): '))
N = int(input('Masukkan jumlah transaksi: '))
for i in range (0,N):
  T = int(input(f'Masukkan nilai transaksi ke-{i+1}: '))
  S = S + T
  print(f'Saldo setelah transaksi ke-{i+1}: Rp{S}')
  if S < 0:
    print(f'Saldo pertama kali negatif pada transaksi ke-{i+1}')
