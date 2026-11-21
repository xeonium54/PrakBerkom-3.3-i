# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 30 September 2026
# Deskripsi : Permasalahan 01, Menghitung biaya dari daya listrik yang terbuang

# kamus
# w = float = daya dalam watt
# j = float = waktu dalam jam
# r = float = tarif dalam rupiah/jam

w = float(input("masukkan daya yang digunakan (watt)"))
j = float(input("masukkan waktu (jam)"))
r = float(input("masukkan tarif yang diberikan (rupiah/kWh)"))

e = (w * j) / 1000
b = e * r

print("Biaya yang terbuang :", b)