# NIM       : 15426129
# Nama      : Kirani Rizky Aulia Khairunissa
# Tanggal   : Rabu, 30 September 2026
# Deskripsi : Praktikum 1 Berpikir Komputasional (Problem 3)

# PROGRAM Penghitungan Durasi Kerja, Tunjangan Makan, dan Upah Pekerja
# Deskripsi:
# User memasukkan data berupa jam dan menit masuk kerja, jam dan menit keluar kerja, batas shift normal dalam menit,
# upah per menit, pengali upah lembur, tunjangan makan, batas maksimal, dan batas minimal tunjangan dalam menit.
# Sistem melakukan penghitungan dan menyajikan total durasi kerja, menit kerja normal, menit kerja lembut, tunjangan
# makan, dan total upah yang diterima pekerja.

# KAMUS
# j1 : int
# m1 : int
# j2 : int
# m2 : int
# N : int
# U : int
# L : float
# M : int
# T_min : int
# total_menit : int
# menit_lembur : int
# menit_normal : int
# tunjangan_makan : float
# upah_normal : float
# upah_lembur : float
# total_upah : float
# total_jam : int
# total_menit : int

# ALGORITMA
print("Penghitungan Durasi Kerja, Tunjangan Makan, dan Upah Pekerja")
print()

j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = int(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = int(input("Masukkan tunjangan makan: "))
T_min = int(input("Masukkan batas minimal tunjangan (menit): "))

total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
total_jam = int(total_menit / 60)
sisa_menit = int(total_menit - (total_jam *60))

menit_lembur = int((total_menit - 480) * 1)
menit_normal = int(total_menit - menit_lembur)

tunjangan_makan = float(menit_lembur * M)

upah_normal = float(menit_normal * U)
upah_lembur = float(menit_lembur * U * L)
total_upah = float(upah_normal + upah_lembur + tunjangan_makan)

print("Total durasi kerja: ", total_jam, "jam", sisa_menit, "menit")
print("Menit kerja normal: ", menit_normal, "menit")
print("Menit kerja lembur: ", menit_lembur, "menit")
print("Tunjangan makan: Rp", tunjangan_makan)
print("Total upah diterima: Rp", total_upah)