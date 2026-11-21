# NIM/Nama : 15626044/Saliha Mahira Al-kwarismy
# Tanggal : 11 November
# Deskripsi : P04_15626044_Problem2

# Fungsi pertama (perbaikan indentasi, return, dan logika di dalam fungsi)
def cek_pin(pin):
    skor = 0
    jumlah_digit = 0
    
    # Pin angka
    for c in pin:
        if c in "0123456789":
            jumlah_digit = jumlah_digit + 1
    skor = jumlah_digit * 4

    # Pin huruf (memperbaiki typo pada alfabet)
    for c in pin:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            skor = skor + 10
            break

    # Panjang pin
    panjang = 0
    for c in pin:
        panjang = panjang + 1

    if panjang >= 8:
        skor = skor + 15
    elif panjang >= 6:
        skor = skor + 5

    # Penalti saat mudah ditebak (memperbaiki pin(i) menjadi pin[i])
    for i in range(panjang - 1):
        angka = pin[i]
        setelah_angka = pin[i+1]
        if angka in "0123456789" and setelah_angka in "0123456789":
            angka_kiri = int(angka)
            angka_kanan = int(setelah_angka)
            if angka_kiri + 1 == angka_kanan:
                skor = skor - 5
            elif angka_kiri - 1 == angka_kanan:
                skor = skor - 5

    # Menentukan kategori kuat, sedang, atau lemah
    if skor >= 40:
        hasil_analisis = "Kuat"
    elif skor >= 20:
        hasil_analisis = "Sedang"
    else: 
        hasil_analisis = "Lemah"
        
    return skor, hasil_analisis

# --- PROGRAM UTAMA ---

# Variabel awal rekap
Kuat = 0
Sedang = 0
Lemah = 0

# Masukkan input berupa jumlah kandidat (disimpan ke variabel N)
N = int(input("Masukkan jumlah kandidat PIN (N): "))

# Pengulangan (loop) sebanyak N kali
for i in range(1, N + 1):
    # Menggunakan input() agar menerima string, bukan int(f"...") yang error
    kandidat = input(f"Kandidat PIN ke-{i}: ")

    skor, hasil_analisis = cek_pin(kandidat)
    print(f"PIN ke-{i} skornya {skor}, tergolong {hasil_analisis}")

    if hasil_analisis == "Kuat":
        Kuat = Kuat + 1
    elif hasil_analisis == "Sedang":
        Sedang = Sedang + 1
    else:
        Lemah = Lemah + 1

print(f"Rekap: Kuat {Kuat}, Sedang {Sedang}, Lemah {Lemah}")