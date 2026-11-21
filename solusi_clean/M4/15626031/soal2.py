
# Nama : Alfathir Sangkara Anindya
# NIM : 15626031
# Tanggal :11/11/2026
# Deskripsi : program Menghitung skor kekuatan PIN

def hitung_skor(pin):
    skor = 0

    angka = []
    for x in pin:
        if x.isdigit() and x not in angka:
            angka.append(x)

    skor = skor + len(angka) * 4

    for x in pin:
        if x.isupper():
            skor = skor + 10
            break

    if len(pin) >= 8:
        skor = skor + 15
    elif len(pin) >= 6:
        skor = skor + 5

    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i+1].isdigit():
            if abs(int(pin[i]) - int(pin[i+1])) == 1:
                skor = skor - 5

    return skor


def kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"


N = int(input("Masukkan jumlah kandidat PIN (N): "))

kuat = 0
sedang = 0
lemah = 0

for i in range(N):
    pin = input("Kandidat PIN ke-" + str(i+1) + ": ")

    skor = hitung_skor(pin)
    hasil = kategori(skor)

    print("PIN ke-" + str(i+1) + " skornya", skor,
          ", tergolong", hasil + ".")

    if hasil == "Kuat":
        kuat = kuat + 1
    elif hasil == "Sedang":
        sedang = sedang + 1
    else:
        lemah = lemah + 1

print("Rekap: Kuat", kuat, ", Sedang", sedang, ", Lemah", lemah)
