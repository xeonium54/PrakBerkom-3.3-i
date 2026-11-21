#Nama : Fadhil Zulhilmi
#NIM : 15626014
#Deskripsi : 

def hitung_skor_pin(pin):
    skor = 0

    digit_unik = set()
    ada_huruf_besar = False

    for karakter in pin:
        if karakter.isdigit():
            digit_unik.add(karakter)
        elif karakter.isupper():
            ada_huruf_besar = True

    skor += len(digit_unik) * 4

    if ada_huruf_besar:
        skor += 10

    panjang = len(pin)
    if panjang >= 8:
        skor += 15
    elif 6 <= panjang <= 7:
        skor += 5

    for i in range (panjang - 1):
        if pin[i].isdigit () and pin[i+1].isdigit():
            selisih = abs(int(pin[i]) - int(pin[i + 1]))
            if selisih == 1:
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

jumlah_kuat = 0
jumlah_sedang = 0
jumlah_lemat = 0

for i in range (1, n + 1): 
    kandidat_pin = input(f"Kandidat PIN ke-{i}: ")
    skor_akhir = hitung_skor_pin(kandidat_pin)
    kategori = tentukan_kategori(skor_akhir)

print(f"PIN ke-{i} skornya {skor_akhir}, tergolong {kategori}. ")

if kategori == "Kuat":
    jumlah_kuat += 1
elif kategori == "Sedang":
    jumlah_sedang += 1
else:
    jumlah_kuat += 1

print(f"Rekap: Kuat{jumlah_kuat}, Sedang {jumlah_sedang}, Lemah {jumlah_lemat}")