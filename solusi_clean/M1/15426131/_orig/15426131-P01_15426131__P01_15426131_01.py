# Nim/Nama : Reyza Aulia Rahman/15426131
# Tanggal: 30/9/2026
# Deskripsi: Mencari tagihan listrik dalam rupiah untuk satu benda listrik

#kamus
#lampuwatt : integral {daya lampu setiap jam}
#waktu : integral {lama lampu menyala}
#tarif : integral {tarif listrik}
#x : integer {mencari total konsumsi}
#y : float {mengkonversi total konsumsi menjadi kilowatt}
#m : float {mencari harga akhir}

lampuwatt = int(input("masukkan daya lamput (watt): "))
waktu = int(input("masukkan lama lampu menyala (jam): "))
tarif = int(input("Masukkan tarif listrik (rupiah per kWh): "))



x = lampuwatt*waktu
y = x/1000

m = y*tarif

print(f"Biaya listrik yang terbuang adalah: Rp {m}")