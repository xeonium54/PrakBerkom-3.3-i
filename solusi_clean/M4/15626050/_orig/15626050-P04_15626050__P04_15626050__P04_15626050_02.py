# NIM/Nama : 15626050/Yohanes Yoel Christopher Naibaho
# Tanggal : 11 November 2026
# Deskripsi : Menghitung kekuatan PIN

# KAMUS
# N, i, j, skor : int
# PIN : str
# kuat, sedang, lemah : int

# Definisi fungsi
def HitungSkor(PIN):
    # Menghitung skor PIN

    # KAMUS LOKAL
    # i, j, jumlah, ditemukan, penalti : int
    # skor : int

    # ALGORITMA
    skor = 0
    jumlah = 0
    penalti = 0

    # Menghitung digit yang berbeda
    for i in range(len(PIN)):
        if (PIN[i] >= '0' and PIN[i] <= '9'):
            ditemukan = 0

            for j in range(i):
                if (PIN[i] == PIN[j]):
                    ditemukan = 1

            if (ditemukan == 0):
                jumlah = jumlah + 1

    skor = jumlah * 4

    # Memeriksa huruf besar
    for i in range(len(PIN)):
        if (PIN[i] >= 'A' and PIN[i] <= 'Z'):
            skor = skor + 10
            break

    # Menghitung poin berdasarkan panjang PIN
    if (len(PIN) >= 8):
        skor = skor + 15
    elif (len(PIN) >= 6):
        skor = skor + 5

    # Menghitung penalti digit berurutan
    for i in range(len(PIN) - 1):
        if (PIN[i] >= '0' and PIN[i] <= '9'):
            if (PIN[i+1] >= '0' and PIN[i+1] <= '9'):

                angka1 = int(PIN[i])
                angka2 = int(PIN[i+1])

                if (angka1 - angka2 == 1 or
                    angka2 - angka1 == 1):
                    penalti = penalti + 5

    skor = skor - penalti

    return skor


def Kategori(skor):
    # Menentukan kategori PIN

    # ALGORITMA
    if (skor >= 40):
        return "Kuat"
    elif (skor >= 20):
        return "Sedang"
    else:
        return "Lemah"


# ALGORITMA PROGRAM UTAMA
N = int(input("Masukkan jumlah kandidat PIN (N): "))

kuat = 0
sedang = 0
lemah = 0

for i in range(1, N+1):
    PIN = input("Kandidat PIN ke -" + str(i) + ": ")

    skor = HitungSkor(PIN)
    hasil = Kategori(skor)

    print("PIN ke -" + str(i) + " skornya " +
          str(skor) + ", tergolong ke dalam kategori " + hasil + ".")

    if (hasil == "Kuat"):
        kuat = kuat + 1
    elif (hasil == "Sedang"):
        sedang = sedang + 1
    else:
        lemah = lemah + 1

print("Rekap Hasil Pinnya : Kuat " + str(kuat) +
      ", Sedang " + str(sedang) +
      ", Lemah " + str(lemah))
