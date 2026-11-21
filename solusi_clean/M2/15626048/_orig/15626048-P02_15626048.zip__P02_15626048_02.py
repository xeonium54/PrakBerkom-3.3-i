# Nim: 15626948
# Tanggal: 14 Oktober 2026
# Deskripsi: Program menentukan tarif parkir

# Kamus
# n: int

# Algoritma
# Berdasarkan durasi
durasi = int(input("Masukan n:"))
listrik = (input("Apakah kendaraan mobil listrik?(Ya/Tidak):"))
pekan = (input("Apakah akhir pekan?(Ya/Tidak):"))

if durasi <=2:
    tarif = 5000
elif durasi <=6:
    tarif = 5000 + 3000*(durasi-2)
else:
    tarif = 5000 + 3000*(6-2) + 2000*(durasi-6)

# Potongan mobil listrik
if listrik == "Ya" and durasi > 2:
    tarif = tarif - 5000

# Tarif akhir pekan
if pekan == "Ya":
    tarif = tarif*1.2

print("Tarif parkir: Rp", tarif)
