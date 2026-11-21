# NIM/Nama : Arya Satya Anggara
# Tanggal : 11 November 2026
# Deskripsi : Program ini menghitung skor dan kategori kekuatan pin berdasarkan karakter, panjang, serta urutan digit, lalu merekap hasilnya


def HitungSkor(pin):
    skor = 0
    digit = []

    for x in pin:
        if x.isdigit() and x not in digit:
            digit.append(x)

    skor = len(digit) * 4

    for x in pin:
        if x.isupper():
            skor += 10
            break

    if len(pin) >= 8:
        skor += 15
    elif len(pin) >= 6:
        skor += 5

    for i in range(len(pin)-1):
        if pin[i].isdigit() and pin[i+1].isdigit():
            if abs(int(pin[i])-int(pin[i+1])) == 1:
                skor -= 5

    return skor


def kategori(skor):
    if skor >= 40:
        return "kuat"
    elif skor >= 20:
        return "sedang"
    else:
        return "lemah"


N = int(input("masukan jumlah kandidat Pin (N): "))

kuat = 0
sedang = 0
lemah = 0

for i in range(1, N+1):
    pin = input("kandidat Pin ke-" + str(i) + ": ")
    skor = HitungSkor(pin)
    kategori = kategori(skor)

    print("Pin ke-", i, "skornya", skor, "tergolong", kategori)

    if kategori == "kuat":
        kuat += 1
    elif kategori == "sedang":
        sedang += 1

print("Rekap: kuat", kuat, "sedang", sedang, "lemah", lemah)