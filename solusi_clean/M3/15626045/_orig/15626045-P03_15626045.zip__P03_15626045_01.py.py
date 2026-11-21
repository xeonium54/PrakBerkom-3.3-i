# NIM/Nama : 15626045 / Anindhita Ramya Rahmadani
# Tanggal  : 28/10/2026
# Deskripsi: Menghitung jumlah saldo tiap pengeluaran ke-N, menentukan total pemasukan dan pengeluaran berdasarkan masukkan saldo awal, jumlah transaksi, dan nilai tiap transaksi.

# KAMUS
# saldo_awal: int
# N: int
# TabInt: array [1..N] of int

# ALGORITMA
saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

TabInt = [0 for i in range (N+1)]
for i in range(1, N+1):
    TabInt[i] = int(input("Masukkan nilai transaksi ke-" + str(i) + ": "))

for i in range(1, N+1):
    TabInt[i] = saldo_awal + TabInt[i]
    print(TabInt[i])