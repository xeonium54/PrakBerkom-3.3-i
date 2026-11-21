# NIM/Nama : 15626024 / Akbar Muhammad Al Ghifari
# Tanggal : 30 September 2026
# Deskripsi : Menghitung total biaya listrik yang terbuang karena penggunaan lampu

# Kamus
# w (int) merupakan daya dari lampu
# j (float) merupakan durasi lamanya suatu lampu dinyalakan dalam jam
# r (int) merupakan tarif listrik rumah Mik dalam rupiah per kWh
# e (float) menghitung energi yang digunakan
# b (int) menghitung biaya yang harus dibayarkan

# Algoritma
w = int(input("Masukkan daya lampu (watt): "))
j = float(input("Masukkan lama lampu menyala (jam): "))
r = int(input("Masukkan tarif listrik (rupiah per kWh): "))

e = float((w*j)/1000)
b = float(e*r)

print(f"Biaya listrik yang terbuang adalah Rp {b}")





