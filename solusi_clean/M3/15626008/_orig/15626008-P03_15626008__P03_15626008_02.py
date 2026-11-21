# NIM/NAMA : 15626008 / Arya Satya Anggara
# Tanggal : 28 Oktober 2026
# Deskripsi : Program ini menghitung batas jual saham menggunakan trailing stop dan menentukan keuntungan atau kerugian saat saham dijual


persen = float(input("masukkan persen trailing stop: "))
harga_beli = float(input("masukkan harga beli saham: "))

puncak = harga_beli
hari = 1

while True:
    harga = float(input("masukkan harga saham hari berikutnya: "))
    hari = hari + 1

    if harga > puncak:
        puncak = harga

    BatasJual = puncak * (1 - persen / 100)

    print("puncak:", puncak)
    print("batas jual:", BatasJual)

    if harga <= BatasJual:
        print("trailing stop ter-trigger!")
        print("harga jual:", harga)

        keuntungan = harga - harga_beli
        print("keuntungan/kerugian:", keuntungan)
        print("terjual pada hari ke-", hari)
        break