# 15626039/Khalif Aufar Aufar Aridkhi
# 30 September 2026
# Praktikum Modul 1

# Memasukkan daya lampu (watt)
daya = int(input("masukkan daya lampu (watt): "))

# Memasukkan lama lampu nya menyala (jam)
lama_lampu = int(input("masukkan lama waktu lampu menyala (jam): "))

# Memasukkan tarif listrik (rupiah per kwh)
tarif = int(input("masukkan tarif listrik (rupiah per kwh) : "))
# 1 kwh = 1000 watt-jam

energi = daya * lama_lampu / 1000

biaya = energi * tarif

print(f"biaya listrik yang terbuang adalah : Rp.{biaya}")
