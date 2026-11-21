# NIM/Nama : 15626045/Anindhita Ramya Rahmadani
# Tanggal  : 11/11/2026
# Deskripsi: Menentukan rasio yang paling sederhana dari sebuah ukuran foto dalam piksel dengan mendefinisikan fungsi ratio.

import math

def ratio(a, b):
    fpb = math.gcd(a, b)
    rasio_a = a // fpb
    rasio_b = b // fpb
    return rasio_a, rasio_b

# KAMUS
# l, t, hasil: int

# ALGORITMA
l = int(input("Masukkan lebah foto (piksel): "))
t = int(input("Masukkan tinggi foto (piksel): "))
hasil_a, hasil_b = ratio(l, t)

print("Aspect ratio disederhanakan menjadi", hasil_a, ":", hasil_b)