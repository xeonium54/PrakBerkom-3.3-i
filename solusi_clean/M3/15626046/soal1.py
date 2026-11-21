#KAMUS
#S: INTEGER, saldo awal
#n: integer, jumlah transaksi
# saldo: integer, saldo abis transaksi
# pemasukan: int, total pemasukan
# pengeluaran : int, total pengeluaran
# pertama-negatif : int, transaksi pertama saat saldo negatif
#i : int, pengulangan

S  = int(input("masukan saldo awal (Rp)"))
N = int(input("masukan jumlah transaksi(N)"))
Saldo = S
Pemasukan = 0
pengeluaran = 0
pertama_negatif = 0
S = for i in range(1, N+1 )
transaksi = int (input("masukan transaksi ke{i}"))

saldo = saldo + transaksi
if transaksi < 0:
pengeluaran + transaksi
elif transaksi > 0:
  pemasukan + transaksi
  print("saldo setelah transaksi ke {i}:Rp {saldo}")
if saldo <0 and pertama_negatif == 0:
  pertama_negatif = i
  print("total pemasukan: rp {pemasukan}, total pengeluaran: rp{pengeluaran}")

