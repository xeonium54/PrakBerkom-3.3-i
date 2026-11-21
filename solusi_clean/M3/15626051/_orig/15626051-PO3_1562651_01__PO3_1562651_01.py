saldo = int(input("masukan saldo awal(Rp): "))
N = int(input("Masukan jumlah transaksi (N): "))

T = [0 for i in range(N)]
for i in range(N):
    T[i] = int(input("masukan nilai transaksi ke-" + str(i + 1) + ": "))

total_masuk = 0
total_keluar = 0
negatif_ke = 0

for i in range(N):
   saldo = saldo + T[i]
   print("saldo setelah transaksi ke-" + str(i + 1) + ": Rp" + str(saldo) + "." )
   if T[i] > 0:
       total_masuk = total_masuk + T[i]
   elif T[i] < 0:
       total_keluar = total_keluar + T[i]

    

if negatif_ke == 0:
    print("saldo anda tidak pernah negatif selama" + str(N)+"transaksi.")
else:
    print("saldo anda pertama kali negatif pada transaksi ke-" + str(negatif_ke)+ ".")

print("total pemasukan: Rp" + str(total_masuk) + ". total pengeluaran: Rp" + str(total_keluar)+ ".")