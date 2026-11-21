#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal : 28 Oktober 2026

#Program Pemantau Saldo E-Wallet

saldo = int(input("Masukkan saldo awal (Rp): "))
n = int(input("Masukkan jumlah transaksi (N): "))

Jumlah_Pemasukan = 0
Jumlah_Pengeluaran = 0
transaksi_negatif_1 = 0
sudah_negatif = False

for i in range(1, n +1):
    transaksi = int(input(f"Masukkan nilai transaksi ke -{i}: "))

    if transaksi > 0:
        Jumlah_Pemasukan += transaksi 
    else:
        Jumlah_Pengeluaran += abs(transaksi)

    saldo += transaksi
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}.")

    if saldo < 0 and not sudah_negatif:
        transaksi_negatif_1 = 1
        sudah_negatif = True

    if sudah_negatif:
        print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{transaksi_negatif_1}.")
    else:
        print("Saldo Tuan Mik tidak pernah negatif selama transaksi.")

    print(f"Total Pemasukan: Rp{Jumlah_Pemasukan}. Jumalh Pengeluaran: Rp{Jumlah_Pengeluaran}")
 