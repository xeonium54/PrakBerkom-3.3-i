''''15626033_Farah Ghiza Humairoh'''
'''30 sepetember 2026'''
'''praktikum berkom'''



'''PROBLEM 3'''
j1 = int(input("masukkan jam masuk: "))
m1 = int(input("masukkan menit masuk: "))
j2 = int(input("masukkan jam keluar: "))
m2 = int(input("masukkan menit keluar: "))
N = int(input("masukkan batas menit kerja normal (N): "))
U = int(input("masukkan upah normal per menit (U): "))
L = int(input("masukkan Pengali lembur (L): "))
M = int(input("maasukkan besar tunjangan makan (M): "))
T_min = int(input("masukkan durasi kerja minimum untuk tunjangan (T_min): "))
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60
menit_lembur = (total_menit - N) * (total_menit < N)
menit_normal = total_menit - menit_lembur
tunjangan_makan = M * (total_menit >= T_min)
total_upah = (menit_normal * U) + (menit_lembur * L * U) + tunjangan_makan
print(f"durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"menit kerja normal: {menit_normal} menit")
print(f"menit lembur: {menit_lembur} menit")
print(f"tunjangan makan: {tunjangan_makan:.2f}")
print(f"total upah yang diterima: {total_upah:.2f}")
