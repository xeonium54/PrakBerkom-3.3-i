# Rabu, 11 November 2026
# Nama  : Vidia Nurafifa
# NIM   : 15626011
# Desc  : Soal 1 - Menyederhanakan Aspect Ratio

# Mencari dengan FPB dan modulo
# Lebar Foto (L)
# Tinggi Foto (T)
# Sisa Pembagian/Modulo (SM)
# Nilai FPB (NF)
# Rasio tinggi setelah disederhanakan (RT)
# Rasio lebar setelah disederhanakan (RL)
# A dan B disini hanya permisalan untuk fungsi FPB

def FPB(A,B):
    while (B!=0):
        SM = A % B
        A = B 
        B = SM 
    return A

L = int(input("Masukkan lebar foto (piksel):"))
T = int(input("Masukkan tinggi foto (piksel):"))

NF = FPB (L, T)

RL = L // NF
RT = T // NF

print("Aspect ratio disederhanakan menjadi",RL, ":",RT)