#Nama/NIM: Aghneo Amar Ahsan
#Tanggal: 28 Oktober 2026
#Deskripsi: 

n = int(input("Masukkan Panjang Kebun: "))
arr_ketinggian = input("Masukkan array ketinggian tanah: ").split()
arr = []

for x in arr_ketinggian: 
    arr.append(int(x))

w = int(input("Masukkan batas toleransi air: "))
totalVolume = 0

for i in range(1, n-1): 
    maxkiri = arr[0]
    for j in range (1, i):
        if arr[j] > maxkiri: 
            maxkiri = arr[j]

    maxkanan = arr[i+1]
    for j in range(i+2, n):
        if arr[j] > maxkanan:
            maxkanan = arr[j]

    if maxkiri < maxkanan:
        batas = maxkiri
    else : 
        batas = maxkanan

    volumetitik = batas - arr[i]
    if volumetitik > 0 : 
       totalVolume = totalVolume + volumetitik

print(f"Total volume genangan air adalah {totalVolume}")  
if totalVolume > w :
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")
