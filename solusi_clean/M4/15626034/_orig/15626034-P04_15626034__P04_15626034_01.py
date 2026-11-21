#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 11 November 2026
#Deskripsi : Menghitung FPB

#kamus a,b : int
def hitung_fpb (a :int, b : int) -> int:
    while b :
        a, b = b, a % b
    return a

def hitung_rasio(lebar: int, tinggi: int) -> tuple[int, int]:
    fpb = hitung_fpb(lebar, tinggi)
    rasio_lebar = lebar // fpb
    rasio_tinggi = tinggi // fpb
    return rasio_lebar, rasio_tinggi

if __name__ == "__main__":
    lebar = int(input("Masukkan lebar: "))
    tinggi = int(input("Masukkan tinggi: "))
    rasio_lebar, rasio_tinggi = hitung_rasio(lebar, tinggi)
    print(f"Rasio lebar : tinggi adalah {rasio_lebar}:{rasio_tinggi}")