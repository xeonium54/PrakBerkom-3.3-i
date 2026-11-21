# Alfathir Sangkara Anindya 
# 15626031
# program penghitungan sisa energi yang terbuang

daya_lampu=100
lama_lampu=48
tarif_listrik=1450



daya_lampu=int(input("masukan daya lampu (watt):"))
lama_lampu=float(input("masukan lama lampu menyala (jam):"))
tarif_listrik=int(input("masukan harga tarif listrik (Rupiah per kwh) :"))

energi=(daya_lampu * lama_lampu)/1000


biaya=(energi * tarif_listrik)

print(f"biaya listrik yang terbuang adalah Rp{biaya:g}")

