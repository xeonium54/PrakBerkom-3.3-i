n = int(input("masukkan panjang kebun: "))
h_input = input("Masukkan array ketinggian tanah: ").split()
H = []
for x in h_input:
    H.append(int(x))
w = int(input("masukkan batas toleransi air: "))
max_kiri = [0] * n
max_kanan = [0] * n
max_sekarang = 0
for i in range(n):
    max_kiri[i] = max_sekarang
    if H[i] > max_sekarang:
        max_sekarang = H[i]

max_sekarang = 0
for i in range(n - 1, -1, -1):
    max_kanan[i] = max_sekarang
    if H[i] > max_sekarang:
        max_sekarang = H[i]

total_volume = 0
for i in range(1, n - 1):
    if max_kiri[i] < max_kanan[i]
    batas_air = max_kiri[i]
    else: 
    batas_air = max_kanan[i]

    if batas_air > H[i]:
        total_volume += batas_air - H[i]
print(f"Total volume genangan air adalah {total_volume}. ")

if total_volume > w:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("kaktus Tuan Ky selamat!")
