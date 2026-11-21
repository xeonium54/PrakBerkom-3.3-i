# NIM/Nama: 15626025/Maria Amatussyafee Nurjaman
# Tanggal: 11/11/2026
# Deskripsi:menghitung skor dan kategori N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori 

# KAMUS
# n, i : int
# pin : str
# skor : int
# kuat, sedang, lemah : int
# hasil : int
# d, c : str

def skor_pin(pin):
    hasil = 0
    for d in "0123456789":
        if d in pin:
            hasil += 4
    for c in pin:
        if c.isupper():
            hasil += 10
            break
    if len(pin) >= 8:
        hasil += 15
    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            if abs(int(pin[i]) - int(pin[i + 1])) == 1:
                hasil -= 5
    return hasil


def kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"

kuat = sedang = lemah = 0
n = int(input("Masukan jumlah kandidat PIN (N): "))
for i in range(1, n + 1):
    pin = input("Kandidat PIN ke-" + str(i) + ": ")
    skor = skor_pin(pin)
    kat = kategori(skor)
    print("Skor: " + str(skor) + ", Kategori: " + kat)
    if kat == "Kuat":
        kuat += 1
    elif kat == "Sedang":
        sedang += 1
    else:
        lemah += 1

print("Kuat: " + str(kuat))
print("Sedang: " + str(sedang))
print("Lemah: " + str(lemah))
