#NIM/Nama: 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal: 30 September 2026
#Deskripsi: Menentukan durasi kerja, menit kerja normal, menit lembur, tunjangan makanan, dan total upah tuan joji
#Judul
print("^"*50)
Judul = "Rincian Hasil Kinerja Tuan Joji"
print(Judul.center(50))
print("^"*50)

print(" ")

#Variabel Upah dan Jam kerja
Jam_Masuk = int(input("Masukkan jam masuk: "))
Menit_Masuk = int(input("Masukkan menit masuk: "))
Jam_Keluar = int(input("Masukkan jam keluar: "))
Menit_keluar = int(input("Masukkan menit keluar: "))
Shift_Normal = int(input("Masukkan batas shift normal(menit): "))
Upah_Menit = int(input("Masukkan upah per menit: "))
Pengali_upah_Lembur = float(input("Masukkan pengali upah lembur: "))
Tunjangan_Makan = int(input("Masukkan tunjangan makan: "))
Batas_Minimal_Tunjangan = int(input("Masukkan batas tunjangan minimal (menit): "))


Durasi_Kerja = (Jam_Keluar * 60 + Menit_keluar) - (Jam_Masuk * 60 + Menit_Masuk)
Durasi_Kerja >= 480

menit_Kerja_Lembur = Durasi_Kerja - Menit_Kerja_Normal 

print(f"Durasi Kerja: {Durasi_Kerja}")


                   

