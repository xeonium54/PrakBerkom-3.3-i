# NIM/Nama : 15626001 / Muhamad Naufal Al Fajri
# Tanggal : 14/ 10 / 2026
# Deskripsi :
durasi = float(input("Masukkan durasi parkir (jam):"))


if durasi <= 2:
    harga = durasi * 5000
    print ("Total tarif parkir adalah Rp", harga)
elif 2 > durasi > 6:
    n1 = durasi-2
    tambah1 = n1 * 3000
    hasil1 = 5000 + tambah1
    mlistrik = input("Apakah mobil listrik? (y/n):")
    if mlistrik == "y" :
        hasil2 = hasil1 - 5000
        akhirpekan = input("Apakah akhir pekan? (y/n):")
    else:
        print ("Total tarif parkir adalah Rp", hasil1)
        if akhirpekan == "y":
            hasil3 = hasil2 * 1,2
            print ("Total tarif parkir adalah Rp", hasil3)
        else:
            print ("Total tarif parkir adalah Rp", hasil2)
    
else:
     tambah2 = durasi-6 * 2000
     hasil1 = 22000 + tambah2
     mlistrik = input("Apakah mobil listrik? (y/n):")
     if mlistrik == "y" :
         hasil2 = hasil1 - 5000
         akhirpekan = input("Apakah akhir pekan? (y/n):")
         if akhirpekan == "y":
             hasil3 = hasil2 * 1,2
             print ("Total tarif parkir adalah Rp", hasil3)
         else:
             print ("Total tarif parkir adalah Rp", hasil2)
     else:
         print ("Total tarif parkir adalah Rp", hasil1)


