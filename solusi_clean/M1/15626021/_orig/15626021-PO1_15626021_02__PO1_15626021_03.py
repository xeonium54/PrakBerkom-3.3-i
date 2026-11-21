# NIM/Nama  : 15626021 / Aufaa Fakhri Ibrahim Irahadi
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung durasi kerja, menit normal, menit lembur, tunjangan makan, dan total upah tanpa menggunakan percabangan (if-else) dan max/min

# KAMUS VARIABEL
# j1, m1          : int (jam dan menit masuk)
# j2, m2          : int (jam dan menit keluar)
# N               : int (batas shift normal dalam menit)
# U               : float (upah per menit)
# L               : float (pengali upah lembur)
# M               : float (nominal tunjangan makan)
# T_min           : int (batas minimal menit untuk dapat tunjangan makan)
# total_menit     : int (total durasi kerja dalam menit)
# durasi_jam      : int (durasi kerja bagian jam)
# durasi_menit    : int (durasi kerja bagian menit)
# selisih         : int (selisih total menit dengan batas normal N)
# menit_lembur    : int (jumlah menit kerja lembur)
# menit_normal    : int (jumlah menit kerja normal)
# dapat_tunjangan : int (flag boolean 1 jika dapat tunjangan, 0 jika tidak)
# tunjangan_makan : float (jumlah tunjangan makan yang didapat)
# upah_normal     : float (total upah menit normal)
# upah_lembur     : float (total upah menit lembut)
# total_upah      : float (total keseluruhan upah yang diterima)

# ALGORITMA
# Input
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))

N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T_Min = int(input("Masukkan batas minimal tunjangan (menit): "))

# 1. Menghitung durasi kerja
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

# 2. Menghitung menit lembur & normal 
selisih = total_menit - N
menit_lembur = (selisih + abs(selisih)) // 2
menit_normal = total_menit - menit_lembur

# 3. Menghitung tunjangan makan
dapat_tunjangan = int(total_menit >= T_Min)
tunjangan_makan = dapat_tunjangan * M

# 4. Menghitung total upah 
upah_normal = menit_lembur * U
upah_lembur = upah_normal * L
total_upah = upah_normal + upah_lembur + tunjangan_makan

#Output
print(f"Total durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"Menit kerja normal: {menit_normal} menit")
print(f"Menit kerja lembur: {menit_lembur} menit")
print(f"Tunjangan makan: Rp{tunjangan_makan: .2f}")
print(f"Total upah diterima: Rp{total_upah: .2f}")