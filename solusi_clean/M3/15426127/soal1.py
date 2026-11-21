# NIM/nama : Luna Febryvazrya
# Tanggal : 28 Oktober 2026
# Deskripsi :

saldo = int(input("Masukkan saldo awal (Rp): "))
transaksi = int(input("Masukkan jumlah transaksi (N): "))
transaksi_1 = int(input("Masukkan nilai transaksi ke-1: "))
transaksi_2 = int(input("Masukkan nilai transaksi ke-2: "))
transaksi_3 = int(input("Masukkan nilai transaksi ke_3: "))
A = int(input("Saldo setelah transaksi ke-1: "))
B = int(input("Saldo setelah transaksi ke-2: "))
C = int(input("Saldo setelah transaksi ke-3: "))

saldo_negatif_pertama = -1
total_pemasukan = 0
total_pengeluaran = 0

for i in range(1, n+1):
    nilai_transaksi = transaksi_1

    saldo += nilai_transaksi

    if nilai_transaksi > 0:
        total_pemasukan += nilai_transaksi
    else:
        total_pengeluaran += abs(nilai_transaksi)

        if saldo < 0 and saldo_negatif_pertama == -1:
            saldo_negatif_pertama = i 

            print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}.")

            if saldo_negatif_pertama != -1:
            print(f"Saldo tuan mik pertama kali negatif pada transaksi ke-{saldo_negatif_pertama}")
print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluaran: Rp-{total_pengeluaran}.")
