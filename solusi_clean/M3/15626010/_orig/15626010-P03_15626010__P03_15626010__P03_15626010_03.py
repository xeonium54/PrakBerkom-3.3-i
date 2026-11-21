# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 28/10/2026
# Deskripsi : Program ini disusun untuk menghitung total volume genangan air hujan yang tertampung di antara tanah berkontur tidak rata, dengan menerapkan konsep array dan pengulangan.

def main():
    n=int(input("masukkan panjang kebun:"))
    h=[int(x) for x in input("Masukkan array ketinggian tanah: ").split()]
    w=int(input("Masukkan batas toleransi air: "))

    max_kiri = [0]*n
    max_kanan = [0]*n

    # Loop untuk mencari nilai maksimum dari sisi kiri
    temp = 0
    for i in range(n):
        if h[i] > temp:
            temp = h[i]
        max_kiri[i]=temp

    # Loop untuk mencari nilai maksimum dari sisi kanan
    temp = 0
    for i in range (n - 1,-1,-1):
        if h[i] > temp:
            temp = h[i]
        max_kanan[i]=temp

    total_genangan = 0
    # Loop untuk menghitung volume genangan di setiap array
    for i in range(n):
        batas_air = max_kiri[i] if max_kiri[i] < max_kanan[i] else max_kanan[i]
        genangan = batas-air - h[i]
        if genangan > 0 :
            total_genangan += genangan

    print(f"Total Volume genangan air adalah {total_genangan}.")

    if total_genangan > w:
        print("Kaktus Ky mati membusuk")

    else:
        print("Kaktus Tuan Ky selamat!")

if __name__ == "__main__":
    main()