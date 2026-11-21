# 15626039/Khalif Aufar Aufar Aridkhi
# 30 September 2026
# Praktikum Modul 1 No 3, Menhitung kon

j1 = int(input(" masukkan jam masuk :"))
m1 = int(input(" masukkan menit masuk :"))
j2 = int(input(" masukkan jam keluar :"))
m2 = int(input(" masukkan menit keluar:"))
n = int(input(" masukkan batas shift normal (menit):"))
u = int(input(" masukkan upah per menit:"))
l = float(input(" masukkan pengali upah lembur:"))
m = int(input(" masukkan tunjangan makan:"))
t = int(input(" masukkan batas minimal tunjangan (menit):"))

t_m = (j2 * 60 + m2) - (j1 * 60 + m1)
t_d = t_m - n

t_d > n, menit_lembur == (t_d - n) * 1 
t_d > n, menit_normal == (t_d - menit_lembur)
t_d > t, tj_makan == 0 + m

t_p = (n*u) + (menit_lembur*u*l) + m

print(f"total durasi kerja:{t_d} menit")
print(f"menit kerja normal:{menit_normal} menit")
print(f"menit kerja lembur:{menit_lembur} menit")
print(f"tunjangan makan:Rp.{m:.2f}")
print(f"total upah diterima:Rp. {t_p:.2f} menit")





