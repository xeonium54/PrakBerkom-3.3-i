#NIM/Nama  : 15426130/ Yudha Putra
#Tanggal   : 30 September 2027
#Deskripsi : Menghitung Upah shift kerja

j1 = int(input("Masukkan jam masuk : "))
m1 = int(input("Masukkan menit masuk : "))
j2 = int(input("Masukkan jam keluar : "))
m2 = int(input("Masukan menit keluar : "))
batas_shift_normal = int(input("Masukkan batas shift normal (menit) : "))
upah = float(input("Masukkan upah per menit : "))
pengali_upah_lembur = float(input("Masukkan pengali upah lembur : "))
tunjangan = float(input("Masukkan tunjangan makan : "))
batas_minimal_tunjangan = float(input("Masukkan batas minimal tunjangan (menit) : "))

#Total Durasi Kerja
total = (j2*60+m2)-(j1*60+m1)

lembur = (total-batas_shift_normal) * (total>batas_shift_normal)
normal = total - lembur
tunjangan_diterima = tunjangan * (total>=batas_minimal_tunjangan)

total_upah = normal* upah + lembur*upah*pengali_upah_lembur+tunjangan_diterima

print(f"Total Durasi Kerja :{total//60} jam {total%60}menit")
print(f"Menit Kerja Normal : {normal} menit")
print(f"Menit kerja lembur : {lembur} menit")
print(f"Tunjangan makan : {tunjangan_diterima:.2f}")
print(f"Total Upah diterima : Rp{total_upah:.2f}")