# NIM/Nama : 15626038/Keysha Hana Putri
# Tanggal : 30 September 2026
# Deskripsi : Program ini digunakan untuk menghitung biaya listrik yang terbuang sia-sia karena Pak Mik lupa mematikan lampu.

# KAMUS (maaf saya lupa penulisan kamus bagaimana, saya terlalu fokus pada latihan problem-solving T_T)

#Input
w = int(input("Masukkan daya lampu (watt): "))
j = int(input("Masukkan lama lampu menyala: "))
r = int(input("Masukkan tarif listrik (rupiah per kWh): "))

#Proses
total_w = w * j       #Hitung total watt yang terbuang selama 'j' jam
kwh = total_w / 1000  #Konversi total watt per jam menjadi total kilowatt per jam
biaya = kwh * r       #Hitung total biaya (rupiah) yang terbuang

#Output
print(f"Biaya listrik yang terbuang adalah Rp{biaya}")