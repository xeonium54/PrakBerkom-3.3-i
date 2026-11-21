
N = int(input("Masukkan panjang kebun: "))
H = input("Masukkan array ketinggian tanah: ").split()
W = int(input("Masukkan batas toleransi air: "))

# Ubah setiap elemen dari string menjadi integer
for i in range(N):
    H[i] = int(H[i])

total = 0


for i in range(1, N - 1):
    
    kiri = H[i]
    for j in range(0, i):
        if H[j] > kiri:
            kiri = H[j]


    kanan = H[i]
    for j in range(i + 1, N):
        if H[j] > kanan:
            kanan = H[j]

    
    if kiri < kanan:
        batas = kiri
    else:
        batas = kanan

   
    total = total + (batas - H[i])


print("Total volume genangan air adalah " + str(total) + ".")
if total > W:
    print("Kaktus Tuan Ky mati membusuk")
else:
    print("Kaktus Tuan Ky hidup")
