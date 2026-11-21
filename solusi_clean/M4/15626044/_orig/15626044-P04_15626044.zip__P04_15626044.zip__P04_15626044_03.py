# NIM/Nama : 15626044/Saliha Mahira Al-kwarismy
# Tanggal : 11 November
# Deskripsi : P04_15626044_Problem3

# Subprogram awal (belajar)
def pilihan_belajar(sisa_jam, sisa_energi, jam_minta, data_belajar, nomor):
    # Durasi maksimal tuan Ky
    jam_maksimal = sisa_jam
    batas_energi = sisa_energi // 5
    if batas_energi < jam_maksimal:
        jam_maksimal = batas_energi

    if jam_minta > jam_maksimal:
        jam_terpakai = jam_maksimal
    else:
        jam_terpakai = jam_minta

    # Masukkan jam belajarnya
    data_belajar[nomor - 1] = data_belajar[nomor - 1] + jam_terpakai

    #Menghitung perkiraan saat pingsan
    if sisa_energi == 0 and sisa_jam > 0:
        sisa_energi = sisa_tenaga + (sisa_jam * 10)
        if sisa_tenaga > 100:
            sisa_tenaga = 100
        sisa_jam = 0

# SUbprogram ke-2 (tidur)
def proses_tidur(sisa_jam, sisa_energi):
    sisa_energi = sisa_energi + (sisa_jam * 10)
    if sisa_energi > 100:
        sisa_energi = 100
    sisa_jam = 0

# SUbprogram ke-3 skor akhir
def rumus_skor_uas(data_belajar, data_target, sisa_tenaga):
    skor_pengumpulan = 0
    for i in range(4):
        waktu_asli = data_belajar[i]
        waktu_dibutuhkan = data_target[i]
        if waktu_asli > waktu_dibutuhkan:
            waktu_asli = waktu_dibutuhkan
        skor_pengumpulan = skor_pengumpulan + (waktu_asli / waktu_dibutuhkan * 20)

    skor_total = skor_pengumpulan + (sisa_energi / 30)


# Masukkan waktu pertama kali

waktu_awal = int(input("Masukkan sisa waktu: "))

# Batas durasi modul
target_waktu = [0, 0, 0, 0]
for i in range(1,5):
    target_waktu[i - 1] = int(input(f"Masukkan durasi untuk modul ke-{i}: "))

# KOdnisi awal
tenaga_awal = 100
waktu_terpakai = [0, 0, 0, 0]
