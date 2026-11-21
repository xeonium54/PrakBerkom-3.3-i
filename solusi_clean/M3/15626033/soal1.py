# NIM = 15626033
# Nama = Farah Ghiza Humairoh
# Deskripsi = pada transaksi ke berapa saldo tuan mik pertama kali menjadi negative
# S = integer {saldo awal}
# N = integer {jumlah transaksi}


S = int(input("masukkan saldo awal (S): "))
N = int(input("masukkan jumlah transaksi (N): "))

saldo = S
total_pemasukan = 0
total_pengeluaran = 0
first_negative = 0

for i in range (1, N + 1):
    T = int(input(f"masukkan nilai transaksi ke-{i}: "))
    saldo += T
    print(f"--> saldo setelah transaksi ke-{i}: Rp {saldo}")
    if T > 0:
        total_pemasukan += T
    elif T < 0:
        total_pengeluaran += abs(T)
    if saldo < 0 and first_negative == 0:
        first_negative = i
print("\n=== RINGKASAN DATA ===")
print(f"total pemasukkan : Rp {total_pemasukan}")
print(f"total pengeluaran: Rp {total_pengeluaran}")
if first_negative > 0:
    print(f"saldo pertama kali menjadi negative pada transaksi ke-: {first_negative}")
else:
    print(f"saldo tidak pernah menjadi negative.")