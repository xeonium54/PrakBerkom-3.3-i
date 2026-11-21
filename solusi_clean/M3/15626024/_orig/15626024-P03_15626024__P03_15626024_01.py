# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 28 October 2026
# Deskripsi : Program yang mengecek dan menghitung sebuah transaksi dan apakah saldo dari transaksi
# dapat mencapai nilai negatif

# Kamus
# Saldo (int) memuat nilai saldo awal
# N (int) memuat berapa kali transaksi terjadi
# Income (int) memuat nilai awal pemasukan
# Outcome (int) memuat nilai awal pengerluaran
# TrMin (int) menghitung rentang di mana saldo sudah mencapai negatif
# Tr (int) memuat nilai transaksi ke i


# Algoritma
Saldo = int(input("Masukkan saldo awal: Rp "))
N = int(input("Masukkan jumlah transaksi "))
Income = 0
Outcome = 0
TrMin = -1



for i in range (1, N+1):
    Tr = int(input(f"Masukkan Nilai transaksi ke {i}: "))
    Saldo += Tr
    
    if Tr > 0:
        Income += Tr
    else:
        Outcome += Tr
    print(f"Saldo setelah transaksi ke-{i} adalah: Rp {Saldo}")

    if Saldo < 0 and TrMin == -1:
        TrMin = i

if TrMin != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke {TrMin}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi.")

print(f"Total pemaasukkan Rp {Income}. Total pengeluaran: Rp {Outcome}.")
