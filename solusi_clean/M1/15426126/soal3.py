jam_masuk = int(input("Masukkan jam masuk:"))
menit_masuk = int(input("Masukkan menit masuk:"))

jam_keluar = int(input("Masukkan jam keluar: "))
menit_keluar = int(input("Masukkan menit keluar: "))

batas_shift = int(input("Masukkan batas shift normal (menit): "))
upah_per_menit = float(input("Masukkan upah per menit: "))
pengali_lembur = float(input("Masukkan pengali upah lembur: "))
tunjangan_makan = float(input("Masukkan tunjangan makan: "))
batas_tunjanngan = int(input("Masukkan batas minimal tunjangan (menit):"))
total_menit = (jam_keluar * 60 + menit_keluar) - (jam_masuk * 60 + menit_masuk)

menit_kerja_normal = total_menit - (total_menit > batas_shift) * (total_menit - batas_shift)
menit_kerja_lembur = (total_menit > batas_shift) * (total_menit - batas_shift)

upah_normal = menit_kerja_normal * upah_per_menit
upah_lembur = menit_kerja_lembur * upah_per_menit * pengali_lembur
