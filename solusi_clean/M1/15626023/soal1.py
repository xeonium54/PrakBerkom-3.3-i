a = float(input("Masukkan daya lampu (watt):"))
b = float(input("Masukkan lama lampu menyala (jam):"))
c = int(input("Masukkan tarif listrik (rupiah per kWh):"))

Energi = a * b / 1000
biaya  = Energi * c

print(f"Biaya listrik yang terbuang adalah: RP{biaya}")