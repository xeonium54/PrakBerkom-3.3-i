# NIM/Nama: Maria Amatussyafee Nurjaman
# Tanggal: 14/10/2026
# Deskripsi: Menghitung total tarif parkir

# KAMUS
# w : integer
# l, p : string

w = int(input("Masukan durasi parkir (jam): "))
l = str(input("Apakah mobil listrik? (y/n): "))
p = str(input("Apakah akhir pekan? (y/n): "))

if w <= 2:
    tarif = 5000
elif w <= 6:
    tarif = 5000 + 3000 * (w - 2)
else:
    tarif = 5000 + 3000 * 4 + 2000 * (w - 6)

if l == "y" and w > 2:
    tarif = tarif - 5000
if p == "y":
    tarif = tarif * 1.2

print(f"Total tarif parkir adalah:", int(tarif))
