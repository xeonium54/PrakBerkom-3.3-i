''''15626033_Farah Ghiza Humairoh'''
'''30 sepetember 2026'''
'''praktikum berkom'''



'''PROBLEM 1'''
daya = float(input("masukkan daya lampu (watt): "))
lama = float(input("masukkan lama lampu menyala (jam): "))
tarif = float(input("masukkan tarif listrik (rupiah per kWh: "))
energi = (daya * lama) / 1000
biaya = energi * tarif
biaya_bersih = [round(biaya, 2), int(biaya)][biaya % 1 ==0]
print(f"biaya listrik yang terbuang adalah Rp{biaya_bersih}")


'''PROBLEM 2'''
c1 = int(input("masukkan konsentrasi larutan pertama (persen): "))
v1 = int(input("masukkan volume larutan pertama (ml): "))
c2 = int(input("masukkan konsentrasi larutan kedua (persen): "))
v2 = int(input("masukkan volume larutan kedua (ml): "))
c3 = int(input("masukkan konsentrasi larutan ketiga (persen): "))
v3 = int(input("masukkan volume larutan ketiga (ml): "))
c_akhir = (c1 * v1 * c2 * v2 * c3 * v3) / (v1 + v2 + v3)
c_akhir_rounded = round(c_akhir, 2)
print(f"konsentrasi akhir larutan campuran adalah {c_akhir_rounded} persen")



'''PROBLEM 3'''
j1 = int(input("masukkan jam masuk: "))
m1 = int(input("masukkan menit masuk: "))
j2 = int(input("masukkan jam keluar: "))
m2 = int(input("masukkan menit keluar: "))
N = int(input("masukkan batas menit kerja normal (N): "))
U = int(input("masukkan upah normal per menit (U): "))
L = int(input("masukkan Pengali lembur (L): "))
M = int(input("maasukkan besar tunjangan makan (M): "))
T_min = int(input("masukkan durasi kerja minimum untuk tunjangan (T_min): "))
total_menit = (j2 * 60 + m2) - (j1 * 60 + m1)
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60
menit_lembur = (total_menit - N) * (total_menit < N)
menit_normal = total_menit - menit_lembur
tunjangan_makan = M * (total_menit >= T_min)
total_upah = (menit_normal * U) + (menit_lembur * L * U) + tunjangan_makan
print(f"durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"menit kerja normal: {menit_normal} menit")
print(f"menit lembur: {menit_lembur} menit")
print(f"tunjangan makan: {tunjangan_makan:.2f}")
print(f"total upah yang diterima: {total_upah:.2f}")
