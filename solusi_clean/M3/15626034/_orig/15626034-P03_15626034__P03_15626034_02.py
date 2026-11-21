#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 28 Oktober 2026
#Deskripsi : Simulasi trailing stop

harga_1 = int(input("Masukkan harga saham hari ke-1: "))
persen = int(input("Masukkan persentase trailing stop: "))
daftar_harga = []
daftar_harga.append(harga_1)
puncak = harga_1
batas_jual = puncak * (1 - persen / 100)
hari = 1
while True:
    hari += 1
    harga_hari_ini = int(input(f"Masukkan harga saham hari ke-{hari}: "))
    daftar_harga.append(harga_hari_ini)
    if harga_hari_ini > puncak:
        puncak = harga_hari_ini
        batas_jual = puncak * (1 - persen / 100)
    if harga_hari_ini <= batas_jual:
        harga_jual = harga_hari_ini
        break
    selisih = harga_hari_ini - harga_1
    if selisih > 0:
        print(f"Harga saham naik sebesar Rp {selisih}Rp")
    elif selisih < 0:
        print(f"Harga saham turun sebesar Rp {-selisih}Rp")
    else:
        print("Harga saham tidak berubah")
    print(f"Harga puncak: Rp {puncak}, batas jual: Rp {batas_jual}")
    print(f"keuntungan/kerugian saat ini: Rp {harga_hari_ini - harga_1}Rp")