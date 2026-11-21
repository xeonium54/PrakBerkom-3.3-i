# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 30 September 2026
# Deskripsi : Permasalahan 03, Menghitung upah berdasarkan waktu kerja

# kamus 
# j1 = float = jam masuk dalam jam
# j2 = float = jam keluar dalam jam
# m1 = float = menit masuk dalam menit
# m2 = float = menit keluar dalam menit
# N = float = batas shift normal dalam menit
# U = float = upah normal dalam rupiah
# L = float = upah lembur dalam rupiah
# M = float = tunjangan makan dalam rupiah
# Tmin = float = batas minimal tunjangan dalam menit

j1 = float(input("Masukkan jam masuk (jam)"))
m1 = float(input("Masukkan menit masuk (menit)"))
j2 = float(input("Masukkan jam keluar (jam)"))
m2 = float(input("Masukkan menit keluar (menit)"))
N = float(input("Masukkan batas shift normal"))
U = float(input("Masukkan upah per menit"))
L = float(input("Masukkan pengali upah lembur"))
M = float(input("Masukkan tunjangan makan"))
Tmin = float(input("Masukkan batas minimal tunjangan"))


total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)

lembur = total_menit - N

upah_lembur = lembur * L

total_menit > Tmin

upah_total = U * N + upah_lembur + M