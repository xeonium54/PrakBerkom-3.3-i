# P02_15626029_02
# HANIF MAHIB YASSAR NURADIYATMA/15626029
# DESC : penentuan harga tarif parkir

# KAMUS 
# PT, Price  = float
# Jenis mobil = string

PT= float(input("Durasi parkir: "))
Jenismobil = str(input("Apakah mobil listrik? "))
weknd=str(input("Apakah akhir pekan? "))
if weknd== "y" or weknd.lower=="Ya":
 weknd=True
else:
 weknd=False

if Jenismobil == "y" or Jenismobil.lower == "Ya":
 Jenismobil1=True
else:
 Jenismobil1=False

if PT>= 2:
 Price1=5000 
if PT>=2:
 Price=Price1
if 2<PT<=6:
 Price2 = 5000+(PT-2)*3000
 if Jenismobil1 == True:
  Price= Price2-5000
if PT>6:
 Price3= 5000+(PT-2)*2000
 if Jenismobil == True:
  Price=Price3-5000
if weknd==True:
 Price=Price*(1.2)

print("harga:",Price)
