# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 30/09/2026
# Deskripsi : program bertujuan menghitung total biaya listrik yang terbuang akibat lampu yang tidak dimatikan.

#memasukan input daya, lama menyala, dan tarif dari pengguna
daya =  int(input("Masukkan Daya Lampu (watt): "))
lama_nyala = int(input("Masukkan lama lampu menyala (jam): "))
tarif = int(input("Masukkan tarif listrik (rupiah per kWh): "))

#menghitung energi listrik dalam setahun
biaya_kebuang = int((daya*lama_nyala*tarif)/1000)

#menampilkan hasil biaya listrik yang terbuang
print (f"Biaya listrik yang terbuang adalah Rp{biaya_kebuang}")