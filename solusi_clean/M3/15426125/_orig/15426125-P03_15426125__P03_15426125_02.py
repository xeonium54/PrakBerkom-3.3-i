# input presentase awal
persen = float(input("Masukkan presentase trailing stop: "))
# pembelian pertama saham
hari = 1
harga_awal = float(input(f"masukkan harga saham hari ke-{hari}: "))
# nilai puncak awal dan batas jual pertama
puncak = harga_awal
batas_jual = puncak * (1 - (persen / 100))
#perulangan untuk hari-hari berikutnya
while True:
    hari += 1
    harga_sekarang = float(input(f"Masukkan harga saham hari ke-{hari}: "))
    if harga_sekarang <= batas_jual:
        persen_str = str(int(persen)) if persen.is_integer() else str(persen)

        print(f"Trailing stop ter trigger pada hari ke-{hari} dengan harga Rp{int(harga_sekarang)}. ")
        print(f"Harga puncak: Rp{int(puncak)}. ")
        print(f"Batas jual (trailing stop {persen_str}%): Rp{batas_jual:.1f}. ")

        perubahan_dana = harga_sekarang - harga_awal
        if perubahan_dana >= 0:
            print(f"Keuntungan: Rp{int(perubahan_dana)}. ")
        else:
            print(f"Kerugian: Rp{int(abs(perubahan_dana))}. ")
        break
    if harga_sekarang > puncak:
        puncak = harga_sekarang
        batas_jual = puncak * (1- (persen / 100))
        

