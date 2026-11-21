# NIM/Nama : 15626007 / Ryssad Sabralnair
# Tanggal : 11 November 2026
# Deskripsi : Merancang Program untuk Menghitung Skor dan Kategori dari N Kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori

n = int(input("Masukkan banyaknya kandidat PIN (N): "))

#SubProgram untuk menghitung skor dan kategori dari N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori
skor = []
kategori = []

#Aturan Pertama: Jika PIN mengandung minimal satu digit angka, Tambahkan 4 poin ke skor untuk setiap digit angka yang berbeda
def hitung_skor(pin):
    digit_berbeda = set()
    for char in pin:
        if char.isdigit():
            digit_berbeda.add(char)
    return len(digit_berbeda) * 4

#Aturan Kedua: Jika PIN mengandung minimal satu huruf besar, Tambahkan 10 poin ke skor
def cek_huruf_besar(pin):
    for char in pin:
        if char.isupper():
            return 10
    return 0

#Aturan Ketiga: Jika panjang PIN minimal 8 karakter, Tambahkan 15 poin ke skor
def cek_panjang(pin):
    if len(pin) >= 8:
        return 15
    return 0

#Aturan Keempat: Jika panjang PIN antara 6 hingga 7 karakter, Tambahkan 5 poin ke skor
def cek_panjang_sedang(pin):    
    if 6 <= len(pin) <= 7:
        return 5
    return 0

#Aturan Kelima: Jika Panjang pin kurang dari 6 karakter, tambahkan 0 poin ke skor
def cek_panjang_pendek(pin):
    if len(pin) < 6:
        return 0
    return 0

#Aturan Keenam: Jika digit angka beruruntun seperti 1234 atau 4321 dan untuk setiap dua digit bersebelahan langsung di dalam PIN dan selisihnya tepat 1(Baik naik maupun turun, kurangi 5 poin dari skor
#Poin berkurang 5 setiap kali ditemukan dua digit berurutan, meskipun digit tersebut muncul lebih dari sekali

def cek_angka_berurutan(pin):
    skor = 0
    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            if abs(int(pin[i]) - int(pin[i + 1])) == 1:
                skor -= 5
    return skor

#Program menghitung skor dan kategori dari N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori

#Menghitung skor dan kategori untuk setiap kandidat PIN
for i in range(n):
    pin = input(f"Masukkan PIN kandidat ke-{i + 1}: ")
    skor_kandidat = hitung_skor(pin) + cek_huruf_besar(pin) + cek_panjang(pin) + cek_panjang_sedang(pin) + cek_panjang_pendek(pin) + cek_angka_berurutan(pin)
    skor.append(skor_kandidat)

    #Menentukan kategori berdasarkan skor
    if skor_kandidat >= 40:
        kategori.append("Kuat")
    elif 20 <= skor_kandidat < 40:
        kategori.append("Sedang")
    else:
        kategori.append("Lemah")
        
#Menampilkan hasil skor dan kategori untuk setiap kandidat PIN
print("\nHasil Skor dan Kategori Kandidat PIN:")
for i in range(n):
    print(f"Kandidat ke-{i + 1}: Skor = {skor[i]}, Kategori = {kategori[i]}")
    
#Menampilkan rekap banyaknya PIN pada tiap kategori
rekap_kategori = {"Kuat": 0, "Sedang": 0, "Lemah": 0}
for k in kategori:
    rekap_kategori[k] += 1
print("\nRekap Banyaknya PIN pada Tiap Kategori:")
for k, v in rekap_kategori.items():
    print(f"{k}: {v} PIN")