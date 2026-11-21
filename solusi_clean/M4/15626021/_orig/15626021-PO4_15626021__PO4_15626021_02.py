# Nama/NIM  : Aufaa Fakhri Ibrahim Irahadi / 15626021
# Tanggal   : 11 November 2026
# Deskripsi : Program menghitung skor kekuatan PIN dan merekap jumlah PIN berdasarkan kategori kuat, sedang, atau lemah

def hitung_skor_pin(pin):
    """Subprogram untuk menghitung skor suatu PIN termasuk penalti digit berurutan."""
    # 1 . Digit berbeda (0-9) yang muncul menyumbang 4 poin (dihitung sekali)
    digit_unik = set()
    for char in pin:
        if '0' <= char <= '9':
            digit_unik.add(char)
    skor = len(digit_unik) * 4

    # 2. Huruf besar minimal satu menambah 10 poin
    ada_huruf_besar = False
    for char in pin:
        if 'A' <= char <= 'Z':
            ada_huruf_besar = True
            break
    if ada_huruf_besar:
        skor += 10

    # 3. Panjang PIN
    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5

    # 4. Penalti digit berurutan (selisih 1 tempat)
    for i in range(panjang - 1):
        c1 = pin [i]
        c2 = pin [i+1]
        if '0' <= c1 <= '9' and '0' <= c2 <= '9':
            if abs(ord(c1) - ord(c2)) == 1:
                skor -= 5

    return skor

def tentukan_kategori(skor):
    """Subprogram untuk menentukan kategori PIN berdasarkan skor."""
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"

def main():
    n = int(input("Masukkan jumlah kandidat PIN (N): "))

    rekap_kuat = 0
    rekap_sedang = 0
    rekap_lemah = 0

    for i in range(1, n + 1):
        pin = input(f"Kandidat PIN ke-{i}: ")
        skor = hitung_skor_pin(pin)
        kategori = tentukan_kategori(skor)

        if kategori == "Kuat":
            rekap_kuat += 1
        elif kategori == "Sedang":
            rekap_sedang += 1
        else:
            rekap_lemah += 1

        print(f"PIN ke-{i} skornya {skor},  tergolong {kategori}")

    print(f"Rekap: Kuat {rekap_kuat}, Sedang {rekap_sedang}, Mudah {rekap_lemah}")

    main()
