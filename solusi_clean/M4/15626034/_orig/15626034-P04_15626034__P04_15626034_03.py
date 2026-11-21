#NIM/NAMA : 15626034/Ahmad Zaky
#Tanggal : 11 November 2026
#Deskripsi : Menghitung FPB


def belajar(w, E, T, t):
    while true:
        m = input ("modul (1-4):")
        if m in "1234":
            m = int(m) - 1
            break

    while true :
        try:
            d = int(input("durasi (JAM):"))
            if d > 0:
                break
        except :
            pass
        if d > w :
            d = w
        max_d, te = 0, E
        while te >= 5 and max_d < d:
            max_d += 1
            te -= 5
        if d > max_d:
            d, E = max_d, 0
        else:
            E -= d * 5
        T[m] += d
        return w - d, E

def bobo(w, E):
    E += w * 25
    return 0, 100 if E > 100 else E

def main():
    n = int(input("total waktu persiapan (JAM):"))
    t = []
    for i in range(4):
        t.append(int(input(f"durasi modul {i + 1} (JAM):")))
    T, E, w = [0, 0, 0, 0], 100, n
    while w > 0:
        print(f"\nSisa waktu persiapan: {w} JAM")
        print(f"Durasi modul: {t}")
        print(f"Durasi belajar: {T}")
        print(f"Energy: {E}")
        a = input("aksi (belajar/bobo):")
        if a == "belajar":
            w, E = belajar(w, E, T, t)
        elif a == "bobo":
            w, E = bobo(w, E)

        print(f"\n prediksi nilai UAS : {nilai(T, t, E):.2f}")

if __name__ == "__main__":
    main()

    #sisa 15 menit udh pusng