# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 30 September 2026
# Deskripsi: Menentukan durasi kerja, menit kerja normal, menit kerja lembur, tunjangan makan, dan total upah Tuan Loji

# KAMUS
# j1 : int 
# m1 : int
# j2 : int
# m2 : int 
# batas_shift : int
# upah_per_menit : int
# pengali_upah_lembur : float
# tunjangan_makan : int
# batas_minimal_tunjangan : int

# Input Tuan Loji
j1 = int(input("Masukkan jam masuk kerja: "))
m1 = int(input("Masukkan menit masuk kerja: "))
j2 = int(input("Masukkan jam keluar kerja: "))
m2 = int(input("Masukkan menit keluar kerja: "))
batas_shift = int(input("Masukkan batas shift (menit): "))
upah_per_menit = int(input("Masukkan upah per menit (Rp): "))
pengali_upah_lembur = float(input("Masukkan pengali upah lembur: "))
tunjangan_makan = int(input("Masukkan tunjangan makan (Rp): "))
batas_minimal_tunjangan = int(input("Masukkan batas minimal tunjangan (menit): "))

# Durasi kerja dalam menit
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

# Menjadikan durasi kerja dalam jam dan menit
jam_kerja = total_menit // 60
menit_kerja = total_menit % 60

# Menentukan menit kerja normal dan menit kerja lembur
pengondisian_lembur = int(total_menit > batas_shift)
menit_lembur = (total_menit - batas_shift) * pengondisian_lembur
menit_normal = total_menit - menit_lembur

# Menentukan tunjangan
pengondisisan_tunjangan = int(total_menit >= batas_minimal_tunjangan)
tunjangan = tunjangan_makan * pengondisisan_tunjangan

# Menghitung total upah yang diterima Tuan Loji
total_upah = (menit_normal * upah_per_menit) + (menit_lembur * upah_per_menit * pengali_upah_lembur) + tunjangan

# Output 
print("Durasi kerja Tuan Loji adalah:", jam_kerja, "jam", menit_kerja, "menit")
print("Menit kerja normal:", menit_normal, "menit")
print("Menit kerja lembur:", menit_lembur, "menit")
print("Tunjangan makan yang diterima Tuan Loji: Rp", f"{tunjangan:.2f}")
print("Total upah yang diterima Tuan Loji: Rp", f"{total_upah:.2f}")