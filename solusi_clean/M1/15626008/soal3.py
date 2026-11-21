#15626008/Arya satya anggara
30 september 2026
Menghitung durasi kerja, upah normal, upah lembur, tunjangan makan, dan total upah berdasarkan waktu kerja yang diberikan.

j2 = int(input("Masukkan jam keluar: "))
... m2 = int(input("Masukkan menit keluar: "))
...
... N = int(input("Masukkan durasi kerja normal maksimal (menit): "))
... U = float(input("Masukkan upah normal per menit: "))
... L = float(input("Masukkan pengali upah lembur: "))
... M = float(input("Masukkan tunjangan makan: "))
... Tmin = int(input("Masukkan minimal durasi untuk tunjangan (menit): "))
...
... total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
...
... # Menghitung menit normal tanpa if-else, max(), atau min()
... menit_normal = (total_menit + N - abs(total_menit - N)) / 2
...
... # Menghitung menit lembur
... menit_lembur = (total_menit - N + abs(total_menit - N)) / 2
...
... # Tunjangan makan menggunakan operasi matematika
... tunjangan = M * ((1 + abs(total_menit - Tmin)) / (1 + abs(total_menit - Tmin)))
...
... # Koreksi tunjangan menggunakan tanda dari selisih
... tunjangan = M * ((total_menit - Tmin + abs(total_menit - Tmin)) / (2 * (total_menit - Tmin + abs(total_menit - Tmin)) + 1))
...
... upah_normal = menit_normal * U
... upah_lembur = menit_lembur * U * L
...
... total_upah = upah_normal + upah_lembur + tunjangan
...
... jam_kerja = total_menit // 60
... menit_kerja = total_menit % 60
...
... print(f"Durasi kerja: {int(jam_kerja)} jam {int(menit_kerja)} menit")
... print(f"Menit kerja normal: {int(menit_normal)} menit")
... print(f"Menit lembur: {int(menit_lembur)} menit")
... print(f"Tunjangan makan: Rp{tunjangan:.2f}")
... print(f"Total upah: Rp{total_upah:.2f}")
...
Masukkan jam masuk: 8
Masukkan menit masuk: 0
Masukkan jam keluar: 17
Masukkan menit keluar: 30
Masukkan durasi kerja normal maksimal (menit): 480
Masukkan upah normal per menit: 1000
Masukkan pengali upah lembur: 1.5
Masukkan tunjangan makan: 25000
Masukkan minimal durasi untuk tunjangan (menit): 360
Durasi kerja: 9 jam 30 menit
Menit kerja normal: 480 menit
Menit lembur: 90 menit
Tunjangan makan: Rp12485.14
Total upah: Rp627485.14
>>>
>>>
... j2 = int(input("Masukkan jam keluar: "))
... m2 = int(input("Masukkan menit keluar: "))
...
... N = int(input("Masukkan durasi kerja normal maksimal (menit): "))
... U = float(input("Masukkan upah normal per menit: "))
... L = float(input("Masukkan pengali upah lembur: "))
... M = float(input("Masukkan tunjangan makan: "))
... Tmin = int(input("Masukkan minimal durasi untuk tunjangan (menit): "))
...
... total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
...
... # Menghitung menit normal tanpa if-else, max(), atau min()
... menit_normal = (total_menit + N - abs(total_menit - N)) / 2
...
... # Menghitung menit lembur
... menit_lembur = (total_menit - N + abs(total_menit - N)) / 2
...
... # Tunjangan makan menggunakan operasi matematika
... tunjangan = M * ((1 + abs(total_menit - Tmin)) / (1 + abs(total_menit - Tmin)))
...
... # Koreksi tunjangan menggunakan tanda dari selisih
... tunjangan = M * ((total_menit - Tmin + abs(total_menit - Tmin)) / (2 * (total_menit - Tmin + abs(total_menit - Tmin)) + 1))
...
... upah_normal = menit_normal * U
... upah_lembur = menit_lembur * U * L
...
... total_upah = upah_normal + upah_lembur + tunjangan
...
... jam_kerja = total_menit // 60
... menit_kerja = total_menit % 60
...
... print(f"Durasi kerja: {int(jam_kerja)} jam {int(menit_kerja)} menit")
... print(f"Menit kerja normal: {int(menit_normal)} menit")
... print(f"Menit lembur: {int(menit_lembur)} menit")
... print(f"Tunjangan makan: Rp{tunjangan:.2f}")
... print(f"Total upah: Rp{total_upah:.2f}")
...
Masukkan jam masuk: 9
Masukkan menit masuk: 15
Masukkan jam keluar: 15
Masukkan menit keluar: 45
Masukkan durasi kerja normal maksimal (menit): 480
Masukkan upah normal per menit: 1200
Masukkan pengali upah lembur: 2
Masukkan tunjangan makan: 20000
Masukkan minimal durasi untuk tunjangan (menit): 300
Durasi kerja: 6 jam 30 menit
Menit kerja normal: 390 menit
Menit lembur: 0 menit
Tunjangan makan: Rp9972.30
Total upah: Rp477972.30
>>>
>>>
... j2 = int(input("Masukkan jam keluar: "))
... m2 = int(input("Masukkan menit keluar: "))
...
... N = int(input("Masukkan durasi kerja normal maksimal (menit): "))
... U = float(input("Masukkan upah normal per menit: "))
... L = float(input("Masukkan pengali upah lembur: "))
... M = float(input("Masukkan tunjangan makan: "))
... Tmin = int(input("Masukkan minimal durasi untuk tunjangan (menit): "))
...
... total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
...
... # Menghitung menit normal tanpa if-else, max(), atau min()
... menit_normal = (total_menit + N - abs(total_menit - N)) / 2
...
... # Menghitung menit lembur
... menit_lembur = (total_menit - N + abs(total_menit - N)) / 2
...
... # Tunjangan makan menggunakan operasi matematika
... tunjangan = M * ((1 + abs(total_menit - Tmin)) / (1 + abs(total_menit - Tmin)))
...
... # Koreksi tunjangan menggunakan tanda dari selisih
... tunjangan = M * ((total_menit - Tmin + abs(total_menit - Tmin)) / (2 * (total_menit - Tmin + abs(total_menit - Tmin)) + 1))
...
... upah_normal = menit_normal * U
... upah_lembur = menit_lembur * U * L
...
... total_upah = upah_normal + upah_lembur + tunjangan
...
... jam_kerja = total_menit // 60
... menit_kerja = total_menit % 60
...
... print(f"Durasi kerja: {int(jam_kerja)} jam {int(menit_kerja)} menit")
... print(f"Menit kerja normal: {int(menit_normal)} menit")
... print(f"Menit lembur: {int(menit_lembur)} menit")
... print(f"Tunjangan makan: Rp{tunjangan:.2f}")
... print(f"Total upah: Rp{total_upah:.2f}")
...
Masukkan jam masuk: 13
Masukkan menit masuk: 0
Masukkan jam keluar: 16
Masukkan menit keluar: 30
Masukkan durasi kerja normal maksimal (menit): 300
Masukkan upah normal per menit: 1250.5
Masukkan pengali upah lembur: 1.75
Masukkan tunjangan makan: 30000
Masukkan minimal durasi untuk tunjangan (menit): 240
Durasi kerja: 3 jam 30 menit
Menit kerja normal: 210 menit
Menit lembur: 0 menit
Tunjangan makan: Rp0.00
Total upah: Rp262605.00