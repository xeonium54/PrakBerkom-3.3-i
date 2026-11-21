# NIM/Nama : 15626004
# Tanggal : 10/14/2026
# Deskripsi : Program memvalidasi sebuah skor peserta ujian 

# KAMUS 
# N : int

# ALGORITMA
skor = int(input("masukkan skor : "))

if 0 <= skor <= 100:
    print("skor valid, dapat diinput ke sistem")
else: 
    print("skor tidak valid, perlu diperiksa ulang")
