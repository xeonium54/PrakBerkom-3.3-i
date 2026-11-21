# Nama: Reyza Aulia Rahman
# NIM: 15426131
# Deskripsi: Cek validitas Skor

# s :integer(tempat pemasukan skor)


s = int(input("Masukkan Skor: "))

if s <= 100:
    print("Skor valid , dapat diinput ke sistem.")
else:
    print("Skor tidak valid, perlu diperiksa ulang.")