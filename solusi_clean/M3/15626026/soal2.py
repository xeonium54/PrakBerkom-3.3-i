# NIM / NAMA : 15626026 / MUTHI'AH AZKA NIAMILLAH
# TANGGAL : 28 OKTOBER 2026
# DESKRIPSI : SOAL 2

persen = float(input("masukkan presentase trailing stop:"))

hari = 1
print("masukkan harga saham hari ke-", hari, ":")
harga_sekarang = int(input())

harga_beli = harga_sekarang

puncak = harga_sekarang
batas_jual = puncak* (1 - persen / 100)

while harga_sekarang > batas_jual:
    hari2 = hari + 1
    print("masukkan harga saham hari ke-", hari2, ":")
    harga_sekarang = int(input())

    if harga_sekarang > puncak:
        puncak = harga_sekarang
        batas_jual = puncak * (1 - persen / 100)

keuntungan = harga_sekarang - harga_beli

print("trailing stop ter-trigger pada hari ke-", hari, "dengan harga Rp", harga_sekarang, ".")
print("harga puncak: Rp", puncak, ".")

if persen.is_integer():
    print("batas jual (trailing stop)", int(persen), "%): Rp", batas_jual)
else:
    print("batas jual (trailing stop)", persen, "%): Rp", batas_jual)

print("keuntungan: Rp", keuntungan, ".")