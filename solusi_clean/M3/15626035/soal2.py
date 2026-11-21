# NIM/Nama : 15626035/Naila Rahmah Zhafirah
# Tanggal : Rabu, 28 Oktober 2026
# Deskripsi : 

# Kamus
harga = []
persen = 0
N = 0
beli = 0
puncak = 0
batas_jual = 0
keuntungan = 0
terjual = False

# Input
persen = float(input("Masukkan persentase trailing stop: "))

for i in range(1, N + 1):
    h = float(input("Masukkan harga saham hari ke-" + str(i) + ":"))
    harga.append(h)

# Inisialisasi
beli = harga[0]
puncak = beli

# Trailing stop
for i in range (1, N):
    if harga[i] > puncak:
        puncak = harga[i]

        batas_jual = puncak * (1 - persen / 100)

        if harga[i] <= batas_jual:
            print("Traling stop ter-trigger pada hari ke-" + str(i + 1))
            print("Harga jual: Rp" + str(harga[i]))
            terjual = True
            keuntungan = harga[i] - beli
            break

# Output
if terjual:
    print("Harga puncak: Rp" + str(puncak))
    print("Batas jual: Rp" + str(batas_jual))
    print("Keuntungan: Rp" + str(keuntungan))
else:
    print("Trailing stop belum ter-trigger.")
    print("Harga puncak: Rp" + str(puncak))
