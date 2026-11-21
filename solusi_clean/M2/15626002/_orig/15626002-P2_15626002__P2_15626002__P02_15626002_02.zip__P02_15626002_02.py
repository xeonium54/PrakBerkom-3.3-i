# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM
# Mencari tarif parkir dengan mengalikan durasi parkir dengan harga parkir

# KAMUS
# Tarif_kurang_dari_2jam: integer
# Tarif_2jam_sampai_6jam: integer
# Tarif_lebih_dari_6jam: integer
# hari: string

# ALGORITMA
Durasi_parkir=int(input("Masukkan durasi parkir(jam):"))
Tarif_kurang_dari_2jam:5000
Tarif_2jam_sampai_6jam:3000
Tarif_lebih_dari_6jam=2000
if Durasi_parkir==2:
    print("Maka tarif flat Rp.5.000")
elif Durasi_parkir>2 and Durasi_parkir<=6:
    print(f"Maka tarif flat RP.3000/jam, 2 jam pertama tetap dihitung {Tarif_kurang_dari_2jam}")
else:
    print(f"Maka tarif flat {Tarif_lebih_dari_6jam}, 6 jam pertama tetap dihitung{Tarif_2jam_sampai_6jam}")
    Jenis_mobil=bool(input("Apakah mobil listrik(True/False):"))
    if Jenis_mobil==False:
        print(f"Maka tarif flat {Tarif_lebih_dari_6jam}")
    else:
        Tarif_lebih_dari_6jam-=5000
        hari=bool(input("Apakah akhir pekan(True/False):"))
        if hari==True:
         print(f"Maka tarif flat {Tarif_lebih_dari_6jam}")
        else:
         Tarif_lebih_dari_6jam*=1,2
         print(f"Maka tarif flat{Tarif_lebih_dari_6jam}")
