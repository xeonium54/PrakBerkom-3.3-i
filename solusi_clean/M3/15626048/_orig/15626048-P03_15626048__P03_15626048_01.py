# Nama: Siti Nawa Aulia
# NIM: 15626048
# Deskripsi: Pogram pemantauan saldo transaksi yang dimiliki Tuan Mik pada aplikasi e-wallet

# Kamus
# saldo: int
# N: int

# Algoritma
s = int(input("Masukan nominal saldo awal:"))
n = int(input("Masukan jumlah transaksi (N):"))

transaksi = []

for i in range(n):
    nilai = int(input("Masukan nilai transaksi ke-", str(i+1) + ": "))
    transaksi.append(x)
    
total_pemasukan = 0
total_pengeluaran = 0
transaksi_negatif = -1 

for i in range (n):
    saldo = saldo + transaksi[i]
    
    if transaksi[i] > 0:
        total_pemasukan = total_pemasukan + transaksi[i]
    elif transaksi[i] < 0:
        total_pengeluaran = total_pemasukan + transaksi[i]
        
    print("Saldo setelah transaksi ke-" + str(i+1) + ": Rp" + str(saldo) + ".")
    
    
    if saldo < 0 and transaksi_negatif == -1:
        transaksi_negatif = i + 1 
        
if transaksi_negatif != -1:
    print("Saldo pertama kali negatif pada transaksi ke-:", str(transaksi_negatif) + ".")
else:
    print("Saldo tidak pernah negatif.")
    
print("Total pemasukan: Rp" + str(total_pemasukan) + ". Total pengeluaran: Rp" + str(total_pengeluaran) + ".")