#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 28 Oktober 2026
#Deskripsi : Program menghitung volume air yang tertampung di kebun kaktus

N = int(input("Masukkan panjang kebun N: "))
raw_inputan = input("Masukkan array ketinggian tanahnya:").split()
H = []
for item in raw_inputan:
    H.append(int(item))
W = int(input("Masukkan volume batas toleransi airnya: "))

kiri_maks = []
current_max = 0
kanan_maks = [0] * N
for i in range(N):
    if current_max < H[i]:
        current_max = H[i]
    kiri_maks.append(current_max)
    kanan_maks [i] = current_max
total_volume_air = 0
for i in range(1,N-1):
    if kiri_maks[i] < kanan_maks[i]:
        dinding_pendek = kiri_maks[i]
    else:
        dinding_pendek = kanan_maks[i]
genangan = dinding_pendek - H[i]
if genangan > 0:
    total_volume_air += genangan
print(f"Total volume air yang tertampung: {total_volume_air}")
if total_volume_air > W:
    print("Kaktus tuan Ky mati membusuk")
else:
    print("Kaktus tuan Ky selamat")