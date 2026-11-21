# Nama/NIM: Maria Amatussyafee Nurjaman/15626025
# Tanggal: 28/10/2026
# Deskripsi: Program memantau saldo

# KAMUS
# S : integer
# N : integer
# t : integer

S = int(input("Saldo awal (RP): "))
N = int(input("Masukan jumlah transaksi: "))

saldo = S
pertama_negatif = 0
total_masuk = 0
total_keluar = 0

for i in range (1, N + 1):
    t = int(input(f"Masukan nilai transaksi ke-{i}: "))
    saldo += t

    if t > 0: 
        total_masuk += t
    else:
        total_keluar += -t

    if saldo < 0 and pertama_negatif == 0:
        pertama_negatif = i

    if saldo < 0:
        print(f"Saldo setelah transaksi ke-{i}: Rp-{-saldo}")
    else:
        print(f"Saldo setelah transaksi ke-{i}: Rp{saldo} ")

    if pertama_negatif != 0:
        print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{pertama_negatif}")
    else:
        print(f"Saldo Tuan Mik tidak pernah negatif")

    print(f"Total pemasukan: Rp{total_masuk}. Total pengeluaran: Rp-{total_keluar}")

