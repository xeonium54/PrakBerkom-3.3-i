# Nama: Reyza Aulia Rahman
# NIM: 15426131
# Deskripsi: Duit pak iwan

# salwal: int (saldo awal, lalu diperbarui jadi saldo berjalan tiap transaksi)
# N: int (jumlah transaksi)
# i: int (indeks perulangan)
# nilai_transaksi: int (nilai transaksi)
# toma: int  (total pemasukan)
# toke: int (total pengeluaran) 
# perne: int (saldo sudah pernah negatif)
# make: int  (saldo pernah negatif)
# tranepe: int (nomor transaksi saat saldo pertama kali negatif)

salwal = int(input("Masukkan Saldo awal (Rp): "))
N = int(input("Masukkan jumlah transaksi (N): "))


perne = 0
toma = 0
toke = 0
make = 0

for i in range (1, N + 1):
    nilai_transaksi = int(input(f"Masukkan nilai transaksi ke-{i}:" ))
    salwal += nilai_transaksi

    if nilai_transaksi >= 0:
        toma += nilai_transaksi
       

    elif nilai_transaksi < 0:
        toke += nilai_transaksi
        
    print(f"Saldo setelah transaksi ke-{i+1}: Rp{salwal}")

    if salwal < 0 and perne == 0:
        make = 1
        tranepe = {N}
        perne = 1


    elif salwal < 0 and not perne == 0:
        print("")


           
    if  make == 1:
        print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{tranepe}")
    
    

    


print(f"Total Pemasukan: Rp{toma}, Total Pengeluaran: Rp{toke}")
   


    
    
    





