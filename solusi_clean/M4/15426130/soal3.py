# NIM/Nama  : 15426130 / Yudha Putra
# Tanggal   : 11 November 2026
# Deskripsi : Simulasi Sistem Kebut Semalam dan prediksi nilai UAS Tuan Ky

ENERGI_PER_JAM = 5      # energi terkuras tiap 1 jam belajar
PULIH_PER_JAM = 12.5    # energi pulih tiap 1 jam tidur
ENERGI_MAKS = 100       # batas maksimal energi


def minta_tindakan():
    """Meminta pilihan tindakan (1/2) hingga valid."""
    pilihan = input("Pilih tindakan (1/2): ")
    while pilihan != "1" and pilihan != "2":
        pilihan = input("Pilihan tidak tersedia! Pilih tindakan (1/2): ")
    return int(pilihan)


def minta_modul():
    """Meminta pilihan modul (1-4) hingga valid."""
    pilihan = input("Pilih modul yang ingin dipelajari (1 -4): ")
    while pilihan not in ("1", "2", "3", "4"):
        pilihan = input("Modul tidak tersedia! "
                        "Pilih modul yang ingin dipelajari (1 -4): ")
    return int(pilihan)


def belajar(modul, durasi, waktu, energi, total_belajar):
    """
    Tindakan belajar. Durasi dipotong oleh sisa waktu dan sisa energi.
    total_belajar (list) diperbarui langsung.
    Mengembalikan (waktu, energi) terbaru.
    """
    # Batas durasi oleh sisa waktu
    if durasi > waktu:
        durasi = waktu

    # Batas durasi oleh sisa energi
    batas_energi = energi / ENERGI_PER_JAM
    if durasi >= batas_energi:
        durasi = batas_energi
        energi = 0                       # energi habis tepat
    else:
        energi = energi - durasi * ENERGI_PER_JAM

    waktu = waktu - durasi
    total_belajar[modul - 1] = total_belajar[modul - 1] + durasi
    return waktu, energi


def tidur(waktu, energi):
    """Tidur selama seluruh sisa waktu. Mengembalikan (waktu, energi)."""
    energi = energi + waktu * PULIH_PER_JAM
    if energi > ENERGI_MAKS:
        energi = ENERGI_MAKS
    return 0, energi


def hitung_nilai(total_belajar, t, energi):
    """Menghitung prediksi nilai UAS berdasarkan rumus pada soal."""
    jumlah_rasio = 0
    for i in range(4):
        ti_belajar = total_belajar[i]
        if ti_belajar > t[i]:            # Ti tidak boleh melebihi ti
            ti_belajar = t[i]
        jumlah_rasio += ti_belajar / t[i]

    faktor_energi = (ENERGI_MAKS ** 2 - (ENERGI_MAKS - energi) ** 2) / 100
    return jumlah_rasio / 4 * faktor_energi


def format_nilai(nilai):
    """Merapikan tampilan: 50.0 -> 50, hindari noise floating point."""
    nilai = round(nilai, 6)
    if nilai == int(nilai):
        return str(int(nilai))
    return str(nilai)


def main():
    waktu = float(input("Masukkan sisa waktu: "))
    t = []
    for i in range(1, 5):
        t.append(float(input("Masukkan durasi untuk modul ke -" + str(i) + ": ")))

    energi = ENERGI_MAKS
    total_belajar = [0, 0, 0, 0]   # Ti: total durasi belajar tiap modul

    # Sesi berlangsung selama masih ada waktu
    while waktu > 0:
        print("1. Belajar")
        print("2. Tidur")
        tindakan = minta_tindakan()

        if tindakan == 1:
            modul = minta_modul()
            durasi = float(input("Masukkan durasi belajar: "))
            waktu, energi = belajar(modul, durasi, waktu, energi, total_belajar)

            if energi == 0:
                print("Tuan Ky terpaksa tidur karena kehabisan energi!")
                waktu, energi = tidur(waktu, energi)
        else:
            waktu, energi = tidur(waktu, energi)

    nilai = hitung_nilai(total_belajar, t, energi)
    print("Prediksi nilai UAS yang akan didapatkan oleh Tuan Ky adalah "
          + format_nilai(nilai) + ".")


main()