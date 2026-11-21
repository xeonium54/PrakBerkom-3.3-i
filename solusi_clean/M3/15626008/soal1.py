S = int(input("Masukkan saldo awal: "))
N = int(input("Masukkan jumlah transaksi: "))

transaksi = []

for i in range(N):
    nilai = int(input("Masukkan transaksi ke-" + str(i+1) + ": "))
    transaksi.append(nilai)

saldo = S
pemasukan = 0
pengeluaran = 0
transaksi_negatif = 0

for i in range(N):
    saldo = saldo + transaksi[i]

    if transaksi[i] > 0:
        pemasukan = pemasukan + transaksi[i]
    elif transaksi[i] < 0:
        pengeluaran = pengeluaran - transaksi[i]

    if saldo < 0 and transaksi_negatif == 0:
        transaksi_negatif = i + 1

    print("Saldo setelah transaksi ke-", i+1, ":", saldo)

print("Total pemasukan:", pemasukan)
print("Total pengeluaran:", pengeluaran)

if transaksi_negatif == 0:
    print("Saldo tidak pernah negatif")
else:
    print("Saldo pertama kali negatif pada transaksi ke-", transaksi_negatif)

print("Saldo akhir:", saldo)