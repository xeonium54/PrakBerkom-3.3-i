# NIM/Nama : 15626023/Andre Partogi Nathanael Butarbutar
# Tanggal : 30/09/2026
# Deskripsi :

a = float(input("Masukkan jam masuk:"))
b = float(input("Masukkan menit masuk:"))
c = float(input("Masukkan jam keluar:"))
d = float(input("Masukkan menit keluar:"))
e = float(input("Masukkan batas shift normal (menit):"))
f = float(input("Masukkan upah per menit:"))
g = float(input("Masukkan pengali upah lembur:"))
h = float(input("Masukkan tunjangan makan:"))
i = float(input("Masukkan batas minimal tunjangan (menit):"))

# total menit ditotal dulu dikali 60 agar dikonversi menjadi menit
total_menit = ((c*60) + d)-((a*60) + b)


# ditentukan untuk mendapatkan syarat dan faktor penggali uang yang akan didapatkan secara total nantinya
selisih = total_menit - e

lembur = (selisih + selisih) // 2
normal = total_menit - lembur
uang_makan = (total_menit >=i) * h
total_upah = (normal * f ) + (lembur * f * g) + uang_makan

# penggunaan pembagian 60 dan modulo 60 adalah agar dapat menentukan satuan jam dan menit nya melalui metode tersebut
print(f" Total durasi kerja: {total_menit // 60} jam {total_menit % 60} menit")
print(f" Menit kerja normal: {normal} menit")
print(f"menit kerja lembur:{lembur} menit ")
print(f" Tunjangan Makan : Rp {uang_makan:.2f}")
print(f"Total upah diterima : Rp{total_upah:.2f}")