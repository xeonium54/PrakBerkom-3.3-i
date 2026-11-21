# Input Saldo Awal dan JUmlah Transaksi
saldo = int(input("Masukkan saldo awal (Rp): "))
n = int(input("Masukkan jumlah transaksi (N): "))

#Pemisalan variabel
saldo_history = []
total_pemasukan = 0
total_pengeluaran = 0
transaksi_negatif_pertama = -1

# input transaksi
for i in range (1, n + 1):
    transaksi = int(input(f"masukkan nilai transaksi ke-{i}: "))

    #hitung saldo sekarang
    saldo += transaksi
    saldo_history.append(saldo)

    # hitung total pemasukkan dan pengeluaran
    if transaksi > 0:
        total_pemasukan += transaksi
    elif transaksi < 0:
        total_pengeluaran += transaksi

    # transaksipertama yang membuat saldo kurang
    if saldo < 0 and transaksi_negatif_pertama == -1:
        transaksi_negatif_pertama = i

# saldo setelah transaksi
for i in range (1, n + 1):
    print(f"Saldo setelah transaksi ke{i}: Rp{saldo_history[i-1]}. ")

if transaksi_negatif_pertama != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{transaksi_negatif_pertama}. ")
else:
    print(f"saldo Tuan Mik tidak pernah negatif selama {n} transaksi. ")

print(f"total pemasukan: Rp{total_pemasukan}. ")
print(f"total pengeluaran: Rp{total_pengeluaran}. ")
