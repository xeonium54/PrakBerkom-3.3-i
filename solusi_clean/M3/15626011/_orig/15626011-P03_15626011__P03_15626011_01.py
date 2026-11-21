# Nama  : Vidia Nurafifa
# NIM   : 15626011
# Desc  : No 1 - Simulasi Saldo E-Wallet

# saldo awal (S)
# jumlah transaksi (N)
# total pengeluaran (tpl) & total pemasukkan (tpm)
# array transasksi T[]
# negatif pertama (np)

S = int(input("Masukkan saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))

T = []
tpm = 0 
tpl = 0 
np = 0 

for i in range(N):
    nilai = int(input("Masukkan nilai transaksi ke-"+ str(i+1) + ": "))
    T.append(nilai)
  
for i in range(N):
    S = S+T[i]
    
    if T[i] > 0:
        tpm = tpm + T[i]
    elif T[i] < 0:
        tpl = tpl + T[i]
        
    print("Saldo setelah transaksi ke-"+ str(i+1) + ": Rp"+ str(S) +".")
    
    if S < 0 and np == 0:
        np = i+1 

if np !=0:
    print("Saldo Tuan Mik pertama kali negatif pada transaksi ke-"+ str(np) +".")
else:
    print("Saldo Tuan Mik tidak pernah negatif selama"+ str(N) +"transaksi.")
    
print("Total Pemasukan : Rp"+ str(tpm) +". Total Pengeluaran : Rp"+ str(tpl) +".")