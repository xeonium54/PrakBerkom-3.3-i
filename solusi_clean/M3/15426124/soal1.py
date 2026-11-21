# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 28 Oktober 2026
# Deskripsi : Program pemantau saldo

# Algoritma
saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (n): "))

transaksi = []
for i in range(N):
    nilai = int(input(f"Masukkan nilai transaksi ke-{i+1}: "))
    transaksi.append(nilai)
    
saldo = saldo_awal
pertama_negatif = -1
total_pemasukan = 0
total_pengeluaran = 0

for i in range(N):
    saldo += transaksi[i]
    print(f"Saldo setelah transaksi ke-{i+1}: Rp.{saldo}.")
    
    if saldo < 0 and pertama_negatif == -1:
        pertama_negatif = i + 1
        
    if transaksi[i] > 0:
        total_pemasukan += transaksi[i]
    else:
        total_pengeluaran += transaksi[i]
        
if pertama_negatif != -1:
    print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{pertama_negatif}.")
else:
    print(f"Saldo Tuan Mik tidak pernah negatif selama {N} transaksi.")

print(f"Total pemasukan: Rp.{total_pemasukan}. Total pengeluaran: Rp.{total_pengeluaran}.")