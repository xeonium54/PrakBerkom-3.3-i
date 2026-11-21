# NIM / Nama  : 15626021 / Aufaa Fakhri Ibrahim Irahadi
# Tanggal     : 28 Oktober 2026
# Deskripsi   : Program menghitung volume genangan air hujan pada kebun berundak tanpa menggunakan fungsi bawaan maks dan min

# KAMUS VARIABEL
# panjang_kebun : int
# input_str : list of str
# batas_toleransi : int
# H : list of int
# left_max : list of int
# right_max : list of int
# curr_max_left : int
# curr_max_right :  int
# total_genangan : int
# dinding_pendek : int
# volume_titik : int
# i : int

# Algoritma
panjang_kebun = int(input("Masukkan panjang kebun: "))
input_str = input("Masukkan array ketinggian tanah: "). split()
batas_toleransi = int(input("Masukkan batas toleransi air: "))

# Mengubah elemen list menjadi bilangan bulat (integer) tanpa fungsi max/min bawaan 
H = []
for i in range(panjang_kebun):
    H.append(int(input_str[i]))

# Membuat array untuk menyimpan dinding tertinggi di sebelah kiri dan kanan massing-masing titik
left_max = [0] * panjang_kebun
right_max = [0] * panjang_kebun

# Mencari dinding tertinggi di sebelah kiri untuk setiap titik 
curr_max_left = 0
for i in range(panjang_kebun):
    if H[i] > curr_max_left:
        curr_max_left = H[i]
    left_max[i] = curr_max_right

# Mencari dinding tertinggi di sebelah kanan untuk setiap titik
curr_max_right = 0
for i in range(panjang_kebun -1, -1, -1):
    if H[i] > curr_max_right:
        curr_max_right = H[i]
    right_max[i] = curr_max_right

# Menghitung total volume genangan air
total_genangan = 0
for i in range(panjang_kebun):
    # menentukan dinding terpendek antara sisi kiri dan kanan (pengganti min)
    if left_max[i] < right_max [i]:
        dinding_pendek = left_max[i]
    else:
        dinding_pendek = right_max[i]

# Volume air pada titik ke-i adalah selisih dinding pendek dan ketinggian tanah 
volume_titik = dinding_pendek - H[i]
if volume_titik > 0:
    total_genangan += volume_titik

print(f"Total volume genangan air adalah {total_genangan}")

# Nasib kaktus Tuan Ky
if total_genangan > batas_toleransi:
    print("Kaktus Tuan Ky mati membusuk")
else:
    print("Kaktus Tuan ky selamat!")