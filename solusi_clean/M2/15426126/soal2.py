def hitung_tarif_parkir():
    # Meminta input dari pengguna sesuai format test case
    durasi = int(input("Masukkan durasi parkir (jam): "))
    is_mobil_listrik = input("Apakah mobil listrik? (y/n): ").strip().lower()
    is_akhir_pekan = input("Apakah akhir pekan? (y/n): ").strip().lower()

    # Menghitung tarif dasar berdasarkan aturan durasi
    if durasi <= 2:
        tarif_dasar = 5000
    elif durasi <= 6:
        tarif_dasar = 5000 + (durasi - 2) * 3000
    else:
        tarif_dasar = 5000 + (4 * 3000) + (durasi - 6) * 2000

    # Aturan tambahan 1: Potongan untuk mobil listrik jika durasi di atas 2 jam
    if is_mobil_listrik == 'y' and durasi > 2:
        tarif_dasar -= 5000

    # Aturan tambahan 2: Pengali akhir pekan
    if is_akhir_pekan == 'y':
        total_tarif = tarif_dasar * 1.2
    else:
        total_tarif = float(tarif_dasar)

    print(f"Total tarif parkir adalah Rp{total_tarif}")

if __name__ == "__main__":
    hitung_tarif_parkir()