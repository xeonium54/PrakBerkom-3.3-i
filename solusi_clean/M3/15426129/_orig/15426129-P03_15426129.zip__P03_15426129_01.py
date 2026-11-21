# Nama: Kirani Rizky Aulia Khairunissa
# NIM: 15426129
# Tanggal: Rabu, 28 Oktober 2026

# PROGRAM Penghitungan E-Wallet
# Deskripsi: User memasukkan saldo awal, jumlah transaksi, dan nilai setiap transaksi; sistem akan menghitung saldo setiap setelah transaksi beserta total pemasukan dan total pengeluaran.

# KAMUS
# ST : array [0, 1, 2, ..., N] for integer (saldo total)
# BT : array [0, 1, 2, ..., N] for integer (besar transaksi)
# S : int (saldo awal)
# N : int (jumlah transaksi)

# ALGORITMA
print("Program Penghitungan E-Wallet")
S = int(input("Masukkan saldo awal (Rp): "))

N = int(input("Masukkan jumlah transaksi (N): "))

ST = [0 for i in range(N)]
ST[0] = S
BT = [0 for i in range(N)]

for i in range(0,N):
    BT[i] = int(input("Masukkan nilai transaksi ke-" + str(i+1) + ": "))

i = 0
ST[i] = S
for i in range(0,N):
    ST[i] = ST[i] + BT[i]
    i = i+1

for i in range(0,N):
    print("Saldo setelah transaksi ke-" + str(i+1) + ": Rp" + str(ST[i]))

min = ST[0]
i = 1
found = False
while (i <= N-1) and (i > 0) and (found == False):
    if ST[i] < min:
        min = ST[i]
    else:
        i = i + 1

print("Saldo Tuan Mik pertama kali negatif pada transaksi ke-" + str(i))

sum_masuk = 0
for i in range(0,N):
    if ST[i] >= 0:
        sum_masuk = sum_masuk + ST[i]
    else:
        sum_masuk = sum_masuk

sum_keluar = 0
for i in range(0,N):
    if ST[i] < 0:
        sum_keluar = sum_keluar - ST[i]
    else:
        sum_keluar = sum_keluar

print("Total pemasukan: Rp" + str(sum_masuk) + ". Total pengeluaran: Rp" + str(sum_keluar) + ("."))