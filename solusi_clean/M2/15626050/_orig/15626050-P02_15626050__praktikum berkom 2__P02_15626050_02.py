# NIM/Nama : 15626050/Yohanes Yoel Christopher Naibaho
# Tanggal : 14-10-2026
# Deskripsi :Menghitung total tarif parkir

# KAMUS
# durasi, tarif : int
# jenis mobil, akhir pekan : str

# ALGORITMA
durasi=int(input("Masukan dursi parkir(jam): "))
jenis_mobil=input("apakah mobil listrik(y/n): ")
akhir_pekan =input("Apakah akhir pekan(y/n): ")

if durasi <=2:
    tarif = 5000
elif durasi <=6 :
    tarif = 5000 + (durasi -2)* 3000
else:
    tarif =5000 + (durasi -2)*3000 + (durasi - 6)*2000
    
if jenis_mobil == "y" and  durasi > 2:
    tarif = tarif - 5000
if akhir_pekan == "y":
    tarif = tarif * 1.2
    
tarif = str(tarif)
print("Total tarif parkir adalah Rp",tarif)