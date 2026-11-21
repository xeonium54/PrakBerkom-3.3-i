"""Nama: Reinhard Emanuel Sinaga
Nim: 15626028

"""

Input persentase trailing stop
persen = float(input("Masukkan persentase trailing stop: "))


harga_saham = []


hari = 0
puncak = 0.0
batas_jual = 0.0
ter_trigger = False


while not ter_trigger:
    hari += 1
    harga = float(input(f"Masukkan harga saham hari ke-{hari}: "))
    harga_saham.append(harga)


    if hari == 1:
        puncak = harga
        batas_jual = puncak * (1 - (persen / 100))
    else:

        if harga > puncak:
            puncak = harga
            batas_jual = puncak * (1 - (persen / 100))


    if harga <= batas_jual:
        ter_trigger = True

#Output
harga_jual = harga_saham[-1]
harga_beli = harga_saham[0]

print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{int(harga_jual)}.")
print(f"Harga puncak: Rp{int(puncak)}.")


print(f"Batas jual (trailing stop {persen}%): Rp{batas_jual}.")


selisih = harga_jual - harga_beli
if selisih >= 0:
    print(f"Keuntungan: Rp{int(selisih)}.")
else:
    print(f"Kerugian: Rp{int(abs(selisih))}.")

