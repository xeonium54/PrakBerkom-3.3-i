# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 28 Oktober 2026
# Deskripsi : Saldo e-Wallet

saldo_awal = int(input('Masukkan saldo awal:'))
n = int(input('Masukkan jumlah transaksi:'))

transaksi = []
for i in range (1,n+1):
 nilai =int(input(f"Masukkan nilai transaksi ke-{i} :"))
 transaksi.append(nilai)

saldo = saldo_awal
pert_negatif = 0
total_masuk = 0
total_keluar = 0

for i in range (n):
 saldo += transaksi [i]
 print(f"Saldo setelah transaksi ke {i + 1} + {saldo}")

 if saldo < 0 and pert_negatif == 0:
  pert_negatif = i + 1

 if transaksi[i] > 0:
  total_masuk += transaksi[i]
 else:
  total_keluar += transaksi[i]

if pert_negatif == 0:
 print(f"Saldo tidak pernah negatif selama {n} transaksi")
else:
 print(f'Saldo pertama kali negatif pada transaksi ke {pert_negatif}')

print(f"Total pemasukkan : Rp{total_masuk} dan Total pengeluaran : Rp{total_keluar}")
 
