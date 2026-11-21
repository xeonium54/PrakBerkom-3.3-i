# NIM/Nama : 15426129/Kirani Rizky Aulia Khairunissa
# Tanggal : Rabu, 14 Oktober 2026

# PROGRAM Validasi Skor Ujian
# Deskripsi: User memasukkan skor ujian lalu sistem memeriksa apakah skor tersebut valid (inklusif, masuk range 0-100) atau tidak

# KAMUS
# skor : integer

# ALGORITMA
skor = int(input("Masukkan skor: "))

print("Program Validasi Skor Ujian")
print()

if -1 < skor < 101:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")