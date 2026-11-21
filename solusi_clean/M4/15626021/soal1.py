# Nama/NIM  : Aufaa Fakhri Ibrahim Irahadi / 15626021
# Tanggal   : 11 November 2026
# Deskripsi : Program menyederhanakan aspect rasio foto menggunakan FPB

def fpb(a, b):
    """Fungsi untuk menghitung FPB dari dua bilangan secara iteratif."""
    while b != 0:
        a, b = b, a % b
    return a 

def main ():
    lebar = int(input("Masukkan lebar foto (piksel): "))
    tinggi = int(input("Masukkan tinggi foto (piksel): "))

    faktor = fpb(lebar, tinggi)
    sederhana_lebar = lebar // faktor
    sederhana_tinggi = tinggi // faktor

    print(f"Aspect rasio disederhanakan menajadi {sederhana_lebar}:{sederhana_tinggi}")

    main ()

