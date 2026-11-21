# Siti Nawa Aulia_15626048
# 30 September 2026
# Menghitung rincian durasi kerja, menit kerja normal, menit lembur dan total upah yang diterima Tuan Joji

# Kamus 
# Jm = Jam Masuk
# Mm = Menit masuk
# Jk = Jam keluar
# Mk = Menit keluar
# Bn = Batas shift normal (menit)
# Pm = Upah per-menit
# Pl = Pengali upah lembur
# Tm = Tunjangan makan
# Bs = Batas minimal tunjangan
# Tds = Total durasi kerja
# Mn = Menit lembur

# Algoritma
Jm = float(input("Masukan jam masuk:"))
Mm = float(input("Masukan menit masuk:"))
Jk = float(input("Masukan jam keluar:"))
Mk = float(input("Masukan menit keluar:"))
Bn = float(input("Masukan batas shit normal"))
Pm = int(input("Masukan upah per-menit"))
Pl = int(input("Masukan pengali upah lembur"))
Tm = int(input("Masukan tunjangan makan"))
Bs = int(input("Masukan batas minimal tunjangan"))

Tds = (Jk*60+Mk)-(Jm*60+Mm)
print(Tds)

Jam = Tds//60
Menit = Tds%60

