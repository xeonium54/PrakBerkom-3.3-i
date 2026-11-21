# NIM/ Nama : Aghneo Amar Ahsan
# Tanggal : 30 September 2026
# Deskripsi : Program ini akan menghitung total biaya listrik yang terbuang 

# Kamus : 
# w, j, tarif, Energi, BiayaTotal : float 
w = float(input("Masukkan daya lampu (watt) : "))
j = float(input("Masukkan lama lampu menyala (jam) : "))
tarif = float(input("Masukkan tarif listrik (rupiah per kWh) : "))

Energi = float((w * j) / 1000)
BiayaTotal = (Energi * tarif)

print("Biaya listrik yang terbuang adalah Rp", BiayaTotal)