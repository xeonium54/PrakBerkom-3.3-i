# Rabu, 11 November 2026
# Nama  : Vidia Nurafifa
# NIM   : 15626011
# Desc  : Soal 2 - Memperhitungkan Kekuatan PIN 

# Aturan PIN (biar inget)
# setiap digit berbeda = 4 poin 
# minimal ada 1 huruf kapital = 10 poin 
# panjang PIN
# minimal 8 char (15 poin)
# 6-7 char (5 poin)
# <6 char (0 poin)
# setiap 2 digit bersebelahan/berurutan (tepat selisih 1)
# akan mendapatkan penalti = -5 poin 
# kategori PIN
# Kuat      : >= 40
# Sedang    : 20 <= x < 40
# Lemah     : <20

# Jumlah kandidat PIN (N)
# Password/kata kunci (PIN)
# Skor Kekuatan PIN (SP)
# Hitung Skor (HS)
# Skor Kapital (SK)
# Digit (D)
# Nilai Digit PIN (No)
# Angka (A)
# Kategori PIN (KP)
# Jumlah PIN Kuat (K)
# Jumlah PIN Sedang (S)
# Jumlah PIN Lemah (L)
# Indeks perulangan (i)

def HS(PIN):

    SP = 0
    SK = 0

    D = [0 for i in range(10)]

    for i in range(len(PIN)):

        if (PIN[i] >= "0" and PIN[i] <= "9"):
            No = int(PIN[i])

            if (D[No] == 0):
                SP += 4
                D[No] = 1

        if (PIN[i] >= "A" and PIN[i] <= "Z"):
            SK = 1

    if (SK == 1):
        SP += 10

    if (len(PIN) >= 8):
        SP += 15
    elif (len(PIN) >= 6):
        SP += 5

    for i in range(len(PIN) - 1):

        if (PIN[i] >= "0" and PIN[i] <= "9") and (PIN[i+1] >= "0" and PIN[i+1] <= "9"):

            A1 = int(PIN[i])
            A2 = int(PIN[i+1])

            if (A1 - A2 == 1) or (A2 - A1 == 1):
                SP -= 5
    return SP

def KP(SP):

    if (SP >= 40):
        return "Kuat"
    elif (SP >= 20):
        return "Sedang"
    else:
        return "Lemah"

N = int(input("Masukkan jumlah kandidat PIN (N): "))

K = 0
S = 0
L = 0

for i in range(N):

    PIN = input("Kandidat PIN ke -" + str(i+1) + ": ")

    SP = HS(PIN)
    KATEGORI = KP(SP)

    print("PIN ke -" + str(i+1) + " skornya", SP, ", tergolong", KATEGORI + ".")

    if (KATEGORI == "Kuat"):
        K += 1
    elif (KATEGORI == "Sedang"):
        S += 1
    else:
        L += 1

print("Rekap : Kuat", K, ", Sedang", S, ", Lemah", L)