# NIM/Nama : 15626001/Muhamad Naufal Al Fajri
# Tanggal : 28 Oktober 2026
# Deskripsi :
persen = float(input("Masukkan persen trailing stop: "))
hari = 1
while True:
    harga = float(input(f"Harga saham hari ke-{hari}: "))
    puncak = harga (max)
    batas_jual = puncak * (1 - persen / 100)

    if harga > puncak:
        puncak = harga
        batas_jual = puncak * (1 - persen / 100)

    print(f"Puncak: {puncak}")
    print(f"Batas jual: {batas_jual}")

    if harga <= batas_jual:
        print("Trailing stop ter-trigger!")
        print(f"Harga jual: {harga}")

        keuntungan = harga (max) - harga (min) 
        print(f"Keuntungan/kerugian per saham: {keuntungan}")

        break

    hari += 1