# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 30/09/2026
# Deskripsi : Program untuk menghitung rincian durasi kerja dan total upah Tuan Joji berdasarkan waktu masuk dan keluar.

#input data shift dari pengguna
jam_masuk = int(input("Masukkan jam masuk: "))
menit_masuk = int(input("Masukkan menit masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))
menit_keluar = int(input("Masukkan menit keluar: "))
batas_shift = int(input("Masukkan batas shift normal (menit): "))
upah_per_menit = float(input("Masukkan upah per menit: "))
pengali_upah_lembur = float(input("Masukan pengali upah lembur: "))
tunjangan_makan = float(input("Masukkan tunjangan makan: "))
batas_minimal_tunjangan = int(input("Masukkan batas minimal tunjangan (menit): "))

#menghitung total durasi kerja (menit)
total_menit = (jam_keluar*60+menit_keluar)-(jam_masuk*60+menit_masuk)

#konversi total menit ke jam dan menit
durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

#hitung menit lembur dan menit normal
menit_lembur = int(total_menit > batas_shift)*(total_menit - batas_shift)
menit_normal = total_menit - menit_lembur

#hitung tunjangan makan
tunjangan_diterima = int(total_menit >= batas_minimal_tunjangan) * tunjangan_makan

#hitung total upah
total_upah = (menit_normal * upah_per_menit)+(menit_lembur * upah_per_menit * pengali_upah_lembur) + tunjangan_diterima

#tampilan durasi kerja, tunjangan, dan total upah
print(f"Total durasi kerja: {durasi_jam} jam {durasi_menit} menit")
print(f"Menit kerja normal: {menit_normal} menit")
print(f"Menit kerja lembur: {menit_lembur} menit")
print(f"Tunjangan makan: Rp{tunjangan_diterima:.2f}")
print(f"Total upah diterima: {total_upah:.2f}")