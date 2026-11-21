# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM mencari saldo tuan mik

# KAMUS
# Saldo awal = intreger
# Jumlah transaksi = intreger
# Saldo setelah transaksi = intreger

# ALGORITMA
sum_val=0

saldo_awal = int(input("Masukkan saldo awal:"))
Jumlah_Transaksi = int(input("Masukkan Jumlah transaksi:"))
Nilai_Transaksi = int(input("Masukkan nilai transaksi:"))

while Nilai_Transaksi<=0:
    Saldo_setelah_transaksi = saldo_awal - Nilai_Transaksi
    print(f"Saldo setelah transaksi{Jumlah_Transaksi}")
    Nilai_Transaksi = int(input("Masukkan jumlah transaksi:"))
else:
    Saldo_setelah_transaksi = saldo_awal + Nilai_Transaksi
    sum_val=sum_val + Nilai_Transaksi
print(f"Saldo Akhir dari Tuan Mik: {sum_val}")
