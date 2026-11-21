#Nama: Febrian Yafi Hakim
#NIM: 15626042
#Deskripsi : problem 2

persen = float(input("Masukkan presentase trailing stop: "))
hari = 1
harga = int(input("Masukkan harga saham hari ke-" + str(hari) + ": "))

harga_awal = harga
puncak = harga
batas_jual = puncak * (1 - (persen / 100))

while (harga > batas_jual):
    hari += 1
    harga = int(input("masukkan harga saham hari ke-" + str(hari) + "."))

    if (harga > puncak):
        puncak = harga
        batas_jual = puncak * (1 - (persen/100))

keuntungan = harga - harga_awal

print("Trailing stop ter-trigger pada hari ke-" + str(hari) + "dengan harga Rp" + str(harga) + "." )
print("Harga puncak: Rp" + str(puncak) + ".")
print("Batas jual (trailing stop)" + str(int(persen)) + "%: Rp" + str(batas_jual) + ".")

if (keuntungan >= 0):
    print("keuntungan: Rp" + str(keuntungan) + ".")
else:
    print("kerugian ; Rp" + str(-keuntungan) + ".")