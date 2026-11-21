# NIM/Nama: Frizka Yunisaf 15626040
# Tanggal: 28 Oktober 2026
# Deskripsi: Pemantauan saldo setelah setiap transaksi gune mengetahui pada transaksi ke berapa saldonya pertama kali menjadi negatif dan total seluruh pemasukkan dan pengeluaran secara terpisah.

S = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

transaksi = [0 for i in range (N)]
for i in range (N):
    transaksi[i] = int(input("Masukkan nilai transaksi ke-" + str(i+1) + ":"))

saldo = S
pemasukan = 0
pengeluaran = 0
N1 = 0

for i in range (N):
    nilai = transaksi[i]
    saldo += nilai
    print ("Saldo setelah transaksi ke-"+ str(i+1)+":Rp" + str(saldo) + ".")

    if nilai >0:
        pemasukan += nilai
    if nilai <0:
        pengeluaran += nilai
    if saldo < 0 and N1 == 0:
        N1 = i+1

if N1 == 0:
    print("Saldo Tuan Mik tidak pernah negatif selama " + str(N) + "transaksi.")

else:
    print("Saldo Tuan Mik pertama kali negatif pada transaksi ke- " + str(N1) + ".")

print("Total pemasukan: Rp " + str(pemasukan) + ". Total pengeluaran: Rp "+ str(pengeluaran) + ".")