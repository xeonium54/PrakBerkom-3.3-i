# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 11 November 2026
# Deskripsi : 

def hitung_prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E):
# Kamus Lokal
    # t1 (float)
    # t2 (float)
    # t3 (float)
    # t4 (float)
    # T1 (float)
    # T2 (float)
    # T3 (float)
    # T4 (float)
    # E (float)
    # eff1 (float)
    # eff2 (float)
    # eff3 (float)
    # eff4 (float)
    # ratarata (float)
    # faktor_energi (float)
    # skor (float)          

    # Algoritma

    # Membatasi Ti supaya tidak melebihi ti
    eff1 = T1
    if eff1 > t1:
        eff1 = t1
    eff2 = T2
    if eff2 > t2:
        eff2 = t2
    eff3 = T3
    if eff3 > t3:
        eff3 = t3
    eff4 = T4
    if eff4 > t4:
        eff4 = t4
    
    ratarata = ((eff1 / t1) + (eff2 / t2) + (eff3 / t3) + (eff4 / t4)) / 4.0
    faktor_energi = (100.0 * 100.0 - (100.0 - E) * (100.0 - E)) / 100.0
    skor = ratarata * faktor_energi
    return skor

# Subprogram untuk tindakan Belajar
def proses_belajar(N, E, t1, t2, t3, t4, T1, T2, T3, T4):
    # Kamus Lokal:
    # N (float)
    # E (float)
    # t1 (float)
    # t2 (float)
    # t3 (float)
    # t4 (float)
    # T1 (float)
    # T2 (float)
    # T3 (float)
    # T4 (float)
    # modul (int)
    # durasi (float)
    # max_durasi_energi (float)
    # N_baru (float)
    # E_baru (float)
    # terpaksa_tidur (bool)

    # Algoritma
    modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
    while modul < 1 or modul > 4:
        modul = int(input("Modul tidak tersedia! Pilih modul yang ingin dipelajari (1-4): "))
    
    durasi = float(input("Masukkan durasi belajar: "))
    
    # Batasan durasi oleh sisa waktu N (
    if durasi > N:
        durasi = N
        
    # Batasan durasi oleh energi E (tiap 1 jam butuh 5 energi)
    max_durasi_energi = E / 5.0
    if durasi > max_durasi_energi:
        durasi = max_durasi_energi
        
    N_baru = N - durasi
    E_baru = E - (durasi * 5.0)
    
    if modul == 1:
        T1 += durasi
    elif modul == 2:
        T2 += durasi
    elif modul == 3:
        T3 += durasi
    elif modul == 4:
        T4 += durasi
        
    terpaksa_tidur = False
    if E_baru <= 0.0:
        E_baru = 0.0
        print("Tuan Ky terpaksa tidur karena kehabisan energi!")
        terpaksa_tidur = True
        N_baru = 0.0
        
    return N_baru, E_baru, T1, T2, T3, T4, terpaksa_tidur

# Subprogram untuk tindakan Tidur
def proses_tidur(N, E):
    # Kamus Lokal:
    # N (float)
    # E (float)
    # M (float)
    # E_baru (float)
    # N_baru (float)

    # Algoritma
    M = N
    E_baru = E + (M * 12.5)
    if E_baru > 100.0:
        E_baru = 100.0
    N_baru = 0.0
    return N_baru, E_baru

# Algoritma program Utama
N = float(input("Masukkan sisa waktu: "))
t1 = float(input("Masukkan durasi untuk modul ke-1: "))
t2 = float(input("Masukkan durasi untuk modul ke-2: "))
t3 = float(input("Masukkan durasi untuk modul ke-3: "))
t4 = float(input("Masukkan durasi untuk modul ke-4: "))

T1 = 0.0
T2 = 0.0
T3 = 0.0
T4 = 0.0
E = 100.0

berjalan = True
while berjalan and N > 0.0 and E > 0.0:
    print("1. Belajar")
    print("2. Tidur")
    tindakan = int(input("Pilih tindakan (1/2): "))
    while tindakan != 1 and tindakan != 2:
        tindakan = int(input("Pilihan tidak tersedia! Pilih tindakan (1/2): "))
        
    if tindakan == 1:
        N, E, T1, T2, T3, T4, terpaksa = proses_belajar(N, E, t1, t2, t3, t4, T1, T2, T3, T4)
        if terpaksa:
            berjalan = False
    elif tindakan == 2:
        N, E = proses_tidur(N, E)
        berjalan = False

skor_akhir = hitung_prediksi(t1, t2, t3, t4, T1, T2, T3, T4, E)
print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {skor_akhir}")

