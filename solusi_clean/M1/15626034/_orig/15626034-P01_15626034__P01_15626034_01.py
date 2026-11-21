#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 30 September 2026
#Deskripsi : Program untuk menghitung total biaya listrik

# w=jumlah watt
# j=lama lampu menyala (jam)
# r=tarif listrik (rupiah per kwh)

#1. konversi watt ke kilowatt
# daya_kw=w*j/1000 
#2.menhitung total energi dalam kwh
# energi_kwh=daya_kw*waktu_jam
#3. menghitung total berdasarkan tarif r
#total_biaya=energi_kwh*tarif_r


#Deklarasi
w=int(input("masukan jumlah watt:"))
j=int(input("masukan lama lampu menyala (jam):"))
r=int(input("masukan tarif listrik (rupiahper kwh):"))

#Proses
energi_kwh = int(w * j / 1000)
print("energi kwh:", energi_kwh)
total_biaya = int(energi_kwh * r)
print("total biaya listrik yang terbuang:", total_biaya)  

#End