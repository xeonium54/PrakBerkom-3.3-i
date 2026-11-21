# Nama: Siti Nawa Aulia
# NIM: 15626048
# Deskripsi: Mmebuat subprogram menghitung FPB dari dua bilangan

# Kamus 
# lebar: int
# tinggi: int
# pembagi: int
# rasio_lebar: int
# rasio_tinggi: int

# Algoritma

def fpb (a,b):
    
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    
    return a 

lebar = int(input("Masukan lebar foto:"))
tinggi = int(input("Masukan tinggi foto:"))

pembagi = fpb (lebar, tinggi)

rasio_lebar = lebar // pembagi
rasio_tinggi = tinggi // pembagi

print("Aspek ratio sederhana:",
    str(rasio_lebar) + ":" + str(rasio_tinggi))