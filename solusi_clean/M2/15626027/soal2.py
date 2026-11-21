#NIM/Nama : 15626027/Muhammad Faiz Dhiaul Haq
#Tanggal : 14 Oktober 2026
#Deskrpisi : Membuat program menghitung tarif parkir

#Kamus:
#durasi : integer {lama durasi parkir dalam satuan jam}
#is_listrik : string {apakah kendaraan merupakan listrik atau tidak}
#is_akhir_pekan : string {Apakah parkir pada saat akhir pekan atau tidak}
#tarif : integer/float {tarif yang harus dibayar}

#input data
durasi = int(input("Masukkan durasi parkir (Jam): "))
is_listrik = input("Masukkan mobil listrik? (y/n): ")
is_akhir_pekan = input("Apakah akhir pekan (y/n): ")

#Tarif dasar
if durasi <= 2:
    tarif = 5000
elif durasi <= 6:
    tarif = 5000 + (durasi-2) * 3000
else:
    tarif = 5000 + (4 * 3000) + (durasi-6) *2000

#Potongan tarif parkir mobil listrik , jika diatas 2 jam
if is_listrik == 'y' and durasi > 2:
    tarif -= 5000

#Tarif parkir jika akhir pekan
if is_akhir_pekan == 'y':
    tarif = tarif * 1.2
else:
    tarif = int (tarif)

#total parkir
print(f"Total tarif parkir adalah Rp{tarif}")