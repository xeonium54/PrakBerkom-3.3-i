# NIM/Nama : 15626001/Muhamad Naufal Al Fajri
# Tanggal : 28 Oktober 2026
# Deskripsi : 

s = int(input("Masukkan saldo awal (Rp): "))
n = int(input("Masukkan jumlah transaksi: "))
saldo = s
total_pemasukan = 0
total_pengeluaran = 0
transaksi_negatif = -1 
for i in range (1, n + 1):
    transaksi = int(input(f"Transaksi ke-{i}: "))
    if transaksi > 0:
        total_pemasukan += transaksi
    elif transaksi < 0:
        total_pengeluaran += -transaksi 
    saldo += transaksi
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}")
    if saldo < 0 and transaksi_negatif == -1:
        transaksi_negatif = i
        if transaksi_negatif == -1:
            print("Saldo tidak pernah menjadi negatif.")
        else:
            print("Saldo pertama kali menjadi negatif pada transaksi ke-",transaksi_negatif)

print("Total pemasukan: Rp", total_pemasukan)
print("Total pengeluaran: Rp", total_pengeluaran)