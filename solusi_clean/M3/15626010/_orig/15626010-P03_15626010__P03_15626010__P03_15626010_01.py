# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 28/10/2026
# Deskripsi : Program ini disusun untuk membantu Tuan Mik memantau perubahan saldo e-wallet miliknya secara berkala setelah melakukan transaksi pemasukan dan pengeluaran.

def main ():
    saldo_awal =  int(input("Masukkan saldo awal (Rp): "))
    n = int(input("Masukkan Jumlah transaksi (N): "))

    transaksi = []
    for i in range(n):
        nilai=int(input(f"Masukkan nilai transaksi ke-{i+1}: "))
        transaksi.append(nilai)

    total_pemasukan = 0
    total_pengeluaran = 0
    pertama_negatif = -1

    current_saldo = saldo_awal

    for i in range(n):
        nilai_transaksi = transaksi [i]
        if nilai_transaksi > 0:
            total_pemasukan += nilai_transaksi
        else:
            total_pengeluaran += nilai_transaksi

        current_saldo += nilai_transaksi
        print(f"Saldo setelah transaksi ke-{i+1}: Rp{current_saldo}")

        if current_saldo <0 and pertama_negatif == -1:
            pertama_negatif = i+1

    if pertama_negatif != -1:
        print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{pertama_negatif}.")
    else:
        print(f"Saldo Tuan Mik tidak pernah negatif selama {n} transaksi.")

    print(f"Total pemasukan: Rp{total_pemasukan}. Total pengeluaran: Rp{total_pengeluaran}")

if __name__ == "__main__":
    main()