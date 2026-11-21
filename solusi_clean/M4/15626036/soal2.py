#NIM/Nama: Aghneo Amar Ahsan
#Tanggal: 11 November 2026
#Deskripsi: Program ini dirancang untuk memberikan penilaian pada suatu kata sandi atau pin

def hitungSkorPin(pin):
    skor = 0
    digitUnik = ""
    hurufBesar = False

    for char in pin: 
        if 'A' <= char <= 'Z':
            hurufBesar = True
        elif '0' <= char <= '9': 
            terdaftar = False
            for d in digitUnik:
                if char == d:
                    terdaftar = True
            if not terdaftar:
                digitUnik += char

    skor += len(digitUnik) * 4 

    if hurufBesar:
        skor += 10

    if len(pin) >= 8:
        skor += 15
    elif 6 <= len(pin) <= 7:
        skor += 5

    for i in range(len(pin) - 1): 
        if ('0' <= pin[i] <= '9') and ('0' <= pin[i+1] <= '9'):
           selisih = int(pin[i]) - int(pin[i+1])
           if selisih == 1 or selisih == -1:
               skor += 5

    if skor >= 40: 
        kategori = "Kuat"
    elif 20 <= skor <= 40: 
        kategori = "Sedang"
    else:
        kategori = "Lemah"

    return skor, kategori

n = int(input("Masukan Jumlah Kandidat PIN: "))
kuat = 0
sedang = 0
lemah = 0

for i in range (1, n+1):
    pin = input(f"Kandidat PIN ke-{i}: ")
    skor, kategori = hitungSkorPin(pin)
    print(f"PIN ke-{i} skornya {skor}, tergolong {kategori}.")

    if kategori == "Kuat":
        kuat += 1
    elif kategori == "Sedang":
        sedang += 1
    else: 
        lemah += 1

print(f"Rekap: Kuat {kuat}, Sedang {sedang}, Lemah {lemah}")