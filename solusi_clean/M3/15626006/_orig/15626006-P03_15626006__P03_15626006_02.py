# NIM / Nama : 15626006 / Maria Zeysta Kamelia Rumanti
# Tanggal : 28 Oktober 2026
# Deskripsi : Simulasi strategi trailing stop pada investasi saham untuk melindungi keuntungan.
# Program akan meminta input harga saham harian dan memperbarui harga puncak tertinggi beserta batas jualnya.
# Ketika harga harian turun hingga berada di bawah batas jual, saham otomatis dijual.
# Lalu program akan menampilkan hari saat ter-trigger, harga puncak, batas jual terakhir, serta total keuntungan atau kerugian yang didapat.

# Input presentase trailing stop
persen = float(input("Masukkan persen trailing stop: "))

if persen.is_integer():
    persen_tampil = int(persen)
else:
    persen_tampil = persen

harga_saham = []

ter_trigger = 0
hari = 1
puncak = 0
batas_jual = 0.0

harga_beli = 0
harga_jual = 0

while ter_trigger == 0:
    harga = int(input(f"Masukkan harga saham hari ke-{hari}: "))
    harga_saham.append(harga)

    if harga > puncak:
        puncak = harga
        batas_jual = puncak * (1 - (persen/100))

    if harga <= batas_jual:
        ter_trigger = 1
    else:
        hari = hari + 1

harga_beli = harga_saham[0]
harga_jual = harga_saham[hari - 1]
selisih = harga_jual - harga_beli

if persen == int(persen):
    persen_tampil = int(persen)
else:
    persen_tampil = persen

print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{harga_jual}.")
print(f"Harga puncak: Rp{puncak}.")
print(f"Batas jual (trailing stop {persen_tampil}%): Rp{batas_jual}.")

if selisih >= 0:
    print(f"Keuntungan: Rp{selisih}.")
else:
    print(f"Kerugian: Rp{-selisih}.")