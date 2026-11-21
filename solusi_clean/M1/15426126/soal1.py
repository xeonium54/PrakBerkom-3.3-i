#NIM/Nama: 15426126/Zhahiran Kayyis Mushaliyyah
#Tanggal: 30 September 2026
#Deskripsi: Problem 1

daya = float(input("Masukkan daya lampu (watt):"))
jam = float(input("Masukkan lama lampu menyala(jam):"))
tarif = float (input("Masukkan tarif listrik (rupiah per kWh):"))

energi = daya * jam / 1000
biaya = energi * tarif 

print("Biaya listrik yang terbuang adalah Rp" + str(int(biaya)))