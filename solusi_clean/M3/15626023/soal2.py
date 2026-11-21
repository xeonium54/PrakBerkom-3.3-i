# NIM/Nama :15626023/Andre Partogi Nathanael Butarbutar
# Tanggal :28/10/2026
# Deskripsi :Simulasi investasi saham

persen = float(input("Masukkan persentase trailing stop:"))
harga_beli = int(input("Masukkan harga saham hari ke -1:"))

hari = 1
harga_terkini = harga_beli
puncak = harga_beli
batas_jual = puncak *(1-persen/100)
trailing_triggered = False

print("saya sudah tidak paham kaaaaaaa")