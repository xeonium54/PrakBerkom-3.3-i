#NIM/Nama   :15626043/Nevlin Fulvian Rohman
#Tanggal    :30 September 2026
#Deskripsi  :Problem 3

#Test Case 1

#j1 : Jam Masuk
#m1 : Menit Masuk
#j2 : Jam Keluar
#m2 : Menit Keluar
#N  : Batas Shift Normal
#U  : Upah per menit
#L  : Pengali Upah Lembur
#M  : Tunjangan Makan
#Tm : Batas Minimal Tunjangan
#W : Total Menit
#W1 : Waktu kerja normal
#W2: Waktu Lembur
#G  : Total Upah

j1 = int(input('Masukkan Jam Masuk='))
m1 = int(input('Masukkan Menit Masuk='))
j2 = int(input('Masukkan Jam Keluar'))
m2 = int(input('Masukkan Menit Keluar='))
N = int(input('Masukkan Batas Shift Normal (menit)='))
U = int(input('Masukkan Upah per menit='))
L = float(input('Masukkan Pengali Upah Lembur='))
M = int(input('Masukkan Tunjangan Makan'))
Tm = int(input('Masukkan Batas Minimal Tunjangan='))

W = (j2*60+m2)-(j1*60+m1)

print(W)
print('Apabila W > N maka W > Tm, sehingga perhitungannya sebagai berikut')

W2 = W-N
W1 = W-W2

G = (N*1000)+(W2*1000*L)+M

print('Total Durasi Kerja', W, 'menit')
print('Menit Kerja Normal', W1, 'menit')
print('Menit Kerja Lembur', W2, 'menit')
print('Tunjangan makan Rp', M)
print('Total Upah Diterima Rp',G)



