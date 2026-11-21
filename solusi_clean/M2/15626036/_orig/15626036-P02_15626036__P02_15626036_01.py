#NIM/Nama : Aghneo Amar Ahsan
#Tanggal : 14 Oktober 2026
#Deskripsi : Program ini dibuat untuk mengecek apakah nilai yang diinputkan sesuai dengan rentang yang diinginkan (0 - 100)

#Kamus
#skor : integer

skor = int(input("Masukkan skor: "))

if 0 <= skor <= 100:
    print("Skor valid, dapat diinput ke sistem")
else: 
    print("Skor tidak valid, perlu diperiksa ulang")