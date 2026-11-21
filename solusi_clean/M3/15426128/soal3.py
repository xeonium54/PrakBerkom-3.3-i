# NIM/Nama              : 15426128 / Fathir Sulihansyah
# Tanggal               : 28 Oktober 2026
# Deskripsi             : Program menghitung total volume genangan air hujan di kebun kaktus 
#                         dan menentukan apakah kaktus selamat atau mati membusuk tanpa fungsi max/min bawaan

# KAMUS KODING
# N                   : int   -> Panjang kebun / jumlah elemen array ketinggian tanah
# raw_input_array     : list  -> List string masukan ketinggian tanah dari input().split()
# W                   : int   -> Batas toleransi volume air maksimal yang dapat ditoleransi kaktus
# H                   : list  -> Array integer yang berisi ketinggian tanah di tiap titik
# total_genangan      : int   -> Akumulator total volume air yang menggenang di seluruh kebun
# i                   : int   -> Indeks iterasi untuk setiap titik tanah
# max_kiri            : int   -> Tinggi dinding maksimum di sebelah kiri titik ke-
# max_kanan           : int   -> Tinggi dinding maksimum di sebelah kanan titik ke-i
# j                   : int   -> Variabel iterasi bantu untuk mencari maksimum kiri/kanan
# batas_air           : int   -> Ketinggian batas air maksimum pada titik ke-i (dinding terpendek)

N = int(input("Masukkan panjang kebun: "))
raw_input_array = input("Masukkan array ketinggian tanah: ").split()
W = int(input("Masukkan batas toleransi air: "))

H = []
for item in raw_input_array:
    H.append(int(item))

total_genangan = 0


for i in range(1, N - 1):
    max_kiri = H[0]
    for j in range(0, i):
        if H[j] > max_kiri:
            max_kiri = H[j]
    max_kanan = H[N - 1]
    for j in range(i + 1, N):
        if H[j] > max_kanan:
            max_kanan = H[j]
            
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
