# NIM/Nama : 15626005/Addien Maulana Bima
# Tanggal : 30 September 2026
# Deskripsi : P01-Biaya Listrik

w = float(input("Masukkan daya lampu (watt) : "))
j = float(input("Masukkan lama lampu menyala (jam) : "))
k = float(input("Masukkan tarif listrik (rupiah per kWh): "))

e = (w*j)/1000
b = e*1500

print(f"Biaya listrik yang terbuang adalah : {b}")

#sudah ya kak