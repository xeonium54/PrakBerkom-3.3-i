# NIM/Nama : 15626004 / Nirmala Rahma Maulida
# Tanggal : 28 Oktober 2026
# Deskripsi : Program untuk menghitung total pemasukkan dan total pengeluaran pada aplikasi e-wallet

# KAMUS
# S, N, saldo, total_pemasukkan, total_pengeluaran, transaksi_negatif pertama: int
 
#ALGORITMA
S = int(input("masukkan saldo awal (Rp) = "))
N = int(input("masukkan jumlah transaksi (N) = "))

saldo = S
total_pemasukan = 0
total_pengeluaran = 0
transaksi_negatif_pertama = -1
akhir_saldo = []

for i in range (1, N + 1):
    nilai_transaksi = int(input("Masukkan nilai transaksi: "))
    saldo += nilai_transaksi
    akhir_saldo

    if nilai_transaksi > 0:
        total_pemasukan += nilai_transaksi
    elif nilai_transaksi < 0:
        total_pengeluaran += (nilai_transaksi)

    if saldo < 0 and transaksi_negatif_pertama == -1:
        transaksi_negatif_pertama = i

for i in range(1, N + 1): 
    print("saldo setelah transaksi = ")

if transaksi_negatif_pertama != -1:
    print("saldo tuan mik pertama kali negatif pada transaksi ke-")


print("total pemasukkan", total_pemasukan, "total_pengeluaran", total_pengeluaran)




    