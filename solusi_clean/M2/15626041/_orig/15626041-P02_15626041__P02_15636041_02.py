# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 14 Oktober 2026
# Deskripsi : Tarif parkir

jamparkir = int(input("Masukan durasi parkir (jam): "))
listrik = input("Apakah mobil listrik? (y/n)")
weekend = input("Apakah akhir pekan? (y/n)")

if jamparkir<=2:
    tarif = 5000
elif 2<jamparkir<=6:
    tarif = (jamparkir-2)*3000+5000
elif 6<jamparkir:
    tarif = (jamparkir-6)*2000+17000

if listrik=="y" and jamparkir>2:
    tariflistrik=-5000
else: 
    tariflistrik=0\

if weekend=="y":
  totaltarif = (tarif+tariflistrik)*1.2

else:
    totaltarif = (tarif+tariflistrik)*1


print(f"Total tarif parkir adalah Rp{totaltarif}")


