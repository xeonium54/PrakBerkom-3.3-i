# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 28 Oktober 2026
# Deskripsi : Saham Strategi Trailing Stop

persen= float(input("Masukkan persentase trailing stop:"))

hari = 1
harga_beli = int(input("Masukkan harga saham ke-1: "))
puncak = harga_beli
harga = harga_beli
terjual = False

while not terjual:
    hari += 1 
    harga = int(input(f"Masukkan harga saham ke-{hari}: "))
    batasjual = puncak*(1-persen/100)
    if harga <= batasjual:
       terjual = True
    elif harga > puncak:
       puncak = harga

batasjual = puncak*(1-persen/100)

print(f"Trailing stop ter-trigger di hari ke-{hari} dengan harga Rp{harga}")
print(f"Harga Puncak : Rp{puncak}")
print(f"Batas Jual (Trailing Stop {persen}%) : Rp.{batasjual}")

keuntungan = harga-harga_beli
if keuntungan >= 0:
   print(f"Keuntungan : Rp.{keuntungan}")
else:
   print(f"Kerugian : Rp.{keuntungan}")