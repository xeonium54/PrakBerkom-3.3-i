# Nama / NIM : Luna Febryvazrya / 15426127
# Tanggal : 11 November 2026
# Deskripsi : Mengubah aspek ratio foto tuan mik

def fpb(a, b):
    """Mencari FPB dari dua bilangan dengan algoritma Euclid"""
    while b != 0:
        a, b = b, a % b
        return a
    
L = int(input("Masukkan lebar foto (piksel): 600 ")) 
T = int(input("Masukkan tinggi foto (piksel): 900 "))

faktor = fpb(L, T)
rasio_lebar = L // faktor
rasio_tinggi = T // faktor

print(f"Aspect ratio disederhanakan menjadi {rasio_lebar}:{rasio_tinggi}")