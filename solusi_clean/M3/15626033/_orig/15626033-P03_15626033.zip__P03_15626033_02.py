# NIM = 15626033
# Nama = farah Ghiza Humairoh
# Deskripsi = membuat program yang mensimulasikan strategi trailing stop, sekaligus menghitung keuntungan dankerugian


persen = float(input("masukkan persentase trailing stop (persen): "))
harga_beli = float(input("masukkan harga saham hari pertama: "))
puncak = harga_beli
batas_jual = puncak * (1 - (persen / 100))
hari = 2
while True:
    harga_hari_ini = float(input(f"masukkan harga saham hari ke--{hari}: "))
    if harga_hari_ini > puncak:
        puncak = harga_hari_ini
        batas_jual = puncak * (1 - (persen / 100))
        print(f">> rekor baru! puncak: {puncak}, batas jual baru: {batas_jual:.2f}")
    if harga_hari_ini <= batas_jual:
        print("\n--- trailing stop ter-trigger! ---")
        print(f"saham dijual pada hari-{hari} dengan harga: {harga_hari_ini}")
        profit_loss = harga_hari_ini - harga_beli
        if profit_loss > 0:
            print(f"tuan mik mendapatkan KEUNTUNGAN sebesar: {profit_loss:.2f}")
        elif profit_loss < 0:
            print(f"tuan mik mengalami KERUGIAN sebesar: {abs(profit_loss):.2f}")
        else:
            print("tuan mik balik modal (tidak untung dan tidak rugi).")
        break
    hari += 1

