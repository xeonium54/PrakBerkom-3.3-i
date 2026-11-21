# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 11 November 2026
# Deskripsi : Program ini menghitung skor kekuatan dan menentukan kategori (kuat, sedang lemah) dari sejumlah kandidat PIN e-wallet berdasarkan keunikan digit, adanya huruf  besar, panjang pin, serta penalti dari digit angka yang berurutan.

def hitung_skor (pin: str) -> int:
    skor = 0

    # setiap digit berbeda (0-9) menyumbang 4 poin
    digit_unik = set (c for c in pin if c.isdigit())
    skor += len(digit_unik)*4

    # Jika pin mengandung minimal satu huruf besar, tambahkan 10 poin
    if any (c.isupper()for c in pin):
        skor += 10

    # panjang pin
    panjang=len(pin)
    if panjang >=  8:
        skor +=15
    elif 6 <= panjang <= 7:
        skor += 5

    # penalti digit berurutan langsung berselisih tepat 1 (naik maupun turun)
    penalti = 0
    for j in range (len(pin)-1):
        if pin [j].isdigit() and pin[j+1].isdigit():
            if abs(ord(pin[j])-ord(pin[j+1]))==1:
                penalti += 5
    skor -= penalti

    return skor

def tentukan_kategori (skor: int)->str:
    if skor >=40:
        return "Kuat"
    elif 20 <= skor <40:
        return "Sedang"
    else:
        return "Lemah"

def main ():
    n = int(input("Masukkan jumlah kandidat pin (N): "))

    count_kuat = 0
    count_sedang = 0
    count_lemah = 0

    for i in range (1, n+1):
        pin = input (f"Kandidat PIN ke-{i}: ")
        skor = hitung_skor(pin)
        kategori = tentukan_kategori(skor)

        print(f"PIN ke-{i} skornya {skor}, tergolong {kategori}. ")

        if kategori == "Kuat":
            count_kuat += 1
        elif kategori == "Sedang":
            count_sedang += 1
        else:
            count_lemah += 1

    print(f"Rekap: Kuat {count_kuat}, Sedang {count_sedang}, Lemah {count_lemah}")

    if __name__ == "__main__":
        main()