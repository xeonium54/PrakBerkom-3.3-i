# Nama = Jihan Salsabila
# NIM = 15626002

# PROGRAM 

# KAMUS

# Definisi fungsi
def hitung_FPB (lebar, tinggi):
    while tinggi!=0:
     aspek_ratio = tinggi, lebar % tinggi
    return lebar

def sederhanakan (lebar, tinggi):
    a = hitung_FPB (lebar, tinggi)
    return lebar//a, tinggi//a

# Program utama
lebar = float(input("Masukkan lebar foto (piksel)): "))
tinggi = float(input("Masukkan tinggi foto (piksel): "))

aspek_ratio = sederhanakan(lebar, tinggi)

print(f"aspek ratio= {lebar}:{tinggi}")