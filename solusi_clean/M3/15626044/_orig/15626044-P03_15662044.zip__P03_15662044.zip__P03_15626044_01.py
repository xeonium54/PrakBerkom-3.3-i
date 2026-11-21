# NIM/Nama: 15626044/Saliha Mahira Al-kwarismy
# Tanggal: 28 Oktober 2026
# Deskripsi: Problem 1

# Saldo awal pengguna
saldo = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N):"))

# variabel awal
total_pemasukan = 0
total_pengeluaran = 0
hitung_transaksi = 0
negatif = 0

# Pengulangan jumlah transaksi sebanyak N
for i in range (1, N + 1):
    nilai_transaksi = int(input(f"Masukkan nilai transaksi ke-{i}: "))

    saldo = saldo + nilai_transaksi
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}")

    if nilai_transaksi > 0:
        total_pemasukan = total_pemasukan + nilai_transaksi

    if nilai_transaksi < 0:
        total_pengeluaran = total_pengeluaran + (nilai_transaksi * -1)

    if saldo < 0:
        if negatif == 0:
            hitung_transaksi = i
            negatif = 1

# Hasil akhir
if negatif > 0:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{hitung_transaksi}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi.")

print("Total pemasukan: Rp" + str(total_pemasukan) + ".Total pengeluaran: Rp" + str(total_pengeluaran))



