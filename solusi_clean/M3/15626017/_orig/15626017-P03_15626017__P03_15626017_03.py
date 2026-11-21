# NIM/Nama      : 15626017 / Naura Vira Vania Ramadhani 
# Berpikir Komputasional ITB
# Tanggal       : 28 Oktober 2026
# Deskripsi     : Program menghitung total volume genangan air hujan di kebun kaktus
#                 menggunakan array tanpa fungsi max/min bawaan.

# Meminta masukan panjang kebun dan array ketinggian tanah 
panjang_kebun = int(input("Masukkan panjang kebun: "))
batas_toleransi = int(input("Masukkan batas toleransi air: "))

# Membuat array kosong untuk menampung ketinggian tanah
H = []

# Memasukkan elemen array satu per satu menggunakan perulangan
for i in range(panjang_kebun):
    tinggi = int(input(f"Masukkan ketinggian tanah titik ke-{i+1}: "))
    H.append(tinggi)

N = len(H)
total_genangan = 0

# Perhitungan genangan air jika panjang kebun lebih dari 2
if N > 2:
    # Membuat array untuk menyimpan tinggi maksimum di kiri dan kanan
    left_max = [0] * N
    right_max = [0] * N
    
    # Mencari tinggi maksimum di sebelah kiri secara manual
    max_kiri = H[0]
    for i in range(N):
        if H[i] > max_kiri:
            max_kiri = H[i]
        left_max[i] = max_kiri
        
    # Mencari tinggi maksimum di sebelah kanan secara manual
    max_kanan = H[N - 1]
    for i in range(N - 1, -1, -1):
        if H[i] > max_kanan:
            max_kanan = H[i]
        right_max[i] = max_kanan
        
    # Menghitung volume genangan air di setiap titik (dari indeks 1 sampai N-2)
    for i in range(1, N - 1):
        # Menentukan dinding terpendek antara kiri dan kanan secara manual (tanpa min())
        dinding_pendek = left_max[i]
        if right_max[i] < dinding_pendek:
            dinding_pendek = right_max[i]
            
        # Hitung genangan air
        genangan_titik = dinding_pendek - H[i]
        if genangan_titik > 0:
            total_genangan += genangan_titik

# Menampilkan hasil
print(f"Total volume genangan air adalah {total_genangan}.")

if total_genangan > batas_toleransi:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")