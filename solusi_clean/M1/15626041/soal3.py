# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 30 September 2026
# Deskripsi : Rincian durasi, menit kerja normal, menit kerja lembur, tunjangan makan, serta total upah

jam_masuk = int(input('Masukkan jam masuk:'))
menit_masuk = int(input('Masukkan menit masuk:'))
jam_keluar = int(input('Masukkan jam keluar:'))
menit_keluar = int(input('Masukkan menit keluar:'))

batas_shift_normal = int(input('Masukan batas shift normal (menit):'))
upah_permenit = float(input('Masukkan upah per menit:'))
pengali_lembur = float(input('Masukkan pengali upah lembur:'))

tunj_makan = int(input('Masukkan tunjangan makan Rp:'))
batas_min_tunj = int(input('Masukkan batas minimal tunjangan:'))

total_menit = (jam_keluar*60+menit_keluar)-(jam_masuk*60-menit_masuk)
menit_normal = total_menit // batas_shift_normal * batas_shift_normal
menit_lembur = total_menit % batas_shift_normal

upah_normal = menit_normal*upah_permenit
upah_lembur = menit_lembur*pengali_lembur*upah_permenit

tunjangan = total_menit // batas_min_tunj * tunj_makan

durasi_jam = total_menit // 60
durasi_menit = total_menit % 60

total_upah = upah_normal+upah_lembur+tunjangan

print(f"Total durasi kerja :{durasi_jam} jam, {durasi_menit} menit")
print(f"Menit kerja normal :{menit_normal}")
print(f"Menit kerja lembur : {menit_lembur}")
print(f"Tunjangan: {tunjangan}")
print(f"Total upah diterima: Rp.{total_upah}")




