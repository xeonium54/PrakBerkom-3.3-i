# Nama  : Vidia Nurafifa
# NIM   : 15626011
# Desc  : No 2 - Simulasi Trailing Stop Saham

# harga beli (hb)
# harga jual (hj)
# puncak/harga tertinggi (pht)
# batas jual (bj)
# presentase (P)
# hari (h)

P = float(input("Masukkan persentase trailing stop: "))
hb = float(input("Masukkan harga saham hari ke-1: "))

pht = hb
h = 1
hj = 0

bj = pht * (1-P/100)

while True:
    h = h + 1
    harga = float(input("Masukkan harga saham hari ke-"+ str(h) + ":"))
    
    if harga > pht:
        pht = harga
        
    bj = pht * (1-P/100)
    
    if harga <= bj:
        hj = harga
        break
    
hasil = hj - hb
print("Trailing stop ter-trigger pada hari ke-"+ str(h) +" dengan harga Rp"+ str(hj) + ".")
print("Harga puncak : Rp"+ str(pht) + ".")
print ("Batas jual (trailing stop "+ str(P) +"%): Rp"+ str(bj) +".")

if hasil > 0:
    print("Keuntungan : Rp"+ str(hasil) + ".")
elif hasil < 0:
    print("Kerugian : Rp"+ str(-hasil) + ".")
else:
    print("Tidak untung maupun rugi.")
