# NIM/Nama : 15626038/Keysha Hana Putri
# Tanggal : 30 September 2026
# Deskripsi : Program ini digunakan untuk menghitung durasi kerja, menit kerja normal, menit kerja lembur, tunjangan makan, dan total upah yang diterima oleh Tuan Joji.

# KAMUS (maaf saya lupa penulisan kamus bagaimana, saya terlalu fokus pada latihan problem-solving T_T)

#Input
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T_min = int(input("Masukkan batas minimal tunjangan (menit): "))

#Proses
total_menit = j2 * 60 + m2 - j1 * 60 + m1 #Hitung total durasi kerja dengan mencari selisih antara jam keluar dan jam masuk

menit_kerja = total_menit . N             #Hitung menit kerja normal dengan mengurangi durasi kerja dengan ...
upah = menit_kerja * U

menit_lembur = total_menit - N            #Hitung menit kerja lembur dengan mengurangi durasi kerja dengan batas shift normal
upah_lembur = U * L

tunjangan = (M >= T_min)

total_upah = {upah} + {upah_lembur} + {tunjangan}

#Output
print(f"Total durasi kerja: {total_menit}")
print(f"Menit kerja normal: {menit_kerja}")
print(f"Menit kerja lembur: {menit_lembur}")
print(f"Tunjangan makan: {tunjangan}")
print(f"Total upah diterima: {total_upah}")

#MAAF, PROGRAMNYA BELUM SELESAI :(