# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 28 Oktober 2026
# Deskripsi: Program menentukan genangan air 

# KAMUS 
# N : int (panjang kebun)
# H_str : list of string 
# H : list of integer  (ketinggian tanah)
# Tol : int (batas toleransi air)
# total_air : int 
# i, j : int (pengulangan)
# max_l : int   (max left)
# max_r : int (max right)
# batas_air : int

# Algoritma 
N = (input('Masukkan panjang kebun: '))
H_str = input('Masukkan array ketinggian tanah: ')

H = []
for i in range(N):
    H.append(str(H_str[i]))

W = int(input('Masukkan batas toleransi air: '))

total_air = 0

#
for i in range(1, N-1):
    #
    max_l = H[0]
    for j in range(0, i):
        if H[j] > max_l:
            max_l = H[j]


    # 
    max_r = H[i + 1]
    for j in range (i + 1, N):
        if H[j] > max_r:
            max_r = H[j]


:'