"""**Problem 2**

Case 1
"""

# NIM / Nama: 15626007 / Ryssad Sabralnair
# Tanggal : 14 Oktober 2026
# Deskripsi : Program Menghitung Tarif Kendaraan

#Problem 2

#Case 1
Durasi_Parkir = int(input("Masukkan Durasi Parkir:"))
Jenis_Mobil = input("Apakah Mobil listrik (y/n): ").strip().lower()
Mobil_listrik = (Jenis_Mobil == "y")

Input_Weekend = input("Apakah akhir pekan? (y/n): ").strip().lower()
Tarif_Akhir_pekan = (Input_Weekend == "y")

#Hitungan Tarif Dasar
if Durasi_Parkir <= 2:
  tarif_dasar = 5000
elif Durasi_Parkir <= 6:
  tarif_dasar = 5000 + (Durasi_Parkir - 2) * 3000
else:
  tarif_dasar = 5000 + (4*3000) + (Durasi_Parkir - 6) * 2000

#Khusus Mobil Listrik
if Mobil_listrik and Durasi_Parkir > 2:
  tarif_dasar = max(0, tarif_dasar - 5000)
#Tarif Weekend
total_tarif = tarif_dasar
if Tarif_Akhir_pekan:
  total_tarif = total_tarif * 1.2

#Menampilkan Tarif yang harus dibayar
print("Total tarif parkir yang harus dibayar:", total_tarif)

"""Case 2"""

# NIM / Nama: 15626007 / Ryssad Sabralnair
# Tanggal : 14 Oktober 2026
# Deskripsi : Program Menghitung Tarif Kendaraan

#Problem 2

#Case 2
Durasi_Parkir = int(input("Masukkan Durasi Parkir:"))
Jenis_Mobil = input("Apakah Mobil listrik (y/n): ").strip().lower()
Mobil_listrik = (Jenis_Mobil == "y")

Input_Weekend = input("Apakah akhir pekan? (y/n): ").strip().lower()
Tarif_Akhir_pekan = (Input_Weekend == "y")

#Hitungan Tarif Dasar
if Durasi_Parkir <= 2:
  tarif_dasar = 5000
elif Durasi_Parkir <= 6:
  tarif_dasar = 5000 + (Durasi_Parkir - 2) * 3000
else:
  tarif_dasar = 5000 + (4*3000) + (Durasi_Parkir - 6) * 2000

#Khusus Mobil Listrik
if Mobil_listrik and Durasi_Parkir > 2:
  tarif_dasar = max(0, tarif_dasar - 5000)
#Tarif Weekend
total_tarif = tarif_dasar
if Tarif_Akhir_pekan:
  total_tarif = total_tarif * 1.2

#Menampilkan Tarif yang harus dibayar
print("Total tarif parkir yang harus dibayar:", total_tarif)

"""Case 3"""

# NIM / Nama: 15626007 / Ryssad Sabralnair
# Tanggal : 14 Oktober 2026
# Deskripsi : Program Menghitung Tarif Kendaraan

#Problem 2
Durasi_Parkir = int(input("Masukkan Durasi Parkir:"))
Jenis_Mobil = input("Apakah Mobil listrik (y/n): ").strip().lower()
Mobil_listrik = (Jenis_Mobil == "y")

Input_Weekend = input("Apakah akhir pekan? (y/n): ").strip().lower()
Tarif_Akhir_pekan = (Input_Weekend == "y")

#Hitungan Tarif Dasar
if Durasi_Parkir <= 2:
  tarif_dasar = 5000
elif Durasi_Parkir <= 6:
  tarif_dasar = 5000 + (Durasi_Parkir - 2) * 3000
else:
  tarif_dasar = 5000 + (4*3000) + (Durasi_Parkir - 6) * 2000

#Khusus Mobil Listrik
if Mobil_listrik and Durasi_Parkir > 2:
  tarif_dasar = max(0, tarif_dasar - 5000)
#Tarif Weekend
total_tarif = tarif_dasar
if Tarif_Akhir_pekan:
  total_tarif = total_tarif * 1.2

#Menampilkan Tarif yang harus dibayar
print("Total tarif parkir yang harus dibayar:", total_tarif)

