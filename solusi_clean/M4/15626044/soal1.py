# NIM/Nama : 15626044/Saliha Mahira Al-kwarismy
# Tanggal : 11 November
# Deskripsi : P04_15626044_Problem1

# Masukkan input berupa lebar dan tinggi
lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

# Fungsi pertama
def mencari_fpb(a,b):
    while a != b:
       if a > b:
            a = a - b
       else:
            b = b - a
    return a      

# Mencari fpb
fpb = mencari_fpb(lebar, tinggi)

# Mencari rasio dari lebar dan tinggi
rasio_lebar = lebar // fpb
rasio_tinggi = tinggi // fpb

# Hasil akhir berupa aspect ratio 
print(f"Aspect ratio disederhanakan menjadi {rasio_lebar}:{rasio_tinggi}")
