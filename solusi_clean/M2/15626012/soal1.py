# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 30 September 2026
# Deskripsi: Program memvalidasi skor ujian 

# KAMUS 
# skor : int

skor = int(input('Masukkan skor: '))


if 0 <= skor <= 100:
    print('skor valid')
else:
    print('skor tidak valid')

