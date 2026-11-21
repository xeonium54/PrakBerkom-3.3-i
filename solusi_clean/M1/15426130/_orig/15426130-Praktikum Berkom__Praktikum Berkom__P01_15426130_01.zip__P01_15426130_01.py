#NIM/Nama  : 15426130/ Yudha Putra
#Tanggal   : 30 September 2027
#Deskripsi : Menghitung biaya listrik yang terbuang

daya = float(input("Masukkan daya lampu (watt): "))
jam = float(input("Masukkan lama lampu menyala (jam): "))
tarif = float(input("Masukkan tarif listrik (rupiaah per kwh): "))

biaya = daya*jam/1000*tarif

print(f"biaya listrik yang terbuang adalah Rp{biaya:.2f}")