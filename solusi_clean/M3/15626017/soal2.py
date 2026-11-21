# NIM/Nama      : 15626017 / Naura Vira Vania Ramadhani
# Berpikir Komputasional ITB
# Tanggal       : 28 Oktober 2026
# Deskripsi     : Program simulasi strategi investasi trailing stop saham 
#                 untuk menghitung titik jual, harga puncak, dan keuntungan/kerugian.

# Meminta masukan persentase trailing stop
persen_trailing = float(input("Masukkan persentase trailing stop: "))

# Hari pertama (pembelian saham)
hari = 1
harga_awal = int(input(f"Masukkan harga saham hari ke-{hari}: "))

puncak = harga_awal
batas_jual = puncak * (1 - persen_trailing / 100)
ter_trigger = False

# Jika di hari pertama langsung ter-trigger (untuk keamanan logika)
if harga_awal <= batas_jual:
    ter_trigger = True
    harga_jual = harga_awal
else:
    # Melakukan pengulangan harian sampai trailing stop ter-trigger
    while not ter_trigger:
        hari += 1
        harga_harian = int(input(f"Masukkan harga saham hari ke-{hari}: "))
        
        # Memeriksa apakah harga memecahkan rekor puncak baru
        if harga_harian > puncak:
            puncak = harga_harian
            batas_jual = puncak * (1 - persen_trailing / 100)
            
        # Memeriksa apakah harga menyentuh atau turun di bawah batas jual
        if harga_harian <= batas_jual:
            ter_trigger = True
            harga_jual = harga_harian

# Menghitung selisih keuntungan atau kerugian terhadap harga beli awal
selisih = harga_jual - harga_awal

print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{harga_jual}.")
print(f"Harga puncak: Rp{puncak}.")
print(f"Batas jual (trailing stop {persen_trailing}%): Rp{batas_jual}.")

if selisih >= 0:
    print(f"Keuntungan: Rp{selisih}.")
else:
    print(f"Kerugian: Rp{abs(selisih)}.")