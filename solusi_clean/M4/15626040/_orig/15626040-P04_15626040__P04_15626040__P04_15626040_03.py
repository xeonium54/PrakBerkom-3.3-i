# NIM/Nama: 15626040/Frizka Yunisaf
# Tanggal: 11 November 2026
# Deskripsi: Memprediksi nilai UAS Tuan KY hasil dari sistem kebut semalam.

def TampilMenu ():
    print ("1. Belajar")
    print ("2. Tidur")
    return

def MintaTindakan ():
    pilihan = int(input("Pilih tindakan (1/2): "))
    while (pilihan !=1 and pilihan !=2):
        pilihan = int(input("Pilihan tidak tersedia! Pilih tindakan (1/2): "))
    return pilihan

def MintaModul ():
    modul= int(input("Pilih modul yang ingin dipelajari (1-4): "))
    while (modul <1  and modul > 4):
        modul = int(input("Modul tidak tersedia! Pilih Modul yang ingin dipelajari (1-4): "))
    return modul  

def BatasDurasi (durasi, waktu, energi):
    batas = waktu
    if (energi / 5 < batas):
        batas = energi / 5
    hasil = durasi
    if (batas < hasil):
        hasil = batas
    return hasil

def EnergiSetelahBelajar (energi, durasi):
    if (durasi*5 >= energi):
        return 0.0
    else:
        return energi - durasi*5

def EnergiSetelahTidur (energi, waktu):
    baru = energi + waktu*12.5
    if (baru > 100):
        baru = 100
    return baru

def Rasio (T,t):
    if (T >= t):
        return 1
    else:
        return T/t

def HitungNilai (T1, t1, T2, t2, T3, t3, T4, t4, energi):
    rata = (Rasio(T1,t1) + Rasio(T2,t2) + Rasio(T3,t3) + Rasio(T4,t4))/4
    return rata*(100*100 - (100-energi)*(100-energi))/100

#Program Utama
waktu = float(input("Masukkan sisa waktu: "))
t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

energi = 100
T1 = 0
T2 = 0
T3 = 0
T4 = 0
selesai = False

while(not selesai):
    TampilMenu()
    pilihan = MintaTindakan()
    if (pilihan == 1):
        modul = MintaModul()
        durasi = float(input("Masukkan durasi belajar: "))
        durasi = BatasDurasi (durasi,waktu,energi)
        energi = EnergiSetelahBelajar (energi,durasi)
        waktu = waktu - durasi
        if (modul == 1):
            T1 += durasi
        elif (modul == 2):
            T2 += durasi
        elif (modul == 3):
            T3 += durasi
        else:
            T4 += durasi

        if (energi == 0):
            print ("Tuan Ky terpaksa tidur karena kehabisan energi.")
            energi = EnergiSetelahTidur(energi,waktu)
            selesai = True
        elif (waktu <= 0):
            selesai = True
    else:
        energi = EnergiSetelahTidur(energi,waktu)
        selesai = True

S = HitungNilai (T1, t1, T2, t2, T3, t3, T4, t4, energi)
if (S == int (S)):
    S = int(S)

print ("Prediksi nilai UAS tang akan didapatkan Tuan Ky adalah " + str(S) + ".")

