#Alfathir Sangkara Anindya -15626031
#10/28/2026
#Deskripsi: Program Menghitung Genangan Air di Kebun Tuan Ky


#codinganyaaaa
n = int(input("Masukkan panjang kebun: "))
tinggi = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
W = int(input("Masukkan batas toleransi air: "))

total = 0

for i in range(n):
    if i > 0 and i < n - 1:
        kiri = tinggi[0]
        kanan = tinggi[i + 1]

        for j in range(i):
            if tinggi[j] > kiri:
                kiri = tinggi[j]

        for j in range(i + 1, n):
            if tinggi[j] > kanan:
                kanan = tinggi[j]

        if kiri < kanan:
            batas = kiri
        else:
            batas = kanan

        if batas > tinggi[i]:
            total = total + batas - tinggi[i]

print("Total volume genangan air adalah", total)

if total > W:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky aman.")
