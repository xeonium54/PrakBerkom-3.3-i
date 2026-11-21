#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal  : Rabu, 28 Oktober 2026
#Deskripsi: Menghitung Volume genangan air dan menentukan nasib kaktus Tuan Ky

#Kamus
#N      : int, Menyimpan panjang kebun
#H_str  : list of str, menyimpan masukan mentah ketinggian tanah
#H      : list of int, menyimpan nilai ketinggian tanah di setiap titik
#W      : int, menyimpan batas toleransi maksimal volume air yang dapat di tampung kebun
#Total air : int, menghitung total volume air genangan yang terperangkap di seluruh titik kebun
#i      : int, penunjuk posisi titik tanah yang sedang dihitung volume airnya pada perulangan pertama
#j      : int, indeks bantuk untuk menelusuri elemen sebelah kanan atau kiri pada perulangan pencarian dinding
#max_kiri : int, menyimpan nilai ketinggian tanah tertinggi di sebelah kiri 
#max_kanan: int, menyimpan nilai ketinggian tanah tertinggi di sebelah kanan


N = int(input("Masukkan panjang kebun: "))

H_str = input("Masukkan array ketinggian tanah: ").split()
H = []
for x in H_str:
    H.append(int(x))

W = int(input("Masukkan batas toleransi air: "))

total_air = 0

for i in range(N): 
    max_kiri = 0
    for j in range(i):
        if H[j] > max_kiri:
            max_kiri = H[j]

batas_air = max_kiri
if max_kanan < batas_air:
    batas_air = max_kanan

if batas_air > H[i]:
    total_air += (batas_air - H[i])

print(f"Total volume genangan air adalah {total_air}.")

if total_air > W:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")
