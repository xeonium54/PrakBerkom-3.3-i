# NIM/Nama: 15626040/Frizka Yunisaf
# Tanggal: 30 September 2026
# Deskripsi: Menghitung biaya listrik yang terbuang selama Tuan Mik berada di luar kota

w = float(input("Input daya lampu (watt): "))
j = float(input("Input durasi lampu menyala (jam): "))
r = int(input("Input tarif listrik (rupiah per kWh): "))
listrik_terbuang = ((w*j)/1000)*r
print("Biaya listrik yang terbuang adalah Rp", listrik_terbuang)
