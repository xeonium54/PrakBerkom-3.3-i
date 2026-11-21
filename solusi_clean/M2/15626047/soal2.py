# NIM / NAMA : 15626047 / JEREMIA ARISTA MATTHEW
# Tanggal: 14 Oktober 2026
# Deskripsi : Sistem Penghitung Tarif Parkir

#Kamus 
# durasi=int
# ev=str
# weekend=str

#Tarif dasar
durasi=int(input("Masukan durasi parkir (jam):"))
ev=str(input("Apakah mobil listrik? (y/n):"))
weekend=str (input("Apakah akhir pekan? (y/n)"))
if durasi <= 2:
    tarif= 5000
elif durasi <= 6:
    tarif= (durasi-2)*3000+5000
else:
    tarif= 5000+(3000*4)+(durasi-6)*2000


#Mobil Listrik
if ev == 'y' and durasi > 2:
    tarif -= 5000

#Weekend
if weekend == 'y' :
    tarif_akhir= 1.2*tarif
else :
    tarif_akhir= tarif

#Output
print (f"Total tarif parkir adalah Rp{tarif_akhir}")