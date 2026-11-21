# Meneirima masukan dari pengguna
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
I = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T = int(input("Masukkan batas minimal tunjangan (menit): "))
#menghitubg total durasi kerja (menit, jam, dan sisa menit)
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60
menit_lembur = (total_menit - N) * (total_menit > N)
menit_normal = total_menit - menit_lembur
#menghitung tunjangan makan dgn boolean
tunjangan_makan = M * (total_menit >= T)
#mengitung total upah yang diterima
total_upah = (menit_normal * U) + (menit_lembur * U * I) + tunjangan_makan
#Tampilan luaran
print(f"Total durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"Menit kerja normal: {menit_normal} menit")
print(f"Menit kerja lembur: {menit_lembur} menit")
print(f"Tunjangan makan: {tunjangan_makan}")
print(f"Total upah diterima: Rp{total_upah}")