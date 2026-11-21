#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 30 September 2026
#Deskripsi : Program untuk menghitung total konsentrasi akhir dari campuran larutan

#v1,v2,v3=volume masing-masing larutan (ml)
#c1,c2,c3=konsetrasi masing-masing larutan (persen, %)

#Deklarasi
v1=int(input("masukan volume larutan 1 (ml):"))
v2=int(input("masukan volume larutan 2 (ml):"))
v3=int(input("masukan volume larutan 3 (ml):"))
c1=int(input("masukan konsentrasi larutan 1 (persen):"))
c2=int(input("masukan konsentrasi larutan 2 (persen):"))
c3=int(input("masukan konsentrasi larutan 3 (persen):"))

#Proses
total_zat = (v1 * c1) + (v2 * c2) + (v3 * c3)
total_volume = v1 + v2 + v3
konsentrasi_akhir = (total_zat / total_volume)

#Output
print("konsentrasi akhir dari campuran larutan adalah:", konsentrasi_akhir, "%")

#END
