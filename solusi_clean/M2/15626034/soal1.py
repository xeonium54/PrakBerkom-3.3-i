#NIM/NAMA : 15626034/Ahmad Zaky 
#Tanggal : 14/10/2026
#Deskripsi : Program otomatisasi validasi skor

#kamus
    #skor : integer

skor = int(input("Masukkan skor: "))
if skor < 0 or skor > 100:
    print("Skor tidak valid, perlu di periksa ulang")
else:
    print("Skor valid, dapat di input ke sistem")

