# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 11 November 2026
# Deskripsi : Program ini bertujuan untuk menyederhanakan aspect ratio sebuah foto berdasarkan input lebar dan tinggi dengan subprogram hitung Faktor Persekutuan Terbesar (FPB)

def hitung_fpb(a, b):
    """Subprogram untuk menghitung Faktor Persekutuan Terbesar (FPB)"""
    while b != 0:
        a, b = b, a%b
    return a

# meminta input dari pengguna
lebar = int(input("Masukkan lebar foto (piksel): "))
tinggi = int(input("Masukkan tinggi foto (piksel): "))

# Mendapatkan nilai FPB menggunakan subprogram
nilai_fpb = hitung_fpb(lebar, tinggi)

# menyederhanakan nilai aspect ratio
lebar_sederhana = lebar // nilai_fpb
tinggi_sederhana = tinggi // nilai_fpb

# menapilkan output hasil penyederhanaan
print(f"Aspect ratio disederhanakan menjadi {lebar_sederhana}:{tinggi_sederhana}")