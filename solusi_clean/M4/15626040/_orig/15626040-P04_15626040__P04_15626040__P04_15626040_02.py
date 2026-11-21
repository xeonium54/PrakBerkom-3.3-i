# NIM/Nama: 15626040/Frizka Yunisaf
# Tanggal: 11 November 2026
# Deskripsi: Menghitung skor dan kategori dari N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori

def AdalahDigit (c):
    return (c>= "0" and c <= "9")

def SkorDigitBeda (pin):
    skor = 0
    for d in range (10):
        ada = False
        for i in range (len(pin)):
            if (pin[i] == str(d)):
                ada = True
        if (ada):
            skor += 4
    return skor

def SkorHurufBesar (pin):
    skor = 0
    for i in range (len(pin)):
        if (pin[i] >= "A" and pin[i] <= "Z"):
            skor = 10
    return skor

def SkorPanjang (pin):
    n = len(pin)
    if (n >= 8):
        return 15
    elif (n >= 6):
        return 5
    else:
        return 0

def PenaltiBerurutan (pin):
    penalti = 0
    for i in range (len(pin) - 1):
        if (AdalahDigit (pin[i]) and AdalahDigit (pin[i+1])): 
            selisih = int(pin[i]) - int(pin[i+1])
            if (selisih == 1 or selisih == -1):
                penalti += 5
    return penalti

def HitungSkor(pin):
    return SkorDigitBeda (pin) +SkorHurufBesar (pin) + SkorPanjang (pin) - PenaltiBerurutan (pin)

def Kategori (skor): 
    if (skor >= 40):
        return "Kuat"
    elif (skor >= 20):
        return "Sedang"
    else:
        return "Lemah"

#Program Utama
N = int(input("Masukkan jumlah kandidiat pin (N): "))
kuat = 0 
sedang = 0
lemah = 0

for i in range (N):
    pin = input("Kandidat PIN ke-" + str(i+1) + ": ")
    skor = HitungSkor (pin)
    kategori = Kategori (skor)
    print  ("PIN ke-" + str (i+1)+ " skornya " + str(skor) + ", tergolong " + kategori + ".")
    if (kategori == "Kuat"):
        kuat += 1
    elif (kategori == "Sedang"):
        sedang += 1
    else:
        lemah += 1

print ("Rekap: Kuat " + str(kuat) + ", Sedang " + str(sedang)+ ", Lemah " + str(lemah))


