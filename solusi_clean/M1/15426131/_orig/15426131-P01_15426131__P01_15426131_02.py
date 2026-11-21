# Nama/Nim: Reyza Aulia Rahman/15426131
# Tanggal: 30/09/2026
# Deskripsi: Mencari konsentrasi akhir sebuah larutan

#kamus
#larper : integral {konsentrasi larutan pertama}
#volper : integral {volume larutan pertama}
#larke : integral {konsentrasi larutan kedua}
#volke : integral {volume larutan kedua}
#larti : integral {konsentrasi larutan ketiga}
#volti : integral {volume larutan ketiga}
#m : float {total hasil perkalian antar konsentrasi dan volume larutan}


larper = int(input("Masukkan konsentrasi larutan pertama (persen): "))
volper = int(input("Masukkan volume larutan pertama (ml): "))
larke = int(input("Masukkan konsentrasi larutan kedua(persen): "))
volke = int(input("Masukkan volume larutan kedua (ml): "))
larti = int(input("masukkan konsentrasi larutan (persen):  "))
volti = int(input("Masukkan volume larutan ketiga (ml): "))

m = ((larper*volper) + (larke*volke) + (larti*volti)) / (volper + volke + volti)

print(f"Konsentrasi akhir larutan campuran adalah {m} persen")









