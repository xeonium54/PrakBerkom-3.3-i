# NIM/Nama: 15626047
# Tanggal: 28 Oktober 2026
# Deskripsi: Simulasi trailing stop

#Kamus
persen=float
price_1=int
price_2=int
hari=int
puncak=int
batas_jual=float
selisih=int

#ALGORITMA
persen=float(input("Masukkan persentase trailing stop:"))
price_1=int(input("Masukkan harga saham hari ke-1:"))

hari=1
puncak= price_1
price_2=price_1
batas_jual= puncak*(1-persen/100)

hari +=1
price_2=int(input(f"Masukkan harga saham hari ke-{hari}:"))

if price_2>puncak:
    puncak=price_2

selisih=price_2-price_1

print(f"Trailing stop ter-trigger pada hari ke-{hari} dengan harga Rp{price_2}")
print(f"Harga puncak: Rp{puncak}")
print(f"Batas Jual (trailing stop {persen}%): Rp{batas_jual}.")

if selisih >=0:
    print (f"Keuntungan: Rp{selisih}")
else:
   print (f"Kerugian: Rp{selisih}") 