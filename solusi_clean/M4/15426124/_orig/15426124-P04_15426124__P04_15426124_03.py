# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 11 November 2026
# Deskripsi : Program simulasi belajar dan tidur (Sistem Kebut Semalam) menjelang UAS.

# Subprogram untuk menghitung prediksi nilai UAS
def hitung_prediksi_nilai(t1, t2, t3, t4, req1, req2, req3, req4, energi_akhir):
    # Membatasi T_i agar tidak melebihi t_i
    eff1 = t1 if t1 < req1 else req1
    eff2 = t2 if t2 < req2 else req2
    eff3 = t3 if t3 < req3 else req3
    eff4 = t4 if t4 < req4 else req4
    
    rata_rasio = (eff1 / req1 + eff2 / req2 + eff3 / req3 + eff4 / req4) / 4.0
    
    # Komponen energi
    e_term = (100.0 * 100.0 - (100.0 - energi_akhir) * (100.0 - energi_akhir)) / 100.0
    
    nilai = rata_rasio * e_term
    return nilai

def main():
    waktu_sisa = int(input("Masukkan sisa waktu: "))
    
    # Durasi minimum penguasaan modul
    t_min1 = int(input("Masukkan durasi untuk modul ke-1: "))
    t_min2 = int(input("Masukkan durasi untuk modul ke-2: "))
    t_min3 = int(input("Masukkan durasi untuk modul ke-3: "))
    t_min4 = int(input("Masukkan durasi untuk modul ke-4: "))
    
    energi = 100.0
    t_belajar1 = 0.0
    t_belajar2 = 0.0
    t_belajar3 = 0.0
    t_belajar4 = 0.0
    
    # Simulasi aksi sampai waktu habis atau energi habis
    while waktu_sisa > 0 and energi > 0:
        print("1. Belajar")
        print("2. Tidur")
        
        # Validasi pilihan tindakan
        tindakan = int(input("Pilih tindakan (1/2): "))
        while tindakan != 1 and tindakan != 2:
            print("Pilihan tidak tersedia!")
            tindakan = int(input("Pilih tindakan (1/2): "))
            
        if tindakan == 1:
            # Validasi pilihan modul
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
            while modul < 1 or modul > 4:
                print("Modul tidak tersedia!")
                modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
                
            durasi_belajar = float(input("Masukkan durasi belajar: "))
            
            # Cek batasan waktu dan energi
            if durasi_belajar > waktu_sisa:
                durasi_belajar = float(waktu_sisa)
                
            energi_dibutuhkan = durasi_belajar * 5.0
            if energi_dibutuhkan > energi:
                durasi_belajar = energi / 5.0
                energi = 0.0
            else:
                energi -= energi_dibutuhkan
                
            waktu_sisa -= durasi_belajar
            
            # Akumulasi durasi modul
            if modul == 1:
                t_belajar1 += durasi_belajar
            elif modul == 2:
                t_belajar2 += durasi_belajar
            elif modul == 3:
                t_belajar3 += durasi_belajar
            elif modul == 4:
                t_belajar4 += durasi_belajar
                
            if energi == 0.0 and waktu_sisa > 0:
                print("Tuan Ky terpaksa tidur karena kehabisan energi!")
                break
                
        elif tindakan == 2:
            # Tidur selama sisa waktu
            energi_tambahan = waktu_sisa * 12.5
            energi += energi_tambahan
            if energi > 100.0:
                energi = 100.0
            waktu_sisa = 0 # Waktu habis karena tidur sampai UAS
            break

    # Hitung dan tampilkan hasil akhir prediksi nilai
    nilai_uas = hitung_prediksi_nilai(t_belajar1, t_belajar2, t_belajar3, t_belajar4, 
                                     t_min1, t_min2, t_min3, t_min4, energi)
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {nilai_uas}.")

if __name__ == "__main__":
    main()