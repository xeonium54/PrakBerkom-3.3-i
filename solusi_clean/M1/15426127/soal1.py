# NIM/Nama : Luna Febryvazrya
# Tanggal : 30 September 2026
# Deskripsi : Praktikum berpikir komputasional

j = int(input("Masukkan daya lampu (j): "))
w = int(input("Masukkan lama lampu menyala (w): "))
r = int(input("Masukkan tarif listrik (r): "))

energi = (j*w) / 1000
biaya = energi * r

nama = "Mik"
print(f"Total biaya listrik yang terbuang akibat lampu menyala: {biaya}")