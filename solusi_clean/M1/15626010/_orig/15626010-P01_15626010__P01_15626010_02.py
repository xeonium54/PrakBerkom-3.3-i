# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 30/09/2026
# Deskripsi : berfungsi untuk menghitung konsentrasi akhir dari 3 jenis campuran larutan pakai rumus rata-rata dan menampilkan hasilnya dengan 1 angka di belakang desimal.

#input larutan pertama
c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukkan Volume larutan pertama (ml): "))

#input larutan kedua
c2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = float(input("Masukkan volume larutan kedua (ml): "))

#input larutan ketiga
c3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = float(input("Masukkan volume larutan ketiga (ml): "))

#hitung konsentrasi akhir pakai rumus campuran
c_akhir = ((c1*v1)+(c2*v2)+(c3*v3))/(v1+v2+v3)

#menampilkan hasil konsentrasi akhir
print(f"Konsentrasi akhir larutan campuran adalah {c_akhir:.1f} persen")