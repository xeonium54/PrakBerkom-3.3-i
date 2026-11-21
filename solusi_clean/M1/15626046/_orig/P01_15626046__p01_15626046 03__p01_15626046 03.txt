Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> j1 = int(input("Masukkan jam masuk: "))
Masukkan jam masuk: 8
>>> m1 = int(input("Masukkan menit masuk: "))
Masukkan menit masuk: 0
>>> j2 = int(input("Masukkan jam keluar: "))
Masukkan jam keluar: 17
>>> m2 = int(input("Masukkan menit keluar: "))
Masukkan menit keluar: 30
>>> N = int(input("Masukkan batas shift normal (menit): "))
Masukkan batas shift normal (menit): 480
>>> U = float(input("Masukkan upah per menit: "))
Masukkan upah per menit: 100
>>> L = float(input("Masukkan pengali upah lembur: "))
Masukkan pengali upah lembur: 1.5
>>> M = float(input("Masukkan tunjangan makan: "))
Masukkan tunjangan makan: 25000
>>> T = int(input("Masukkan batas minimal tunjangan (menit): "))
Masukkan batas minimal tunjangan (menit): 360
>>> total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
>>> jam = total_menit // 60
>>> menit = total_menit % 60
>>> menit_normal = min(total_menit, N)
>>> menit_lembur = max(total_menit - N, 0)
>>> if total_menit >= T:tunjangan = M else:tunjangan = 0
SyntaxError: invalid syntax
>>> if total_menit >= T
SyntaxError: expected ':'
>>> if total_menit >= T:
...      tunjangan = M
... else: tunjangan = 0
...     
...     
... 
...     
>>> 
>>> total_upah = (menit_normal * U) + (menit_lembur * U * L) + tunjangan
>>> print(f"Total durasi kerja: {jam} jam {menit} menit")
Total durasi kerja: 9 jam 30 menit
