# NIM/Nama : 15626005/Addien Maulana Bima
# Tanggal : 30 September 2026
# Deskripsi : Uprak 01_Menghitung konsentrasi akhir larutan

c1 = float(input("Masukkan konsentrasi larutan pertama : "))
v1 = float(input("Masukkan volume larutan pertama : "))
c2 = float(input("Masukkan konsentrasi larutan kedua : "))
v2 = float(input("Masukkan volume larutan kedua : "))
c3 = float(input("Masukkan konsentrasi larutan ketiga : "))
v3 = float(input("Masukkan volume larutan ketiga : "))

langkah_pertama = c1*v1+c2*v2+c3*v3
langkah_kedua = v1+v2+v3
konsentrasi_akhir = langkah_pertama/langkah_kedua

print(f"konsentrasi akhir larutan adalah : {konsentrasi_akhir} persen")

