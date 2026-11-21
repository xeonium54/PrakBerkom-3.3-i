# Alfathir Sangkara Anindya
# 15626031
# program menghitung total durasi kerja dalam menit

# data data
j1=9
m1=15
j2=15
m2=45
N=480
U=1200
L=2.0
M=2000
T_min=300



j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T_min = int(input("Masukkan batas minimal tunjangan (menit): "))

total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)


durasi_jam = total_menit // 60
durasi_sisa_menit = total_menit % 60


selisih_lembur = total_menit - N
menit_lembur = int((selisih_lembur + abs(selisih_lembur)) / 2)
menit_normal = total_menit - menit_lembur


dapat_tunjangan = int(total_menit >= T_min)
tunjangan_makan = M * dapat_tunjangan


upah_normal = menit_normal * U
upah_lembur = menit_lembur * U * L
total_upah = upah_normal + upah_lembur + tunjangan_makan


print(f"Total durasi kerja: {durasi_jam} jam {durasi_sisa_menit} menit")
print(f"Menit kerja normal: {menit_normal} menit")
print(f"Menit kerja lembur: {menit_lembur} menit")
print(f"Tunjangan makan: Rp{tunjangan_makan:.2f}")
print(f"Total upah diterima: Rp{total_upah:.2f}")