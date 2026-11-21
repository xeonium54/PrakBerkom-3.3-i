# Nama: Reyza Aulia Rahman
# NIM: 15426131
# Deskripsi: Skor pin


def nilaiskor(pin):
    skor = 0
    digitunik = ""

    for angka in pin:
        if angka.isdigit() and angka not in digitunik:
            skor += 4
            digitunik += angka

    for huruf in pin:
        if huruf.isupper():
            skor += 10
            break

    if len(pin) >= 8:
        skor += 15
    elif len(pin) >= 6:
        skor += 5

    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i+1].isdigit():
            numba1 = int(pin[i])
            numba2 = int(pin[i+1])
            if numba1 + 1 == numba2 or numba1 - 1 == numba2:
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

for i in range(1, N + 1):
    pin = input(f"Kandidat PIN ke-{i}: ")
    skor = nilaiskor(pin)
    hasil = kategori(skor)
    print(f"PIN ke-{i} skornya {skor}, tergolong {hasil}.")

    if hasil == "Kuat":
        kuat += 1
    elif hasil == "Sedang":
        sedang += 1
    else:
        lemah += 1

print(f"Rekap: Kuat {kuat}, Sedang {sedang}, Lemah {lemah}")