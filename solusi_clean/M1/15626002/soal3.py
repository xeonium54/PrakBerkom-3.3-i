# Nama = Jihan Salsabila
# NIM = 15626002

# KAMUS
# Jam masuk = integer
# Menit masuk = integer
# Jam keluar = integer
# Menit keluar = integer

# ALGORITMA
J1 = int(input("Masukkan Jam masuk:"))
M1 = int(input("Masukkan menit masuk:"))
J2 = int(input("Masukkan Jam keluar:"))
M2 = int(input("Masukkan menit keluar:"))
N = int(input("Masukkan batas shift normal(menit):"))
Upah_Permenit = int(input("Masukkan upah permenit:"))
Upah_Lembur = int(input("Masukkan upah lembur:"))
Tunjangan_Makan = int(input("Masukkan tunjangan makan:"))
Batas_Minimal_Tunjangan = int(input("Masukkan batas minimal mendapatkan tunjangan(menit):"))

Total_Durasi_Kerja = (J2*60+M2)-(J1*60+M1)
print(f"Maka total durasi kerja tuan Loji adalah {Total_Durasi_Kerja}(menit)")

Menit_lembur = (Total_Durasi_Kerja-N)*1
Menit_Kerja_Normal = (Total_Durasi_Kerja-Menit_lembur)
print(f"Maka tunajangan makanan belaku karena total menit>{Batas_Minimal_Tunjangan}")

Total_Upah = (N*Upah_Permenit)+(Menit_lembur*Upah_Permenit*Upah_Lembur)+Tunjangan_Makan
print(f"Maka total upah yang diberikan kepada tuan loji sebesar:{Total_Upah}")