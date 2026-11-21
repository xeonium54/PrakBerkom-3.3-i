# NIM/Nama : 15626035/Naila Rahmah Zhafirah
# Tanggal : 11 November 2026
# Deskripsi : Menghitung skor dan kategori dari N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori.

# KAMUS
data = {
    "kuat" : 0,
    "sedang" : 0,
    "lemah" : 0
}

# Menghitug skor pin
def hitung_skor(pin):
    skor = 0
    digit = ""

    # Menghitung digit berbeda
    for x in pin:
        if x.isdigit() and x not in digit:
            digit += x

    skor += len(digit) * 4

    # Huruf kapital
    for x in pin:
        if x.isupper():
            skor += 10
            break

    # Panjang pin
    if len(pin) >= 8:
        skor += 15
    elif len(pin) >= 6:
        skor += 5

    # Digit berurutan
    for i in range(len(pin)-1):
        if pin[i].isdigit() and pin[i+1].isdigit():
            if abs(int(pin[i])-int(pin[i+1])) == 1:
                skor -= 5

    return skor

# Menentukan kategori
def kategori(skor):
    if skor >= 40:
        return "kuat"
    elif skor >= 20:
        return "sedang"
    else:
        return "lemah"

# Input kandidat
n = int(input("Masukkan jumlah kandidat PIN (N): "))

for i in range(n):
    pin = input("Kandidat PIN ke-" + str(i+1) + ": ")

    skor = hitung_skor(pin)
    hasil = kategori(skor)

    print("PIN ke-" , i+1, "skornya", skor,
          ", tergolong", hasil.capitalize())

    data[hasil] += 1

# Output
print("Rekap: Kuat", data["kuat"],
      ", Sedang", data["sedang"],
      ", Lemah", data["lemah"])