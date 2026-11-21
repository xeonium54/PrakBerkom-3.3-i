# NIM/Nama       : 15626017/Naura Vira Vania Ramadhani 
# Tanggal        : 11 November 2026
# Deskripsi      : Menyederhanakan aspect ratio foto menggunakan fungsi FPB (GCD)

def hitung_fpb(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def main():
    lebar = int(input("Masukkan lebar foto (piksel): "))
    tinggi = int(input("Masukkan tinggi foto (piksel): "))
    
    fpb = hitung_fpb(lebar, tinggi)
    
    sederhana_lebar = lebar // fpb
    sederhana_tinggi = tinggi // fpb
    
    print(f"Aspect ratio disederhanakan menjadi {sederhana_lebar}:{sederhana_tinggi}")

if __name__ == "__main__":
    main()