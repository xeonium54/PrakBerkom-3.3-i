# NIM / Nama : 15626018 / Chantal Carissa Zuleika
# Tanggal    : 30 September 2026
# Deskripsi  : Menghitung durasi kerja, lembur, tunjangan makan, dan total upah

# Kamus
# j1          : jam masuk
# m1          : menit masuk
# j2          : jam keluar
# m2          : menit keluar
# N           :  batas shift normal (menit)
# U           : upah per menit
# L           : pengali upah lembur
# M           : tunjangan makan
# Tmin        : batas minimal tunjangan makan (menit)
# total_menit : total durasi kerja (menit)
# jam         : durasi kerja dalam jam
# menit       : sisa durasi kerja dalam menit
# normal      : menit kerja normal
# lembur      : menit kerja lembur
# tunjangan   : tunjangan makan
# total-upah  : total upah yang diterima 

j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal: "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembut: "))
M = float(input("Masukkan tunjangan makan: "))
Tmin = int(input("Masukkan batas minimal tunjangan (menit): "))

total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

jam = total_menit // 60
menit = total_menit % 60

lembur = (total_menit > N) * (total_menit - N)
normal = total_menit - lembur

tunjangan = (total_menit >= Tmin) * M

total_upah = (normal * U) + (lembur * U * L) + tunjangan

print("Total durasi kerja:", jam, "jam", menit, "menit")
print("Menit kerja normal:", normal, "menit")
print("Menit kerja lembur:", lembur, "menit")
print(f"Tunjangan makan: Rp{tunjangan: .2f}")
print(f"Total upah diterima: Rp{total_upah: .2f}")
