# Nama: Kirani Rizky Aulia Khairunissa
# NIM: 15426129
# Tanggal: Rabu, 28 Oktober 2026

# PROGRAM Analisis Kondisi Kaktus
# Deskripsi: User memasukkan panjang kebun, array ketinggian tanah, dan batas toleransi air, lalu sistem menghitung total volume genangan air serta kondisi kaktusnya

# KAMUS
# H : array of integer (ketinggian tanah)
# V : array of integer (volume genangan)
# N : int, range array

# ALGORITMA
print("Program")
N = int(input("Masukkan panjang kebun: "))

T = [0 for i in range(N)]

for i in range(0,N):
    T = int(input("Masukkan array ketinggian tanah: "))

batas = int(input("Masukkan batas toleransi air: "))

V = [0 for i in range(N)]

min = T[0]
i = 1
found = False
while (i <= N) and (i > 0) and (found == False):
    if T[i] < min:
        min = T[i]
    else:
        i = i + 1

i = 0
for i in range(1,N-1):
    V[i] = min - T[i]

sumvolume = 0
for i in range(0,N):
    sumvolume = sumvolume + V[i]

print("Total volume genangan air adalah " + str(sumvolume) + ".")

if sumvolume > min:
    print("Kaktus Tuan Ky mati membusuk!")
elif sumvolume < min:
    print("Kaktus Tuan Ky selamat!")
else:
    print("Ada kesalahan.")