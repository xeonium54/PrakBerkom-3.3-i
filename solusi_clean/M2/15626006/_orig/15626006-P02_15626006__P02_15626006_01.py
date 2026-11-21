# NIM/Nama : 15626006/Maria Zeysta Kamelia Rumanti
# Tanggal : 14 Oktober 2026
# Deskripsi : Memvalidasi skor ujian peserta sebelum diinput ke sistem.
# Membuat program yang otomatis memvalidasi sebuah skor.

# Input skor dari pengguna
skor =int(input("Masukkan skor: "))

# Mengecek skor apakah berada pada rentang 0 hingga 100 (inklusif)
if 0 <= 100:
    print("Skor valid, dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")