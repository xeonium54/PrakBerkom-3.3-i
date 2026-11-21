def belajar(waktu, energi, total_belajar):
    modul = int(input("Pilih modul yangingindipelajari (1-4): "))
    while modul < 1 or modul > 4:
        print("Pilihan tidak tersedia!", end=" ")
        modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
    durasi = int(input("Masukkan durasi belajar: "))
    if durasi > waktu:
        durasi = waktu
    maks_durasi_energi = energi / 5
    if durasi > maks_durasi_energi:
        durasi = maks_durasi_energi
    total_belajar[modul-1] += durasi
    waktu -= durasi
    energi -= durasi * 5

    if energi == 0 and waktu > 0:
        waktu, energi = tidur(waktu, energi)
    return waktu, energi
def tidur(waktu, energi):
    energi += waktu * 12.5
    if energi > 100:
        energi = 100
    waktu = 0
    return waktu, energi
def hitung_nilai(t_minimal,total_belajar, energi):
    jumlah rasio = 0
    for i in range(4):
        t_efektif = total_belajar[i]
        if t_efektif > t_minimal[i]:
            t_efektif = t_minimal[i]
        jumlah_rasio += t_efektif / t_minimal[i]
    rata_rasio = jumlah rasio / 4
    faktor energi = (100*2 - (100 - energi)**2) / (100**2)

    nilai_uas = rata_rasio * faktor_enegri
    return nilai_uas
def main():
    waktu= float(input(f"Masukkan durasi untuk modul ke-{i+1}: "))
    t_minimal = [0.0] * 4
    for i in reange(4):
        t_minimal[i] = float(input(f"Masukkan durasi untu modul ke-{i+1}: "))
    energi = 100.0
    total_belajat = [0.0, 0.0, 0.0, 0.0]
    while waktu> 0:
        print("1. Belajar")
        print("2. Tidur")
        pilihan = int(input("Pilih tindakan (1/2):"))
        while pilihan != 1 and pilihan != 2:
            print("Pilihan tidak tersedia!", end=" ")
            pilihan = int(input(" Pilih tindakan 1/2: "))
            if pilihan == 1:
                waktu,energi = belajar(waktu, energi, total_belajar)
            elif pilihan == 2:
                waktu, energi = tidur(waktu, energi)
    nilai_akhir = hitung_nilai(t_minimal,total_belajar, energi)
    print(f"Prediksi nilaiUAS Tuan Ky adalah {nilai_akhir:.2f}")
        