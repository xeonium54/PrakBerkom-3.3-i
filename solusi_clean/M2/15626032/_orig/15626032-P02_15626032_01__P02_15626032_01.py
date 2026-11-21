# NIM/Nama : 15626032/Muhamad Faiz Abdul Aziz
# Tanggal : 14 Oktober 2026
# Deskripsi : Memvalidasi skor ujian

S = int(input("Masukan skor: "))

if (S > 100):
    print(str(S) + " Skor tidak valid, perlu di periksa ulang")
else: # S <= 0
    print(str(S) + " Skor valid, dapat diinput ke sistem")