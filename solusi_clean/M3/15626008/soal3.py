# NIM/NAMA : 15626008 / Arya Satya Anggara
# Tanggal : 28 Oktober 2026
# Deskripsi : program ini menghitung total genangan air berdasarkan ketinggian tanah, hasilnya digunakan untuk menentukan apakah kaktus selamat atau mati sesuai batas toleransi air


N = int(input("masukkan jumlah titik tanah: "))
H = list(map(int, input("masukkan ketinggian tanah: ").split()))
W = int(input("masukkan batas toleransi air: "))

total = 0

for i in range(1, N - 1):
    kiri = H[i]
    kanan = H[i]

    for j in range(i):
        if H[j] > kiri:
            kiri = H[j]

    for j in range(i + 1, N):
        if H[j] > kanan:
            kanan = H[j]

    if kiri < kanan:
        batas = kiri
    else:
        batas = kanan

    if batas > H[i]:
        total = total + (batas - H[i])

print("total volume genangan air:", total)

if total > W:
    print("kaktus tuan ky mati")
else:
    print("kaktus tuan ky selamat")