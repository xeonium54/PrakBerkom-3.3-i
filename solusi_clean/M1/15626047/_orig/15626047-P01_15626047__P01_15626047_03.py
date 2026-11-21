# NIM/Nama  : 15626047 / Jeremia Arista Matthew Sugiarto
# Tanggal   : 30 September 2026
# Deskripsi : Menghitung

#KAMUS
#j= Jam
#m= Menit
#1= Masuk
#2= Keluar
#N= Durasi kerja normal 
#L= Durasi kerja lembur
#U= Upah kerja normal
#L= Pengali upah kerja lembur 
#Tmin= Batas minimum jam kerja untuk dapat tunjangan makan
#TM= Tunjangan makan (Kerja>Tmin)

#Input
j1=int(input("Masukkan jam masuk:"))
m1=int(input("Masukkan menit masuk:"))
j2=int(input("Masukkan jam keluar:"))
m2=int(input("Masukkan menit keluar:"))
N=int (input("Masukkan batas shift normal (menit):"))
U=int (input("Masukan upah per menit:"))
L=float (input ("Masukan pengali upah lembur:"))
TM=int (input("Masukan tunjangan makan:"))
Tmin=int (input("Masukan batas minimal tunjangan (menit):"))

#Algoritma 
durasi= (j2*60+m2)-(j1*60+m1)
jam_kerja= durasi//60
menit_kerja= durasi%60
durasi_lembur= durasi-N
tunjangan_makan=bool(durasi>=Tmin)+TM
upah_lembur= durasi_lembur*L*U

#OUTPUT
print(f"Total durasi kerja: {jam_kerja} jam {menit_kerja} menit")
print(f"Menit kerja normal: {N} menit")
print(f"Menit kerja lembur: {durasi_lembur}")
print(f"Tunjangan makan: {tunjangan_makan}")
print(f"Total upah diterima:Rp {U*N+tunjangan_makan+upah_lembur}")