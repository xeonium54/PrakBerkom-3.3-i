
# NIM/Nama :
# Tanggal : 11 November 2026
# Deskripsi : Menyederhanakan aspect ratio foto

# KAMUS
# lebar, tinggi, faktor : int

# DEFINISI FUNGSI
def FPB(A, B):
    # Menghitung FPB dari A dan B

    # KAMUS LOKAL
    # sisa : int

    # ALGORITMA
    while (B != 0):
        sisa = A % B
        A = B
        B = sisa

    return A


# ALGORITMA PROGRAM UTAMA
lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

faktor = FPB(lebar, tinggi)

lebar = lebar // faktor
tinggi = tinggi // faktor

print("Aspect ratio disederhanakan menjadi "
      + str(lebar) + ":" + str(tinggi))
