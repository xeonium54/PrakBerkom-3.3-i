# NIM/Nama : 15626019/Naura Nur Aprilia
# Tanggal : 11-11-2026
# Deskripsi: Program untuk menyederhanakan aspect ratio foto

# KAMUS
a : int #Lebar_Foto (piksel)
b : int #Tinggi_Foto (piksel)
x : int
y : int

a = int(input("Masukkan lebar foto (piksel): "))
b = int(input("Masukkan tinggi foto (piksel): "))

x = a/300
y = b/300

print ("Aspect ratio disederhanakan menjadi: ", x , ":" , y)