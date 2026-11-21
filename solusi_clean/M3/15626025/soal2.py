# Nama/NIM: Maria Amatussyafee NUrjaman
# Tanggal: 28/10/2026
# Deskripsi: Program simulasi trailing stop, menghitung keuntungan dan kerugian

# KAMUS
# P = float
# H = integer
# h = integer

P = float(input("Masukan persentase trailing stop: "))
H = int(input("Masukan harga saham hari ke-1: "))

puncak = H
batas = puncak * (1 - P / 100)
hari = 1

while True: 
    hari += 1
    h = int(input(f"Masukan harga saham hari ke-{hari}: "))

    if h > puncak: 
        puncak = h
        batas = puncak * (1 - P / 100)
    elif h <= batas:
        break

    untung = h - H

    print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{h}")
    print(f"Harga puncak: Rp{puncak}")
    print(f"Batas jual (trailing stop {P:g}%): Rp{batas}")
    if untung >= 0:
        print(f"Keuntungan: Rp{untung}")
    else:
        print(f"Keuntungan: Rp{-untung}")

    
