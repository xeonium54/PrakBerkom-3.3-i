# NIM/NAMA : 15626050/YOHANES YOEL CHRISTOPHER NAIBAHO
# TANGGAL  : 28/10/2026
# DESKRIPSI:Memantau saldo miliknya setiap transaksi

# KAMUS 
# S, N, Saldo, pemasukan, pengeluaran, negatif , i : int
# transaksi : array [0.. N-1] of int

# ALGORITMA
S = int(input("Input Saldo awal Tuan Mik(Rp): "))
N = int (input("Berapa kali Tuan Mik melakukan transaksi(N) : "))

saldo = S
pemasukan = 0
pengeluaran = 0
negatif = 0

for i in range(0, N):
    transaksi = int(input("transaksi ke-" + str(i + 1) + ": "))
    saldo = saldo + transaksi
    if transaksi > 0:
        pemasukan = pemasukan + transaksi
    elif transaksi < 0:
        pengeluaran= pengeluaran + transaksi[i]
        
    if saldo < 0 and negatif == 0:
        negatif = i + 1

if negatif != 0:
    print("pertama negatif pad transaksi ke-", negatif)
else:
    print("Saldo Tuan Mik tak pernah negatif selama",N, "transaksi")
    
print("total pemasukan:", pemasukan)
print("total pengeluaran:", pengeluaran)