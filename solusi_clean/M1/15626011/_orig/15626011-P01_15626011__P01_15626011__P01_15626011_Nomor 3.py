# NIM/Nama  : Vidia Nurafifa
# Tanggal   : Rabu, 30/09/2026
# Deskripsi : Menghitung upah dan tunjangan

# sn = batas shift normal (menit)
# u = upah (per menit)
# ul = upah lembur
# tm = tunjangan makan 
# bmt = batas minimal tunjangan

j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan jam keluar: "))

sn = float(input("Masukkan batas shift normal: "))
u = float(input("Masukkan  upah per menit: "))
ul = float(input("pengali upah lembur: "))
tm = float(input("tunjangan makan: "))
bmt = float(input(" batas minimal tunjangan (menit): "))

menit_masuk = j1 * 60 + m1
menit_keluar = j2 * 60 + m2
total_menit = menit_keluar - menit_masuk

menit_normal = (total_menit + sn - abs(total_menit - sn))/2
menit_lembur = (total_menit - sn + abs(total_menit - sn))/2

tunjangan = tm * (total_menit >= bmt)

upah_normal = menit_normal * u
upah_lembur = menit_lembur * u * ul
total_upah = upah_normal + upah_lembur + tunjangan

jam = total_menit // 60
menit = total_menit % 60

print("Total durasi kerja:", int(jam), "jam", int(menit), "menit")
print("Menit kerja normal:", int(menit_normal), "menit")
print("Menit kerja lembur:", int(menit_lembur), "menit")

print(f"Tunjangan makan: Rp{tunjangan:.2f}")
print(f"Total upah diterima: Rp{total_upah:.2f}")











