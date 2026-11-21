# NIM/Nama :15626023/Andre Partogi Nathanael Butarbutar
# Tanggal :30/09/2026
# Deskripsi : penggunaan pyhton

a = float(input("Masukkan konsentrasi larutan pertama (persen):"))
b = float(input("Masukkan volume larutan pertama (ml):"))
c = float(input("Masukkan konsentrasi larutan kedua (persen):"))
d = float(input("Masukkan volume larutan kedua (ml):"))
e = float(input("Masukkan konsentrasi larutan ketiga (persen):"))
f = float(input("Masukkan volume larutan ketiga (ml):"))

c_akhir = (a*b + c*d + e*f)/ (b + d + f)

print(f"Konsentrasi akhir larutan campuran adalah:{c_akhir} persen")