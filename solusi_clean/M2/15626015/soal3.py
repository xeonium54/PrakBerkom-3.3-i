# NIM/Nama : 15626015/Ken Btari Syahidah
# Tanggal : 14 Oktober 2026
# Deskripsi : Mendeteksi apakah kereta A dan B
#             akan melintasi jalur yang sama atau tidak
#             dalam waktu yang sama dan jika kereta melintasi
#             jalur dalam waktu yang sama, maka terdeteksi konflik 
#             dan salah satu kereta harus menunggu berdasarkan prioritas

# KAMUS
# Jenis_A : str : Jenis kereta A (Eksekutif/Bisnis/Kargo)
# Jarak_A : int : Jarak kereta A dalam meter
# Kec_A : int : Kecepatan kereta A dalam (m/s)
# Jenis_B : str : Jenis kereta B (Eksekutif/Bisnis/Kargo)
# Jarak_B : int : Jarak kereta B dalam meter
# Kec_B : int : Kecepatan kereta B dalam (m/s)


Jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo) : ")
Jarak_A = int(input("Masukkan jarak Kereta A (m) : "))
Kec_A = int(input("Masukkan kecepatan Kereta A (m/s) : "))

Jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo) : ")
Jarak_B = int(input("Masukkan jarak Kereta B (m) : "))
Kec_B = int(input("Masukkan kecepatan Kereta B (m/s) : "))

TA = Jarak_A / Kec_A
TB = Jarak_B / Kec_B

if (TA >= TB) :
    selisih = TA - TB
else :
    selisih = TB - TA

if (selisih >= 30) :
    if (TA > TB) :
        print("Jalur aman. Kereta A melintas duluan tanpa henti")
    else :
        print("Jalur aman. Kereta B melintas duluan tanpa henti")

if (selisih < 30) :
    if (Jenis_A == "Eksekutif") :
        prioritasA = 3
    elif (Jenis_A == "Bisnis") :
        prioritasA = 2
    else :
        prioritasA = 1

if (selisih < 30) :
    if (Jenis_B == "Eksekutif") :
        prioritasB = 3
    elif (Jenis_B == "Bisnis") :
        prioritasB = 2
    else :
        prioritasB = 1

if (Jenis_A != Jenis_B) :
    if (prioritasA > prioritasB) :
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
        print("Kereta B harus berhenti dan menunggu selama" , TA + TB , "detik")
    elif (prioritasA < prioritasB) :
        print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
        print("Kereta A harus berhenti dan menunggu selama" , TA + TB , "detik")
