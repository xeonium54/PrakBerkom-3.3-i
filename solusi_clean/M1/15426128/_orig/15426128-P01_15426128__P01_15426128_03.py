# Nim/Nama : 15426128/Fathir Sulihansyah
# Tanggal  : 30 September 2026
# Deskripsi: Tuan Joji yang menghitung waktu kerjanya untuk menentukan upah

# === KAMUS DATA ===
# j1, m1 : int (jam dan menit masuk)
# j2, m2 : int (jam dan menit keluar)
# n      : int (batas menit kerja normal)
# u      : float (upah per menit)
# l      : float (pengali lembur)
# m      : float (tunjangan makan)
# T_min  : int (minimal menit untuk dapat tunjangan makan)
#
# total_menit     : int (total durasi kerja)
# durasi_jam      : int (durasi dalam jam)
# durasi_menit    : int (sisa durasi dalam menit)
# menit_normal    : float (menit kerja normal)
# menit_lembur    : float (menit lembur)
# tunjangan_makan : float (uang makan yang didapat)
# total_upah      : float (total gaji yang diterima)

j1 = int(input("Jam masuk : "))
m1 = int(input("Menit masuk : "))
j2 = int(input("Jam keluar : "))
m2 = int(input("Menit keliar: "))
n = int(input("Masukkan batas waktu normal :"))
u = float(input("Masukkan upah per menit: "))
l = float(input("Masukkan pengali upah lembur : "))
m = float(input("Masukkan tunjangan makan : "))
T_min = int(input("Masukkan batas minimal tunjangan: "))

total_menit = (j2*60+m2) - (j1*60+m1)
durasi_jam = total_menit //60
durasi_menit = total_menit % 60

menit_normal = (total_menit + n - abs(total_menit - n))/2

selisih_lembur = total_menit - n
menit_lembur = (selisih_lembur + 0 + abs(selisih_lembur - 0))/2

dapat_tunjangan = int(total_menit >= T_min)
tunjangan_makan = dapat_tunjangan*m

upah_normal = menit_normal * u
upah_lembur = menit_lembur * (u*l)
total_upah = upah_normal + upah_lembur + tunjangan_makan

print("\n=== RINCIAN HASIL ===")
print(f"Total durasi kerja: {durasi_jam} jam, {durasi_menit} menit,({total_menit} menit)")
print(f"Menit kerja normal: {menit_normal: .2f} menit")
print(f"Menit kerja lembur: {menit_lembur: .2f} menit")
print(f"Tunjangan makan: Rp{tunjangan_makan: .2f}")
print(f"Total upah di terima: Rp{total_upah:.2f}") 

    