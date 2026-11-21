# NIM/Nama               : 15426128/Fathir Sulihansyah 
# Tanggal                : 11 November 2026
# Deskripsi              : Program untuk menyederhanakan aspect ratio foto menggunakan FPB.

# KAMUS KODING
# Spesifikasi Subprogram:
# fpb(a: int, b: int) -> int
#   {Menghitung dan mengembalikan Faktor Persekutuan Terbesar (FPB) dari bilangan a dan b 
#    menggunakan Algoritma Euclidean}
#
# Variabel Utama (main):
# lebar            : int   {Input lebar foto dalam piksel}
# tinggi           : int   {Input tinggi foto dalam piksel}
# faktor           : int   {Hasil perhitungan FPB dari lebar dan tinggi}
# lebar_sederhana  : int   {Hasil pembagian lebar dengan FPB}
# tinggi_sederhana : int   {Hasil pembagian tinggi dengan FPB}

def fpb(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def main():
    lebar = int(input("Masukkan lebar foto (piksel): "))
    tinggi = int(input("Masukkan tinggi foto (piksel): "))
    
    faktor = fpb(lebar, tinggi)
    
    lebar_sederhana = lebar // faktor
    tinggi_sederhana = tinggi // faktor
    
    print(f"Aspect ratio disederhanakan menjadi {lebar_sederhana}:{tinggi_sederhana}")

if __name__ == "__main__":
    main()
