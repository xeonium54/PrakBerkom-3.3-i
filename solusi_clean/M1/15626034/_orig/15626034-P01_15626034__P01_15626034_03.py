#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 30 September 2026
#Deskripsi : Program menghitung durasi, lembur, dan tunjangan secara akurat menggunakan aljabar murni tanpa if-else.

#1. Total durasi kerja dalam menit (D)= (J2 * 60 + M2) - (J1 * 60 + M1)
#2. Konversi durasi kerja ke jam dan menit
#   Jam_durasi = D // 60
#   Menit_durasi = D % 60
#3. menit kerja normal dan lembur (menggunakan aljabar mutlak) selisih = D-N
#   abs_selisih = (selisih**2)**0.5
#   normal = (D + abs_selisih) / 2
#   lembur = (D - abs_selisih) / 2
#4. Tunjangan makan, tunjangan= M*int(D >= T) (menggunakan aljabar murni tanpa if-else)
#5. perhitungan upah
#   upah_normal = normal * U
#   upah_lembur = lembur * U * L
#   total_upah = upah_normal + upah_lembur + tunjangan

#Deklarasi
j1=int(input("masukan jam masuk:"))
m1=int(input("masukan menit masuk:"))
j2=int(input("masukan jam keluar:"))
m2=int(input("masukan menit keluar:"))
N=int(input("masukan batas shift normal:"))
U=int(input("masukan upah per menit:"))
L=int(input("masukan pengali lembur:"))
M=int(input("masukan tunjangan makan:"))
batas_minimal_tunjangan = int(input("masukan batas minimal durasi kerja untuk mendapatkan tunjangan:"))

#Proses
D = (j2 * 60 + m2) - (j1 * 60 + m1)
print("total durasi kerja dalam menit:", D)
menit_kerja_normal = (D + ((D - N)**2)**0.5) / 2
print("menit kerja normal:", menit_kerja_normal)
menit_lembur = (D - ((D - N)**2)**0.5) / 2
print("menit lembur:", menit_lembur)
tunjangan = M * int(D >= batas_minimal_tunjangan)
print("tunjangan makan:", tunjangan)
total_upah = (menit_kerja_normal * U) + (menit_lembur * U * L) + tunjangan
print("total upah yang diterima:", total_upah)

#END
