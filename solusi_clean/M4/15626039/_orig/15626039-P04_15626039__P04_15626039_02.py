#15626039/Khalif Aufar A
#11 November 2026
#No 2, PIN

#Kamus
#pin, tk = str
#skor, dgu, panjang, angka1, angka2, selisih = int
#kapital = bool
#kuat, sedang, lemah, n, i = int
#d, huruf = char

def hitungskor(pin):
    skor = 0

    dgu = 0
    for d  in "0123456789":
        if d in pin:
            dgu += 1
    skor += dgu * 4

    kapital = False
    for huruf in pin:
        if 'A' <= huruf <= 'Z':
            kapital = True
    if kapital:
        skor += 10

    panjang = 0
    for huruf in pin:
        panjang += 1
    if panjang >= 8:
        skor += 15
    elif panjang >= 6:
        skor += 5 

    for i in range (panjang - 1):
        if '0' <= pin[i] <= '9' and '0' <= pin[i+1] <= '9':
            angka1 = int(pin[i])
            angka2 = int(pin[i+1])
            selisih = angka1 - angka2
            if selisih == 1 or selisih == -1:
                skor -= 5
    return skor

def kategori(skor):
    if skor >= 40:
        return "kuat"
    elif skor >= 20:
        return "sedang"
    else:
        return "lemah"

def main():
    n = int(input("masukkan jumlah kandidat PIN :"))
    kuat = 0
    sedang = 0
    lemah = 0

    for i in range(1, n+1):
        pin = input("Kandidat PIN ke-" + str(i) + ":")
        skor = hitungskor(pin)
        tk = kategori(skor)

        if tk == "kuat":
            kuat += 1
        elif tk == "sedang":
            sedang += 1
        else:
            lemah += 1

        print("PIN ke-" + str(i) + "skornya" + str(skor) +", tergolong" + tk)
    print("Rekap: kuat" + str(kuat) + ", sedang" + str(sedang) + ", lemah" + str(lemah))   
main()


