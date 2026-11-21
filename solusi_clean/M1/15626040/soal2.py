# NIM/Nama: 15626040/Frizka Emily Yunisaf
# Tanggal: 30 September 2026
# Deskripsi: Menghitung konsentrasi akhir larutan

C1 = int(input("Masukkan konsentrasi larutan pertama (persen): "))
V1 = int(input("Masukkan volume larutan pertama (ml): "))
C2 = int(input("Masukkan konsentrasi larutan kedua (persen): "))
V2 = int(input("Masukkan volume larutan kedua (ml): "))
C3 = int(input("Masukkan konsentrasi larutan ketiga (persen): "))
V3 = int(input("Masukkan volume larutan ketiga (ml): "))

C_akhir = ((C1*V1)+(C2*V2)+(C3*V3))/(V1+V2+V3)
print("Konsentrasi akhir larutan campuran adalah ",C_akhir,"persen")
