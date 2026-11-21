# NIM/Nama : 15426126 
# Tanggal  : 28 Oktober 2026
# Deskripsi: Menghitung saldo e-wallet dan transaksi

saldo = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

pemasukan = 0
pengeluaran = 0
pertama_negatif = 0

for i in range(1, N + 1):
    transaksi = int(input("Masukkan nilai transaksi ke-" + str(i) + ": "))

    # Perbarui saldo
    # TODO: saldo ditambah transaksi

    # Hitung total pemasukan dan pengeluaran
    if transaksi > 0:
        # TODO: tambahkan transaksi ke pemasukan
        pass
    elif transaksi < 0:
        # TODO: tambahkan transaksi ke pengeluaran
        pass

    print("Saldo setelah transaksi ke-" + str(i) + ": Rp" + str(saldo))

    # Catat transaksi pertama saat saldo negatif
    # TODO: periksa saldo dan pertama_negatif

if pertama_negatif == 0:
    print("Saldo Tuang Mik tidak pernah negatif selama " + str(N) + " transaksi.")
else:
    print("Saldo Tuang Mik pertama kali negatif pada transaksi ke-" + str(pertama_negatif) + ".")

print("Total pemasukan: Rp" + str(pemasukan) + ". Total pengeluaran: Rp" + str(pengeluaran) + ".")
