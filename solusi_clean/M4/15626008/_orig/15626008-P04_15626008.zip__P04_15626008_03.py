# NIM/Nama : Arya Satya Anggara
# Tanggal : 11 November 2026
# Deskripsi : Program ini digunakan untuk memprediksi nilai UAS berdasarkan total waktu belajar pada empat modul dan sisa energi sebelum ujian

def belajar(T, E, W, modul, durasi):
    if durasi > W:
        durasi = W
    if durasi * 5 > E:
        durasi = E / 5

    T[modul-1] += durasi
    E -= durasi * 5
    W -= durasi

    return T, E, W


def tidur(E, W):
    E += W * 12.5
    if E > 100:
        E = 100
    W = 0
    return E, W


def HitungNilai(T, t, E):
    total = 0

    for i in range(4):
        if T[i] > t[i]:
            total += 1
        else:
            total += T[i] / t[i]

    S = (total / 4) * 100
    return S


E = 100
W = float(input("Masukkan waktu sebelum UAS: "))

t = []
for i in range(4):
    t.append(float(input("Waktu minimal modul: ")))

T = [0, 0, 0, 0]

while W > 0 and E > 0:
    print("1. belajar")
    print("2. tidur")

    pilihan = int(input("pilih tindakan: "))

    while pilihan != 1 and pilihan != 2:
        pilihan = int(input("pilihan salah, masukkan lagi: "))

    if pilihan == 1:
        modul = int(input("pilih modul (1-4): "))
        while modul < 1 or modul > 4:
            modul = int(input("modul salah, masukkan lagi: "))

        durasi = float(input("durasi belajar: "))
        T, E, W = belajar(T, E, W, modul, durasi)

    else:
        E, W = tidur(E, W)

if W > 0:
    E, W = tidur(E, W)

nilai = HitungNilai(T, t, E)

print("prediksi nilai uas:", nilai)
