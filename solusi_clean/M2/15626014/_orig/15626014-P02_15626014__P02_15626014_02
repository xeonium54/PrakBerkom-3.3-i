#Nama : Fadhil Zulhilmi
#NIM : 15626014
#Deskripsi = Menghitung total tarif yang harus dibayar

#Pake float karena ada kemungkinan angka desimal
durasi = float(input("Masukkan durasi parkir (jam) :"))
mobil_listrik = input("Apkah mobil listrik? (y/n) :"). lower ()
akhir_pekan = input ("Apakah akhir pekan? (y/n)"). lower ()

if durasi <= 2:
    tarif = 5000
elif durasi <= 6:
    tarif = 5000 + (durasi - 2) * 3000
else :
    tarif = 5000 + (4 * 3000) + (durasi - 6) * 2000

if mobil_listrik == "y" and  durasi > 2:
    tarif -= 5000

if akhir_pekan == "y":
    tarif *= 1.2

print(f"Total tarif parkir adalah Rp{tarif}")