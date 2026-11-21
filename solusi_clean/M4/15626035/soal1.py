# NIM/Nama : 15626035/Naila Rahmah Zhafirah
# Tanggal : 11 November 2026
# Deskripsi : Menghitung aspek rasio foto

# SUB PROGRAM
def fpb(a, b):
    while b !=0:
        a, b = b, a % b
    return a

# KAMUS
foto = {
    "lebar": 0,
    "tinggi": 0,
    "fpb": 0,
    "rasio_lebar": 0,
    "rasio_tinggi": 0
}

# Input
foto["lebar"] = int(input("Masukkan lebar foto (piksel): "))
foto["tinggi"] = int(input("Masukkan tinggi foto (piksel): "))

# Menghitung FPB
foto["fpb"] = fpb(foto["lebar"], foto["tinggi"])

# Aspek rasio
foto["rasio_lebar"] = foto["lebar"] // foto["fpb"]
foto["rasio_tinggi"] = foto["tinggi"] // foto["fpb"]

# Output
print("Aspect ratio disederhanakan menjadi",
      str(foto["rasio_lebar"]) + ":" + str(foto["rasio_tinggi"]))
