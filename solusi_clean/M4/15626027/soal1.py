#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal  : 11 November 2026
#Deskripsi :  Menghitung FPB

def hitung_fpb(a, b):
  """
  Fungsi untuk menghitung faktor persekuatuan terbesar menggunakan algoritma euclidean.
  """
  while b != 0:
    a, b = b, a % b
  return a

#Input dari pengguna untk lebar dan tinggi foto
lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (Piksel): "))

fpb = hitung_fpb(lebar, tinggi)

lebar_sederhana = lebar // fpb
tinggi_sederhana = tinggi // fpb

print(f"Aspect ratio disederhanakan menjadi  {lebar_sederhana} : {tinggi_sederhana}")