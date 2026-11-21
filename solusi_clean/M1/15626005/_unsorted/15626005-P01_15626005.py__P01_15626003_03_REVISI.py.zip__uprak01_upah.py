# NIM/Nama : 15626005/Addien Maulana Bima
# Tanggal : 30 September 2026
# Deskripsi : Uprak01_Jam lembur

jm = int(input("Masukkan jam masuk : "))
mm = int(input("Masukkan menit masuk : "))
jk = int (input("Masukkan jam keluar : "))
mk = int(input("Masukkan menit keluar : "))
bm = int(input("Masukkan batas shift normal : "))
upm = int(input("Masukkan upah per menit : "))
pul = float(input("Masukkan pengali upah lembur : "))
tm = int(input("Masukkan tunjangan makan : "))
bmt = int(input("Masukkan batas minimal tunjangan : "))

total_durasi_kerja = (jk*60+mk)-(jm*60+mm)
dalam_jam = total_durasi_kerja//60
dalam_menit = total_durasi_kerja%60
menit_kerja_normal = bm                      
waktu_lembur = total_durasi_kerja-bm
makan = total_durasi_kerja-bmt
tunjangan_makan = tm
total_upah = (bm*upm)+(waktu_lembur*upm*pul)+tunjangan_makan

print(f"Total durasi kerja adalah : {total_durasi_kerja} menit = {dalam_jam} jam {dalam_menit} menit")
print(f"Menit kerja normal adalah : {menit_kerja_normal} menit")
print(f"Menit kerja lembur adalah : {waktu_lembur} menit ")
print(f"Tunjangan makan adalah : {tunjangan_makan}")
print(f"Total upah yang didapatkan : {total_upah} rupiah")
                                 