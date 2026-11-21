#Nama: Febrian Yafi Hakim
#NIM: 15626042
#Deskripsi : problem 1

saldo = int(input("Masukkan saldo awal (Rp): "))
n = int(input("Masukkan jumlah transaksi (N): "))

transaksi = [0 for i in range(n)]

for i in range(n) :
    transaksi[i] = int(input("Masukkan nilai transaksi ke-" + str(i+1) + ": ")) 

total_pemasukan = 0 
total_pengeluaran = 0
transaksi_negatif_pertama = -1

for i in range(n) :
    nilai = transaksi[i]
    saldo += nilai

    if (nilai > 0):
        total_pemasukan += nilai
    elif (nilai < 0):
        total_pengeluaran += nilai
        
    print("Saldo setelah transaksi ke-" + str(i + 1) + ": Rp" + str(saldo) + ".")
    
    if (saldo < 0) and (transaksi_negatif_pertama == -1):
     transaksi_negatif_pertama = i + 1

if (transaksi_negatif_pertama != -1):
    print("Saldo Tuan Mik pertama kali negatif pada transaksi ke-" + str(transaksi_negatif_pertama) + ".")

print("Total pemasukan: Rp" + str(total_pemasukan) + ". Total pengeluaran: Rp" + str(total_pengeluaran) + ".")