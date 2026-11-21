
# NIM/Nama : 15626051/ Rafa Davlin Ginting Suka
# Tanggal  : 11 November 2026
# Deskripsi: Prediksi nilai UAS Tuan Ky (Sistem Kebut Semalam)

def pilih_tindakan():
    pilihan = input("Pilih tindakan (1/2): ")
    while pilihan != "1" and pilihan != "2":
        pilihan = input("Pilihan tidak tersedia! Pilih tindakan (1/2): ")
    return pilihan

def pilih_modul():
    modul = input("Pilih modul yang ingin dipelajari (1-4): ")
    while modul not in ["1", "2", "3", "4"]:
        modul = input("Modul tidak tersedia! Pilih modul yang ingin dipelajari (1-4): ")
    return int(modul)

def belajar(T, waktu, energi):
    modul = pilih_modul()
    durasi = float(input("Masukkan durasi belajar: "))
    if durasi > waktu:
        durasi = waktu
    if durasi * 5 >= energi:
        durasi = energi / 5
        energi = 0
    else:
        energi = energi - durasi * 5
    T[modul - 1] = T[modul - 1] + durasi
    waktu = waktu - durasi
    return waktu, energi

def tidur(waktu, energi):
    energi = energi + waktu * 12.5
    if energi > 100:
        energi = 100
    return energi

def hitung_nilai(T, t, energi):
    jumlah = 0
    for i in range(4):
        pakai = T[i]
        if pakai > t[i]:
            pakai = t[i]
        jumlah = jumlah + pakai / t[i]
    rata = jumlah / 4
    pengali = (100 * 100 - (100 - energi) * (100 - energi)) / 100
    return rata * pengali

waktu = float(input("Masukkan sisa waktu: "))
t = []
T = [0, 0, 0, 0]
for i in range(4):
    t.append(float(input("Masukkan durasi untuk modul ke-" + str(i + 1) + ": ")))
energi = 100
selesai = False
while not selesai:
    print("1. Belajar")
    print("2. Tidur")
    pilihan = pilih_tindakan()
    if pilihan == "1":
        waktu, energi = belajar(T, waktu, energi)
        if energi == 0:
            print("Tuan Ky terpaksa tidur karena kehabisan energi!")
            energi = tidur(waktu, energi)
            selesai = True
        elif waktu == 0:
            selesai = True
    else:
        energi = tidur(waktu, energi)
        selesai = True
nilai = hitung_nilai(T, t, energi)
if nilai == int(nilai):
    nilai = int(nilai)
print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah " + str(nilai) + ".")