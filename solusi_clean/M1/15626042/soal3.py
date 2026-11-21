#NIM/Nama   :Febrian Yafi Hakim 15626042 
#Tanggal    :30 September 2026
#Deskripsi  : Menghitung total biaya listrik yang terbuang akibat lampu menyala

#Disclaimer saya belum tau bagaimana format penulisan kamus yang baik dan benar...

#Input
#j = jam masuk, m = menit masuk, x = batas shift normal
j1 = int(input("masukkan jam masuk: "))
m1 = int(input("masukkan jam masuk: "))
j2 = int(input("masukkan jam masuk: "))
m2 = int(input("masukkan jam masuk: "))
s = int(input("masukkan batas shift normal (menit): "))
u = float(input("masukkan upah per menit: "))
l = float(input("masukkan pengali upah lembur: "))
m = float(input("masukkan Tunjangan makan: "))
T_min = int(input("masukkan batas minimal tunjangan (menit): "))

#1. Total durasi kerja (menit)
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

#Format durasi dalam jam dan menit (pake opertaor // dan %)
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

#2. Perhitungan menit lembur (pake boolean)
#kalo total_menit > s maka true (1)
#kalo total_menit < s maka false(0)
is_lembur = int(total_menit > s)
menit_lembur = (total_menit - s) * is_lembur

#mwnit normal
menit_normal = total_menit - menit_lembur

#3.perhitungan runjangan makan (pake bool)
#jika toal_menit > T_min maka true (1), jika tidak bernilai false (0)
is_dapet_tunjangan = int(total_menit >= T_min)
tunjangan_makan = m * is_dapet_tunjangan

#4.Total Upah
total_upah = (menit_normal * u) + (menit_lembur* u * l) + tunjangan_makan

#output
print(f"Total durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"Menit kerja normal: {menit_normal} menit")
print(f"Menit kerja lembur: {menit_lembur} menit")
print(f"Tunjangan makan: Rp{tunjangan_makan:.2f}")
print(f"Total upah diterima: Rp{total_upah:.2f}")