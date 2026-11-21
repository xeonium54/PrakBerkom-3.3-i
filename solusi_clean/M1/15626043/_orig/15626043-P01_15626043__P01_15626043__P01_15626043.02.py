#NIM/Nama   :15626043/Nevlin Fulvian Rohman
#Tanggal    :30 September 2026
#Deskripsi  :Problem 2

#Kamus
#c1 : Konsentrasi Larutan 1
#c2 : Konsentrasi Larutan 2
#c3 : Konsentrasi Larutan 3
#c4 : Konsentrasi Akhir
#v1 : Volume Larutan 1
#v2 : Volume Larutan 2
#v3 : Volume Larutan 3

#Test Case 1
c1 = int(input('Masukkan Konsentrasi Larutan Pertama (persen)='))
v1 = int(input('Masukkan volume larutan pertama (ml)='))
c2 = int(input('Masukkan Konsentrasi Larutan Kedua (persen)='))
v2 = int(input('Masukkan volume larutan kedua (ml)='))
c3 = int(input('Masukkan Konsentrasi Larutan Ketiga (persen)='))
v3 = int(input('Masukkan volume larutan Ketiga (ml)='))

c4 = ((c1*v1)+(c2*v2)+(c3*v3))/(v1+v2+v3)

print('Konsentrasi akhir larutan campuran adalah', c4, 'persen')