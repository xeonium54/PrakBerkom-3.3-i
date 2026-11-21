# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 28 Oktober 2026
# Deskripsi : Menghitung pemasukan dan pengeluaran dari e-wallet
#           tuan mik dan mencari kapan saldonya pertamakali 
#           menjadi negatif(jika pernah), serta mengetahui total
#           seluruh pengeluaran dan pemasukan secara terpisah

# KAMUS
# Saldo_i = int
# N = int = jumlah transaksi
# T1 = int = Transaksi pertama
# T2 = int = transaksi kedua
# T3 = int = transaksi ketiga

# ALGORITMA
S = int(input("Masukkan saldo awal (Rp) "))
N = int(input("Masukkan jumlah transaksi (N)"))

saldo = S
masuk = 0
keluar = 0
minus_1 = 0

for i in range(1, N + 1):
    trans = int(input("Masukkan nilai transaksi ke- "))
    saldo = saldo + trans
    print("Saldo setelah transaksi ke- " , saldo)

    if trans > 0:
        masuk = masuk + trans
    elif trans < 0:
        keluar = keluar + trans
    if saldo < 0 and minus_1 == 0:
        minus_1 = i

if minus_1 == 0:
    print("Saldo Tuan Mik tidak pernah negatif selama" , N , "transaksi")
else:
    print("Saldo Tuan Mik pertamakali negatif pada transaksi ke-" , minus_1)

print("Total pemasukan: " , masuk)
print("Total pengeluaran: " , keluar)