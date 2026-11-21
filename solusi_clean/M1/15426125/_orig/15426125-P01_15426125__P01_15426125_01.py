# input dari pengguna
daya_lampu = int(input("Masukkan daya lampu (watt): "))
lama_menyala = int(input("Masukkan lama lampu menyala (jam): "))
tarif_listrik = int(input("Masukkan tarif listrik (rupiah per kWh: )"))
#energi yg terbuang
energi_kWh = (daya_lampu * lama_menyala / 1000)
#total biaya
total_biaya = energi_kWh * tarif_listrik
#hasil akhir
biaya_akhir = int(total_biaya)
#tampilan hasil akhir
print("Biaya listrik yang terbuang adalah Rp{biaya_akhir}")