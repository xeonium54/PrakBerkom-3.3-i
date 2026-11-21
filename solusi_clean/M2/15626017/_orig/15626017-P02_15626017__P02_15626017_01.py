# NIM/Nama : 15626017 / Naura Vira Vania Ramadhani 
# Tanggal : 14 Oktober 2026
# Deskripsi : Program untuk memvalidasi apakah skpor ujian berada pada rentang 0 hingga 100 

# Membaca masukan skor dari use
skor = int(input("Masukkan skor:"))

# Membaca pengecekan validitas skor 
if 0 <= skor <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")