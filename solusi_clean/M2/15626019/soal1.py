# NIM/Nama : 15626019
Tanggal : 14-10-2026
#Deskripsi : Membuat program otomatis untuk memvalidasi sebuah skor yang valid pada rentang 0 hingga 100

# KAMUS
# x : int # skor

# ALGORITMA
x = int(input("Masukkan skor: "))

if(x >= 0 or x <=100):
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")