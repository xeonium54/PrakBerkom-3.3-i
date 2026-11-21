# NIM/Nama: Maria Amatussyafee Nurjaman
# Tanggal: 14/10/2026
# Deskripsi: Program validasi skor

# KAMUS
# s : integer

s = int(input("Masukan skor: "))

if (s >= 0 and s <= 100):
    print("Skor valid, dapat diinput ke sistem")
else:
    print("Skor tidak valid, perlu diperiksa ulang")
    