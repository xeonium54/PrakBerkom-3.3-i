# NIM/Nama : 15626020/Rudianto
# Tanggal   : 28 Oktober 2026
# Deskripsi : Menghitung volume genangan air pada kebun

N = int(input("Masukkan panjang kebun: "))
H = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
W = int(input("Masukkan batas toleransi air: "))

total = 0

for i in range(1, N - 1):
    kiri = H[0]

    for j in range(1, i):
        if H[j] > kiri:
            kiri = H[j]

    kanan = H[i + 1]

    for j in range(i + 2, N):
        if H[j] > kanan:
            kanan = H[j]

    if kiri < kanan:
        batas = kiri
    else:
        batas = kanan

    if batas > H[i]:
        total = total + batas - H[i]

print("Total volume genangan air adalah " + str(total) + ".")

if total > W:
    print("Kaktus Tuan Ky mati membusuk !")
else:
    print("Kaktus Tuan Ky selamat !")

N = int(input("Masukkan panjang kebun: "))
H = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
W = int(input("Masukkan batas toleransi air: "))

total = 0

for i in range(1, N - 1):
    kiri = H[0]

    for j in range(1, i):
        if H[j] > kiri:
            kiri = H[j]

    kanan = H[i + 1]

    for j in range(i + 2, N):
        if H[j] > kanan:
            kanan = H[j]

    if kiri < kanan:
        batas = kiri
    else:
        batas = kanan

    if batas > H[i]:
        total = total + batas - H[i]

print("Total volume genangan air adalah " + str(total) + ".")

if total > W:
    print("Kaktus Tuan Ky mati membusuk !")
else:
    print("Kaktus Tuan Ky selamat !")

N = int(input("Masukkan panjang kebun: "))
H = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
W = int(input("Masukkan batas toleransi air: "))

total = 0

for i in range(1, N - 1):
    kiri = H[0]

    for j in range(1, i):
        if H[j] > kiri:
            kiri = H[j]

    kanan = H[i + 1]

    for j in range(i + 2, N):
        if H[j] > kanan:
            kanan = H[j]

    if kiri < kanan:
        batas = kiri
    else:
        batas = kanan

    if batas > H[i]:
        total = total + batas - H[i]

print("Total volume genangan air adalah " + str(total) + ".")

if total > W:
    print("Kaktus Tuan Ky mati membusuk !")
else:
    print("Kaktus Tuan Ky selamat !")

