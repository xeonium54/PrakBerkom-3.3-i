#Nama : Febrian Yafi Hakim
#NIM : 15626042
#Problem 2

durasi = int(input("masukkan durasi parkir (jam): "))
Tipe = input("apakah mobil listrik? (y/n): ")
AP = input("Apakah akhir pekan? (y/n):") #AP = Akhir Pekan

if (durasi <= 2):
    tarif = 5000
elif (durasi <= 6):
    tarif = 5000 + ((durasi - 2) * 3000)
else: 
    tarif = 17000 + ((durasi - 6) * 2000)

if (Tipe == 'y' and durasi > 2):
    tarif -= 5000

if (AP == 'y'):
    tarif = int(tarif * 1.2)

print("Total tarif parkir adalah Rp" + str(tarif))