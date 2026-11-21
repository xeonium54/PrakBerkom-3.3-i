# NIM/Nama :1562023 / Andre Partogi N Butarbutar
# Tanggal :14/10/2026
# Deskripsi :Percabangan

#Kamus
# A = skor yang ingin dimasukkan dan yang akan di proses

#Algoritma

A = int(input("Masukkan skor:")) # input angka

if A >= 0 and A <= 100 : # fungsi if dan else untuk menentukan variabel A apakah skor valid atau tidak
    print("Skor valid , dapat diinput ke sistem")
else :
    print("Skor tidak valid , perlu diperiksa ulang.")
