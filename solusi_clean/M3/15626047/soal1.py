# NIM/Nama: 15626047
# Tanggal: 28 Oktober 2026
# Deskripsi: Mengetahui saldo, pemasukan, dan pengeluaran

#Kamus
saldo=int
n=int
pemasukan=int
pengeluaran=int

#ALGORITMA
saldo=int(input("Masukkan saldo awal (Rp):"))
n=int(input("Masukan Jumlah transaksi (N):"))
pemasukan = 0
pengeluaran = 0
negatif_pertama=-1
cat_saldo = []

for i in range (1, n+1):
    transaksi=int(input(f"Masukkan nilai transaksi ke-{i}:"))
    saldo += transaksi

    cat_saldo.append(f"Saldo setelah transaksi ke-{i}: Rp{saldo}")

    if saldo < 0 and negatif_pertama==-1:
        negatif_pertama= i

    if transaksi > 0:
        pemasukan += transaksi
    else :
        pengeluaran += transaksi

for cat in cat_saldo:
    print(cat)

if negatif_pertama != -1:
    print (f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{negatif_pertama}.")
else :
    print (f"Saldo Tuan Mik tidak pernah negatif selama {n} transaksi.")

print(f"Total pemasukan: Rp {pemasukan}. Total pengeluaran: Rp {pengeluaran}")