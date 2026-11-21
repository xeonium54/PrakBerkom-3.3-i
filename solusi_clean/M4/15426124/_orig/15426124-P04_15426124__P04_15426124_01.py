# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 11 November 2026
# Deskripsi : Menyederhanakan aspek rasio foto

def fpb(a, b):
    """Fungsi untuk menghitung FPB dari dua bilangan a dan b menggunakan algoritma Euclidean."""
    while b != 0:
        a, b = b, a % b 
    return a 
    
def main():
    #meminta masukkan lebar dan tinggi foto
    lebar = int(input("Masukkan lebar foto (piksel): "))
    tinggi = int(input("Masukkan tinggi foto (piksel): "))
    
    #menghitung FPB dari lebar dan tinggi foto
    faktor = fpb(lebar, tinggi)
    
    #menyederhanakan rasio
    lebar_sederhana = lebar // faktor
    tinggi_sederhana = tinggi // faktor
    
    #menampilkan hasil
    print(f"Aspek rasio disederhanakan menjadi {lebar_sederhana}:{tinggi_sederhana}.")
    
if __name__ == "__main__":
    main()