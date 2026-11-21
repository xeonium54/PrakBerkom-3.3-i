"""Nama: Reinhard Emanuel Sinaga
Nim: 15626028
"""

n = int(input("Masukkan panjang kebun: "))


input_tanah = input("Masukkan array ketinggian tanah: ").split()


h = []
for x in input_tanah:
    h.append(int(x))


w = int(input("Masukkan batas toleransi air: "))


max_kiri = []
current_max_kiri = 0
for i in range(n):
    max_kiri.append(current_max_kiri)

    if h[i] > current_max_kiri:
        current_max_kiri = h[i]


max_kanan = []

for i in range(n):
    max_kanan.append(0)

current_max_kanan = 0

for i in range(n - 1, -1, -1):
    max_kanan[i] = current_max_kanan

    if h[i] > current_max_kanan:
        current_max_kanan = h[i]


total_air = 0

for i in range(n):

    if i == 0 or i == n - 1:
        continue


    if max_kiri[i] < max_kanan[i]:
        batas_air = max_kiri[i]
    else:
        batas_air = max_kanan[i]


    volume_titik = batas_air - h[i]


    if volume_titik > 0:
        total_air += volume_titik

#OUTPUT
print(f"Total volume genangan air adalah {total_air}.")

if total_air > w:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")