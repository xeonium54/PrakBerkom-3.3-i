def hitung_belajar(waktu, energi, durasi_req):
    durasi = durasi_req
    
    if durasi > waktu:
        durasi = waktu
        
    energi_butuh = durasi * 5
    if energi_butuh > energi:
        durasi = energi // 5
        energi_sisa = 0
    else:
        energi_sisa = energi - durasi * 5
        
    waktu_sisa = waktu - durasi
    return durasi, waktu_sisa, energi_sisa

def hitung_tidur(waktu, energi):
    energi_tambah = waktu * 12.5
    energi_total = energi + energi_tambah
    if energi_total > 100:
        energi_total = 100
    waktu_sisa = 0
    return waktu_sisa, energi_total

def hitung_nilai(T1, T2, T3, T4, t1, t2, t3, t4, E):
    if T1 > t1:
        T1 = t1
    if T2 > t2:
        T2 = t2
    if T3 > t3:
        T3 = t3
    if T4 > t4:
        T4 = t4
        
    skor_modul = (T1 / t1 + T2 / t2 + T3 / t3 + T4 / t4) / 4
    faktor_energi = (100**2 - (100 - E)**2) / 100
    nilai = skor_modul * faktor_energi
    return nilai

waktu = int(input("Masukkan sisa waktu: "))
t1 = int(input("Masukkan durasi untuk modul ke-1: "))
t2 = int(input("Masukkan durasi untuk modul ke-2: "))
t3 = int(input("Masukkan durasi untuk modul ke-3: "))
t4 = int(input("Masukkan durasi untuk modul ke-4: "))

T1 = 0
T2 = 0
T3 = 0
T4 = 0
energi = 100

while waktu > 0:
    print("1. Belajar")
    print("2. Tidur")
    aksi = int(input("Pilih tindakan (1/2): "))
    while aksi != 1 and aksi != 2:
        aksi = int(input("Pilihan tidak tersedia! Pilih tindakan (1/2): "))
        
    if aksi == 1:
        modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
        while modul < 1 or modul > 4:
            modul = int(input("Pilihan tidak tersedia! Pilih modul yang ingin dipelajari (1-4): "))
            
        durasi_minta = int(input("Masukkan durasi belajar: "))
        durasi_riil, waktu, energi = hitung_belajar(waktu, energi, durasi_minta)
        
        if modul == 1:
            T1 += durasi_riil
        elif modul == 2:
            T2 += durasi_riil
        elif modul == 3:
            T3 += durasi_riil
        elif modul == 4:
            T4 += durasi_riil
            
        if energi == 0:
            waktu, energi = hitung_tidur(waktu, energi)
            break
    else:
        waktu, energi = hitung_tidur(waktu, energi)
        break

nilai_uas = hitung_nilai(T1, T2, T3, T4, t1, t2, t3, t4, energi)

if nilai_uas == int(nilai_uas):
    print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah " + str(int(nilai_uas)) + ".")
else:
    print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah " + str(nilai_uas) + ".")