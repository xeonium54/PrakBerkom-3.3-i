#Nama/NIM: Aghneo Amar Ahsan
#Tanggal: 28 Oktober 2026
#Deskripsi: 

PersentaseTrailingStop = int(input("Masukkan persentase trailing stop: "))

sahamArray = []
keuntungan = 0
batasJual = 0
puncak = 0
for i in range (0, 100000) :
    saham = int(input(f"Masukkan harga saham hari ke-{i+1}: "))

    sahamArray.append(saham)

    if puncak > sahamArray[i]:
        puncak = sahamArray[i]

    batasJual = puncak * ((100 - PersentaseTrailingStop)/100)

    if sahamArray[i] <= batasJual: 
        print(f"Trailing Stop ter-triger pada hari ke-{i+1} dengan harga Rp.", sahamArray[i])
        keuntungan = sahamArray[i] - sahamArray[0]
        break

print(f"Batas jual (trailing stop {PersentaseTrailingStop}%): ", batasJual)
print("Keuntungan: ", keuntungan)