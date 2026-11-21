# NIM / NAMA : 15626026 / MUTHI'AH AZKA NIAMILLAH
# TANGGAL : 28 OKTOBER 2026
# DESKRIPSI : SOAL 3

n = int(input("masukkan panjang kebun: "))
h_input = input("masukkan array ketinggian tanah: ")
w = int(input("masukkan batas toleransi air: "))

h = [0] * n
for i in range(n):
    h[i] = int(h_input[i])

total_volume = 0

for i in range(n):
    max_left = 0
    for j in range(0,1):
        if h[j] > max_right:
            max_right = h[j]   
    if max_left > h[i] and max_right > h[i]:
        if max_left < max_right:
            batas_air = max_left
        else:
            batas_air = max_right
        total_volume += (batas_air - h[i])

print("total volume genangan air adalah " + str(total_volume)+".")

if total_volume > w:
    print("kaktus tuan ky mati membusuk!")
else:
    print("kaktus tuan ky selamat!")