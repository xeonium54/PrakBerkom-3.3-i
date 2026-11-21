# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 28 Oktober 2026
# Deskripsi : Simulasi Strategi trailing stop saham

# Algoritma
persen = float(input("Masukkan persentase trailing stop: "))
harga_awal = int(input("Masukkan harga saham hari ke-1: "))

puncak = harga_awal
hari = 1
triggered = False

while not triggered:
    hari += 1
    harga = int(input(f"Masukkan harga saham hari ke-{hari}: "))
    
    if harga > puncak:
        puncak = harga
    
    batas_jual = puncak * (1 - persen / 100)
    
    if harga <= batas_jual:
        triggered = True
        keuntungan = harga - harga_awal
        print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp.{harga}.")
        print(f"Harga puncak: Rp.{puncak}.")
        print(f"Batas jual (trailing stop {persen}%): Rp.{batas_jual}.")
        if keuntungan >= 0:
            print(f"Keuntungan: Rp.{keuntungan}.")
        else:
            print(f"Kerugian: Rp.{abs(keuntungan)}.")