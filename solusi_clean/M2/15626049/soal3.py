# NIM / Nama : 15626049 Hisyam Fithroturrohim
# TANGGAL    : Rabu, 14 Oktober 2026
# DESKRIPSI  : Praktikum Berpikir Komputasional soal 3 (Waktu kereta)

kereta_A = str(input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo) : "))
jarak_A = int(input("Masukkan jarak kereta A (m) : "))
kecepatan_A = int(input("Masukkan kecepatan Kereta A (m/s) : "))
kereta_B = str(input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo) : "))
jarak_B = int(input("Masukkan jarak Kereta B (M) : "))
kecepatan_B = int(input("Masukkan kecepatan Kereta B (m/s) : "))

waktu_A = jarak_A // kecepatan_A
waktu_B = jarak_B // kecepatan_B
selisih = waktu_B - waktu_A

if selisih >= 30 or selisih <= -30 :
  print(f"Jalur aman. Kereta A melintas duluan tanpa henti.")
else:
  print(f"Konflik terdeteksi! Kereta A diprioritaskan melintas")


