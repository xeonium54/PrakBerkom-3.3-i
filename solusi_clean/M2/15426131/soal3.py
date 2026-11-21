
# Nama: Reyza Aulia Rahman
# NIM: 15426131
# Deskripsi: Cek laju kereta

# KA :integer(cek jenis kereta A)
# KB :text(cek apakah listrik atau gak)
# DA :integer(cek jarak A)
# DB :integer(cek jarak B)
# TA ::integer(cek waktu A)
# TB :integer(cek waktu B)
# M :integer(cek jika kode lanjut atau tidak)
# N :integer(cek jika kode lanjut atau tidak)
# I :integer(cek jika kode lanjut atau tidak)

KA = input("Masukkan jenis kereta A (Eksekutif/Bisnis/Kargo): ")
DA = int(input("Masukkan Jarak Kereta A (m): "))
VA = int(input("Masukkan kecepatan Kereta A (m/s): "))
KB = input("Masukkna jenis kereta B (Eksekutif/Bisnis/Kargo): ")
DB = int(input("Masukkan jarak kereta B (m): "))
VB = int(input("Masukkan kecepatan Kereta B (m/s): "))


if KA == ("Eksekutif"):
    KA = 3
elif KA == ("Bisnis"):
    KA = 2
else:
    KA = 1

if KB == ("Eksekutif"):
    KB = 3
elif KB == ("Bisnis"):
    KB = 2
else:
    KB = 1

TA = DA/VA 
TB = DB/VB

if TA - TB >= 30:
    print("Jalur aman. Kereta B melintas duluan tanpa henti.")
    I = 0
elif TA - TB <= - 30:
    print("Jalur aman, kereta A melintas duluan tanpa henti")
    I = 0
else:
    I = 1

if I == 0:
    print("")
elif I == 1 and KA > KB:
    print("Kereta A melaju duluan")
    print(f"Kereta B harus menunggu selama {TA + 40 - TB} detik")
    N = 0
elif I == 1 and KA < KB:
    print("Kereta B melaju duluan")
    print(f"Kereta A harus menunggu selama {TB + 40 - TA} detik")
    N = 0
elif I == 1 and KA == KB:
    N = 1
else:
    N = 1

if 0 < TA - TB < 30 and N == 1 and I == 1:
    print(f"Konflik terdeteksi, kereta A harus mengalah {TB + 40 - TA} detik")
    M = 0
elif 0 > TA - TB > -30 and N == 1 and I == 1:
    print(f"konflik terdeteksi, kereta B harus mengalah {TA + 40 - TA} detik")
    M = 0
else:
    M = 1 


if M == 1 and DA < DB and I == 1 and N == 1:
    print("Kereta A diproritaskan duluan")
    print(f"Kereta B harus menunggu selama {TB - 40 - TA} detik")
elif M == 1 and DA > DB and I == 1 and N == 1:
    print("Kereta B diproritaskan duluan")
    print(f"Kereta B harus menunggu selama {TB - 40 - TA} detik")
elif M == 1 and DA == DB and I == 1 and N == 1:
    print("Kereta A diproritaskan duluan karena berada di jalur utama")
    print(f"Kereta B harus menunggu selama {TA - 40 - TB} detik")
else:
    print("")

