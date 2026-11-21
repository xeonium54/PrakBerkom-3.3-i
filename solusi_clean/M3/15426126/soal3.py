# NIM/Nama: 15426126
# Tanggal : 28 Oktober 2026
# Deskripsi: Menghitung volume genangan air di kebun kaktus Tuan Ky

N = int(input("Masukkan panjang kebun: "))
H_str = input("Masukkan array ketinggian tanah: ").split()

# Konversi elemen array dari string ke integer tanpa fungsi max/min
H = []
for x in H_str:
    H.append(int(x))

W = int(input("Masukkan batas toleransi air: "))

# Array untuk menyimpan tinggi dinding maksimum di sebelah kiri dan kanan setiap elemen
left_max = [0] * N
right_max = [0] * N

# Cari tinggi maksimum dari kiri
current_max = 0
for i in range(N):
    if H[i] > current_max:
        current_max = H[i]
    left_max[i] = current_max

# Cari tinggi maksimum dari kanan
current_max = 0
for i in range(N - 1, -1, -1):
    if H[i] > current_max:
        current_max = H[i]
    right_max[i] = current_max

# Hitung total volume genangan air
total_air = 0
for i in range(N):
    # Tentukan batas air (dinding terpendek di antara kiri dan kanan)
    if left_max[i] < right_max[i]:
        batas_air = left_max[i]
    else:
        batas_air = right_max[i]
    
    # Volume air di titik i adalah batas_air dikurangi ketinggian tanah saat ini
    genangan = batas_air - H[i]
    if genangan > 0:
        total_air += genangan

print("Total volume genangan air adalah " + str(total_air) + ".")

# Cek apakah kaktus selamat atau mati
if total_air > W:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")