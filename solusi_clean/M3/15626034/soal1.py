#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 28 Oktober 2026
#Deskripsi : Program penghitung saldo

saldo_awal = int(input("Masukkan saldo awal Rp : "))
N = int(input("Masukkan jumlah transaksi N: "))
transaksi = []
saldo_setelah = []
for i in range(1, N + 1):
    nilai = int(input(f"Masukkan nilai transaksi ke-{i} Rp : "))
    transaksi.append(nilai)
saldo_sekarang = saldo_awal
transaksi_negatif_pertama = None
for i in range(N):
    saldo_sekarang += transaksi[i]
    saldo_setelah.append(saldo_sekarang)
    if saldo_sekarang < 0 and transaksi_negatif_pertama is None:
        transaksi_negatif_pertama = i + 1
total_pemasukan = 0
total_pengeluaran = 0
for t in transaksi:
    if t > 0:
        total_pemasukan += t
    else:
        total_pengeluaran += (-t)
for i in range(N):
    print(f"Saldo setelah transaksi ke-{i + 1}: Rp {saldo_setelah[i]}")
if transaksi_negatif_pertama is not None:
    print(f"Saldo tuan pertama kali menjadi negatif setelah transaksi ke-{transaksi_negatif_pertama}")
else:
    print("Saldo tuan tidak pernah menjadi negatif")

print(f"Total pemasukan: Rp {total_pemasukan}")
print(f"Total pengeluaran: Rp {total_pengeluaran}")
