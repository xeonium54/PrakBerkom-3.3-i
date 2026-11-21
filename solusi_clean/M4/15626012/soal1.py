# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 11 November 2026
# Deskripsi: Program menyederhanakan aspect ratio 

# KAMUS 
# fpb (x, y) : int 
# lebar, tinggi, factor, lebar, tinggi : int 

def fpb(x, y):


    while y != 0:
        x, y = y, x % y
    return x


x = int(input('Masukkan lebar: '))
y = int(input('Masukkan tinggi: '))
factor = fpb(x, y)
lebar = x // factor 
tinggi = y // factor

print(f'aspect ratio yang dihasilkan adalah {lebar}:{tinggi}')








