# NIM/Nama : 15626004 / Nirmala Rahma Maulida
# Tanggal : Rabu, 11 November 2026
# Deskripsi : Program menyederhanakan aspect ratio foto Tuan Mik menggunakan subprogram untuk menghitung FPB
# KAMUS :
# lebar, tinggi : int

# subprogram perhitungan
def hitungFPB (a,b):
    # KAMUS LOKAL
    # int
    # Algoritma subprogram
    while b != 0:
        aspek_ratio = a % b
        a = b
        b = aspek_ratio
    return a

# Algoritma program utama 
lebar = int(input("masukkan lebar foto (piksel) = "))
tinggi = int(input("masukkan tinggi foto (piksel) = "))

fpb_val = hitungFPB(lebar, tinggi)

r_lebar = lebar // fpb_val
r_tinggi = tinggi // fpb_val

print("aspect ratio disederhanakan menjadi" + str(r_lebar) +  ":" + str(r_tinggi))