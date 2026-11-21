#Alfathir Sangkara Anindya 
#15626031
#Deskripsi:Program memvalidasi nilai skor ujian peserta

skor=85

skor = int(input("Masukkabn skor : "))
if skor >=0 and skor <=100:
    print("skor valid, bisa diinput ke sistem")
else:
    print("skor tidak valid, tidak bisa diinput ke sistem")