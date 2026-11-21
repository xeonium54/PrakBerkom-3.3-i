# NIM/Nama : Luna Febryvazrya
# Tanggal : 30 September 2026 
# Deskripsi : Merincikan serta menjumlahkan durasi kerja dan total upah yang diterima oleh toji

a = int(input("Masukkan jam masuk (a): "))
b = int(input("Masukkan menit masuk (b): "))
c = int(input("Masukkan jam keluar (c): "))
d = int(input("Masukkan menit keluar (d): "))
e = int(input("Masukkan batas shift normal (e): "))
f = int(input("Masukkan upah per menit (f): "))
g = int(input("Masukkan pengali upah lembur (g): "))
h = int(input("Masukkan tunjangan makan (h): "))
i = int(input("Masukkan batas minimal tunjangan (i): "))

total_durasi_jam_kerja = ((c*60) + d) - ((a*60) + b)

# Total durasi kerja dalam jam dan menit
jam = total_durasi_jam_kerja // 60
menit = total_durasi_jam_kerja % 60

# Menit lembur
lembur = (total_durasi_jam_kerja - e)*1
# Menit normal
normal = total_durasi_jam_kerja - lembur

print(f"tunjangan makan, {menit} >= 360 ")

# Total upah 
total_upah = (e*1000) + (lembur*1000*g) + h 

print(f"total durasi jam kerja, {jam} durasi menit kerja, {menit} menit kerja normal {normal} menit kerja lembur {lembur} tunjangan makan, {h}, dan total upah yang diterima oleh toji sebesar {total_upah}")

