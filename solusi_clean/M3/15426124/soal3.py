# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 28 Oktober 2026
# Deskripsi : Menghitung volume genangan air

# Algoritma
N = int(input("Masukkan panjang kebun: "))
raw_input = input("Masukkan array ketinggian tanah: ").split()
H = []
for x in raw_input:
    H.append(int(x))

W = int(input("Masukkan batas toleransi air: "))

total_genangan = 0

for i in range(1, N - 1):
    # Mencari dinding tertinggi di sebelah kiri secara manual
    max_kiri = H[0]
    for j in range(i):
        if H[j] > max_kiri:
            max_kiri = H[j]
        
    # Mencari dinding tertinggi di sebelah kanan secara manual
    max_kanan = H[N - 1]
    for j in range(i + 1, N):
        if H[j] > max_kanan:
            max_kanan = H[j]
            
    # Menentukan batas air (dinding yang lebih pendek)
    if max_kiri < max_kanan:
        batas_air = max_kiri
    else:
        batas_air = max_kanan
        
    if batas_air > H[i]:
        total_genangan += (batas_air - H[i])

print(f"Total volume genangan air adalah {total_genangan}.")
if total_genangan > W:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")