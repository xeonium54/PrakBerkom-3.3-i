# NIM/Nama : Addien Maulana Bima
# Tanggal : 28 Oktober 2026
# Deskripsi : Program Pelacak training-stop saham

persen = float(input("Masukkan presentase trailing stop : "))

hari = 1
harga_awal = int(input(f"Masukkan harga saham pada hari ke-{hari}: "))
puncak = harga_awal

tertrigger = False 
harga_trigger = 0

while not tertrigger:
    batas_jual = puncak * ( 1 - persen / 100)
    hari += 1
    harga = int(input(f"Masukkan harga saham hari ke-{hari}: "))

    if harga <= batas_jual:
        tertrigger = True
        harga_trigger = harga
    elif harga > puncak:
        puncak = harga

keuntungan = harga_trigger-harga_awal

print(f"Trailing stop tertrigger pada hari ke-{hari} dengan harga Rp{harga_trigger}.")
print(f"Harga puncak Rp{puncak}")
print(f"Batas jual (trailing stop {int(persen)}%): Rp{batas_jual}.")
print(f"Keuntungan : Rp{keuntungan}.")
