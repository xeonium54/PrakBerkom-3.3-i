"""Problem 2"""

# Subprogram 1 (Fungsi): Menghitung skor kekuatan suatu PIN
def hitung_skor_pin(pin):
    skor = 0
    digit_unik = ""
    ada_huruf_besar = False


    for karakter in pin:
        if '0' <= karakter <= '9':
            if karakter not in digit_unik:
                digit_unik += karakter
                skor += 4
        elif 'A' <= karakter <= 'Z':
            ada_huruf_besar = True


    if ada_huruf_besar:
        skor += 10


    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5


    for i in range(panjang - 1):
        karakter_sekarang = pin[i]
        karakter_berikut = pin[i + 1]

        if ('0' <= karakter_sekarang <= '9') and ('0' <= karakter_berikut <= '9'):
            selisih = abs(int(karakter_sekarang) - int(karakter_berikut))
            if selisih == 1:
                skor -= 5

    return skor

# Subprogram 2 (Fungsi): Menentukan kategori PIN berdasarkan skor
def tentukan_kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"

# Subprogram 3 (Prosedur): Mengatur input, proses perulangan N kandidat, dan output
def jalankan_program():
    n = int(input("Masukkan jumlah kandidat PIN (N): "))

    jumlah_kuat = 0
    jumlah_sedang = 0
    jumlah_lemah = 0

    for i in range(1, n + 1):
        pin = input(f"Kandidat PIN ke-{i}: ")

        skor = hitung_skor_pin(pin)
        kategori = tentukan_kategori(skor)

        print(f"PIN ke-{i} skornya {skor}, tergolong {kategori}.")

        if kategori == "Kuat":
            jumlah_kuat += 1
        elif kategori == "Sedang":
            jumlah_sedang += 1
        else:
            jumlah_lemah += 1

    print(f"Rekap: Kuat {jumlah_kuat}, Sedang {jumlah_sedang}, Lemah {jumlah_lemah}")

# Pemanggilan subprogram utama

