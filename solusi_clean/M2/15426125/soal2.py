nama: Nailini Kaylara Madhani
nim: 15426125
tanggal: 14 Oktober 2026



durasi = int(input("Masukkan durasi parkir (jam): "))
mobil_listrik = input("Apakah mobil listrik? (y/n): ").lower()
akhir_pekan = input("Apakah akhir pekan? (y/n): ").lower()
if durasi <= 2:
    tarif = 5000
if durasi > 2 and durasi <= 6:
    tarif = 5000 + (durasi - 2) * 3000
if durasi > 6:
    tarif = 5000 (4 * 3000) + (durasi - 6) * 2000

if mobil_listrik == 'y' and durasi > 2:
    tarif -= 5000
if akhir_pekan == 'y':
    tarif *= 1.2

    print(f"Total tarif parkir adalah Rp{tarif}")