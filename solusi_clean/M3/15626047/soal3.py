# NIM/Nama: 15626047
# Tanggal: 28 Oktober 2026
# Deskripsi: Total volume genangan air dan nasib kaktus Tuan Ky

#Kamus
n=int
H=int
w=int
total_air=int
i=int
j=int
kiri_max=int
kanan_max=int
batas_air=int

#ALGORITMA
n=int(input("Masukkan panjang kebun: "))
H=[int(x) for x in input ("Masukkan array ketinggian tanah: ").split()]
w=int(input("Masukkan batas toleransi air: "))

total_air=0

for i in range(1,n-1):
    kiri_max=0
    for j in range (0,i):
        if H[j]>kiri_max:
            kiri_max=H[j]
    kanan_max=0
    for j in range (0,i):
            if H[j]>kanan_max:
                kanan_max=H[j]

batas_air=kiri_max if kiri_max<kanan_max else kanan_max

if batas_air > H[i]:
     total_air += (batas_air-H[i])

print (f"Total volume genangan air adalah {total_air}")

if total_air > w:
     print ("Kaktus Tuan Ky mati membusuk!")
else:
     print ("Kaktus Tuan Ky selamat!")