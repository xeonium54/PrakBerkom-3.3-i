#NIM/Nama : Aghneo Amar Ahsan
#Tanggal : 14 Oktober 2026
#Deskripsi : Program ini dibuat untuk menghitung biaya parkir berdasarkan durasi, jenis mobil ,dan akhirpekan 

#Kamus 
#durasi : integer
#biaya : float
#jenisMobil, akhirPekan : string


durasi = int(input("Masukkan durasi parkir (jam): "))
jenisMobil = str(input("Apakah mobil listrik? (y/n): "))
akhirPekan = str(input("Apakah akhirpekan? (y/n): "))

if durasi <= 2:
    if akhirPekan == "Y" or jenisMobil == "y":
        biaya = 5000 * 1.2
    elif akhirPekan == "N" or jenisMobil == "n":
        biaya = 5000

elif 2 < durasi <= 6:
    if jenisMobil == "Y" or jenisMobil == "y":
        if akhirPekan == "Y" or akhirPekan == "y":
             biaya = (3000 * (durasi - 2)) * 1.2
        elif akhirPekan == "N" or akhirPekan == "n":
             biaya = (3000 * (durasi - 2))
    elif jenisMobil == "N" or jenisMobil == "n":
        if akhirPekan == "Y" or akhirPekan == "y":
             biaya = (5000 + (3000 * (durasi - 2))) * 1.2
        elif akhirPekan == "N" or akhirPekan == "n":
             biaya = 5000 + (3000 * (durasi - 2))
    
elif durasi > 6:
    if jenisMobil == "Y" or jenisMobil == "y":
        if akhirPekan == "Y" or akhirPekan == "y":
             biaya = (3000 * (durasi - 2)) * 1.2
        elif akhirPekan == "N" or akhirPekan == "n":
             biaya = (3000 * (durasi - 2))
    elif jenisMobil == "N" or jenisMobil == "n":
        if akhirPekan == "Y" or akhirPekan == "y":
             biaya = (((5000) + (3000 * 4)) + (2000 * (durasi - 6))) * 1.2
        elif akhirPekan == "N" or akhirPekan == "n":
             biaya = (((5000) + (3000 * 4)) + (2000 * (durasi - 6)))

print(f"Total tarif parkir adalah Rp.{biaya}")