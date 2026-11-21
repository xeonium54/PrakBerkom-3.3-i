''''15626033_Farah Ghiza Humairoh'''
'''30 sepetember 2026'''
'''praktikum berkom'''



'''PROBLEM 1'''
daya = float(input("masukkan daya lampu (watt): "))
lama = float(input("masukkan lama lampu menyala (jam): "))
tarif = float(input("masukkan tarif listrik (rupiah per kWh: "))
energi = (daya * lama) / 1000
biaya = energi * tarif
biaya_bersih = [round(biaya, 2), int(biaya)][biaya % 1 ==0]
print(f"biaya listrik yang terbuang adalah Rp{biaya_bersih}")


