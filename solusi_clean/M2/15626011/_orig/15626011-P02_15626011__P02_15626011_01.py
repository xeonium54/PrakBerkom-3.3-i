# NIM/Nama  : Vidia Nurafifa
# Tanggal   : Rabu, 14/10/2026
# Deskripsi : Memeriksa skor valid atau tidak

#skor/score = scr 
# 0 s/d 100 (inklusif) = valid, selain itu = invalid

scr= float(input("Masukkan skor: "))

if 0 <= scr <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")

