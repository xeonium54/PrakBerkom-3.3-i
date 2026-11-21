# NIM/Nama :15626023/Andre Partogi Nathanael Butarbutar
# Tanggal :11/11/2026
# Deskripsi :Menyederhanakan Aspek Rasio melalui fpb

def fpb(a, b):
    while (b != 0):
        sisa = a % b
        a = b
        b = sisa
    return a

#program utama
#pakai int karena ukuran piksel selalu bilangan bulat

lebar = int(input("Masukkan lebar foto (piksel):"))
tinggi = int(input("Masukkan tinggi foto (piksel):"))


faktor = fpb(lebar , tinggi)

#dibagi fpb agar rasio bisa menjadi lebih sederhana
# pakai // agar  hasilnya tidak .0
rasio_lebar = lebar // faktor
rasio_tinggi = tinggi // faktor

print("Aspect ratio disederhanakan menjadi " + str(rasio_lebar) + ":" + str(rasio_tinggi))
            


