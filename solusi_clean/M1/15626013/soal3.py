# NIM/Nama :
# Tanggal : 30 September 2026
# Deskripsi : Menghitung durasi kerja, kerja normal, lembur,
#             tunjangan makan, dan total upah tanpa percabangan.

# Input waktu masuk
j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))

# Input waktu keluar
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))

# Input ketentuan kerja
N = int(input("Masukkan batas shift normal (menit): "))
U = float(input("Masukkan upah per menit: "))
L = float(input("Masukkan pengali upah lembur: "))
M = float(input("Masukkan tunjangan makan: "))
Tmin = int(input("Masukkan batas minimal tunjangan (menit): "))

# Mengubah waktu menjadi total menit
waktu_masuk = j1 * 60 + m1
waktu_keluar = j2 * 60 + m2

# Menghitung total durasi kerja
total_menit = waktu_keluar - waktu_masuk

# Menghitung menit normal dan menit lembur
# abs() digunakan sebagai pengganti max() dan min()
selisih_normal = abs(total_menit - N)

menit_normal = (total_menit + N - selisih_normal) / 2
menit_lembur = (total_menit - N + selisih_normal) / 2

# Mengubah total menit menjadi jam dan menit
jam_kerja = total_menit // 60
menit_sisa = total_menit % 60

# Menentukan tunjangan berdasarkan batas minimal
# True bernilai 1 dan False bernilai 0 dalam operasi matematika
faktor_tunjangan = int(total_menit >= Tmin)

# Menghitung tunjangan
tunjangan = M * faktor_tunjangan

# Menghitung upah normal
upah_normal = menit_normal * U

# Menghitung upah lembur
upah_lembur = menit_lembur * U * L

# Menghitung total upah
total_upah = upah_normal + upah_lembur + tunjangan

# Menampilkan hasil
print(f"Total durasi kerja: {int(jam_kerja)} jam {int(menit_sisa)} menit")
print(f"Menit kerja normal: {int(menit_normal)} menit")
print(f"Menit kerja lembur: {int(menit_lembur)} menit")
print(f"Tunjangan makan: Rp{tunjangan:.2f}")
print(f"Total upah diterima: Rp{total_upah:.2f}")