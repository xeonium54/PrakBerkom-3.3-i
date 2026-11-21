# NIM/Nama : 15626012/Muhammad Dzaky Nouvaldi
# Tanggal: 14 Oktober 2026
# Deskripsi: Program menghitung total tarif parkir 

#KAMUS
# durasi : int 
# isEV : bool
# isWeekend : bool

durasi = int(input('Masukkan durasi parkir (jam): '))
is_EV = input('Apakah mobil EV? (y/n): ')
is_Weekend = input('Apakah akhir pekan? (y/n): ')

if durasi <= 2:
    tarif = 5000
elif durasi <= 6:
    tarif = 5000 + (durasi -2) * 3000
else:
    tarif = 5000 + 4 * 3000 + (durasi - 6) * 2000


if is_EV == 'y' and durasi > 2:
    tarif -= 5000


if is_Weekend == 'y':
    tarif_total = tarif * 1.2
else:
    tarif_total = tarif 

print('Total tarif parkir: Rp', tarif_total)