# NIM/Nama       : B15626017/Naura Vira Vania Ramadhani 
# Tanggal        : 11 November 2026
# Deskripsi      : Simulasi belajar dan tidur untuk memprediksi nilai UAS Tuan Ky

def hitung_prediksi_nilai(t1, t2, t3, t4, req1, req2, req3, req4, energi_akhir):
    # Batasi T_i maksimal sebesar t_i
    effective_t1 = t1 if t1 < req1 else req1
    effective_t2 = t2 if t2 < req2 else req2
    effective_t3 = t3 if t3 < req3 else req3
    effective_t4 = t4 if t4 < req4 else req4
    
    rasio_penguasaan = (effective_t1 / req1 + effective_t2 / req2 + effective_t3 / req3 + effective_t4 / req4) / 4.0
    faktor_energi = (100.0**2 - (100.0 - energi_akhir)**2) / 100.0
    
    return rasio_penguasaan * faktor_energi

def main():
    sisa_waktu = int(input("Masukkan sisa waktu: "))
    t1_req = int(input("Masukkan durasi untuk modul ke-1: "))
    t2_req = int(input("Masukkan durasi untuk modul ke-2: "))
    t3_req = int(input("Masukkan durasi untuk modul ke-3: "))
    t4_req = int(input("Masukkan durasi untuk modul ke-4: "))
    
    energi = 100.0
    t1_aktual = 0
    t2_aktual = 0
    t3_aktual = 0
    t4_aktual = 0
    
    sedang_belajar = True
    while sisa_waktu > 0 and energi > 0 and sedang_belajar:
        print("1. Belajar")
        print("2. Tidur")
        
        tindakan = int(input("Pilih tindakan (1/2): "))
        while tindakan != 1 and tindakan != 2:
            print("Pilihan tidak tersedia!", end=" ")
            tindakan = int(input("Pilih tindakan (1/2): "))
            
        if tindakan == 1:
            # Validasi pilihan modul
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
            while modul < 1 or modul > 4:
                print("Modul tidak tersedia!", end=" ")
                modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
                
            durasi_belajar = float(input("Masukkan durasi belajar: "))
            
            if durasi_belajar > sisa_waktu:
                durasi_belajar = float(sisa_waktu)
                
            energi_dibutuhkan = durasi_belajar * 5.0
            if energi_dibutuhkan > energi:
                # Durasi dipotong hingga batas maksimal energi yang tersisa
                durasi_belajar = energi / 5.0
                energi = 0.0
                print("Tuan Ky terpaksa tidur karena kehabisan energi!")
                sedang_belajar = False
            else:
                energi -= energi_dibutuhkan
                
            sisa_waktu -= int(durasi_belajar)
            
            if modul == 1:
                t1_aktual += durasi_belajar
            elif modul == 2:
                t2_aktual += durasi_belajar
            elif modul == 3:
                t3_aktual += durasi_belajar
            elif modul == 4:
                t4_aktual += durasi_belajar
            
            if energi <= 0.0:
                energi = 0.0
                sedang_belajar = False
                
        elif tindakan == 2:
            # Tidur hingga waktu habis
            energi += sisa_waktu * 12.5
            if energi > 100.0:
                energi = 100.0
            sisa_waktu = 0
            sedang_belajar = False
            
    
    prediksi_nilai = hitung_prediksi_nilai(
        t1_aktual, t2_aktual, t3_aktual, t4_aktual,
        t1_req, t2_req, t3_req, t4_req,
        energi
    )
    
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {prediksi_nilai}.")

if __name__ == "__main__":
    main()