# Program Rincian Durasi Kerja, Upah, dan Tunjangan
# Deskripsi: Menghitung total upah yang diterima yang termasuk di dalamnya tunjangan makanan berdasarkan durasi kerja (jam dan menit keluar - jam dan menit masuk), batas shift, upah per menit, pengali upah lembur, tunjngan makan (rupiah), dan batas minimal tunjangan (menit).

# KAMUS
# j1 : int
# m1 : int
# j2 : int
# m2 : int
# shift_normal : int
# u : float
# l : float
# t_makan : float
# t_min : int
# durasi : int
# menit_normal : int
# tunjangan : float
# total_upah : float

# ALGORITMA
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
shift_normal = int(input("Masukkan batas shift normal (menit): "))
u = float(input("Masukkan upah per menit (Rupiah): "))
l = float(input("Masukkan pengali upah lembur: "))
t_makan = float(input("Masukkan tunjangan makan (Rupiah): "))
t_min = int(input("Masukkan batas minimal tunjangan (menit): "))

durasi = (j2*60+m2)-(j1*60+m1)
menit_lembur = durasi - shift_normal
menit_normal = durasi - menit_lembur
tunjangan = (menit_normal % t_min)* t_makan
total_upah = (shift_normal*u)+(menit_lembur*u*l)+tunjangan

print("Total durasi kerja: ", durasi, "menit")
print("Menit kerja normal: ", menit_normal, "menit")
print("Menit kerja lembur: ", menit_lembur, "menit")
print("Tunjangan makan: Rp", tunjangan)
print("Total upah diterima: Rp", f"{total_upah:.2f}")
