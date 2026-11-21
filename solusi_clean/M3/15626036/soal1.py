#Nama/NIM: Aghneo Amar Ahsan
#Tanggal: 28 Oktober 2026
#Deskripsi: 

#Kamus : 

saldo = int(input("Masukkan saldo awal (RP): "))

Transaksi = int(input("Masukkan jumlah transaksi: "))

TransaksiArray = []
for i in range (Transaksi): 
    masukkan = int(input(f"Masukkan nilai transaksi ke-{i+1}: "))
    TransaksiArray.append(masukkan)

saldo_setelah = saldo
setelah_transaksi_array = []
for i in range (Transaksi): 
    saldo_setelah = saldo_setelah + TransaksiArray[i]
    setelah_transaksi_array.append(saldo_setelah)
    print(f"Saldo setelah transaksi ke-{i+1}: Rp.", saldo_setelah)

pemasukan = 0
pengeluaran = 0
for i in range (Transaksi): 
    if setelah_transaksi_array[i] < 0:
        print(f"Saldo Tuan Mik pertama kali negatif pada transaksi ke-{i+1}")

    if TransaksiArray[i] < 0:
        pengeluaran = pengeluaran + TransaksiArray[i]
    elif TransaksiArray[i] >= 0:
        pemasukan = pemasukan + TransaksiArray[i]

print("Total Pemasukan: Rp.", pemasukan,"Total Pengeluaran: Rp.", pengeluaran )
    


