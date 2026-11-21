# NIM/Nama  : 15426130 / Yudha Putra
# Tanggal   : 28 Oktober 2026
# Deskripsi : Menghitung total volume genangan air di kebun Tuan Ky dan
#             menentukan apakah kaktus selamat (tanpa max() dan min()).

N = int(input("Masukkan panjang kebun: "))
data = input("Masukkan array ketinggian tanah: ").split()
W = int(input("Masukkan batas toleransi air: "))

# Ubah hasil split (string) menjadi array bilangan bulat
H = [0 for i in range(N)]
for i in range(N):
    H[i] = int(data[i])

total = 0
# Titik paling kiri dan paling kanan tidak bisa menampung air
for i in range(1, N - 1):
    # Dinding tertinggi di kiri (termasuk titik i)
    kiri = H[i]
    for j in range(0, i):
        if H[j] > kiri:
            kiri = H[j]
    # Dinding tertinggi di kanan (termasuk titik i)
    kanan = H[i]
    for j in range(i + 1, N):
        if H[j] > kanan:
            kanan = H[j]
    # Batas air = dinding yang lebih pendek
    if kiri < kanan:
        batas = kiri
    else:
        batas = kanan
    # Volume air di titik i
    total += batas - H[i]

print("Total volume genangan air adalah " + str(total) + ".")
if total > W:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")