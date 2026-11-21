# NIM/Nama : Maria Amatussyafee Nurjaman
# Tanggal : 30 September 2026
# Deskripsi : Menghitung durasi kerja, menit kerja normal, menit lembur, tunjangan makan dan total upah

# PROGRAM : Problem 3

# KAMUS
# jam_masuk, menit_masuk, jam_keluar, menit_keluar, batas_shift_normal, upah_per_menit, pengali_lembur, tunjangan_makan, batas_minimal_tunjangan : integer
# total_durasi_kerja, menit_lembur, menit_lembur, menit_normal, total_upah : integer

# ALGORITMA
jam_masuk = int(input("Masukan jam masuk: "))
menit_masuk = int(input("Masukan menit masuk: "))
jam_keluar = int(input("Masukan jam keluar: "))
menit_keluar = int(input("Masukan menit keluar: "))
batas_shift_normal = int(input("Masukan batas shift normal (menit): "))
upah_per_menit = int(input("Masukan upah per menit: "))
pengali_upah_lembur = int(input("Masukan pengali upah lembur: "))
tunjangan_makan = int(input("Masukan tunjangan makan: "))
batas_minimal_tunjangan = int(input("Masukan minimal tunjangan (menit): "))

total_durasi_kerja = (jam_keluar * 60 + menit_keluar) - (jam_masuk * 60 + menit_masuk)
total_durasi_kerja > batas_shift_normal = menit_lembur 
menit_lembur = (total_durasi_kerja - batas_shift_normal) * 1
menit_normal = total_durasi_kerja - menit_lembur
total_durasi_kerja >= batas_minimal_tunjangan = tunjangan_makan
total_upah = (batas_shift_normal * upah_per_menit) + (menit_lembur * upah_per_menit * pengali_upah_lembur)

print(f"Total durasi kerja adalah {total_durasi_kerja}")
print(f"Menit kerja normal: {menit_normal}")
print(f"Menit kerja lembur: {menit_lembur}")
print(f"Tunjangan makan: {tunjangan_makan}")
print(f"Total upah diterima: {total_upah}")