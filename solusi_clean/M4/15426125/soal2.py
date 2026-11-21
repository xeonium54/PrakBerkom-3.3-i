def hitung_skor(pin):
    skor = 0
    digit_unik = ""
    ada_huruf_besar = False

    for karakter in pin:
        if "0" <= karakter <= "9":
            if karakter not in digit_unik:
                digit_unik += karakter
        elif "A" <= karakter <= "Z":
            ada_huruf_besar = True

     skor += len(digit_unit) * 4
     if ada_huruf_besar:
    skor += 10
    panjang = len(pin)
    if panjang >= 8:
         skor += 15
    elif 6 <= panjang <= 7:
        skor += 5
    for i in rang (panjang - 1):
        karakter_sekarang = pin[i]
        karakter_berikutnya = pin[i + 1]

        if ("0" <= karakter_sekarang <= "9") and ("0" <= karakter_berikutnya <= "9"):
            selisih = abs(int(karakter_sekarang - karakter_berikutnya))
            if selisih == 1:
                skor -= 5
    return skor
def tentukan_kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
else:
    return "Lemah"

n = int(input("Masukkan jumblah kandidat PIN (N): "))
jumlah_kuat = 0
jumlah_sedang = 0
jumlah_lemah = 0

for i in range(1, n +1):
    kandidat_pin = input(f"Kandidat PIN ke-{i}: ")
    skor_pin = hitung_skor(kandidat_pin)
    kategori_pin = tentukan_kategori(skor_pin)

    print(f"PIN ke {i} skornya{skor_pin}, tergolong {kategori_pin}.")
    if kategori_pin == "Kuat":
        jumlah_kuat += 1
    elif kategori_pin == "Sedang":
        jumlah_sedang += 1
    else:
        jumlah_lemah += 1

print(f"Rekap: Kuat {jumlah_kuat}, Sedang {jumlah_sedang}, Lemah {jumlah_lemah}")
     