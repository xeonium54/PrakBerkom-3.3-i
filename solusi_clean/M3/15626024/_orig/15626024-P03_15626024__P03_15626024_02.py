# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 28 October 2026
# Deskripsi : 

# Kamus
# persenTS (int) menginput nilai persentase trailing stop
# persen (float) merupakan versi float dari persenTS
# hari (int) menghitung hari
# sPrice (int) menghitung harga saham pada hari pertama
# puncak (int) menghitung harga saham tertinggi yang pernah dicapai
# batas_jual (float) batas harga terendah sebelum TS ter-trigger
# trigger (bool) mengecek apakah TS sudah terpicu atau belum
# price (int) masukkan harga saham harian
# selisih (int) selisih harga akhir dan awal untuk menghitung untung/rugi
# persen_str (str) format persen pada string

# Algoritma
persenTS = input("Masukkan persentase trailing stop: ")
persen = float(persenTS)
persen_str = str

hari = int(1)
sPrice = int(0)
puncak = int(0)
batas_jual = float(0.0)
trigger = bool(False)

while not trigger:
    price = int(input(f"Masukkan harga saham hari ke-{hari}:" ))

    if hari == 1:
        sPrice = price
        puncak = price
        batas_jual = puncak * (1.0 - (persen/100.0))
    else:
        if price > puncak:
            puncak = price
            batas_jual = puncak * (1.0 - (persen/100.0))

    if price <= batas_jual:
        trigger = True
        print(f"Trailing stop ter -trigger pada hari ke -{hari} dengan harga Rp{price}.")
        print(f"Harga puncak: Rp{puncak}")

        if persen == int(persen):
            persen_str = str(int(persen))
        else:
            persen_str = str(persen)
        print(f"Batas jual (trailing stop {persenTS}%): Rp{batas_jual}")
        selisih = price - sPrice
        if selisih >= 0:
            print(f"Keuntungan: Rp{selisih}.")
        else:
            print(f"Kerugian: Rp {-selisih}.")
    else:
        hari += 1