# NIM / Nama : 15626006 / Maria Zeysta Kamelia Rumanti
# Tanggal : 28 Oktober 2026
# Deskripsi : 
# Pemrograman untuk membuat simulasi pelacakan saldo e-wallet yang menghitung dan menampilkan sisa saldo setelah setiap transaksi.
# Pemrograman juga diminta untuk bisa mendeteksi pada traksaksi ke-berapa saldo pertama kali menyentuh angka negatif.
# Menghitung rekapitulasi total keseluruhan pemasukan (nilai positif) dan pengeluaran (nilai negatif) secara terpisah di akhir.

# Input transaksi pengguna
saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

# Menyimpan data nilai transaksi
transaksi = []
for i in range (N):
    nilai = int(input(f"Masukkan nilai transaksi ke-{i+1}: "))
    transaksi.append(nilai)

total_pemasukan = 0
total_pengeluaran = 0
negatif_pertama = 0

riwayat_saldo = []

for i in range (N):
    saldo = saldo_awal + transaksi [i]
    riwayat_saldo.append(saldo)

    if saldo <0 and negatif_pertama == 0:
        negatif_pertama = i + 1

    if transaksi[i] >0:
        total_pemasukan = total_pemasukan + transaksi[i]
    elif transaksi[i] <0:
        total_pengeluaran = total_pengeluaran + transaksi[i]

for i in range (N):
    print(f"Saldo setelah transaksi ke-{i+1}: Rp{riwayat_saldo[i]}")

if negatif_pertama >0:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{negatif_pertama}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi.")

print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluaran: Rp{total_pengeluaran}.")