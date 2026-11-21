# NIM/Nama  : 15626047 / Jeremia Arista Matthew Sugiarto
# Tanggal   : 30 September 2026
# Deskripsi : Total biaya listrik terbuang akibat lampu menyala selama Tuan Mik sedang memiliki perjalanan

#KAMUS
#w: Daya Lampu
#j: Lama lampu menyala
#r: Tarif listrik per kWh
#biaya: Biaya listrik yang terbuang


#Input
w= int (input("Masukan daya lampu (watt):"))
j= float (input("Masukan lama lampu menyala (jam):"))
r= int (input("Masukan tarif listrik (rupiah per kWh):"))

#Algoritma
biaya=float(w*j/1000*r)

#Output
print (f"Biaya listrik yang terbuang adalah Rp{biaya}")