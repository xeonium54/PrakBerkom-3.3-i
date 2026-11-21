# NIM/Nama : 15626044/Saliha Mahira Al-kwarismy
# Tanggal : 2023-03-30
# Deskripsi : Problem 1

daya = int(input("Masukkan daya lampu (watt): "))
jam = int(input("Masukkan lama lampu menyala (jam): "))
kwH = int(input("Masukkan tarif listrik (rupiah per kWh): "))
# Catatan: 1 kWh = 1000 watt * 1 jam

# Menghitung biaya listrik 
biaya = (daya * jam * kwH) / 1000

# Menghitung total biaya listrik yang terbuang
print(f"Total biaya listrik yang terbuang adalah Rp {biaya}")