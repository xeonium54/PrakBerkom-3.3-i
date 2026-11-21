# NIM / Nama : 15626049 Hisyam Fithroturrohim
# TANGGAL    : Rabu, 14 Oktober 2026
# DESKRIPSI  : Praktikum Berpikir Komputasional soal 2 (Tarif parkir)

durasi_parkir = int(input("Masukkan durasi parkir (jam) : "))
jenis_mobil = bool(input("Apakah mobil listrik? (y/n) : "))
kapan = bool(input("Apakah akhir pekan? (y/n) : "))


if durasi_parkir <= 2 :
  print("Total tarif parkir adalah Rp5000")
  if kapan == True and jenis_mobil == False:
    tarif = 5000 * 1.2
    print(f"Total tarif parkir adalah Rp{tarif}")
elif durasi_parkir > 2 and jenis_mobil == True:
  tarif = (durasi_parkir - 2) * 3000
  print(f"Total tarif parkir adalah Rp{tarif}")
  if durasi_parkir > 5:
    tarif_akhir = (6 * 3000) + (durasi_parkir - 6) * 2000
    print(f"Total tarif akhir adalah Rp{tarif_akhir}")
    if kapan == True:
      tarif_parkir = tarif_akhir * 1.2
      print(f"Total tarif parkir adalah Rp{tarif_akhir}")
else:
  tarif = 5000 + (durasi_parkir - 2) * 3000
  print(f"Total tarif parkir adalah Rp{tarif}")
  if kapan == True:
    tarif = tarif * 1.2
    print(f"Total tarif parkir adalah Rp{tarif}")