# NIM / Nama : 15626006/Maria Zeysta Kamelia Rumanti
# Tanggal : 11 November 2026
# Deskripsi : Program untuk  menghitung skor dan kategori dari N kandidat PIN, serta menampilkan rekap banyaknya PIN pada tiap kategori

def evaluasi_pin(pin):
    # KAMUS
    # skor, panjang_pin, i, j, selisih : int
    # ada_huruf_besar, sudah_ada : bool
    # digit_unik : list of str
    # char_sekarang, char_berikutnya : str

    # ALGORITMA
    skor = 0
    panjang_pin = len(pin)

    # Cek digit berbeda (0-9)
    digit_unik = []
    for i in range(panjang_pin):
        char_sekarang = pin[i]

        # Cek apakah karakter adalah angka (0-9)
        if char_sekarang >= '0' and char_sekarang <= '9':
            sudah_ada = False

        # Cek apakah karakter sudah masuk list
        for j in range(len(digit_unik)):
            if digit_unik[j] == char_sekarang:
                sudah_ada = True

        # Jika belum ada
        if sudah_ada == False:
            digit_unik.append(char_sekarang)

    # Tambah 4 poin untuk tiap digit berbeda
    skor = skor + (len(digit_unik) * 4)

    # Cek minimal satu huruf besar
    ada_huruf_besar = False
    for i in range(panjang_pin):
        char_sekarang = pin[i]
        # Huruf besar di rentang A-Z
        if char_sekarang >= 'A' and char_sekarang <= 'Z':
            ada_huruf_besar = True

    # Tambah 10 poin
    if ada_huruf_besar == True:
        skor = skor + 10

    # Cek panjang PIN
    if panjang_pin >= 8:
        skor = skor + 15
    elif panjang_pin >= 6 and panjang_pin <= 7:
        skor = skor + 5

    # Digit bersebelahan yang selisihnya 1
    for i in range(panjang_pin - 1):
        char_sekarang = pin[i]
        char_berikutnya = pin[i + 1]

        # Pastikan kedua karakter adalah angka
        if (char_sekarang >= '0' and char_sekarang <= '9') and (char_berikutnya >= '0' and char_berikutnya <= '9'):
            selisih = int(char_sekarang) - int(char_berikutnya)

            if selisih < 0:
                selisih = selisih * -1

            if selisih == 1:
                skor = skor - 5

    if skor >= 40:
        kategori = "Kuat"
    elif skor >= 20 and skor < 40:
        kategori = "Sedang"
    else:
        kategori= "Lemah"

# PROGRAM UTAMA
# KAMUS
# n, jumlah_kuat, jumlah_sedang, jumlah_lemah, i, skor_pin : int
# pint_kandidat, kategori_pin : str

# ALGORITMA
n = int(input("Masukkan jumlah kandidat PIN (N): "))

jumlah_kuat = 0
jumlah_sedang = 0
jumlah_lemah = 0

for i in range (1, n + 1):
    pin_kandidat = input(f"Kandidat Pin ke-{i}: ")

skor_pin, kategori_pin = evaluasi_pin(pin_kandidat)

print(f"PIN ke-{i} skornya {skor_pin}, tergolong {kategori_pin}.")

# Rekap kategori PIN
if kategori_pin == "Kuat":
    jumlah_kuat = jumlah_kuat + 1
elif kategori_pin == "Sedang":
    jumlah_sedang = jumlah_sedang + 1
else: 
    jumlah_lemah = jumlah_lemah + 1

print(f"Rekap: Kuat {jumlah_kuat}, Sedang {jumlah_sedang}, Lemah {jumlah_lemah}.")