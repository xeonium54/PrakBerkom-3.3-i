# NIM / Nama : 15626006/Maria Zeysta Kamelia Rumanti
# Tanggal : 11 November 2026
# Deskripsi : Program memprediksi nilai UAS

def nilai_terkecil (a, b):
    if a < b:
        return a
    return b

def minta_input_tindakan():
    print("1. Belajar")
    print("2. Tidur")
    pilihan = int(input("Pilih tindakan (1/2): "))
    while pilihan != 1 and pilihan != 2:
        pilihan = int(input("Pilihan tidak tersedia! Pilih tindakan (1/2): "))
    return pilihan

def minta_input_modul():
    pilihan = int(input("Pilih modul yang ingin dipelajari (1-4): "))
    while pilihan < 1 or pilihan > 4:
        pilihan = int(input("Pilihan tidak tersedia! Pilih modul yang ingin dipelajari (1-4):" "))
    return pilihan

def aksi_belajar(sisa_waktu, energi, T_list):
    modul = minta_input_modul()
    durasi = int(input("Masukkan durasi belajar: "))

    durasi_waktu = nilai_terkecil(durasi, sisa_waktu)

    durasi_maks_energi = energi / 5
    durasi_final = nilai_terkecil(durasi_waktu, durasi_maks_energi)

    sisa_waktu -= durasi_final
    energi -= (durasi_final * 5)
    T_list[Modul - 1] += durasi_final

    return sisa_waktu, energi, T_list

def aksi_tidur(sisa_waktu, energi)
    tambahan_energi = sisa_waktu * 12.5
    energi += tambahan_energi

    energi = nilai_terkecil(energi, 100)

    sisa_waktu = 0
    return sisa_waktu, energi

def hitung_prediksi(T_list, t_list, energi):
    sum_rasio = 0
    for i in range(4):
        T_efektif = nilai_terkecil(T_list[i], t_list[i])
        sum_rasio += (T_efektif / t_list[i])

    # Rumus Prediksi
    bagian1 = sum_rasio / 4
    bagian2 = ((100 *100) - (100 - energi)**2) / 100
    prediksi = bagian1 * bagian2

    return prediksi

# PROGRAM UTAMA
sisa_waktu = int(input(f"Masukkan durasi untuk modul ke-{i+1}: "))

t_list = [0, 0, 0, 0]
for i in range (4):
    t_list[i] = int(input(f"Masukkan durasi untuk modul ke-{i+1}: "))

energi = 100.0
T_list = [0, 0, 0, 0]

while sisa_waktu > 0:
    if energi <= 0:
         sisa_waktu, energi = aksi_tidur(sisa_waktu, energi)
         break

    tindakan = minta_input_tindakan()

    if tindakan == 1:
        sisa_waktu, energi, T_list = aksi_belajar(sisa_waktu, energi, T_list)
    elif tindakan == 2:
        sisa_waktu, energi = aksi_tidur(sisa_waktu, energi)
        break 

nilai_UAS = hitung_prediksi(T_list, t_list, energi)

if nilai_UAS % 1 == 0:
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {int(nilai_UAS)}.")
else:
    print(f"Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah {nilai_UAS}.")
    