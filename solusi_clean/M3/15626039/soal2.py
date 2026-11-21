# NIM/Nama : 15626039/Khalif Aufar Aridkhi
# Tanggal : 28 Oktober 2026
# Deskripsi : Nomer 2, Menghitung saham

# KAMUS
#p = int
#h = int
#hb = int
#puncak = int
#b = float
#hari = int
#u = int

p = int(input("Masukkan persentase trailing stop:"))
h =  int(input("Masukkan harga saham hari ke -1:"))

puncak = h
b = puncak * (1- p / 100)
hari = 1

while h > b:
 h = int(input("Masukkan harga saham hari ke-"+str(hari + 1) + ":"))
 hari = hari + 1

 if h > puncak:
  puncak = h
  b = puncak * (1-p / 100)

u = h - b
   
print("Trailling stop ter-trigger pada hari ke-", hari, "dengan harga Rp", h)
print("Harga puncak: Rp", puncak)
print("Batas jual (trailing stop)", p, "%):Rp", b)
print("Keuntungan: Rp", u)
  
