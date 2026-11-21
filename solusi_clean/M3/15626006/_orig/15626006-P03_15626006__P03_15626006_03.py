# NIM / Nama : 15626006 / Maria Zeysta Kamelia Rumanti
# Tanggal : 28 Oktober 2026
# Deskripsi : Simulasi perhitungan total  volume air hujan yang terperangkap di celah-celah kebun Tuan Ky.
# Menghitung total volume genangan air di seluruh area kebun (kecuali titik paling ujung)
# Lalu membandingkan dengan batas toleransi W.
# Jika total air melebihi batas W, kaktus Tuan Ky akan mati.
# Jika kurang dari atau sama dengan W, kaktus dinyatakan selamat.

N = int(input("Masukkan panjang kebun: "))
input_tanah = input("Masukkan array ketinggian tanah: ").split()
W = int(input("Masukkan batas toleransi air: "))

H = []
for i in range(N):
    H.append(int(input_tanah[i]))

total_air = 0

for i in range(1, N-1):
    max_kiri = H[0]
    for j in range(i):
        if H[j] > max_kiri:
            max_kiri = H[j]

    max_kanan = H[i+1]
    for j in range(i+1, N):
        if H[j] > max_kanan:
            max_kanan = H[j]

    batas_air = max_kiri
    if max_kanan < max_kiri:
        batas_air = max_kanan

    if batas_air > H[i]:
        total_air = total_air + (batas_air - H[i])

print(f"Total volume genangan air adalah {total_air}.")

if total_air > W:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat.")