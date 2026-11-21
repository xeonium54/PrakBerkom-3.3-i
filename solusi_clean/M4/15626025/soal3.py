# NIM/Nama: 15626025/Maria Amatussyafee Nurjaman
# Tanggal: 11/11/2026
# Deskripsi: Prediksi nilai UAS

# KAMUS 
# waktu : float
#

def belajar(modul, durasi, waktu, energi, T):
    if durasi > waktu:
        durasi = waktu
    if durasi * 5 > energi:
        durasi = energi / 5
    else:
        energi = energi - durasi * 5
    T[modul - 1] = T[modul - 1] + durasi 
    return waktu - durasi, energi

def tidur(waktu, energi):
    energi = energi + waktu * 12.5
    if energi > 100:
        energi = 100
    return 0, energi

def prediksi(T, t, energi):
    jumlah = 0 
    for i in range(4):
        if T[i] > t[i]:
            T[i] = t[i]
        jumlah = jumlah + T[i] / t[i] 
    return jumlah / 4 * (100 * 100 - (100 - energi) ** 2) / 100


energi = 100
T = []
t = []
waktu = float(input("Masukan sisa waktu: "))
for i in range(1, 5):
    t.append (float(input("Masukan durasi untuk modul ke-" + str(i) + ": ")))
    
while waktu > 0: 
    print("1. Belajar")
    print("2. Tidur")
    pilihan = int(input("Pilih tindakan (1/2): "))
    while pilihan != 1 and pilihan != 2:
            pilihan = int(input("Pilihan tidak tersedia! Pilih tindakan (1/2): "))

    if pilihan == 1: 
        modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
        while modul <1 or modul > 4:
            modul = int(input("Modul tidak tersedia! Pilih modul yang ingin dipelajari: "))
        durasi = float(input("Masukan durasi belajar: "))
        waktu, energi = belajar(modul, durasi, waktu, energi, T)
        if energi == 0 and waktu > 0:
            print("Tuan Ky terpaksa tidur karena kehabisan energi!")
            waktu, energi = tidur(waktu, energi)
    else:
         waktu, energi = tidur(waktu, energi)

print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah " + "%g" % prediksi(T, t, energi) + ".")