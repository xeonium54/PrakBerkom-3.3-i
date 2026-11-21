# Nama: Kirani Rizky Aulia Khairunissa
# NIM: 15426129
# Tanggal: Rabu, 28 Oktober 2026

# PROGRAM Analisis Saham dengan Strategi Trailing Stop
# Deskripsi: User memasukkan persentase trailing stop dan harga saham selama 5 hari, lalu sistem menyebutkan kapan trailing stop tertrigger dan pada harga berapa, harga puncak, batas jual, dan keuntungan

# KAMUS
# T : array [0, 1, 2, ..., n] of integer

# ALGORITMA
print("Program Analisis Saham dengan Strategi Trailing Stop")

persen = int(input("Masukkan persentase trailing stop: "))
T = [0 for i in range(5)]

for i in range(0,5):
    T[i] = int(input("Masukkan harga saham hari ke-" + str(i+1) + ": "))

i = 0
max = T[0]
while (i > 0):
    if T[i] > max:
        max = T[i]
        i = i
    else:
        i = i+1

batasjual = max * (1 - (persen / 100))

udahtrigger = T[0]
haritrigger = 0
while (i > 0) and (i < 5):
    if T[i] <= batasjual:
        udahtrigger = T[i]
        haritrigger = i
    else:
        i = i+1

untung = batasjual - max

print("Trailing stop ter-trigger pada hari ke-" + str(haritrigger) + " dengan harga Rp" + str(udahtrigger) + ".")
print("Harga puncak: Rp" + str(max))
print("Batas jual (trailing stop " + str(persen) + "%): Rp" + str(batasjual) + ".")
print("Keuntungan: Rp" + str(untung) + ".")