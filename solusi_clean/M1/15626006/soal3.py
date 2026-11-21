# NIM / Nama : 15626006 / Maria Zeysta Kamelia Rumanti
# Tanggal : 30 September 2026
# Deskripsi : Program menghitung upah kerja paruh waktu. Program ini menghitung rincian waktu kerja, upah normal, uang lembur, dan tunjangan makan.
print("Problem 3")

#KAMUS
j1 = int
m1 = int
j2 = int
m2 = int
N = int #batas shift normal
U = float #upah per menit
L = float #upah lembur
M = float #tunjangan makan
T_minimum = float #batas minimal tunjangan

j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
T_minimum = float(input("Masukkan batas minimal tunjangan (menit): "))

#Hitung total menit
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

#Hitung menit lembur dan menit normal
menit_lembur = (total_menit - N) * (total_menit > N)
menit_normal = total_menit - menit_lembur

#Hitung tunjangan makan
tunjangan_didapat = M * (total_menit >= T_minimum)

#Hitung total upah
total_upah = (menit_normal * U) + (menit_lembur * U * L) + tunjangan_didapat

print("Total durasi kerja: ", durasi_jam, "jam", durasi_menit, "menit")
print("Menit kerja normal: ", menit_normal, "menit")
print("Menit kerja lembur: ", menit_lembur, "menit")

print("Tunjangan makan: Rp", tunjangan_didapat)
print("Total upah diterima: Rp", total_upah)