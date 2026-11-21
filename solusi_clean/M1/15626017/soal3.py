# NIM/Nama  : 15626017 / Naura Vira Vania Ramadhani
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung rincian durasi kerja dan total upah tanpa if-else/max/min

# KAMUS
# j1, m1             : int (jam dan menit masuk kerja)
# j2, m2             : int (jam dan menit keluar kerja)
# N                  : int (batas shift normal dalam menit)
# U                  : float (upah kerja normal per menit)
# L                  : float (pengali upah lembur)
# M                  : float (tunjangan makan dalam rupiah)
# T_min              : int (batas minimal menit untuk dapat tunjangan)
# total_menit        : int (total durasi kerja dalam menit)
# durasi_jam         : int (komponen jam dari total durasi)
# durasi_menit       : int (komponen menit dari total durasi)
# selisih            : int (selisih total_menit terhadap N)
# menit_lembur       : int (durasi kerja lembur dalam menit)
# menit_normal       : int (durasi kerja normal dalam menit)
# dapat_tunjangan    : int (flag boolean 1/0 apakah dapat tunjangan)
# tunjangan_diterima : float (nominal tunjangan makan yang didapat)
# total_upah         : float (total upah bersih yang diterima)

# Input data 
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))

N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T_min = int(input("Masukkan batas minimal tunjangan (menit): "))

# 1. Menghitung total durasi kerja dalam menit
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

# Durasi dalam jam dan menit
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

# 2. Menghitung menit lembur (menggunakan rumus nilai mutlak abs)
selisih = total_menit - N
menit_lembur = int((selisih + abs(selisih)) / 2)

# 3. Menghitung menit normal
menit_normal = total_menit - menit_lembur

# 4. Menghitung tunjangan makan (perbandingan boolean menghasilkan 1 atau 0)
dapat_tunjangan = int(total_menit >= T_min)
tunjangan_diterima = M * dapat_tunjangan

# 5. Menghitung total upah
total_upah = (menit_normal * U) + (menit_lembur * U * L) + tunjangan_diterima

print(f"Total durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"Menit kerja normal: {menit_normal} menit")
print(f"Menit kerja lembur: {menit_lembur} menit")
print(f"Tunjangan makan: Rp{tunjangan_diterima:.2f}")
print(f"Total upah diterima: Rp{total_upah:.2f}")