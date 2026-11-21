# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM Skor
# Memvalidasi skor

# KAMUS
# skor = integer

# ALGORITMA
skor = int(input("Masukkan besar skor:"))
if skor>0 and skor<100:
    print("Skor valid. dapat diinput ke dalam sistem")
else:
    print("Skor tidak valid, perlu diperiksa ulang")