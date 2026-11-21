# NIM/Nama : 15626004 / Nirmala Rahma Maulida
# Tanggal : 28 Oktober 2026
# Deskripsi : Program menstimulasikan strategi trailing stop dan menghitung keuntungan dan kerugiannya 


# KAMUS
# persentase, harga_awal, batas_jual, harga_sekarang, harga_awal, harga_jual: float
 
#ALGORITMA
persentase = float(input("masukkan persentase trailing stop = "  ))
harga_awal = float(input("masukkan harga hari ke-1: "))

puncak = harga_awal
batas_jual = puncak * (1 - persentase / 100)
hari = 1
harga_sekarang = harga_awal

while True:
    if harga_sekarang  <= batas_jual:
        print("trailing stop ")
        print("harga puncak",)
        print("batas jual")

        untung_rugi = harga_sekarang - harga_awal
        if untung_rugi >= 0:
            print("keuntungan", untung_rugi)
        else:
            print("kerugian", untung_rugi)

    hari += 1
    harga_sekarang = float(input("masukkan harga saham"))

if harga_sekarang > puncak:
    puncak = harga_sekarang