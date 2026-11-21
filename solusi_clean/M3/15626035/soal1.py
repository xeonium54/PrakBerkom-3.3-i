# NIM/Nama : 15626035/Naila Rahmah Zhafirah
# Tanggal : Rabu, 28 Oktober 2026
# Deskripsi : Menghitung saldo e-wallet Tuan Mik setelah beberapa kali transaksi

# KAMUS
saldo_awal = 0
N = 0
transaksi = 0
saldo = 0
total_pemasukan = 0
total_pengeluaran = 0
pertama_negatif = 0

# INPUT
saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N); "))

# Inisialisasi
saldo = saldo_awal

# Proses transaksi
for i in range(1, N + 1):
    transaksi = int(input("Masukkan nilai transaksi ke-" + str(i) + ": "))

    saldo = saldo + transaksi

    if transaksi > 0:
        total_pemasukan = total_pemasukan + transaksi
    else:
        if transaksi < 0:
            total_pengeluaran = total_pengeluaran + transaksi

        if saldo < 0:
            if pertama_negatif == 0:
                pertama_negatif = i
                
        print("Saldo setelah transaksi ke-" + str(i) + ": Rp" + str(saldo) + ".")

# Menampilkan saldo pertama kali negatif
if pertama_negatif == 0:
   print("Saldo Tuan Mik tidak pernah negatif selama" + str(N) + "transaksi.")
else:
    print("Saldo Tuan Mik pertama kali negatif pada transaksi  ke-" + str(pertama_negatif) + ".")

# Total pemasukan dan pengeluaran
print("Total pemasukan: Rp" + str(total_pemasukan))
print("Total pengeluaran: Rp" + str(-total_pengeluaran))
