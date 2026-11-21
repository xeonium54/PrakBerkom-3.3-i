# NIM/Nama : 15626032/Muhamad Faiz Abdul Aziz
# Tanggal : 28 Oktober 2026
# Deskripsi : Menghitung saldo 

Saldo_Awal = int(input("Masukan saldo awal (Rp): "))
Jumlah_Transaksi = int(input("Masukan jumlah transaksi (N): "))

riwayat = [0 for i in range(Jumlah_Transaksi)]
masuk = 0
keluar = 0
negatif = 0

i = 0
while i < Jumlah_Transaksi:
    t = int(input("Masukan nilai transaksi ke -" + str(i + 1) + ": "))

    Saldo_Awal = Saldo_Awal + t
    riwayat[i] = Saldo_Awal

    if t > 0:
        masuk = masuk + t

    elif t < 0:
        keluar = keluar + t

    if Saldo_Awal < 0 and negatif == 0:
        negatif = i + 1

    i = i + 1

print("Saldo setelah transaksi ke -" + str(i) + ": Rp" + str(Saldo_Awal) + ": ")

i = 0
while i < Jumlah_Transaksi:
    print("Saldo setelah transaksi ke -" + str(i + 1) + ": Rp" + str(riwayat[i]) + ".")
    i = i + 1

if negatif == 0:
    print("Saldo tuan Mik tidak pernah negatif selama", Jumlah_Transaksi, "transaksi.")
else:
    print("Saldo tuan Mik pertama kali negatif pada transaksi ke -" + str(negatif) + ".")

    print("Total pemasukan: Rp" + str(masuk) +  ". Total pengeluaran: Rp" + str(keluar) + ".")