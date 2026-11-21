#NIM: 15626027
#Nama: Muhammad Faiz Dhiaul Haq
#30 September 2026
#Deskripsi: Mencari total biaya listrik Pak Mik yangg terbuang 

#Judul
print("="*50)
Judul = "Biaya listrik Pak Mik"
print(Judul.center(50))
print("="*50)

print(" ")

#variabel
Daya = int(input("Masukkan daya lampu (watt): "))                             #Daya Lampu
Lama_Lampu_Menyala = int(input("Masukkan lama lampu menyala (jam): "))        #Lama lampu menyala
Tarif_Listrik = int(input("Masukkan tarif listrik (rupiah per kwh): "))       #Energi dalam Kwh
Energi = Daya * Lama_Lampu_Menyala / 1000

Biaya_Terbuang = Energi * Tarif_Listrik                                       #Biaya listik Pak Mik yang terbuang

print(f"Biaya Listrik yang terbuang adalah {Biaya_Terbuang}")