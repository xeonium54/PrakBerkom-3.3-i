
# Nama/Nim: Reyza Aulia Rahman/15426131
# Tanggal: 30/09/2026
# Deskripsi: Mencari total upah seseorang bekerja

#Kamus:
#j1   : integer {waktu masuk dalam jam}
#m1   : integer {waktu masuk dalam menit}
#j2   : integer {waktu keluar dalam jam}
#m2   : integer {waktu keluar dalam menit}
#bsn  : integer {waktu batas shift normal}
#upm  : integer {upah per menit untuk waktu normal}
#upl  : float {memasukkan pengalian untuk waktu lembur}
# tjm  : integer {tunjangan makanan}
#btm  : integer {minimal waktu kerja batas tunjangan makanan}


#totme  : integer {total menit}
#kelem  : integer {total waktu kerja lembur}
#kenor  : integer {total waktu kerja normal}
#upnor  : integer {upah total untuk waktu normal}
#uplem  : float {upah total lembur}
#low    : float/int {melakukan pengecekan jika waktu tunjangan lebih dari minimum}

#totmej : integer {mengkonversi jumlah kerja dalam satuan jam}
#totmen : integer  {mengkonversi jumlah sisa waktu kerja dalam satuan menit setelah mengknversi ke jam}
#totup  : float {total upah}


j1 = int(input("Masukkan jam masuk: "))
m1 = int(input("Masukkan menit masuk: "))
j2 = int(input("Masukkan jam keluar: "))
m2 = int(input("Masukkan menit keluar: "))
bsn = int(input("Masukkan batas shift normal (menit): "))
upm = int(input("masukkan upah per menit: Rp."))
upl = float(input("masukkan pengali upah lembur: "))
tjm = int(input("masukkan tunjangan makan: Rp:"))
btm = int(input("masukkan batas minimal tunjangan (menit): "))

totme = ((j2*60) + m2) - ((j1*60) + m1)

kelem = totme - bsn
kenor = totme - kelem
upnor = kenor*upm
uplem = kelem*upl


low = tjm * (totme >= btm)

totmej = totme//60
totmen = totme - (totmej*60)
print(f"Total durasi kerja : {totmej} jam {totmen} menit")
print(f"Menit kerja normal: {kenor}")
print(f"Menit Kerja lembur: {kelem}")
print(f"Rp.{low}.00")


totup = (upnor) + (uplem) + low
print(f"Total upah diterima Rp.{totup}.00")


