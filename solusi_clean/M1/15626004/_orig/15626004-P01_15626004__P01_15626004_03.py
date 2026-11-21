# NIM/Nama: Nirmala Rahma Maulida
# Tanggal : 30 September 2026
# Deksripsi : Pada praktikum ini membantu Tuan joji untuk menghitung luaran upah dan tunjangan 
 
# KAMUS
# j1, m1, j2, m2, Tmin, N = int
# U, L, M = float 

j1 = int(input("masukkan jam masuk: "))
m1 = int(input("masukkan menit masuk: "))
j2 = int(input("masukkan jam keluar: "))
m2 = int(input("masukkan menit keluar: "))
N = int(input("masukkan batas shift normal (menit): "))
U = float(input("masukkan upah per menit: "))
L = float(input("masukkan pengali upah lembur: "))
M = float(input("masukkan tunjangan makan: "))
T = int(input("masukkan minimal tunjangan (menit): "))

#perhitungan durasi
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

menit_normal = min(total_menit, N)
menit_lembur = max (0, total_menit - N)

tunjangan_makan = M * int(total_menit >= T)

upah_normal = menit_normal * U
upah_lembur = menit_lembur * U * L

total_upah = upah_normal + upah_lembur + tunjangan_makan

print("total durasi kerja", durasi_jam)
print("menit kerja normal", menit_normal)
print("menit kerja lembur", menit_lembur)
print("tunjangan makan", tunjangan_makan)
print("total upah diterima", total_upah)

