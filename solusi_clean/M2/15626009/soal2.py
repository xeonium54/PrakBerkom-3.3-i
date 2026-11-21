NAMA : ARDINA
TANGGAL : 14/10/2026
DESKRIPSI : MEMBUAT MODUL 2
print("masukkan durasi parkir N : ", end= "")  #1
print("tambahkan mobil listrik N : ", end= "") #2
print("apakah akhir pekan N :", end= "")       #3
print("total tarif parkir 500 :", end= "")     #4
N = int(input())

if (N > 0):
  print(str(N) + "parkir sebentar sudah murah , tidak perlu biaya tambahan ")
elif (N < 0):
  print(str(N) + "setelah potongsn mobil listrik , jika ada")

# str (N) berfungsi mengubah N menjadi string agar dapat dikontenasi saat print
