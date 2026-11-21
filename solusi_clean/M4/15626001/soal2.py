# NIM/Nama : 15626001 / Muhamad Naufal Al Fajri
# Tanggal : 11 November  2026
# Deskripsi :
n = int(input("Masukkan jumlah kandidat PIN: "))

kuat = 0
sedang = 0
lemah = 0
 
for i in range(n):
    pin = input(f"Masukkan PIN ke-{i+1}: ")

print("=== REKAPITULASI ===")
print("Kuat:", kuat)
print("Sedang:", sedang)
print("Lemah:", lemah)