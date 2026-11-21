# NIM/Nama               : 15426128/Fathir Sulihansyah 
# Tanggal                : 11 November 2026
# Deskripsi              : Program simulasi Sistem Kebut Semalam (SKS) untuk memprediksi nilai UAS.

# KAMUS KODING
# Spesifikasi Subprogram:
# hitung_prediksi_nilai(t1, t2, t3, t4, d1, d2, d3, d4, energi_akhir) -> float
#   {Menghitung prediksi nilai UAS berdasarkan durasi belajar tiap modul (dibatasi 
#    maksimum sebesar durasi penguasaan modul d_i) dan sisa energi akhir}
#
# Variabel Utama (main):
# sisa_waktu        : int     {Sisa waktu tersisa sebelum UAS dimulai (dalam jam)}
# d1, d2, d3, d4    : int     {Durasi minimum penguasaan modul 1-4}
# t1, t2, t3, t4    : int     {Total durasi belajar yang sudah dialokasikan untuk modul 1-4}
# energi            : float   {Jumlah energi Tuan Ky (maksimal 100)}
# tindakan          : int     {Pilihan menu utama: 1 (Belajar) atau 2 (Tidur)}
# modul             : int     {Pilihan modul belajar (1 sampai 4)}
# durasi_belajar    : float   {Input durasi belajar}
# durasi_int        : int     {Durasi belajar setelah dipotong batasan sisa waktu & energi}
# energi_dibutuhkan : float   {Energi yang diperlukan untuk durasi belajar tertentu}

def hitung_prediksi_nilai(t1, t2, t3, t4, d1, d2, d3, d4, energi_akhir) -> float:
    eff_t1 = t1 if t1 < d1 else d1
    eff_t2 = t2 if t2 < d2 else d2
    eff_t3 = t3 if t3 < d3 else d3
    eff_t4 = t4 if t4 < d4 else d4
    
    rata_rasio = ((eff_t1 / d1) + (eff_t2 / d2) + (eff_t3 / d3) + (eff_t4 / d4)) / 4.0
    faktor_energi = (100.0**2 - (100.0 - energi_akhir)**2) / 100.0
    
    return rata_rasio * faktor_energi

def main():
    sisa_waktu = int(input("Masukkan sisa waktu: "))
    
    d1 = int(input("Masukkan durasi untuk modul ke-1: "))
    d2 = int(input("Masukkan durasi untuk modul ke-2: "))
    d3 = int(input("Masukkan durasi untuk modul ke-3: "))
    d4 = int(input("Masukkan durasi untuk modul ke-4: "))
    
    energi = 100.0
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    
    while sisa_waktu > 0 and energi > 0:
        print("1. Belajar")
        print("2. Tidur")
        
        tindakan = 0
        while tindakan != 1 and tindakan != 2:
            tindakan = int(input("Pilih tindakan (1/2): "))
            if tindakan != 1 and tindakan != 2:
                print("Pilihan tidak tersedia!", end=" ")
                
        if tindakan == 1:
            modul = 0
            while modul < 1 or modul > 4:
                modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
                if modul < 1 or modul > 4:
                    print("Modul tidak tersedia!", end=" ")
                    
            durasi_belajar = float(input("Masukkan durasi belajar: "))
            durasi_int = int(durasi_belajar)
            
            if durasi_int > sisa_waktu:
                durasi_int = sisa_waktu
                
            energi_dibutuhkan = durasi_int * 5.0
            if energi_dibutuhkan > energi:
                durasi_int = int(energi // 5.0)
                energi = 0.0
            else:
                energi -= energi_dibutuhkan
                
            sisa_waktu -= durasi_int
            
            if modul == 1:
                t1 += durasi_int
            elif modul == 2:
                t2 += durasi_int
            elif modul == 3:
                t3 += durasi_int
            elif modul == 4:
                t4 += durasi_int
                
            if energi <= 0 and sisa_waktu > 0:
                print("Tuan Ky terpaksa tidur karena kehabisan energi!")
                energi += sisa_waktu * 12.5
                sisa_waktu = 0
                break
                
        elif tindakan == 2:
            energi += sisa_waktu * 12.5
            sisa_waktu = 0
            break
            
    if energi > 100.0:
        energi = 100.0
        
    prediksi = hitung_prediksi_nilai(t1, t2, t3, t4, d1, d2, d3, d4, energi)
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {prediksi}.")

if __name__ == "__main__":
    main()
