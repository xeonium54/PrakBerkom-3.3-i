# NIM/Nama : 15626041/Dean Navarro Gratia Plena
# Tanggal : 30 September 2026
# Deskripsi : Menghitung biaya listrik yang terbuang

daya_lampu = float(input('Masukan daya lampu:')) / 1000
lama_lampu = float(input('Masukan lama lampu menyala: '))
tarif_listrik = float(input('Masukan tarif listrik:'))

biaya_listrik = daya_lampu*lama_lampu*tarif_listrik

print(f"Biaya listrik yang terbuang : Rp.{biaya_listrik}")