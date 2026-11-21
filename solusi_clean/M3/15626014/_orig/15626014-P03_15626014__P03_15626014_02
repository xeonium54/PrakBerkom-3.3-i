#Nama : Fadhil Zulhilmi
#NIM : 15626014
#Deskripsi : Membuat program untuk mensimulasikan strateegi triling stop, sekaligus menghitung keuntungan atau kerugiannya

persen = float(input("Masukkan persentase trailing stop: "))
harga_beli = int(input("Masukkan harga saham hari ke-1: "))
puncak = harga_beli
batas_jual = puncak * (1 - persen / 100) 

hari = 1
harga_jual = harga_beli

while True:
    hari += 1
    harga = int(input(f"Masukkann harga saham hari ke-{hari}: "))
    if harga > puncak:
        puncak = harga
        batas_jual = puncak *(1 - persen / 100)

        if harga <= batas_jual:
            harga_jual = harga
            print(f"Traling stop ter-trigger pada hari ke-{hari} dengan harga Rp{harga_jual}. ")
        break

        print(f"Harga puncak: Rp{puncak}. ")
        print(f"Batas jual (trailing stop{persen:g}%): Rp{batas_jual}. ")
        print(f"Keuntungan: Rp{harga_jual - harga_beli:g}. ")