# NIM/NAMA : Arya Satya Anggara
# Tanggal : 14 Oktober 2026
# Deskripsi : Program untuk menghitung tarif parkir berdasarkan durasi, jenis kendaraan, dan hari parkir menggunakan percabangan

durasi = int(input("Masukkan durasi parkir (jam): "))
listrik = input("Apakah mobil listrik? (y/n): ")
akhirpekan = input("Apakah parkir pada akhir pekan? (y/n): ")

if durasi <= 2:
    tarif = 5000
elif durasi <= 6:
    tarif = 5000 + (durasi - 2) * 3000
else:
    tarif = 5000 + (4 * 3000) + (durasi - 6) * 2000

if listrik == "y" and durasi > 2:
    tarif = tarif - 5000

if akhirpekan == "y":
    tarif = tarif * 1.2

print("Total tarif parkir: Rp", int(tarif))