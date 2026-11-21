#NAMA/NIM :RUDIANTO
#Tanggal : 11 November 2026
#Deskripsi : Problem 2

def hitung_skor(pin):
    skor = 0
    digit_unik = ""

    # Menghitung digit berbeda
    for karakter in pin:
        if karakter.isdigit():
            if karakter not in digit_unik:
                digit_unik += karakter

    skor += len(digit_unik) * 4

    # Jika terdapat huruf besar
    for karakter in pin:
        if karakter.isupper():
            skor += 10
            break

    # Menghitung bonus panjang PIN
    if len(pin) >= 8:
        skor += 15
    elif len(pin) >= 6:
        skor += 5

    # Menghitung penalti digit berurutan
    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            if abs(int(pin[i]) - int(pin[i + 1])) == 1:
                skor -= 5

    # Menentukan kategori PIN
    if skor >= 40:
        kategori = "Kuat"
    elif skor >= 20:
        kategori = "Sedang"
    else:
        kategori = "Lemah"

    return skor, kategori


n = int(input("Masukkan jumlah kandidat PIN (N): "))

kuat = 0
sedang = 0
lemah = 0

for i in range(n):
    pin = input("Kandidat PIN ke-" + str(i + 1) + ": ")

    skor, kategori = hitung_skor(pin)

    print("PIN ke-" + str(i + 1) + " skornya", skor,
          ", tergolong", kategori + ".")

    if kategori == "Kuat":
        kuat += 1
    elif kategori == "Sedang":
        sedang += 1
    else:
        lemah += 1

print("Rekap: Kuat", kuat, ", Sedang", sedang, ", Lemah", lemah)

#NAMA/NIM :RUDIANTO
#Tanggal : 11 November 2026
#Deskripsi : Test Case 2

def hitung_skor(pin):
    skor = 0
    digit_unik = ""

    # Menghitung digit berbeda
    for karakter in pin:
        if karakter.isdigit():
            if karakter not in digit_unik:
                digit_unik += karakter

    skor += len(digit_unik) * 4

    # Jika terdapat huruf besar
    for karakter in pin:
        if karakter.isupper():
            skor += 10
            break

    # Menghitung bonus panjang PIN
    if len(pin) >= 8:
        skor += 15
    elif len(pin) >= 6:
        skor += 5

    # Menghitung penalti digit berurutan
    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            if abs(int(pin[i]) - int(pin[i + 1])) == 1:
                skor -= 5

    # Menentukan kategori PIN
    if skor >= 40:
        kategori = "Kuat"
    elif skor >= 20:
        kategori = "Sedang"
    else:
        kategori = "Lemah"

    return skor, kategori


n = int(input("Masukkan jumlah kandidat PIN (N): "))

kuat = 0
sedang = 0
lemah = 0

for i in range(n):
    pin = input("Kandidat PIN ke-" + str(i + 1) + ": ")

    skor, kategori = hitung_skor(pin)

    print("PIN ke-" + str(i + 1) + " skornya", skor,
          ", tergolong", kategori + ".")

    if kategori == "Kuat":
        kuat += 1
    elif kategori == "Sedang":
        sedang += 1
    else:
        lemah += 1

print("Rekap: Kuat", kuat, ", Sedang", sedang, ", Lemah", lemah)

#NAMA/NIM :RUDIANTO
#Tanggal : 11 November 2026
#Deskripsi : Test Case 3

def hitung_skor(pin):
    skor = 0
    digit_unik = ""

    # Menghitung digit berbeda
    for karakter in pin:
        if karakter.isdigit():
            if karakter not in digit_unik:
                digit_unik += karakter

    skor += len(digit_unik) * 4

    # Jika terdapat huruf besar
    for karakter in pin:
        if karakter.isupper():
            skor += 10
            break

    # Menghitung bonus panjang PIN
    if len(pin) >= 8:
        skor += 15
    elif len(pin) >= 6:
        skor += 5

    # Menghitung penalti digit berurutan
    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            if abs(int(pin[i]) - int(pin[i + 1])) == 1:
                skor -= 5

    # Menentukan kategori PIN
    if skor >= 40:
        kategori = "Kuat"
    elif skor >= 20:
        kategori = "Sedang"
    else:
        kategori = "Lemah"

    return skor, kategori


n = int(input("Masukkan jumlah kandidat PIN (N): "))

kuat = 0
sedang = 0
lemah = 0

for i in range(n):
    pin = input("Kandidat PIN ke-" + str(i + 1) + ": ")

    skor, kategori = hitung_skor(pin)

    print("PIN ke-" + str(i + 1) + " skornya", skor,
          ", tergolong", kategori + ".")

    if kategori == "Kuat":
        kuat += 1
    elif kategori == "Sedang":
        sedang += 1
    else:
        lemah += 1

print("Rekap: Kuat", kuat, ", Sedang", sedang, ", Lemah", lemah)

