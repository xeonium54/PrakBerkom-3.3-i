# Nama / NIM : Muthi'ah Azka Niamillah / 15626026
# Tangga; : Rabu, 11 November 2026
# Deskripsi : Soal 2

def hitung_skor(pin):
    skor = 0

    digit_unik = ""
    for karakter in pin:
        if '0' <= karakter <= '9':
            if karakter not in digit_unik:
                digit_unik += karakter
    skor += len(digit_unik)*4

    ada_huruf_besar = False
    for karakter in pin:
        if 'A' <= karakter <= 'Z':
            ada_huruf_besar = True
            break
        if ada_huruf_besar:
        skor += 10

    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5

    for i in range(panjang-1):
        c1 = pin[i]
        c2 = pin [i+1]
        if ('0'<= c1 <='9') and ('0'<= c2 <= '9'):
            if abs(int(c1) - int(c2)) == 1:
                skor -= 5

    return skor
def tentukan_kategori (skor):
    if skor >= 40:
        return "kuat"
    elif skor >= 20:
        return "sedang"
    else:
        return "lemah" 

n = int(input("masukkan jumlah kadidat PIN (N): "))

jendela_kuat = 0
jendela_sedang = 0
jendela_lemah = 0

for i in range(1, n+1):
    pin = input("Kandidat PIN ke {i}: ")
    hitung_skor = hitung_skor (pin)
    kategori = tentukan_kategori (skor)

    print("PIN ke", i, "skor nya", skor, "tergolong", kategori)

    if kategori == "kuat":
        jumlah_kuat += 1
    elif kategori == "sedang":
        jumlah_sedang += 1
    else:
        jumlah_lemah += 1
print("rekapL Kuat", jumlah_kuat, "sedang", jumlah_sedang, "lemah", jumlah_lemah)