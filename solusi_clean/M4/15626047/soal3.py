# NIM/Nama  : 15626047/Jeremia Arista Matthew Sugiarto
# Tanggal   : 11 November 2026
# Deskripsi : Program memprediksi nilai UAS berdasarkan aktivitas belajar dan tidur.

# Subprogram untuk menghitung durasi belajar dan energi setelah belajar (tanpa min/max)
def proses_belajar(durasi_input, sisa_waktu, sisa_energi):
    # Dibatasi oleh sisa waktu
    durasi = durasi_input
    if durasi > sisa_waktu:
        durasi = sisa_waktu
    
    # Dibatasi oleh energi yang tersedia (tiap 1 jam butuh 5 energi)
    max_durasi_energi = sisa_energi / 5.0
    
    kehabisan_energi = False
    if durasi >= max_durasi_energi:
        durasi = max_durasi_energi
        sisa_energi = 0.0
        kehabisan_energi = True
    else:
        sisa_energi -= durasi * 5.0

    sisa_waktu -= durasi
    return durasi, sisa_waktu, sisa_energi, kehabisan_energi

# Subprogram untuk menghitung energi setelah tidur
def proses_tidur(sisa_waktu, sisa_energi):
    sisa_energi += sisa_waktu * 12.5
    if sisa_energi > 100.0:
        sisa_energi = 100.0
    return sisa_energi

# Subprogram untuk menghitung prediksi nilai UAS
def hitung_nilai_uas(T1, T2, T3, T4, t1, t2, t3, t4, E):
    # Batasi Ti tidak boleh melebihi ti
    if T1 > t1: T1 = t1
    if T2 > t2: T2 = t2
    if T3 > t3: T3 = t3
    if T4 > t4: T4 = t4

    rasio_modul = (T1/t1 + T2/t2 + T3/t3 + T4/t4) / 4.0
    faktor_energi = (100.0**2 - (100.0 - E)**2) / 100.0
    
    return rasio_modul * faktor_energi

# Algoritma Utama
sisa_waktu = float(input("Masukkan sisa waktu: "))
t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

energi = 100.0
T1, T2, T3, T4 = 0.0, 0.0, 0.0, 0.0

selesai = False

while sisa_waktu > 0 and energi > 0 and not selesai:
    print("1. Belajar")
    print("2. Tidur")
    
    tindakan = input("Pilih tindakan (1/2): ")
    while tindakan != "1" and tindakan != "2":
        tindakan = input("Pilihan tidak tersedia! Pilih tindakan (1/2): ")
        
    if tindakan == "1":
        modul = input("Pilih modul yang ingin dipelajari (1-4): ")
        while modul not in ["1", "2", "3", "4"]:
            modul = input("Modul tidak tersedia! Pilih modul yang ingin dipelajari (1-4): ")
            
        durasi_input = float(input("Masukkan durasi belajar: "))
        
        durasi_real, sisa_waktu, energi, kehabisan = proses_belajar(durasi_input, sisa_waktu, energi)
        
        # Tambahkan ke total waktu modul terkait
        if modul == "1": T1 += durasi_real
        elif modul == "2": T2 += durasi_real
        elif modul == "3": T3 += durasi_real
        elif modul == "4": T4 += durasi_real
        
        if kehabisan:
            print("Tuan Ky terpaksa tidur karena kehabisan energi!")
            energi = proses_tidur(sisa_waktu, energi)
            sisa_waktu = 0
            selesai = True
            
    elif tindakan == "2":
        energi = proses_tidur(sisa_waktu, energi)
        sisa_waktu = 0
        selesai = True

nilai_akhir = hitung_nilai_uas(T1, T2, T3, T4, t1, t2, t3, t4, energi)

# Menampilkan output nilai (tanpa desimal jika bernilai bulat pas seperti test case 1)
if nilai_akhir == int(nilai_akhir):
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {int(nilai_akhir)}.")
else:
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {nilai_akhir}.")