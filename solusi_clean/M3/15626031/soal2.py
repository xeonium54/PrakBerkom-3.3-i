#Alfathir Sangkara Anindya -15626031
#10/28/2026
#Deskripsi: Program  Simulasi trailing stop saham

persen = float(input("Masukkan persentase trailing stop: "))
beli = int(input("Masukkan harga saham hari ke-1: "))

puncak = beli
batas = puncak * (1 - persen / 100)
hari = 1

while True:
    harga = int(input(f"Masukkan harga saham hari ke-{hari+1}: "))
    hari += 1

    if harga > puncak:
        puncak = harga

    batas = puncak * (1 - persen / 100)

    if harga <= batas:
        print(f"Trailing stop ter-trigger hari ke-{hari} dengan harga Rp{harga}.")
        print(f"Harga puncak: Rp{puncak}")
        print(f"Batas jual (trailing stop {persen}%): Rp{batas:.0f}")
        print(f"Keuntungan: Rp{harga - beli}")
        break
