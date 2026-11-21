# Kamus
# persen: float, persentase trailing stop
# harga: integer, harga saham setiap hari
# puncak: integer, harga tertinggi saham
# batas_jual: float, batas harga jual
# harga_beli: integer, harga saham saat dibeli
# harga_jual: integer, harga saham saat dijual
# keuntungan: float, keuntungan atau kerugian
# hari: integer, nomor hari

persen = float(input("Masukkan persentase trailing stop:"))
hari = 1
harga = int(input("Masukkan harga saham hari ke-1: "))

harga_beli = harga
puncak = harga
batas_jual = puncak * (1 - persen / 100)
while harga >= batas_jual:
    hari = hari + 1
    harga = int(input(f"Masukkan harga saham hari ke-{hari}: "))
    if harga > puncak:
        puncak = harga
        batas_jual = puncak * (1 - persen / 100)
        harga_jual = harga
keuntungan = harga_jual - harga_beli

print("keuntungan:RP:{}")
print("Trailing stop ter-trigger pada hari ke-{} dengan harga Rp{}.".format(hari, harga_jual))

