#P03_15626029_01
# Nama : Hanif Mahib Yassar Nuradiyatma
# NIM : 15626029
#desc: menentukan detail saldo tuan mik setelah transaksi

# Kamus
# s,t,nt, i,masuk,out = int

s=int(input("Masukan saldo awal: "))
t=int(input("Masukan jumlah transaksi"))

for i in range (1,n+1):
    t=int(input("Masukan nilai transaksi ke-",str(i),":"))

masuk = 0
for i in range (t):
    s += nt[i]
    if nt[i]>0:
     masuk += nt[i] 
    else: 
       out +=nt[i]
    if s>0 and min==0:
       min=i+1
    print("Saldo tuan mik pertama negatif setelah transaksi ke-", str(i+1),":",s )
    if min==0:
         print("saldo tuan mik tidak pernah negatif selama",n,"transaksi")
    else:
         print("Saldo tuan mik pertama kali negatif pada transaksi ke-",min)
    print("Total pemasukan:",masuk,".","Total pengeluaran",out)





 