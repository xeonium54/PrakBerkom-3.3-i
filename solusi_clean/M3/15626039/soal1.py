# NIM/Nama : 15626039/Khalif Aufar Aridkhi
# Tanggal : 28 Oktober 2026
# Deskripsi : Nomer 1, Menghitung pemasukan dan pengeluaran saldo

# KAMUS
#s = int
#n = int
#nt = int
#i = int
#m = int
#k = int
#negatif = int


s = int(input("masukkan saldo awal (Rp):"))
n = int(input("Masukkan jumlah transaksi (N):"))

m = 0
k = 0
negatif = 0

for i in range(1, n + 1):
 nt = int(input("masukkan nilai transaksi ke-" + str(i) + ":"))
 s = s + nt

 if nt > 0:
  m = m + nt
 else:
  k = k - nt

 if s < 0 and negatif == 0:
  negatif = i
    
 print("saldo setelah transaksi ke-", i,":Rp", s)

if negatif == 0:
  print("Saldo Tuan Mik tidak pernah negatif selama {n} transaksi ")
else:
  print("Saldo Tuan Mik pertama kali negatif pada transaksi ke-", negatif)

print("Total pemasukan: Rp", m)
print("Total pengeluaran: Rp", k)