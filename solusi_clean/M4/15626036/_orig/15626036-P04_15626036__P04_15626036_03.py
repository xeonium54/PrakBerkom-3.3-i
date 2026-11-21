#NIM/Nama: Aghneo Amar Ahsan
#Tanggal: 11 November 2026
#Deskripsi: 

def hitungPrediksi(T1, T2 ,T3, T4, t1, t2, t3, t4, E):
    effT1 = T1 if T1 <= t1 else t1
    effT2 = T2 if T2 <= t2 else t2
    effT3 = T3 if T3 <= t3 else t3
    effT4 = T4 if T4 <= t4 else t4

    ratio = (effT1 / t1 + effT2 / t2 + effT3 / t3 + effT4 / t4) / 4
    energi = (100**2 - (100 - E)**2) / 100
    
    return ratio * energi

def aksiTidur(sisaWaktu, E): 
    E += (sisaWaktu * 12.5)
    if E > 100: 
        E = 100.0
    return E

def aksiBelajar(sisaWaktu, E, T1, T2 ,T3, T4): 
    while True: 
        modul = int(input("Pilih yang ingin dipelajari (1 - 4)"))
        if 1 <= modul <= 4: 
            break
        print("Modul Tidak Tersedia!!!", end=" ")

        durasi = float(input("Masukkan durasi belajar: "))

        durasiAktual = durasi

        if durasiAktual > sisaWaktu: 
            durasiAktual = sisaWaktu

        maxDurasiEnergi = E / 5
        if durasiAktual > maxDurasiEnergi: 
            durasiAktual = maxDurasiEnergi

        E -= (durasiAktual * 5)

        if modul == 1:
            T1 += durasiAktual
        elif modul == 2:
            T2 += durasiAktual
        elif modul == 3:
            T3 += durasiAktual
        elif modul == 4:
            T4 += durasiAktual

        if E == 0 and sisaWaktu > 0: 
            print("Tuan Ky terpaksa tidur karena kehabisan energi!!!")
            sisaWaktu, E = aksiTidur(sisaWaktu, E)

        return sisaWaktu, E, T1, T2 ,T3, T4

sisa_waktu = float(input("Masukkan sisa waktu: "))
t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

E = 100.0
T1, T2, T3, T4 = 0.0, 0.0, 0.0, 0.0

while sisa_waktu > 0:
    print("1. Belajar")
    print("2. Tidur")
    while True:
        pilihan = int(input("Pilih tindakan (1/2): "))
        if pilihan == 1 or pilihan == 2:
            break
        print("Pilihan tidak tersedia!", end=" ")
        
    if pilihan == 1:
        sisa_waktu, E, T1, T2, T3, T4 = aksiBelajar(sisa_waktu, E, T1, T2, T3, T4)
    elif pilihan == 2:
        sisa_waktu, E = aksiTidur(sisa_waktu, E)

nilai_prediksi = hitungPrediksi(T1, T2, T3, T4, t1, t2, t3, t4, E)

if nilai_prediksi == int(nilai_prediksi):
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {int(nilai_prediksi)}.")
else:
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {nilai_prediksi}.")