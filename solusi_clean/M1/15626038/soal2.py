# NIM/Nama : 15626038/Keysha Hana Putri
# Tanggal : 30 September 2026
# Deskripsi : Program ini digunakan untuk menghitung konsenstrasi akhir dari sebuah larutan campuran yang dibuat dengan mencampurkan tiga larutan yang berbeda.

# KAMUS (maaf saya lupa penulisan kamus bagaimana, saya terlalu fokus pada latihan problem-solving T_T)

#Input
c1 = int(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = int(input("Masukkan volume larutan pertama (ml): "))
c2 = int(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = int(input("Masukkan volume larutan kedua (ml): "))
c3 = int(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = int(input("Masukkan volume larutan ketiga (ml): "))

#Proses
n = c1 * v1 + c2 * v2 + c3 * v3 #Hitung total mol (n) dari penjumlahan masing-masing mol larutan
v = v1 + v2 + v3                #Hitung total volume (v) dari seluruh larutan
M_akhir = n / v                 #Hitung konsentrasi (M) akhir dengan membagi mol (n) dengan volume (v) larutan

#Output
print(f"Konsentrasi akhir larutan campuran adalah {M_akhir} persen")