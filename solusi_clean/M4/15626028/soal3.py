"""Problem 3"""

# Program Prediksi Nilai UAS Tuan Ky

# Subprogram 1 (Fungsi): Tindakan Tidur
def tindakan_tidur(sisa_waktu, energi):
    energi = energi + (sisa_waktu * 12.5)

    if energi > 100:
        energi = 100
    return energi

# Subprogram 2 (Fungsi): Tindakan Belajar
def tindakan_belajar(sisa_waktu, energi, total_belajar):
    modul = int(input("Pilih modul yang ingin dipelajari (1-4): "))
    while modul < 1 or modul > 4:
        modul = int(input("Pilihan modul tidak tersedia! Pilih modul yang ingin dipelajari (1-4): "))

    durasi = float(input("Masukkan durasi belajar: "))


    if durasi > sisa_waktu:
        durasi = sisa_waktu


    maks_durasi_energi = energi / 5.0
    if durasi >= maks_durasi_energi:
        durasi = maks_durasi_energi
        energi = 0
    else:
        energi = energi - (durasi * 5)

    total_belajar[modul - 1] += durasi
    sisa_waktu -= durasi


    if energi == 0 and sisa_waktu > 0:
        print("Tuan Ky terpaksa tidur karena kehabisan energi!")
        energi = tindakan_tidur(sisa_waktu, energi)
        sisa_waktu = 0

    return sisa_waktu, energi

# Subprogram 3 (Fungsi): menghitung prediksi nilai di uas
def hitung_prediksi_uas(total_belajar, target_modul, energi):
    jumlah_rasio = 0.0

    for i in range(4):
        waktu_efektif = total_belajar[i]
        if waktu_efektif > target_modul[i]:
            waktu_efektif = target_modul[i]
        jumlah_rasio += waktu_efektif / target_modul[i]

    skor_belajar = (jumlah_rasio / 4.0) * 100
    penalti_energi = ((100 - energi) ** 2) / 100.0
    nilai_uas = skor_belajar - penalti_energi

    return nilai_uas

# Subprogram 4 (Prosedur): Alur Utama Program
def jalankan_program():
    sisa_waktu = float(input("Masukkan sisa waktu: "))
    energi = 100.0

    target_modul = [0.0, 0.0, 0.0, 0.0]
    total_belajar = [0.0, 0.0, 0.0, 0.0]

    for i in range(4):
        target_modul[i] = float(input(f"Masukkan durasi untuk modul ke-{i + 1}: "))

    while sisa_waktu > 0:
        print("1. Belajar")
        print("2. Tidur")
        pilihan = int(input("Pilih tindakan (1/2): "))

        while pilihan != 1 and pilihan != 2:
            pilihan = int(input("Pilihan tidak tersedia! Pilih tindakan (1/2): "))

        if pilihan == 1:
            sisa_waktu, energi = tindakan_belajar(sisa_waktu, energi, total_belajar)
        else:
            energi = tindakan_tidur(sisa_waktu, energi)
            sisa_waktu = 0

    nilai_akhir = hitung_prediksi_uas(total_belajar, target_modul, energi)

    if nilai_akhir == int(nilai_akhir):
        print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {int(nilai_akhir)}.")
    else:
        print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {nilai_akhir}.")

# Pemanggilan subprogram utama
jalankan_program()