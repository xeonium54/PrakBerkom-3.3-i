# NIM/Nama: 15626040/Frizka Yunisaf
# Tanggal: Rabu, 14 Oktober 2026
# Deskripsi: Program yang otomatis memvalidasi sebuah skor

nilai = int(input("Masukkan skor: "))
if nilai>0:
    if nilai<100:
        print("Skor valid, dapat diinput ke sistem")
    if nilai>100:
        print("Skor tidak valid, perlu diperiksa ulang")
    if nilai==100:
        print("Skor valid, dapat diinput ke sistem")
elif nilai<0:
    print("Skor tidak valid, perlu diperiksa ulang")
else:
    print("Skor valid, dapat diinput ke sistem")
