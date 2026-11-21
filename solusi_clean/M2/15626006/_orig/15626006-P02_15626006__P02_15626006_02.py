# NIM/Nama : 15626006/Maria Zeysta Kamelia Rumanti
# Tanggal : 14 Oktober 2026
# Deskripsi : Program yang dapat menghitung total tarif yang harus dibayar berdasarkan lama durasi parkir dalam jam.

# Input dari pengguna
durasi = int(input("Masukkan durasi parkir (jam): "))
mobil_listrik = input("Apakah mobil listrik? (y/n): ")
akhir_pekan = input("Apakah akhir pekan? (y/n): ")

# Hitung tarif dasar parkir
if durasi <= 2:
    tarif = 5000
elif durasi <= 6:
    # 2 jam pertama Rp.5000, sisanya Rp.3000/jam
    tarif = 5000 + (durasi - 2) * 3000
else:
    # 6 jam pertama Rp.5000 + (4 jam * 3000) = Rp.17000
    # Di atas 6 jam Rp.2000/jam
    tarif = 17000 + (durasi - 6) * 2000

# Aturan tambahan pertama: Potongan untuk mobil listrik
if mobil_listrik == 'y' and durasi > 2:
    tarif -= 5000

# Aturan tambahan kedua: Potongan akhir pekan, setelah potongan mobil listrik (jika ada)
if akhir_pekan == 'y':
    tarif *= 1.2

# Total tarif parkir yang harus dibayar
print("Total tarif parkir adalah Rp.", tarif)