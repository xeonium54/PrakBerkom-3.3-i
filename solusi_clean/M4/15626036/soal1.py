#NIM/Nama: Aghneo Amar Ahsan
#Tanggal: 11 November 2026
#Deskripsi: Program ini membantu menyederhanakan aspek rasio suatu foto

def fpb(a, b): 
    while b != 0: 
        a, b = b, a % b
    return a  

a = int(input("Masukkan lebar foto (piksel): "))
b = int(input("Masukkan tinggi foto (piksel): "))

faktor = fpb(a, b)
print(f"Aspect rasio disederhanakan menjadi {a//faktor} : {b//faktor}")