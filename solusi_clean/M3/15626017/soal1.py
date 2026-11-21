# NIM/Nama      : 15626017 / Naura Vira Vania Ramadhani 
# Berpikir Komputasional ITB
# Tanggal       : 28 Oktober 2026
# Deskripsi     : Program simulasi e-wallet untuk memantau saldo harian, 
#                 mencari transaksi pertama yang membuat saldo negatif, 
#                 serta menghitung total pemasukan dan pengeluaran.

# Meminta masukan saldo awal dan jumlah transaksi 
saldo = int(input("Masukkan saldo awal (Rp): "))
N = int(input(" jumlah transaksi (N): "))

# Inisialisasi variabel pelacak 
transaksi_pertama_negatif = -1
total_pemasukan = 0
total_pengeluaran = 0 

# Menggunakan pengulangan untuk memproses setiap transaksi 
for i in range(1, N + 1):
    nilai_transaksi = int(input(f"Masukkan nilai transaksi ke-{i}"))

    # Memperbarui saldo 
    saldo += nilai_transaksi 

    # Mencatat saldo setelah transaksi 
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}.")

    # Memeriksa total pemasukkan dan pengeluaran
    if saldo < 0 and transaksi_pertama_negatif == -1:
        transaksi_pertama_negatif = i

    # Memisahkan total pemasukan dan pengeluaran 
    if nilai_transaksi > 0:
        total_pemasukan += nilai_transaksi 
    else:
        total_pengeluaran += nilai_transaksi

# Menampilkan hasil akhir pengecekan saldo negatif 
if transaksi_pertama_negatif != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{transaksi_pertama_negatif}.")
else:
    total_pengeluaran += nilai_transaksi 

# Menampilkan hasil akhir pengecekan saldo negatif 
if transaksi_pertama_negatif != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{transaksi_pertama_negatif}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi.")

# Menampilkan total pemasukan dan pengeluaran
print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluaran: Rp{total_pengeluaran}.")