#NIM/Nama : 15626019/Naura Nur Aprilia
#Tanggal : 14-10-2026
#Deskripsi : Membuat program untuk menghitung total tarif parkir yang harus Tuan Mik bayar

# KAMUS
# x : float # Durasi parkir (dalam jam)
# y : str # Pertanyaan jenis mobil
# z : str # Pertanyaan terkait hari
# total : int

# ALGORITMA
x = int(input("Masukkan durasi parkir (jam): "))
y = str(input("Apakah mobil listrik? (yes/no) "))
z = str(input("Apakah akhir pekan? (yes/no) "))
total a = int(input())
total b = int(input())
total c = int(input())
total d = int(input())
total e = int(input())
total f = int(input())
total g = int(input())
total h = int(input())
total i = int(input())
total j = int(input())

total a = 5000 * x
total b = 5000 * x * 1.2
total c = 3000 * x
total d = 3000 * x - 5000
total e = 3000 * x * 1.2
total f = 3000 * x * 1.2 - 5000
total g = 2000 * x
total h = 2000 * x - 5000
total i = 2000 * x * 1.2
total j = 2000 * x * 1.2 - 5000

if(x = 2 and y = no and z = no):
    print("Total tarif parkir adalah , total a")
elif(x = 2 and y = yes and z = no):
    print("Total tarif parkir adalah , total a")
elif(x = 2 and y = yes and z = yes):
    print("Total tarif parkir adalah , total b")
elif(x >= 2 or x = 6 and y = no and z = no):
    print("Total tarif parkir adalah , total c")
elif(x >= 2 or x = 6 and y = yes and z = no):
    print("Total tarif parkir adalah , total d")
elif(x >= 2 or x = 6 and y = no and z = yes):
    print("Total tarif parkir adalah , total e")
elif(x >= 2 or x = 6 and y = yes and z = yes):
    print("Total tarif parkir adalah , total f")
elif(x >= 6 and y = no and z = no):
    print("Total tarif parkir adalah , total g")
elif(x >= 6 and y = yes and z = no):
    print("Total tarif parkir adalah , total h")
elif(x >= 6 and y = no and z = yes):
    print("Total tarif parkir adalah , total i")
else:
    print("Total tarif parkir adalah , total j")