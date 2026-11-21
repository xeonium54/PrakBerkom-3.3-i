#Alfathir Sangkara Anindya 
#15626031
#Deskripsi:Program menghitung total tarif parkir

#durasi=1
#jenis= n
#hari=n

durasi= int(input("masukkan durasi parkir anda (jam): "))
jenis=input("apakah mobil anda mobil listrik? (y/n): ").lower()
hari=input("apakah ini akhir pekan? (y/n): ").lower()

#menghitung tarif dasar
if durasi <= 2:
    tarif=5000
else:
    if durasi <=6:
        tarif= 5000 + (durasi - 2) * 3000
    else:
        tarif= 5000 + 4 * 3000 + (durasi-6) * 2000

#potongan buat kalau mobil listrik
if jenis == "y":
    tarif = tarif - 5000
else:
    tarif = tarif


#tarif akhir pekan

if hari == "y":
    tarif = tarif * 1.2
else:
    tarif = tarif
    

#OUTPUT AKHIR
print("total tarif parkir adalah Rp", tarif)


