#Nama : Febrian Yaif Hakim
#NIM : 15626042
#Tanggal: 11 Nov 2026

#Problem 2
def hitung_skor(pin):
    skor = 0
    panjang = 0
    ada_besar = False
    ada_digit = [False for i in range(10)]

    for c in pin:
        panjang += 1
        if "A" <= c <= "Z":
            ada_besar = True
        elif "0" <= c <= "9":
            ada_digit[int(c)] = True

    for ada in ada_digit:
        if ada:
            skor += 4

    if ada_besar:
        skor += 10

    if panjang >= 8:
        skor += 15
    elif panjang >= 6:
        skor += 5

    for i in range(panjang - 1):
        if ("0" <= pin[i] <= "9") and ("0" <= pin[i + 1] <= "9"):
            d1 = int(pin[i])
            d2 = int(pin[i + 1])
            if (d1 - d2 == 1) or (d2 - d1 == 1):
                skor -= 5

    return skor

def tentukan_kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif skor >= 20:
        return "Sedang"
    else:
        return "Lemah"

n = int(input("Masukkan jumlah kandidat PIN (N): "))
kuat = 0
sedang = 0
lemah = 0

for i in range(1, n + 1):
    pin = input("Kandidat PIN ke-" + str(i) + ": ")
    skor = hitung_skor(pin)
    kat = tentukan_kategori(skor)
    
    print("PIN ke-" + str(i) + " skornya " + str(skor) + ", tergolong " + kat + ".")
    
    if kat == "Kuat":
        kuat += 1
    elif kat == "Sedang":
        sedang += 1
    else:
        lemah += 1

print("Rekap: Kuat " + str(kuat) + ", Sedang " + str(sedang) + ", Lemah " + str(lemah))