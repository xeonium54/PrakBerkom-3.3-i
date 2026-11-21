# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 11 November 2026
# Deskripsi : 

def SyaratPin(pin):
# Kamus Lokal
    # skor (int)
    # hitungUnik (int)
    # ditemukan (bool)
    # panjang (int)
    # kapital (bool)

    # Algoritma
#   Subprogram syarat
#   Hitung digit berbeda
    skor = 0
    hitungUnik = 0
    ditemukan = [False] * 10
    for char in pin:
        if '0' <= char <= '9':
            if not ditemukan [int(char)]:
                ditemukan [int(char)] = True
                hitungUnik += 1
    skor += hitungUnik * 4

#   Hitung panjang pin 
    panjang = 0
    for _ in pin:
        panjang += 1

# Cek Huruf Besar
    kapital = False
    i = 0
    while i < panjang and not kapital:
        if 'A' <= pin[i] <= 'Z':
            kapital = True
        i += 1
# Bonus tambahan poin untuk kapital dan panjang
    if kapital:
        skor += 10

    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5
# Penalti untuk syarat pin
    for j in range(panjang - 1):
        if '0' <= pin[j] <= '9' and '0' <= pin[j+1] <= '9':
            selisih = int(pin[j]) - int(pin[j+1])
            if selisih == 1 or selisih == -1:
                skor -= 5

    return skor
#   Subprogram kategori
def kategori(skor):
    if skor >= 40:
        return "Kuat"
    elif 20 <= skor < 40:
        return "Sedang"
    else:
        return "Lemah"
# Algoritma program utama
n = int(input("Masukkan jumlah kandidat pin: "))

nKuat = 0
nSedang = 0
nLemah = 0

for i in range(1, n + 1):
    pin = input(f"Kandidat PIN ke-{i}: ")
    skor = SyaratPin(pin)
    hitungKategori = kategori(skor)

    print(f"PIN ke-{i} skornya {skor}, tergolong {hitungKategori}")

    if hitungKategori == "Kuat":
        nKuat += 1
    elif hitungKategori == "Sedang":
        nSedang += 1
    else:
        nLemah += 1

print(f"Rekap: Kuat {nKuat}, Sedang {nSedang}, Lemah {nLemah}")
