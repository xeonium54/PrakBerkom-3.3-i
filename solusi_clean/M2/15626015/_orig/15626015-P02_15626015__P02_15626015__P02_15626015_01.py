# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 14 Oktober 2026
# Deskripsi : Validasi skor apakah valid atau tidak menggunakan if-else

# KAMUS
# skor : int = skor ujian peserta

# ALGORITMA
# input nilai skor dalam bentuk data integer
skor = int(input("Masukkan skor : "))

# Jika skor kurang dari sama dengan 100 dan lebih dari sama dengan nol
# maka skor valid dan dapat diinput ke dalam sistem 
if (skor <= 100 and skor >= 0) :
    print("Skor valid, dapat diinput ke sistem.")
else :
    print("Skor tidak valid, perlu diperiksa ulang")