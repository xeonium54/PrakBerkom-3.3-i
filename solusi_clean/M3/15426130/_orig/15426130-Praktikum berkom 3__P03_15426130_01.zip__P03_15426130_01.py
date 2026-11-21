# NIM/Nama  : 15426130 / Yudha Putra
# Tanggal   : 28 Oktober 2026
# Deskripsi : Memantau saldo e-wallet Tuan Mik setelah setiap transaksi,
#             transaksi pertama yang membuat saldo negatif, total pemasukan
#             dan total pengeluaran.

saldo_awal = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

# Array untuk menyimpan nilai setiap transaksi
transaksi = [0 for i in range(N)]
for i in range(N):
    transaksi[i] = int(input("Masukkan nilai transaksi ke-" + str(i + 1) + ": "))

saldo = saldo_awal
pertama_negatif = 0      # 0 artinya saldo belum pernah negatif
total_masuk = 0          # total transaksi bernilai positif
total_keluar = 0         # total transaksi bernilai negatif

for i in range(N):
    saldo += transaksi[i]
    print("Saldo setelah transaksi ke-" + str(i + 1) + ": Rp" + str(saldo) + ".")
    # Catat transaksi pertama yang membuat saldo negatif
    if saldo < 0 and pertama_negatif == 0:
        pertama_negatif = i + 1
    # Pisahkan pemasukan dan pengeluaran
    if transaksi[i] > 0:
        total_masuk += transaksi[i]
    elif transaksi[i] < 0:
        total_keluar += transaksi[i]

if pertama_negatif == 0:
    print("Saldo Tuan Mik tidak pernah negatif selama " + str(N) + " transaksi.")
else:
    print("Saldo Tuan Mik pertama kali negatif pada transaksi ke-" + str(pertama_negatif) + ".")

print("Total pemasukan: Rp" + str(total_masuk) + ". Total pengeluaran: Rp" + str(total_keluar) + ".")