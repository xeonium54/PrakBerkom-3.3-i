# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 28 Oktober 2026
# Deskripsi: Program tracker saldo e-wallet 

# KAMUS
# saldo : int
# N : int (jumlah transaksi)
# i : int (Pengulangan)
# t : int (Nilai transaksi pada transaksi ke-i)
# saldo_negatif : int (Ketika saldo menyentuh < Rp 0.)
# total_income : int 
# total_outcome : int 

saldo = int(input('Masukkan saldo awal (Rp): '))
N = int(input('Masukkan jumlah transaksi (N):'))

saldo_negatif = 0
total_income = 0
total_outcome = 0

#
for i in range(1, N + 1):
    t = int(input(f'Masukkan transaksi ke-{i} (Rp): '))
    saldo += t
    print(f'saldo setelah transaksi ke-{i}: Rp{saldo} ')

# cek kapan pertama kali negatif
    if saldo < 0 and saldo_negatif == 0:
        saldo_negatif = i


# akumulasi income dan outcome
    if t > 0:
        total_income += t
    elif t < 0:
        total_outcome += t

# output saldo kalau negatif 
    if saldo_negatif != 0:
        print(f'saldo pertama kali negatif pada transaksi ke-{saldo_negatif}.')
    else:
        print(f'saldo tidak pernha negatif selama {N} transaksi, ')



# output pemasukan dan pengeluaran 
print(f'total_income: Rp{total_income}. total_outcome: Rp{total_outcome}.')
