# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 28 October 2026
# Deskripsi : 

# Kamus
# n (int) panjang kebun
# input_tanah (str) array input untuk string ketinggian input
# w (int) batas toleransi v air maksimum yang bisa ditampung kaktus
# h (int) array penampung nilai ketinggian tanah tiap titik
# total_air (int) akumulasi total volume air 
# i (int) indeks perulangan utama untuk mengecek titik input_tanah
# j (int) indeks perulangan untuk membantu mencari dinding tertinggi
# max_kiri (int) nilai ketinggian tanah tertinggi di sebelah kiri titik i
# max_kanan (int) nilai ketinggian tanah tertinggi di sebelah kanan titik i
# batas_air (int) batas ketinggian genangan air pada titik i

# Algoritma
n = int(input("Masukkan panjang kebun: "))
input_tanah = input("Masukkan array ketinggian tanah: ").split()

w = int(input("Masukkan batas toleransi air: "))

h = [0] * n
for i in range(n):
    h[i] = int(input_tanah[i])

total_air = 0

for i in range (1, n-1):
    max_kiri = h[0]
    for j in range (0, i):
        if h[j] > max_kiri:
            max_kiri = h[j]

    max_kanan = h[i+1]
    for j in range (i+1, n):
        if h[j] > max_kanan:
            max_kanan = h[j]

    if max_kiri < max_kanan:
        batas_air = max_kiri
    else:
        batas_air = max_kanan

    if batas_air > h[i]:
        total_air += (batas_air - h[i])

print(f"Total volume genangan air adalah {total_air}.")

if total_air > w:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus tuan Ky selamat!")