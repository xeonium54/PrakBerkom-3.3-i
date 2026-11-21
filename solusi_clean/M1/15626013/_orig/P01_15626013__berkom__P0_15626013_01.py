#NIM/Nama : 15626013/Natali Stela Br Sinaga
#Tanggal : 30 September 2026
#Deskripsi : Menghitung biaya listri yang terbuang akibat lampu menyala

#Meminta input dari pengguna
w = float(input("Masukan daya lampu(watt):"))
j = float(input("Masukan lama lampu menyala (jam):"))
r = float(input("Masukan tarif listrik(rupiah per (kWh):")) 

# Menghitung energi listrik dalam kWh
energi = (w * j) / 1000

# Menghitung biaya listrik
biaya = energi * r

# Menampilkan hasil
print(f"Biaya listrik yang terbuang adalah Rp{biaya:g}")