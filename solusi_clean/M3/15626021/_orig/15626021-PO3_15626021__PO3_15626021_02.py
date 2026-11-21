# NIM / Nama : 15626021 / Aufaa Fakhri Ibrahim Irahadi
# Tanggal    : 28 Oktober 2026
# Deskripsi  : Program simulasi investasi saham dengan strategi trailing stop untuk melindungi keuntungan / membatasi kerugian

# KAMUS VARIABEL
# persen_ts : float
# hari      : int
# harga_beli : int
# harga_puncak : int
# batas_jual : float
# triggered : bool
# harga_hari_ini : int
# harga_jual : int
# selisih : int

# Algoritma
persen_ts = float(input("Masukkan presentase trailing stop: "))

# Hari ke-1 (Pembelian Saham)
hari = 1
harga_beli = int(input(f"Masukkan harga saham hari ke-{hari}: "))
harga_puncak = harga_beli

# Menghitung batas jual awal
batas_jual = harga_puncak * (1 - persen_ts / 100)
triggered = False

# Perulangan mencatat harga harian hingga trailing stop ter-trigger
while not triggered:
    hari += 1
    harga_hari_ini = int(input(f"Masukkan harga saham hari ke-{hari}: "))

    # Cek apakah hari ini memecahkan rekor puncak baru
    if harga_hari_ini > harga_puncak:
        harga_puncak = harga_hari_ini
        batas_jual = harga_puncak * (1 - persen_ts / 100)

    # Cek apakah trailing stop ter-trigger (harga turun <= batas jual)
    if harga_hari_ini <= batas_jual:
        triggered = True
        harga_jual = harga_hari_ini

# Menghitung keuntungan atau kerugian
selisih = harga_jual - harga_beli

print(f"Trailing stop ter-triggered pada hari ke-{hari} dengan harga Rp{harga_jual}")
print(f"Harga puncak = Rp{harga_puncak}")
print(f"Batas jual (trailing stop {persen_ts}%): Rp{batas_jual}")

if selisih >= 0:
    print(f"Keuntungan: Rp{selisih}")
else:
    print(f"Kerugian: Rp{abs(selisih)}")