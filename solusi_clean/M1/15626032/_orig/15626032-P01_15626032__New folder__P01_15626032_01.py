# NIM/Nama : 15626032/Muhamad Faiz Abdul Aziz
# Tanggal : 30 September 2026
# Deskripsi : Membantu Tuan Mik menentukan total biaya listrik yang terbuang

# Kamus 
daya_lampu = int(input("Masukan daya lampu (watt): "))
lama_lampu = int(input("Masukan lama lampu menyala (jam): "))
tarif_listrik = int(input("Masukan tarif listrik (rupiah per kwh): "))

# Logaritma
Energi = (daya_lampu * lama_lampu) / 1000
Biaya = Energi * tarif_listrik

# Hasil 
print(f"Biaya listrik yang terbuang adalah RP {Biaya}")