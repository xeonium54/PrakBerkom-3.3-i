#NIM/Nama   :15626043/Nevlin Fulvian Rohman
#Tanggal    : 30 September 2026
#Deskripsi  : Problem 1

#Kamus
#w : Daya Lampu
#j : Lama Lampu Menyala
#r : Tarif Listrik
#e : Energi
#b : Biaya Akhir

#Test Case 1
w = int(input('Masukkan daya lampu (watt)='))
j = int(input('Masukkan lama lampu menyala (jam)='))
r = int(input('Masukkan tarif listrik (rupiah per kWh)='))

e = (w*j)/1000

b = e*r
print('Biaya listrik yang terbuang adalah Rp',b)