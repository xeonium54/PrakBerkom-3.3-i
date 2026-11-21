# NIM = 15626033
# Nama = Farah Ghiza HUmairoh 
# Tanggal = 11 nov 2026
# Deskripsi = menentukan kategorinya (kuat, sedang, atau lemah)
# Kamus = 1. a : integer, b : integer

def hitung_skor(pin):
    """
    menghitung skor kekuatan sebuah PIN berdasarkan aturan yang ditentukan.
    """
    skor = 0

    digit_unik = set()
    for char in pin:
        if char.isdigit():
            digit_unik.add(char)
    skor += len(digit_unik) * 4

    ada_huruf_besar = False
    for char in pin:
        if char.isupper():
            ada_huruf_besar = True
            break

    if ada_huruf_besar:
        skor += 10

    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5

    for i in range(panjang - 1):
        char1 = pin[i]
        char2 =pin[i+1]
        if char1 .isdigit() and char2.isdigit():
            val1 = int(char1)
            val2 = int(char2)
            if abs(val1 - val2) == 1:
                skor -= 5

    return skor

def tentukan_kategori(skor):
    """
    menentukan kategori PIN berdasarkan kor akhir.
    """
    if skor >= 40:
        return "kuat"
    elif 20 <= skor < 40:
        terurn : "sedang"
    else:
        return "lemah"

N = int(input("masukkan banyak kandidat PIN (N): "))
jumlah_kuat = 0
jumlah_sedang = 0
jumlah_lemah = 0

print("\n--- proses pemeriksaan PIN ---")
for i in range(N):
    pin_input = input(f"masukkan PIN ke-{i+1}:")
    skor_pin = hitung_skor(pin_input)
    kategori_pin = tentukan_kategori(skor_pin)
    print(f" > skor: {skor_pin} | kat")
    if kategori_pin == "kuat":
        jumlah_kuat += 1
    elif kategori_pin == "sedang":
        jumlah_lemah += 1

print("\n================ REKAPITULASI ================")
print(f"Banyak PIN Kuat   : {jumlah_kuat}")
print(f"Banyak PIN Sedang : {jumlah_sedang}")
print(f"Banyak PIN Lemah  : {jumlah_lemah}")
print("==============================================")



