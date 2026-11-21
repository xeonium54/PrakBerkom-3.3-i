# Nama  : Vidia Nurafifa
# NIM   : 15626011
# Desc  : No 3 - Menghitung Genangan Air di Kebun kaktus

# panjang kebun (pk)
# array ketinggian tanah (kt[])
# toleransi air (bt)
# batas tolenrasi air (ba)
# total volume air genangan (tv)
# kaktus busuk Y/N 

pk = int(input("Masukkan panjang kebun: "))
kt = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
ba = int(input("Masukkan batas toleransi air: "))

tv = 0

for i in range(1, pk -1):
    puncak_kiri = kt[0]
    for j in range(0, i):
        if kt[j] > puncak_kiri:
            puncak_kiri = kt[j]
            
    puncak_kanan = kt[i+1]
    for j in range(i+1, pk):
        if kt[j] > puncak_kanan:
            puncak_kanan = kt[j]
            
    if puncak_kiri < puncak_kanan:
        bt = puncak_kiri
    else:
        bt = puncak_kanan
            
    genangan = bt - kt[i]
    
    if genangan > 0:
        tv = tv + genangan
        
print("Total volume genangan air adalah "+ str(tv) +".")

if tv > ba:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("kaktus Tuan Ky selamat!")