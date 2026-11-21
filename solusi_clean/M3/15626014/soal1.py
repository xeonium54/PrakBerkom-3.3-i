#Nama : Fadhil Zulhilmi
#NIM : 15626014
#Deskripsi : Membuat program untuk memantau saldo e-wallet berdasarkan transaki

saldo = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

saldo_awal = saldo
total_pemasukan = 0
total_pengeluaran = 0
pertama_negatif = 0

for i in range (1 , N + 1):
    transaksi = int(input("Masukkan nilai ransaksi k-{i}: "))

    saldo += transaksi

    if transaksi > 0:
        total_pemasukan += transaksi
    elif transaksi < 0:
        total_pengeluaran += transaksi

    if saldo < 0 and pertama_negatif == 0:
        pertama_negatif = i

    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}")

    if pertama_negatif == 0:
        print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi. ")
    else:
        print(f"Saldo Tuan Mik pertama kali negatif pada transaksi k-{pertama_negatif}. ")

    print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluran: Rp{total_pengeluaran}.")


