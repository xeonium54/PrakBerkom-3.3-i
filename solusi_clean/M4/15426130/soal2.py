# NIM/Nama  : 15426130 / Yudha Putra
# Tanggal   : 11 November 2026
# Deskripsi : Menghitung skor kekuatan PIN, kategori, dan rekap kategori


def hitung_skor(pin):
    """Mengembalikan skor kekuatan sebuah PIN sesuai aturan soal."""
    skor = 0

    # 1) Setiap digit berbeda menyumbang 4 poin (dihitung sekali)
    digit_terlihat = ""
    for c in pin:
        if c.isdigit() and c not in digit_terlihat:
            digit_terlihat += c
            skor += 4

    # 2) Minimal satu huruf besar -> +10
    ada_besar = False
    for c in pin:
        if c.isupper():
            ada_besar = True
    if ada_besar:
        skor += 10

    # 3) Poin dari panjang PIN
    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif panjang >= 6:
        skor += 5

    # 4) Penalti digit bersebelahan yang selisihnya tepat 1 -> -5 per pasangan
    for i in range(panjang - 1):
        a = pin[i]
        b = pin[i + 1]
        if a.isdigit() and b.isdigit():
            selisih = int(a) - int(b)
            if selisih == 1 or selisih == -1:
                skor -= 5

    return skor


def tentukan_kategori(skor):
    """Mengembalikan kategori PIN berdasarkan skor."""
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"


def main():
    n = int(input("Masukkan jumlah kandidat PIN (N): "))

    kuat = 0
    sedang = 0
    lemah = 0

    for i in range(1, n + 1):
        pin = input("Kandidat PIN ke -" + str(i) + ": ")
        skor = hitung_skor(pin)
        kategori = tentukan_kategori(skor)
        print("PIN ke -" + str(i) + " skornya " + str(skor)
              + ", tergolong " + kategori + ".")

        if kategori == "Kuat":
            kuat += 1
        elif kategori == "Sedang":
            sedang += 1
        else:
            lemah += 1

    print("Rekap: Kuat " + str(kuat) + ", Sedang " + str(sedang)
          + ", Lemah " + str(lemah))


main()