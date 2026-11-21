# NIM/Nama: 15626040/Frizka Emily Yunisaf
# Tanggal: 30 September 2026
# Deskripsi: Menghitung rincian durasi kerja, menit kerja normal, menit lembur, tunjangan makan, dan total upah yang diterima Tuan Joji

J1 = int(input("Masukkan jam masuk: "))
M1 = int(input("Masukkan menit masuk: "))
J2 = int(input("Masukkan jam keluar: "))
M2 = int(input("Masukkan menit keluar: "))
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = int(input("Masukkan tunjangan makan: "))
T_min = int(input("Masukkan batas minimal tunjangan (menit): "))

durasi_kerja = (J2*60+M2)-(J1*60+M1)
jam_kerja = durasi_kerja//60
menit_kerja = durasi_kerja % 60
tidak_lembur = (durasi_kerja+N-1)//N
lembur = tidak_lembur*(durasi_kerja-N)
kerja_normal = durasi_kerja-lembur
tidak_tunjangan = (kerja_normal+T_min-1)//T_min
total_upah = (kerja_normal*U)+(lembur*U*L)+M*tidak_tunjangan

print("Total durasi kerja:",jam_kerja, "jam", menit_kerja, "menit")
print("Menit kerja normal:",kerja_normal)
print("Menit kerja lembur:", lembur)
print("Tunjangan makan: Rp",M)
print("Total upah yang diterima Tuan Joji adalah Rp",total_upah)