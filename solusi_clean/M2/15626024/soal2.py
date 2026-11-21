# NIM/Nama  : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal   : 14 October 2026
# Deskripsi : Program yang mengecek tarif parkir sebuah kendaraan berdasarkan beberapa syarat
# seperti Durasi, Ev atau bukan, dan Weekend atau tidak

# Kamus
# D (int) menginput durasi parkir
# Ev (str) mengecek status apakah mobil listrik/bukan
# W (str) mengecek apakah akhir pekan
# Dpros (int) proses pengecekan di if else bag. D
# Evpros (int) proses pengecekan di if else bag. Ev
# Total (float) total akhir tarif parkir yang akan dibayarkan

# Algoritma
D = int(input("Masukkan durasi parkir (jam): "))
Ev = str(input("Apakah mobil listrik (y/n)? "))
W = str(input("Apakah akhir pekan (y/n)? "))
Dpros = int
Evpros = int
Total = float

if (0 <= D <= 2):
    Dpros = int(D*5000)
elif 2 < D <= 6:
    Dpros = int(5000+((D-2)*3000))
elif D > 6:
    Dpros = int(17000+((D-6)*2000))

if (Ev == str("y")):
    if (D > 2):
        Evpros = int(Dpros - 5000)
    else:
        Evpros = Dpros
elif (Ev == str("n")):
    Evpros = int(Dpros)

if (W == str("y")):
    Total = int(Evpros)*(1.2)
elif(W == str("n")):
    Total = int(Evpros)

print(f"Total tarif parkir adalah Rp{Total}")

