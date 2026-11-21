# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 28 Oktober 2026
# Deskripsi: Program trailing stop untuk suatu harga saham

# KAMUS
# persen : float (berapa persen railing stocknya)
# hari : int (hari pergerakan harga saham)
# harga : int 
# harga_beli : float
# peak : float (Harga saham tertinggi pada hari itu)
# batas_jual : float ( Harga saham sebelum railing stock aktif)
# selisih : float (Gain/Loss)


# Algoritma 
persen = float(input('Masukkan persentase railing stop: '))

hari = 1
harga = float(input('Masukkan harga saham hari ke-{hari}: '))
harga_beli = harga 
peak = harga 
batas_jual = peak * (1.0 - persen / 100.0)

# Pengulangan sampai railing stock nyala
while harga > batas_jual:
    hari += 1
    harga = float(input('Masukkan harga saham hari ke-{hari}: '))

    if harga > peak:
        peak = harga 
        batas_jual = peak * (1.0 - persen / 100.0)


# Biar bilangan bulat 
if persen == int(persen):
    persen_str = f'{int(persen)}%'
else:
    persen_str = f'[persen]%'


print(f'Trailing stop ter-trigger pada hari ke {hari} dengan harga Rp{int(harga)}')
print(f'harga puncak: Rp{int(peak)}')
print(f'Batas jual (trailing stop {persen_str}: Rp{batas_jual}')

selisih = harga - harga_beli
if selisih >= 0:
    print (f'keuntungan: Rp{int(selisih)}')
else:
    print (f'kerugian: Rp{int(-selisih)}')