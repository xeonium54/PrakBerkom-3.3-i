#NAMA/NIM :RUDIANTO
#Tanggal : 11 November 2026
#Deskripsi : Problem 3

def belajar(durasi, waktu, energi):
    if durasi > waktu:
        durasi = waktu

    if durasi * 5 > energi:
        durasi = energi / 5

    energi = energi - (durasi * 5)
    waktu = waktu - durasi

    return durasi, waktu, energi


def tidur(waktu, energi):
    energi = energi + (waktu * 12.5)

    if energi > 100:
        energi = 100

    return energi


def prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E):
    if T1 > t1:
        T1 = t1
    if T2 > t2:
        T2 = t2
    if T3 > t3:
        T3 = t3
    if T4 > t4:
        T4 = t4

    rata = ((T1 / t1) + (T2 / t2) +
            (T3 / t3) + (T4 / t4)) / 4

    energi = (100 ** 2 - (100 - E) ** 2) / 100

    return rata * energi


def menu():
    print("1. Belajar")
    print("2. Tidur")


N = float(input("Masukkan sisa waktu: "))

t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

E = 100
T1 = 0
T2 = 0
T3 = 0
T4 = 0

while N > 0:

    if E == 0:
        E = tidur(N, E)
        N = 0
    else:
        menu()
        pilihan = int(input("Pilih tindakan (1/2): "))

        if pilihan == 1:
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))

            if modul >= 1 and modul <= 4:
                durasi = float(input("Masukkan durasi belajar: "))

                if modul == 1:
                    hasil, N, E = belajar(durasi, N, E)
                    T1 = T1 + hasil

                elif modul == 2:
                    hasil, N, E = belajar(durasi, N, E)
                    T2 = T2 + hasil

                elif modul == 3:
                    hasil, N, E = belajar(durasi, N, E)
                    T3 = T3 + hasil

                elif modul == 4:
                    hasil, N, E = belajar(durasi, N, E)
                    T4 = T4 + hasil
            else:
                print("Pilihan modul tidak tersedia!")

        elif pilihan == 2:
            E = tidur(N, E)
            N = 0

        else:
            print("Pilihan tidak tersedia! Pilih tindakan (1/2):")

hasil = prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E)

print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah", hasil)

#NAMA/NIM :RUDIANTO
#Tanggal : 11 November 2026
#Deskripsi : Test Case 2

def belajar(durasi, waktu, energi):
    if durasi > waktu:
        durasi = waktu

    if durasi * 5 > energi:
        durasi = energi / 5

    energi = energi - (durasi * 5)
    waktu = waktu - durasi

    return durasi, waktu, energi


def tidur(waktu, energi):
    energi = energi + (waktu * 12.5)

    if energi > 100:
        energi = 100

    return energi


def prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E):
    if T1 > t1:
        T1 = t1
    if T2 > t2:
        T2 = t2
    if T3 > t3:
        T3 = t3
    if T4 > t4:
        T4 = t4

    rata = ((T1 / t1) + (T2 / t2) +
            (T3 / t3) + (T4 / t4)) / 4

    energi = (100 ** 2 - (100 - E) ** 2) / 100

    return rata * energi


def menu():
    print("1. Belajar")
    print("2. Tidur")


N = float(input("Masukkan sisa waktu: "))

t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

E = 100
T1 = 0
T2 = 0
T3 = 0
T4 = 0

while N > 0:

    if E == 0:
        E = tidur(N, E)
        N = 0
    else:
        menu()
        pilihan = int(input("Pilih tindakan (1/2): "))

        if pilihan == 1:
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))

            if modul >= 1 and modul <= 4:
                durasi = float(input("Masukkan durasi belajar: "))

                if modul == 1:
                    hasil, N, E = belajar(durasi, N, E)
                    T1 = T1 + hasil

                elif modul == 2:
                    hasil, N, E = belajar(durasi, N, E)
                    T2 = T2 + hasil

                elif modul == 3:
                    hasil, N, E = belajar(durasi, N, E)
                    T3 = T3 + hasil

                elif modul == 4:
                    hasil, N, E = belajar(durasi, N, E)
                    T4 = T4 + hasil
            else:
                print("Pilihan modul tidak tersedia!")

        elif pilihan == 2:
            E = tidur(N, E)
            N = 0

        else:
            print("Pilihan tidak tersedia! Pilih tindakan (1/2):")

hasil = prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E)

print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah", hasil)

#NAMA/NIM :RUDIANTO
#Tanggal : 11 November 2026
#Deskripsi : Test Case 3
def belajar(durasi, waktu, energi):
    if durasi > waktu:
        durasi = waktu

    if durasi * 5 > energi:
        durasi = energi / 5

    energi = energi - (durasi * 5)
    waktu = waktu - durasi

    return durasi, waktu, energi


def tidur(waktu, energi):
    energi = energi + (waktu * 12.5)

    if energi > 100:
        energi = 100

    return energi


def prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E):
    if T1 > t1:
        T1 = t1
    if T2 > t2:
        T2 = t2
    if T3 > t3:
        T3 = t3
    if T4 > t4:
        T4 = t4

    rata = ((T1 / t1) + (T2 / t2) +
            (T3 / t3) + (T4 / t4)) / 4

    energi = (100 ** 2 - (100 - E) ** 2) / 100

    return rata * energi


def menu():
    print("1. Belajar")
    print("2. Tidur")


N = float(input("Masukkan sisa waktu: "))

t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

E = 100
T1 = 0
T2 = 0
T3 = 0
T4 = 0

while N > 0:

    if E == 0:
        E = tidur(N, E)
        N = 0
    else:
        menu()
        pilihan = int(input("Pilih tindakan (1/2): "))

        if pilihan == 1:
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))

            if modul >= 1 and modul <= 4:
                durasi = float(input("Masukkan durasi belajar: "))

                if modul == 1:
                    hasil, N, E = belajar(durasi, N, E)
                    T1 = T1 + hasil

                elif modul == 2:
                    hasil, N, E = belajar(durasi, N, E)
                    T2 = T2 + hasil

                elif modul == 3:
                    hasil, N, E = belajar(durasi, N, E)
                    T3 = T3 + hasil

                elif modul == 4:
                    hasil, N, E = belajar(durasi, N, E)
                    T4 = T4 + hasil
            else:
                print("Pilihan modul tidak tersedia!")

        elif pilihan == 2:
            E = tidur(N, E)
            N = 0

        else:
            print("Pilihan tidak tersedia! Pilih tindakan (1/2):")

hasil = prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E)

print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah", hasil)