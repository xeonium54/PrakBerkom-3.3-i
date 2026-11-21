# NIM/Nama  : 15426130 / Yudha Putra
# Tanggal   : 11 November 2026
# Deskripsi : Menyederhanakan aspect ratio foto menggunakan FPB (subprogram)


def fpb(a, b):
    """Menghitung FPB dua bilangan bulat positif dengan algoritma Euclid."""
    while b != 0:
        a, b = b, a % b
    return a


def main():
    lebar = int(input("Masukkan lebar foto (piksel): "))
    tinggi = int(input("Masukkan tinggi foto (piksel): "))

    pembagi = fpb(lebar, tinggi)  # faktor penyederhana rasio
    print("Aspect ratio disederhanakan menjadi "
          + str(lebar // pembagi) + ":" + str(tinggi // pembagi))


main()