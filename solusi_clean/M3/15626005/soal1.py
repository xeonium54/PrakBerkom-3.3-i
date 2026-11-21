# NIM/Nama : Addien Maulana Bima
# Tanggal : 28 Oktober 2026
# Deskripsi : Program Pemantau Saldo 

s = int(input("Masukkan saldo awal (Rupiah) : "))
n = int(input("Masukkan jumlah transaksi : "))

total_pemasukan = 0
total_pengeluaran = 0
negatif_pertama = -1
riwayat = []

for i in range (1, n+1):
    transaksi = int(input(f"Masukkan nilai transaksi ke-{i} : "))
    s+= transaksi
    riwayat.append ((i, s))

    if transaksi > 0:
        total_pemasukan+=transaksi
    else:
        total_pengeluaran += transaksi
        
    if s < 0 and negatif_pertama == -1:
        negatif_pertama = i

for i, saldo in riwayat:
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}.")

if negatif_pertama != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{negatif_pertama}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {n} transaksi.")

print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluaran: Rp{total_pengeluaran}.")



    