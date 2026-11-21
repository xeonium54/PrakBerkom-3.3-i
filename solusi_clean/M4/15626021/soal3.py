# Nama/NIM  : Aufaa Fakhri Ibrahim Irahadi / 15626021
# Tanggal   : 11 November 2026
# Deskripsi : Program simulasi Sistem Kebut Semalam (SKS) untuk memprediksi nilai UAS tanpa fungsi min/max bawaan

def hitung_nilai_uas(T1, T2, T3, T4, t1, t2, t3, t4, E):
    """Subprogram untuk menghitung prediksi nilai akhir UAS"""
    # Jika Ti melebih ti, maka nilai Ti dibatasi menjadi ti
    if T1 > t1:
        T1 = t1
    if T2 > t2:
        T2 = t2
    if T3 > t3:
        T3 = t3
    if T4 > t4:
        T3 = t4

    rerata_penguasaan = ((T1/t1) + (T2/t2) + (T3/t3) + (T4/t4)) / 4.0
    faktor_energi =(100.0**2 - (100.0 - E)**2) / 100.0

    S = rerata_penguasaan * faktor_energi
    return S    

def main():
    waktu_tersisa = int(input("Masukkan sisa waktu: "))

    t1 = int(input("Masukkan durasi untuk modul ke-1: "))
    t2 = int(input("Masukkan durasi untuk modul ke-2: "))
    t3 = int(input("Masukkan durasi untuk modul ke-3: "))
    t4 = int(input("Masukkan durasi untuk modul ke-4: "))

    energi = 100.0
    T1 = 0
    T2 = 0
    T3 = 0
    T4 = 0

    habis_energi_paksa = False

    while waktu_tersisa > 0 and energi > 0:
        print("1. Belajar")
        print("2. Tidur")

        tindakan = int(input("Pilih tindakan (1/2): "))
        while tindakan !=1 and tindakan !=2:
            print("Pilihan tidak tersedia!")
            tindakan = int(input("Pilih tindakan (1/2): "))

        if tindakan == 1:
            modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
            while modul < 1 or modul > 4 :
                print("Modul tidak tersedia")
                modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))

            durasi_belajar = float(input("Masukkan durasi belajar: "))

            durasi_int = int(durasi_belajar)

            if durasi_int > waktu_tersisa:
                durasi_int = waktu_tersisa

            energi_diperlukan = durasi_int * 5.0
            if energi_diperlukan > energi:
                durasi_int = int(energi / 5.0)
                energi = 0.0
            else:
                energi -= durasi_int

            waktu_tersisa -= durasi_int

            if modul == 1:
                T1 += durasi_int
            elif modul == 2:
                T2 += durasi_int
            elif modul == 3:
                T3 += durasi_int
            elif modul == 4:
                T4 += durasi_int

            if energi == 0.0 and waktu_tersisa > 0:
                habis_energi_paksa = True
                print("Terpaksa tidur karena kehabisan energi!")
                break

        elif tindakan == 2:
            energi_tambahan = waktu_tersisa * 12.5
            energi += energi_tambahan
            waktu_tersisa = 0
            if energi > 100.0:
                energi = 100.0
            break

    nilai_uas = hitung_nilai_uas(T1, T2, T3, T4, t1, t2, t3, t4, energi)
    print(f"Prediksi nilai UAS yang akan didapatkan adalah {nilai_uas}")

main ()