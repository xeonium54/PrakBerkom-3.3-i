#NIM/Nama: 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal: 30 September 2026
#Deskripsi: Menghitung Konsentrasi akhir larutan campuran milik Pak Mik

#judul
print("-"*50)
Judul = "Konsentrasi akhir larutan campuran Pak Mik"
print(Judul.center(50))
print("-"*50)

#Variabel Konsentrasi dan volume larutan pertama
C1 = int(input("Masukkan konsentrasi larutan pertama (persen): "))
V1 = int(input("Masukkan volume larutan pertama (ml): "))

#Variabel konsentrasi dan volume larutan kedua
C2 = int(input("Masukkan konsentrasi larutan kedua (persen): "))
V2 = int(input("Masukkan volume larutan kedua (ml): "))

#Variabel konsentrasi dan volume larutan ketiga
C3 = int(input("Masukkan konsentrasi larutan ketiga (persen): "))
V3 = int(input("Masukkan volume larutan ketiga (ml): "))

#rumus akhir
C_akhir = (((C1 * V1) + (C2 * V2) + (C3 * V3)) / (V1 + V2 + V3))

print(f"Konsentrasi akhir larutan campuran adalah {C_akhir}")