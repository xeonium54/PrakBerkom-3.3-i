# NIM/Nama : 15626023 / Andre Partogi N Butarbutar
# Tanggal :14/10/2026
# Deskripsi :Percabangan 


 #kamus
# A = durasi parkir  yang akan diinput
# B = menentukan apakah itu sbuah mobil listrik
# C = menentukan apakah akhir pekan atau tidak
# tarif = jumlah perhitungan ketika suatu vairabel memenuhi syarat yang disebutkan
# total = tarif total yang dihasilkan


#Algoritma
A = int(input("Masukkan durasi parkir (jam):"))
B = input("Apakah mobil listrik? (y/n):")
C = input("Apakah akhir pekan? (y/n):")


if A <= 2 : #Menyatakan syarat bahwa Durasi hingga 2 jam atau tidak. Jika tidak akan dilanjutkan ke algoritma berikutnya
    tarif = 5000
elif A > 2 and A <= 6 : #Menyatakan syarat bahwa Durasi di atas 2 jam hingga 6 jam atau tidak. Jika tidak akan dilanjutkan ke algoritma berikutnya
    tarif= (A - 2) * 3000 + 5000
else :
    tarif = 5000 + (4*3000) +(A-6)*2000  

if B == 'y' and A > 2: #sama dengan sebelumnya ini merupakan persyaratan yang dibuat untuk membuat kode membaca apakah sesuai syarat atau tidak
    if C == 'y' :
        total = (tarif - 5000)* 1.2
    else :
        total = (tarif - 5000)
else :
    if  C== 'y' :
        total = tarif * 1.2
    else :
        total = tarif

print(f"Total tarif parkir adalah Rp{total}")


