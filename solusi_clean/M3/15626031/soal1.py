#Alfathir Sangkara Anindya -15626031
#10/28/2026
#Deskripsi

saldo = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

pemasukan = 0
pengeluaran = 0
transaksi_negatif = 0

for i in range(1, N + 1):
    nilai = int(input(f"Masukkan nilai transaksi ke-{i}: "))

    saldo += nilai

    if nilai > 0:
        pemasukan += nilai
    elif nilai < 0:
        pengeluaran += nilai

    if saldo < 0 and transaksi_negatif == 0:
        transaksi_negatif = i

    print(f"Saldo setelah transaksi ke-{i}: Rp{saldo}")

if transaksi_negatif != 0:
    print(
        f"Saldo Tuan Mik pertama kali negatif "
        f"pada transaksi ke-{transaksi_negatif}."
    )
else:
    print(
        f"Saldo Tuan Mik tidak pernah negatif "
        f"selama {N} transaksi."
    )

print(f"Total pemasukan: Rp{pemasukan}")