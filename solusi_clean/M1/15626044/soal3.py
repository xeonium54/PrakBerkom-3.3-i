# NIM/Nama : 15626044/Saliha Mahira Al-kwarismy
# Tanggal : 2023-03-30
# Deskripsi : Problem 3

# Masukkan data
# j1 adalah jam masuk
# m1 adalah menit masuk
# j2 adalah jam keluar
# m2 adalah menit keluar
# N  adalah durasi normal maksimal, kelebihan waktu kerja di atas N dihitung lembur
# U adalah upah rupiah per menit 
# L adalah upah lembur rupiah per menit
# M adalah tunjangan makan
# T_min adalah batas minimal tunjangan

# Masukkan data
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T_min = int(input("Masukkan batas minimal tunjangan (menit): "))

# Rumus total durasi kerja dalam menit
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

# Konversi durasi kerja ke jam dan menit
jam_kerja = total_menit // 60
menit_kerja = total_menit % 60

# Rumus upah dan tunjangan
# Jika total_menit lebih dari N, maka upah lembur dihitung
# Jika tidak, menghasilkan 0
menit_lembur = int(total_menit > N) * (total_menit - N)
menit_normal = total_menit - menit_lembur

# Rumus tunjangan makan
# Jika total_menit lebih dari T_min, maka tunjangan makan diberikan
# Jika tidak, menghasilkan 0
tunjangan_makan = int(total_menit > T_min) * M

# Rumus total upah
total_upah = (total_menit * U) + tunjangan_makan

# Menampilkan hasil upah yang diterima Tuan Joji
print(f"Total durasi kerja: {jam_kerja} jam {menit_kerja} menit")
print(f"Menit kerja normal {menit_normal} menit")
print(f"Menit kerja lembur {menit_lembur} menit")
print(f"Tunjangan makan: {tunjangan_makan}")
print(f"Total upah diterima: Rp{total_upah}")