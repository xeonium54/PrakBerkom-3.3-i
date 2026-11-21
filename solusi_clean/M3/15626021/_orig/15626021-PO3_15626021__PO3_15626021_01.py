# NIM/Nama  : 15626021 / Aufaa Fakhri Ibrahim Irahadi
# Tanggal   : 28 Oktober 2026 
# Deskripsi : Program pemantauan saldo e-wallet, pelacakan saldo negatif pertama, serta perhitungan total pemasukan dan pengeluaran

# KAMUS VARIABEL
# saldo_awal                : int
# N                         : int
# saldo                     : int
# transaksi_negatif_pertama : int
# total_pemasukan           : int
# total_pengeluaran         : int
# i                         : int
# nilai_transaksi           : int

# Algoritma
saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

saldo = saldo_awal
transaksi_negatif_pertama = -1
total_pemasukkan = 0
total_pengeluaran = 0

for i in range (1, N + 1):
    nilai_transaksi = int(input(f"Masukkan nilai transaksi ke-{i}: "))
    saldo += nilai_transaksi

    # Menampilkan saldo setelah transaksi ke-i
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}.")

    # Melacak kapan saldo pertama kali negatif
    if saldo < 0 and transaksi_negatif_pertama == -1:
        transaksi_negatif_pertama = i

    # Memisahkan total pemasukan dan total pengeluaran
    if nilai_transaksi > 0:
        total_pemasukkan += nilai_transaksi
    else:
        total_pengeluaran += nilai_transaksi

# Menampilan informasi saldo negatif pertama kali
if transaksi_negatif_pertama != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{transaksi_negatif_pertama}")
else:
    print(f"Saldo Tuan Mik pernah negatif selama {N} transaksi")

# Menampilkan total pemasukan dan pengeluaran
print(f"Total pemasukan: Rp{total_pemasukkan}. Total Pengeluaran: Rp{total_pengeluaran}")
