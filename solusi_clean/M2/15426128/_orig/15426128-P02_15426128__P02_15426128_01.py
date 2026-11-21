# NIM/Nama : 15426128/Fathir Sulihansyah 
# Tanggal  : 14 Oktober 2026
# Deskripsi: Program untuk memvalidasi skor ujian peserta

# Kamus koding : 
# 0 <= skor <= 100 : Untuk memastikan bahwa skor yang di input
# if dan else : Pembuat dua kemungkinan apakah dapat di input atau tidak

skor = int(input("Masukkan skor = "))

if 0 <= skor <= 100 :
    print("Skor valid, dapat diinput ke sistem")
else :
    print("Skor tidak valid, perlu di periksa ulang")


