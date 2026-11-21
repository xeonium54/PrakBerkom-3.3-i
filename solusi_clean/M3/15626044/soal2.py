# Nama: Saliha Mahira Al-kwarismy
# NIM: 15626044
# Deskripsi: Problem 2

persen = float(input("Masukkan persentase trailing stop: "))

# variabel awal
hari = 1
puncak = 0
batas_jual = 0.0
harga_awal = 0

# Looping harga
while True:
    harga_sekarang = int(input(f"Masukkan harga saham hari ke-{hari}: "))
    # Harga beli pertama kali
    if hari == 1:
        harga_awal = harga_sekarang
        puncak = harga_sekarang
        batas_jual = puncak * (1 - (persen / 100))
    # Mengecek harga pada hari pertama
    if harga_sekarang > puncak:
        puncak = harga_sekarang
        batas_jual = puncak * (1 - (persen / 100))
    # Berada di atas atau bawah batas harga jual
    if harga_sekarang <= batas_jual:
        print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{harga_sekarang}.")
        break
    hari += 1

# Hasil akhir
print(f"Harga puncak: Rp{puncak}.")
print(f"Batas jual (trailing stop {int(persen)}%): Rp{batas_jual:1f}.")

# Hitung keuntungan atau kegagalan
selisih = harga_sekarang - harga_awal
if harga_sekarang >= harga_awal:
    keuntungan = harga_sekarang - harga_awal
    print(f"Keuntungan: Rp{keuntungan}.")
else:
    kerugian = harga_awal - harga_sekarang
    print(f"Kerugian: Rp{kerugian}.")