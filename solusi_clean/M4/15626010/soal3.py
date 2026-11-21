# NIM/Nama : 15626010/Faiz Abdurrahman
# Tanggal : 11 November 2026
# Deskripsi : program ini mensimulasikan manajemen waktu belajar sistem kebut semalam untuk 4 modul kuliah Tuan Ky beserta manajemen energi dan perhitungan prediksi nilai ujian akhir (UAS).

def hitung_nilai_uas(t_belajar, t_min, e_akhir):
    t_efektif = []
    for i in range(4):
        # Jika T melebihi t_i, maka T dibatasi menjadi t_i
        if t_belajar[i] > t_min[i]:
            t_efektif.append(t_min[i])
        else:
            t_efektif.append(t_belajar[i])

    term1=((t_efektif[0] / t_min[0])+(t_efektif[1]/t_min[1])+(t_efektif[2]/t_min[2])+(t_efektif[3]/t_min[3]))/4.0

    term2=(100.0*((100.0- e_akhir) **2))/100.0
    return term1*term2

def main ():
    energi= 100.0
    sisa_waktu = float(input("Masukkan sisa waktu: "))

    durasi_min=[]
    for i in range (1,5):
        d_min = float(input(f"Masukkan  durasi untuk modul ke-{i}: "))
        durasi_min.append(d_min)

    durasi_belajar = [0.0,0.0,0.0,0.0]

    habis_energi_paksa = False

    while sisa_waktu > 0 :
        # validasi pilihan tindakan 1 atau 2
        while True:
            print("1. Belajar")
            print("2. Tidur")
            pilihan_tindakan = int(input("Pilih tindakan (1/2): "))
            if pilihan_tindakan == 1 or pilihan_tindakan == 2:
                break
            print("Pilihan tidak tersedia! Pilih tindakan (1/2):", end=" ")

        if pilihan_tindakan == 1:
            # validasi modul 1 sampai 4
            while True:
                pilihan_modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
                if 1 <= pilihan_modul <= 4:
                    break
            print("Modul tidak tersedia! Pilih modul yang ingin dipelajar (1-4):", end=" ")

            durasi = float(input("Masukkan durasi belajar: "))

            # Batasan sisa waktu
            if durasi > sisa_waktu:
                durasi = sisa_waktu

            # cek energi
            energi_dibutuhkan = durasi*5.0
            if energi_dibutuhkan > energi:
                durasi = energi / 5.0
                energi = 0.0
                sisa_waktu -= durasi
                durasi_belajar[pilihan_modul - 1]+= durasi
                print("Tuan Ky terpaksa tidur karena kehabisan energi!")
                habis_energi_paksa = True
                break
            else:
                energi -= energi_dibutuhkan
                sisa_waktu -= durasi
                durasi_belajar[pilihan_modul -1] += durasi

            if energi == 0.0:
                break
        elif pilihan_tindakan == 2:
            M = sisa_waktu
            sisa_waktu = 0.0
            energi += M*12.5
            if energi > 100.0:
                energi=100.0
            break

    skor_uas = hitung_nilai_uas(durasi_belajar, durasi_min, energi)
    print (f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah{skor_uas}.")

if __name__ == "__main__":
    main()