# NIM/Nama : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal : 30 September 2026
# Deskripsi : 

# Kamus:
# j1 (int) = Jam Masuk
# m1 (int) = Menit Masuk
# j2 (int) = Jam Keluar
# m2 (int) = Menit keluar
# N (int) = Batas durasi kerja normal maksimal dalam menit
# U (int) = Upah per menit 
# L (float) = Pengali upah per menit (khusus lembur)
# M (int) = Tunjangan makan (dengan durasi Tmin)
# Tmin (int) = Minimal durasi mendapat tunjangan
# TotalMenit (int) = menghitung total durasi kerja dalam menit
# TotalJam (int) = total durasi kerja dalam jam
# TotalJamM (int) = sisa menit setelah dimodulo totalmenit

# Algoritma
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = int(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = int(input("Masukkan tunjangan makan: "))
Tmin = int(input("Masukkan batas minimal tunjangan (menit): "))
TotalMenit = int(((j2*60)+m2)-((j1*60)+m1))
TotalJam = int((TotalMenit/60))
TotalJamM = int(TotalMenit%60)
TotalMLembur = int((TotalMenit - N))
TotalUpah = float(((U*(TotalMenit - TotalMLembur))+(TotalMLembur*U*L)+M))

print(f"Total Durasi Kerja: {TotalJam} jam {TotalJamM} menit ")
print(f"Menit kerja normal: {(TotalMenit - TotalMLembur )} menit")
print(f"Menit kerja lembur: {TotalMLembur} menit")
print(f"Tunjangan Makan: Rp {M}")
print(f"Total upah diterima: Rp{TotalUpah.2f}")


