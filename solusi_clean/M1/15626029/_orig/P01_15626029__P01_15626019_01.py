# NIM/Nama : 15626029/Hanif Mahib Yassar Nuradiyatma
# Tanggal : 30 Sept 2026
# Deskripsi : program ngitung duit buat bayar listrik

# KAMUS
# P, t, B, T, D : float

# CODE
P = float(input("Daya Lampu :"))
t = float(input("Waktu lampu nyala : "))
B = float(input("Harga Listrik per kWh : "))

T = float(P * t)/1000

D = float(T * B)

print("Duit yang harus dibayar karena lupa matiin lampu : Rp",D)