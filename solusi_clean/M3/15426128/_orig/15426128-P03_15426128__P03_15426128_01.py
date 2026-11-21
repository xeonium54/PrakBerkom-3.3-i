# NIM/Nama              : 15426128 / Fathir Sulihansyah
# Tanggal               : 28 Oktober 2026
# Deskripsi             : Program pemantau saldo e-wallet Tuan Mik, menghitung saldo setelah tiap transaksi, 
#                         mendeteksi kapan saldo pertama kali negatif, serta total pemasukan dan pengeluaran

# KAMUS KODING
# saldo_awal      : int   -> Nilai masukan sald awal e-wallet sebelum transaksi
# N               : int   -> Jumlah total transaksi yang akan dilakukan
# saldo_sekarang  : int   -> Variabel pelacak jumlah saldo terakhir setelah transaksi
# pertama_negatif : int   -> Menandai urutan transaksi ke berapa saldo pertama kali kurang dari 0
# total_pemasukan : int   -> Akumulator total seluruh nilai transaksi positif
# total_pengeluaran: int  -> Akumulator total seluruh nilai transaksi negatif
# i               : int   -> Variabel iterasi perulangan dari 1 hingga N
# nilai_transaksi : int   -> Besar nilai uang pada transaksi ke-i (positif/negatif)


saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

saldo_sekarang = saldo_awal
pertama_negatif = 0
total_pemasukan = 0
total_pengeluaran = 0

for i in range(1, N + 1):
    nilai_transaksi = int(input(f"Masukkan nilai transaksi ke-{i}: "))
    saldo_sekarang += nilai_transaksi
    
    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo_sekarang}.")
    
    if saldo_sekarang < 0 and pertama_negatif == 0:
        pertama_negatif = i
        
    if nilai_transaksi > 0:
        total_pemasukan += nilai_transaksi
    else:
        total_pengeluaran += nilai_transaksi

if pertama_negatif != 0:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{pertama_negatif}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi.")

print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluaran: Rp{total_pengeluaran}.")
