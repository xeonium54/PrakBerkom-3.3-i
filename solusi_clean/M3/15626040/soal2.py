# NIM/Nama: Frizka Yunisaf 15626040
# Tanggal: 28 Oktober 2026
# Deskripsi: Program simulasi strategi training stop sekaligus menghitung keuntungan atau kerugian.

PT= int(input("Masukkan persentase trailing stop: "))
HB = int(input("Masukkan harga saham hari ke-1: "))
P = HB
BJ = P*(1-(PT/(100)))

hari = 1
harga = HB

while harga > BJ:
    hari += 1
    harga = int(input("Masukkan harga saham hari ke -" + str(hari) + ": "))
    if harga > P:
        P = harga
        BJ = P*(1-(PT/(100)))

print ("Trailing stop ter-trigger pada hari ke- " + str(hari) + " dengan harga Rp " + str(harga) + ".")
print ("Harga puncak: Rp " + str(P) + ".")
print ("Batas jual (trailing stop " + str(PT) + "%): Rp " + str(BJ) +".")
print ("Keuntungan: Rp " + str(harga-HB) + ".")
