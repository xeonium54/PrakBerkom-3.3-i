#NIM/Nama: 15426126/Zhahiran Kayyis Mushaliyyah
#Tanggal: 30 September 2026
#Deskripsi: Problem 2

c1 = float(input("Masukkan konsentrasi larutan pertama (persen):"))
v1 = float(input("Masukkan volume larutan pertama (ml):"))

c2 = float(input("Masukkan konsentrasi larutan kedua (persen):"))
v2 = float(input("Masukkan volume larutan kedua (ml):"))

c3 = float(input("Masukkan konsentrasi larutan ketiga (persen):"))
v3 = float(input("Masukkan volume larutan ketiga (ml):"))

konsentrasi_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)
print("Konsentrasi akhir larutan campuran adalah", konsentrasi_akhir, "persen")