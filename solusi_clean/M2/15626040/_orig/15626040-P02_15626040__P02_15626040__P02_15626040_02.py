# NIM/Nama: 15626040/Frizka Yunisaf
# Tanggal: Rabu, 14 Oktober 2026
# Deskripsi: Menghitung total tarif parkir

durasi_parkir = float(input("Masukkan durasi parkir (jam): "))
listrik = str(input("Apakah mobil listrik (y/n): "))
akhir_pekan = str(input("Apakah akhir pekan (y/n): "))

#P1:hingga 2 jam, listrik, akhir pekan
P1 = 5000*1.2
#P2: 2-6 jam, listrik, akhir pekan
P2 = ((5000+(3000*(durasi_parkir-2)))-5000)*1.2
#P3: 2-6 jam, listrik, bukan akhir pekan
P3 = ((5000+(3000*(durasi_parkir-2)))-5000)
#P4: 2-6 jam, bukan listrik, bukan akhir pekan
P4 = (5000+(3000*(durasi_parkir-2)))
#P5: >6 jam, listrik, akhir pekan
P5 = ((5000+(3000*4)+(2000*(durasi_parkir-6)))-5000)*1.2
#P6: >6 jam, listrik, bukan akhir pekan
P6 = ((5000+(3000*4)+(2000*(durasi_parkir-6)))-5000)
#P7: >6 jam, bukan listrik, bukan akhir pekan
P7 = ((5000+(3000*4)+(2000*(durasi_parkir-6))))
#P8 = >6 jam, bukan listrik, akhir pekan
P8 = ((5000+(3000*4)+(2000*(durasi_parkir-6))))*1.2
#P9: 2-6 jam, bukan listrik, akhir pekan
P9 = (5000+(3000*(durasi_parkir-2)))*1.2

if (durasi_parkir<=2):
    if (akhir_pekan=="y"):
        print("Total tarif parkir adalah Rp",P1)
    else:
        print("Total tarif parkir adalah Rp5000")

elif durasi_parkir>2 and durasi_parkir<=6:
    if listrik=="y" and akhir_pekan=="y":
        print("Total tarif parkir adalah Rp",P2)
    if listrik=="y" and akhir_pekan=="n":
        print("Total tarif parkir adalah Rp",P3)
    if listrik=="n" and akhir_pekan=="y":
        print("Total tarif parkir adalah Rp",P9)
    else:
        print("Total tarif parkir adalah Rp", P4)

elif durasi_parkir>6: 
    if listrik=="y" and akhir_pekan=="y":
        print("Total tarif parkir adalah Rp",P5)
    if listrik=="y" and akhir_pekan=="n":
        print("Total tarif parkir adalah Rp",P6)
    if listrik=="n" and akhir_pekan=="y":
        print("Total tarof parkir adalah Rp",P8)

else:
    print("Total tarif parkir adalah Rp",P7)