# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 14/10/2026
# Deskripsi : Program ini berfungsi untuk memvalidasi apakah skor ujian peserta berada dalam rentang 0 hingga 100 secara otomatis. Skor yang ada di luar rentang dinyatakan tidak valid.

#Program Validasi Skor

#deklarasi:
#    skor: integer

#Algoritma:
#   input skor
#   If skor >== 0 And skor <== 100 Then
#       Output "Skor valid, dapat diinput ke sistem."
#   Else
#       Output "Skor tidak valid, perlu diperiksa ulang."
#   Endif       

#menerima input skor dari pengguna
skor = int(input("Masukkan Skor: "))

#memvalidasi apakah skor di rentang 0 hingga 100
if 0 <= skor <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")