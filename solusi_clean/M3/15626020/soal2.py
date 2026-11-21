# NIM/Nama : 15626020/Rudianto
# Tanggal   : 28 Oktober 2026
# Deskripsi : Simulasi strategi trailing stop saham

persen_text = input("Masukkan persentase trailing stop: ")
persen = float(persen_text)

harga_beli = int(input("Masukkan harga saham hari ke -1: "))
puncak = harga_beli
hari = 1

while True:
    hari = hari + 1
    harga = int(input("Masukkan harga saham hari ke -" + str(hari) + ": "))

    if harga > puncak:
        puncak = harga

    batas_jual = puncak * (1 - persen / 100)

    if harga <= batas_jual:
        break

print("Trailing stop ter - trigger pada hari ke -" + str(hari) + " dengan harga Rp" + str(harga) + " .")
print("Harga puncak : Rp" + str(puncak) + " .")
print("Batas jual ( trailing stop " + persen_text + "%): Rp" + str(batas_jual) + " .")

hasil = harga - harga_beli

if hasil > 0:
    print("Keuntungan : Rp" + str(hasil) + ".")
elif hasil < 0:
    print("Kerugian : Rp" + str(-hasil) + ".")
else:
    print("Keuntungan atau kerugian : Rp0.")

persen_text = input("Masukkan persentase trailing stop: ")
persen = float(persen_text)

harga_beli = int(input("Masukkan harga saham hari ke -1: "))
puncak = harga_beli
hari = 1

while True:
    hari = hari + 1
    harga = int(input("Masukkan harga saham hari ke -" + str(hari) + ": "))

    if harga > puncak:
        puncak = harga

    batas_jual = puncak * (1 - persen / 100)

    if harga <= batas_jual:
        break

print("Trailing stop ter - trigger pada hari ke -" + str(hari) + " dengan harga Rp" + str(harga) + " .")
print("Harga puncak : Rp" + str(puncak) + " .")
print("Batas jual ( trailing stop " + persen_text + "%): Rp" + str(batas_jual) + " .")

hasil = harga - harga_beli

if hasil > 0:
    print("Keuntungan : Rp" + str(hasil) + ".")
elif hasil < 0:
    print("Kerugian : Rp" + str(-hasil) + ".")
else:
    print("Keuntungan atau kerugian : Rp0.")

persen_text = input("Masukkan persentase trailing stop: ")
persen = float(persen_text)

harga_beli = int(input("Masukkan harga saham hari ke -1: "))
puncak = harga_beli
hari = 1

while True:
    hari = hari + 1
    harga = int(input("Masukkan harga saham hari ke -" + str(hari) + ": "))

    if harga > puncak:
        puncak = harga

    batas_jual = puncak * (1 - persen / 100)

    if harga <= batas_jual:
        break

print("Trailing stop ter - trigger pada hari ke -" + str(hari) + " dengan harga Rp" + str(harga) + " .")
print("Harga puncak : Rp" + str(puncak) + " .")
print("Batas jual ( trailing stop " + persen_text + "%): Rp" + str(batas_jual) + " .")

hasil = harga - harga_beli

if hasil > 0:
    print("Keuntungan : Rp" + str(hasil) + ".")
elif hasil < 0:
    print("Kerugian : Rp" + str(-hasil) + ".")
else:
    print("Keuntungan atau kerugian : Rp0.")
