persen_str = input("masukan presentase trailing stop: ")
persen = float(persen_str)

hari = 1
beli = int(input("masukan harga saham hari ke-1: " ))
puncak = beli
batas = puncak *(1- persen / 100)

terjual = False
while terjual == False:
    hari = hari + 1
    harga = int(input("masukan harga saham hari ke-" + str(hari) + ": "))
    if harga <= batas:
        terjual = True
    elif harga > puncak :
        puncak = harga
        batas = puncak * (1 - persen / 100)

print("trailing stop ter-triger pada hari ke-" + str(hari) + "dengan harga Rp" + str(harga) + ".")
print("harga puncak: Rp" + str(puncak) + ".")
print("batas jual (trailing stop "+ persen_str +"%): Rp" + str(batas) + ".")
print("keuntungan: Rp" + str(harga-beli)+".")