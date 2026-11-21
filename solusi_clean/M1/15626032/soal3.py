# NIM/Nama : 15626032/Muhamad Faiz Abdul Aziz
# Tanggal : 30 September 2026
# Deskripsi : Menghitung total upah diterima

# Kamus
jm = int(input("Masukan jam masuk: "))
mm = int(input("Masukan menit masuk: "))
jk = int(input("Masukan jam keluar: "))
mk = int(input("Masukan menit keluar: "))
bs = int(input("Masukan batas shift normal (menit): "))
u = int(input("Masukan upah per menit: "))
pu = float(input("Masukan pengali upah lembur: "))
tm = int(input("Masukan tunjangan makan: "))
mt = int(input("Masukan batas minimal tunjangan (menit): "))
tdk = int(input("Total durasi kerja: jam menit"))
mkn = int(input("Menit kerja normal: "))
mkl = int(input("Menit kerja lembur: "))

# Logaritma
pul = 1.5
Total_durasi_kerja = (jk*60*mk) - (jm*60*mm)
Menit_normal = (Total_durasi_kerja - mkl)
Menit_lembur = (Total_durasi_kerja - Menit_normal)
Total_Upah = (Menit_normal*u) + (mkl*u*pu) + tm 

# Hasil

print(f"Total Upah diterima: Rp{Total_Upah}")