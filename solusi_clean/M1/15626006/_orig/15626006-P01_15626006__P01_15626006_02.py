# NIM / Nama : 15626006 / Maria Zeysta Kamelia Rumanti
# Tanggal : 30 September 2026
# Deskripsi : Program menghitung konsentrasi larutan kimia. Program ini mengkalkulasi persentase konsentrasi akhir dari pencampuran tiga larutan berdasarkan volume dan konsentrasi masing-masing.
print("Problem 2")

#KAMUS
c1 = float
v1 = float
c2 = float
v2 = float
c3 = float
v3 = float
c_akhir = float

c1 = float(input("Masukkan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukkan volume larutan pertama (ml): "))

c2 = float(input("Masukkan konsentrasi larutan kedua (persen): "))
v2 = float(input("Masukkan volume larutan kedua (ml): "))

c3 = float(input("Masukkan konsentrasi larutan ketiga (persen): "))
v3 = float(input("Masukkan volume larutan ketiga (ml): "))

#Hitung konsentrasi larutan akhir
c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)

print("Konsentrasi akhir dari larutan campuran adalah", c_akhir, "persen")