# NIM/Nama: 15426126
# Tanggal : 28 Oktober 2026
# Deskripsi: Menghitung saldo e-wallet dan transaksi

saldo = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

pemasukan = 0
pengeluaran = 0
pertama_negatif = 0

for i in range(1, N + 1):
    transaksi = int(input("Masukkan nilai transaksi ke-" + str(i) + ": "))
    
    # Perbarui saldo
    saldo += transaksi
    
    # Hitung total pemasukan dan pengeluaran
    if transaksi > 0:
        pemasukan += transaksi
    elif transaksi < 0:
        pengeluaran += abs(transaksi)
        
    print("Saldo setelah transaksi ke-" + str(i) + ": Rp" + str(saldo))
    
    # Catat transaksi pertama saat saldo negatif
    if saldo < 0 and pertama_negatif == 0:
        pertama_negatif = i

if pertama_negatif == 0:
    print("Saldo Tuan Mik tidak pernah negatif selama " + str(N) + " transaksi.")
else:
    print("Saldo Tuan Mik pertama kali negatif pada transaksi ke-" + str(pertama_negatif) + ".")
    
print("Total pemasukan: Rp" + str(pemasukan) + ". Total pengeluaran: Rp" + str(pengeluaran) + ".")