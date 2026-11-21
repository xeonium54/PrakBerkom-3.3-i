# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 28 Oktober 2026
# Deskripsi : menghitung batas jual saham menggunakan metode trailing stop
#             dengan menggunakan harga tertinggi (puncak) sebagai acuan 
#             dan menghitung keuntungannya

# KAMUS
# persT = float = persentase trailing stop
# harga = int = harga saham tiap harinya
# beli = int = harga beli pertamakali

persT = float(input("Masukkan pesentase trailing stop: "))
beli = int(input("Masukkan harga saham hari ke-1: "))

puncak = beli
hari = 1
harga = beli
batas = puncak * (1 - persT / 100)
trigger == False

while trigger == False:
    hari = hari + 1
    harga = int(input("Masukkan harga saham hari ke- :"))

    if harga > puncak:
        puncak = harga

    batas = puncak * (1 - persT / 100)

    if harga <= batas:
        trigger = True

untung = harga - beli 

print("Trailing stop ter-trigger pada hari ke-" , hari , "dengan harga Rp." , harga)
print("Harga puncak: Rp." , puncak)
print("Batas jual (trailing stop" , persT , "%): Rp." , batas )

if untung > 0:
    print("Keuntungan: Rp." , untung)
else:
    print("Kerugian: Rp." , -untung)