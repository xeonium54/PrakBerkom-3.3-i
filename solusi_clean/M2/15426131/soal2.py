# Nama: Reyza Aulia Rahman
# NIM: 15426131
# Deskripsi: Cek harga parkiran

# s :integer(tempat pemasukan durasi parkir)
# m :text(cek apakah listrik atau gak)
# n :text(cek apakah akhir pekan)
#
#



s = int(input("Masukkan durasi parkir: "))
m = input("Apakah mobil listrik? (y/n): ")
n = input("Apakah Akhir pekan? (y/n): ")

if s <= 2:
    ss = 5000
elif 2 < s < 6:
    ss = ((s-2)*3000) + 5000
else:
    ss = (s-6)*2000 + 17000

if m == ("y"):
    wow = ss-5000
else:
    wow = ss

if n == ("y"):
    wowie = (wow*12)/10
else:
    wowie = wow

print(f"Total tarif parkir adalah: Rp{wowie}")
  