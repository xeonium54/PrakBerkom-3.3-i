#15626039/Khalif Aufar A
#14 Oktober 2026
# No 2, Parkir mobil
#KAMUS
#d = float
#dp = float
#ml = string
#dl = float
#ap = string
#dk = float 

#input durasi awal
d = float(input("masukkan durasi parkir (jam):"))

if d<=2:
    dp = 5000
elif d>2 and d<=6:
    dp = 5000+(d-2)*3000 

else: 
    dp = 5000+(4*3000)+(d-6)*2000 
#cek mobil apakah listrik
ml = input("apakah mobil listrik (yes/no):")
if ml == "yes" and d > 2:
 dl = dp - 5000
else:
 dl = dp
#cek apakah parkir di akhir pekan
ap = input("apakah akhir pekan (yes/no):")
if ap == "yes" and d > 2:
  dk = dl * 1,2
else:
  dk = dp
 #Menghasilkan program
print("total tarif parkir adalah:Rp",int(dk))


