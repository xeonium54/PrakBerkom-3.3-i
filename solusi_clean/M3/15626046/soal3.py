# Kamus
# N: integer, panjang kebun
# H: array ketinggian tanah
# W: integer, batas toleransi air
# kiri: array ketinggian tertinggi dari kiri
# kanan: array ketinggian tertinggi dari kanan
# volume: integer, total genangan air
# air: integer, ketinggian air pada suatu titik
# i: integer, indeks pengulangan

N = int(input("Masukkan panjang kebun: "))
H = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
W = int(input("Masukkan batas toleransi air: "))

kiri = [0] * N
kanan = [0] * N
volume = 0

for i in range(1, N):
    if H[i] > H[i-1]:
        kiri[i] = kiri[i-1]
         kiri[i] = H[i]
         for i in range(N - 2, -1, -1):
    kanan[i] = kanan[i + 1]
    if H[i] > kanan[i]:
        kanan[i] = H[i]
        volume = 0

for i in range(N):
    if kiri[i] < kanan[i]:
        air = kiri[i]
    else:
        air = kanan[i]

    air = air - H[i]

    if air > 0:
        volume = volume + air
        if volume > W:
print("kaktus membusuk:", volume)
else:
    print("kaktus tidak membusuk")
