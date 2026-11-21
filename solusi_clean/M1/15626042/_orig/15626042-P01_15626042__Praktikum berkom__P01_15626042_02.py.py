#NIM/Nama   :Febrian Yafi Hakim 15626042 
#Tanggal    :30 September 2026
#Deskripsi  :Menghitung konsentrasi akhir campuran 3 buah larutan

#Disclaimer saya belum tau bagaimana format penulisan kamus yang baik dan benar...

#Input
#Masih sama menggunakan float(input) untuk memasukan data/angka dan menjadikan c dan v sebagai variabel konsentrasi dan larutan
c1 = float(input("Masukan konsentrasi larutan pertama (persen): "))
v1 = float(input("Masukan volume larutan pertama(ml): "))

c2 = float(input("Masukan konsentrasi larutan kedua (persen): "))
v2 = float(input("Masukan volume larutan kedua(ml): "))

c3 = float(input("Masukan konsentrasi larutan ketiga (persen): "))
v3 = float(input("Masukan volume larutan ketiga(ml): "))

#Proses
#menggunakan c_akhir sebagai variabel rumus untuk menghitung konsentrasi dan larutan
c_akhir = (c1 * v1 + c2 * v2 + c3 * v3) / (v1 + v2 + v3)

#Output
#untuk menampilkan hasil perhitungan
print(f"konsentrasi akhir larutan campuran adalah {c_akhir:} persen")