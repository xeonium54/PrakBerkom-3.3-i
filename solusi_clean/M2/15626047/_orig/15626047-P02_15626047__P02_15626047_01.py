# NIM / NAMA : 15626047 / JEREMIA ARISTA MATTHEW
# Tanggal: 14 Oktober 2026
# Deskripsi : Sistem Pemvalidasi Nilai 

#Kamus
#nilai=int 

#Algoritma
nilai=int (input("Masukkan skor: "))
if 0 <=nilai<= 100:
    print ("Skor valid, dapat diinput ke sistem.")

else: 
    print ("Skor tidak valid, perlu diperiksa ulang.")