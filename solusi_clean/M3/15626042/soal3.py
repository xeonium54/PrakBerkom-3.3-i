#Nama: Febrian Yafi Hakim
#NIM: 15626042
#Deskripsi : problem 3

n = int(input("Masukkan panjang kebun: "))

input_h = input("Masukkan array ketinggian tanah: ").split()

H = [0 for i in range (n)]

for i in range(n):
    H[i] = int(input_h[i])

w = int(input("masukkan batas toleransi air: "))

max_kiri = [0 for i in range(n)]
max_kanan = [0 for i in range(n)]

tertinggi_kiri = 0
for i in range(n):
    if (H[i] > tertinggi_kiri):
        tertinggi_kiri = H[i]
max_kiri[i] = tertinggi_kiri

tertinggi_kanan = 0

for i in range(n):
    indeks = n - 1 - i
    if (H[indeks] > tertinggi_kanan):
        tertinggi_kanan = H[indeks]
        max_kanan[indeks] = tertinggi_kanan

total_air = 0
for i in range(n):
    batas_air = max_kiri[i]
if (max_kanan[i] < batas_air):
    batas_air = max_kanan[i]

    genangan = batas_air - H[i]

    if (genangan > 0):
        total_air += genangan

print("Total volume genangan air adalah " + str(total_air) + ".")

if (total_air > w):
    print("Kaktus tuan ky mati membusuk")
else:
    print("Kaktus Tuan Ky akan selamat")