# NIM / NAMA : 15626026 / MUTHI'AH AZKA NIAMILLAH
# TANGGAL : RABU, 28 OKTOBER 2026
# DESKRIPSI : SOAL 1

saldo = int(input("Masukkan saldo awal (Rp): "))
n = int(input("Masukkan jumlah transaksi (N): "))

total_pemasukkan = 0
total_pengeluaran = 0
transaksi_negatif_pertama = 0

for i in range(1, n + 1):
    print("masukkan nilai transaksi ke-", i, ":")
    transaksi = int(input())

    if transaksi > 0:
        total_pemasukkan = total_pemasukkan + transaksi
    else:
        total_pengeluaran = total_pengeluaran + transaksi
    
    saldo = saldo + transaksi
    print("saldo setelah transaksi ke-", i,": Rp")

if transaksi_negatif_pertama > 0:
    print("saldo tuan mik pertama kali negatif pada transaksi ke-", transaksi_negatif_pertama)
else: 
    print("saldo tuan mik tidak pernah negatif selama", n, "transaksi")