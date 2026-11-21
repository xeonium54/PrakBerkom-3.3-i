#NIM/Nama : 15626027_Muhammad Faiz Dhiaul Haq
#Tanggal : 14 Oktober 2026
#Deskripsi : Membuat program memvalidasi skor

#Kamus 
#Skor : Integer {Skor ujian peserta yang diinput pengguna}

#Input Skor dari pengguna
skor = int(input("Masukkan skor: "))

#Validasi skor
if 0 <= skor <= 100:
    print("Skor Valid, dapat diinput ke sistem")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")