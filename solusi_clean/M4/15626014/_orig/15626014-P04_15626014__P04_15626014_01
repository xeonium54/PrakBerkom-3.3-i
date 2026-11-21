#Nama : Fadhil Zulhilmi
#NIM : 15626014
#Deskripsi : 

def hitung_fpb (a,b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

fpb = hitung_fpb(lebar, tinggi)

lebar_sederhana = lebar // fpb
tinggi_sederhana = tinggi // fpb

print (f"Aspect ratio disederhanakan menjadi {lebar_sederhana} : {tinggi_sederhana}" )
