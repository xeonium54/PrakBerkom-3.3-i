#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 11 November 2026
#Deskripsi : Menghitung skor dan kategori PIN


def hitung_skor_pin (pin:str) -> int:
    skor = 0
    digit_unik = set(char for char in pin if char.isdigit())
    skor += len(digit_unik) * 4
    if any(char.isupper() for char in pin):
        skor += 10
    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5
    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            d1 = int(pin[i])
            d2 = int(pin[i + 1])
            if abs(d1 - d2) == 1:
                skor -= 5
    return skor

def tentukan_kategori(skor: int) -> str:
    if skor < 20:
        return "Lemah"
    elif 20 <= skor <= 40:
        return "Sedang"
    else:
        return "Kuat"

def main():
    try:
        n = int(input("Masukkan jumlah kandidat PIN (N): "))
    except ValueError:
        print("jumlah PIN harus berupa bilangan bulat")
    return

    daftar_pin = []
    for i in range(n):
        pin = input(f"Masukkan PIN kandidat ke-{i + 1}: ")
        daftar_pin.append(pin)
    rekap = {"Lemah": 0, "Sedang": 0, "Kuat": 0}

    print("\nHasil Evaluasi:")
    for i, pin in enumerate(daftar_pin, start=1):
        skor = hitung_skor_pin(pin)
        kategori = tentukan_kategori(skor)
        rekap[kategori] += 1
        print(f"PIN {i} ({pin}): Skor = {skor}, Kategori = {kategori}")

    print("\nRekap Kategori:")
    for kategori, jumlah in rekap.items():
        print(f"jumlah PIN {kategori}: {jumlah}")

if __name__ == "__main__":
    main()

    

        

       