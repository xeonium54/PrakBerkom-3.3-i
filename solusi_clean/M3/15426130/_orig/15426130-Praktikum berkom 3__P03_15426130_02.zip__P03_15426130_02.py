# NIM/Nama  : 15426130 / Yudha Putra
# Tanggal   : 28 Oktober 2026
# Deskripsi : Simulasi trailing stop saham Tuan Mik: terus membaca harga harian
#             sampai harga <= BatasJual, lalu hitung keuntungan/kerugian.

persen_teks = input("Masukkan persentase trailing stop: ")
persen = float(persen_teks)

# Hari pertama: saham dibeli
hari = 1
harga = int(input("Masukkan harga saham hari ke-1: "))
harga_beli = harga
puncak = harga
batas = puncak * (1 - persen / 100)

terpicu = False
while not terpicu:
    hari += 1
    harga = int(input("Masukkan harga saham hari ke-" + str(hari) + ": "))
    # Rekor baru: puncak dan batas jual ikut naik
    if harga > puncak:
        puncak = harga
        batas = puncak * (1 - persen / 100)
    # Trailing stop ter-trigger bila harga <= batas jual
    if harga <= batas:
        terpicu = True

print("Trailing stop ter-trigger pada hari ke-" + str(hari) + " dengan harga Rp" + str(harga) + ".")
print("Harga puncak: Rp" + str(puncak) + ".")
print("Batas jual (trailing stop " + persen_teks + "%): Rp" + str(batas) + ".")

selisih = harga - harga_beli
if selisih >= 0:
    print("Keuntungan: Rp" + str(selisih) + ".")
else:
    print("Kerugian: Rp" + str(-selisih) + ".")