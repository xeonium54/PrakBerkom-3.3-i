# NIM/Nama              : 15426128 / Fathir Sulihansyah
# Tanggal               : 28 Oktober 2026
# Deskripsi             : Program simulasi strategi investasi saham trailing stop milik Tuan Mik sekaligus menghitung keuntungan atau kerugian saat trailing stop ter-trigger

# KAMUS KODING
# persentrailing  : float -> Persentase trailing stop yang dimasukkan oleh pengguna
# persen          : float -> Persentase dalam bentuk desimal (persentrailing / 100)
# harga_beli      : int   -> Harga saham pada hari pertama saat dibeli
# hari            : int   -> Penghitung hari investasi berjalan
# puncak          : int   -> Harga saham tertinggi yang pernah dicapai sejak dibeli
# batas_jual      : float -> Batas harga minimal (Puncak * (1 - persen)) untuk menjual saham
# harga_sekarang  : int   -> Harga saham pada hari iterasi berjalan
# tertrigger      : bool  -> Status boolean penanda apakah trailing stop sudah aktif/ter-trigger
# selisih         : int   -> Perhitungan keuntungan atau kerugian (harga jual - harga beli)


persentrailing = float(input("Masukkan persentase trailing stop: "))
persen = persentrailing / 100.0

hari = 1
harga_beli = int(input(f"Masukkan harga saham hari ke-{hari}: "))
puncak = harga_beli
batas_jual = puncak * (1 - persen)

tertrigger = False
while not tertrigger:
    hari += 1
    harga_sekarang = int(input(f"Masukkan harga saham hari ke-{hari}: "))
    
    if harga_sekarang > puncak:
        puncak = harga_sekarang
        batas_jual = puncak * (1 - persen)
        
    if harga_sekarang <= batas_jual:
        tertrigger = True

selisih = harga_sekarang - harga_beli

print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{harga_sekarang}.")
print(f"Harga puncak: Rp{puncak}.")
print(f"Batas jual (trailing stop {persentrailing}%): Rp{batas_jual}.")

if selisih >= 0:
    print(f"Keuntungan: Rp{selisih}.")
else:
    print(f"Kerugian: Rp{-selisih}.")
