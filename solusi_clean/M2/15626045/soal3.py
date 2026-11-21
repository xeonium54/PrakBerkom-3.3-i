# NIM/Nama : 15626045/Anindhita Ramya Rahmadani
# Tanggal : 14/10/2026
# Deskripsi : Menentukan urutan prioritas antara dua kereta yang melintas dan waktu tunggu bagi kereta yang harus mengalah berdasarkan masukan jenis kereta, jarak ke persimpangan (meter), dan kecepatan tempuh (m/s)

jenis_a = str(input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): "))
jarak_a = int(input("Masukkan jarak Kereta A (m): "))
v_a = int(input("Masukkan kecepatan Kereta A (m/s): "))
jenis_b = str(input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): "))
jarak_b = int(input("Masukkan jarak Kereta B (m): "))
v_b = int(input("Masukkan kecepatan Kereta B (m/s): "))

waktu_a = jarak_a // v_a
waktu_b = jarak_b // v_b

if (waktu_a > waktu_b):
    selisih = waktu_a - waktu_b
else:
    selisih = waktu_b - waktu_a

if (selisih >= 30):
    if (waktu_a < waktu_b) and (selisih >= 30):
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:
    if ("Eksekutif" > "Bisnis" > "Eksekutif"):
        
