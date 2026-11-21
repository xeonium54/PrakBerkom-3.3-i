# NIM/Nama : 15626035/Naila Rahmah Zhafirah
# Tanggal : 14 Oktober 2016
# Deskripsi :

# Kamus
jenis_kereta_A = ""
jenis_kereta_B = ""
jarak_kereta_A = 0
jarak_kereta_B = 0
kecepatan_kereta_A = 0
kecepatan_kereta_B = 0
waktu_kereta_A = 0
waktu_kereta_B = 0
prioritas_kereta_A = 0
prioritas_kereta_B = 0
waktu_tunggu = 0

# Input Kereta A
jenis_kereta_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
jarak_kereta_A = int(input("Masukkan jarak Kereta A (m): "))
kecepatan_kereta_A = int(input("Mauskkan kecepatan Kereta A (m/s): "))

# Input Kereta B
jenis_kereta_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
jarak_kereta_B = int(input("Masukkan jarak Kereta B (m): "))
kecepatan_kereta_B = int(input("Mauskkan kecepatan Kereta B (m/s): "))

# Menghitung waktu tiba
waktu_kereta_A = jarak_kereta_A / kecepatan_kereta_A
waktu_kereta_B = jarak_kereta_B / kecepatan_kereta_B

# Selisih
if waktu_kereta_A >= waktu_kereta_B:
    selisih = waktu_kereta_A - waktu_kereta_B
else:
    selisih = waktu_kereta_B - waktu_kereta_A

# Keamanan jalur
if selisih >= 30:
    if waktu_kereta_A <= waktu_kereta_B:
        print("Jalur aman. Kereta A melintas duluan tanp henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:
    print("Konflik terdeteksi")

    # Menentukan prioritas Kereta A
    if jenis_kereta_A == "Eksekutif":
        prioritas_kereta_A = 3
    else:
        if jenis_kereta_A == "Bisnis":
            prioritas_kereta_A = 2
        else:
            prioritas_kereta_A = 1

    # Menentukan prioritas Kereta B
        if jenis_kereta_B == "Eksekutif":
            prioritas_kereta_B = 3
        else:
            if jenis_kereta_B == "Bisnis":
                prioritas_kereta_B = 2
            else:
                prioritas_kereta_B = 1

    # Menentukan kereta yang diprioritaskan
    if prioritas_kereta_A > prioritas_kereta_B:
        waktu_tunggu = waktu_kereta_A + 40 - waktu_kereta_B
        print("Kereta B harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")
    else:
        if prioritas_kereta_B > prioritas_kereta_A:
            waktu_tunggu = waktu_kereta_B + 40 - waktu_kereta_A
            print("Kereta A harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")
        else:
            if waktu_kereta_A < waktu_kereta_B:
                waktu_tunggu = waktu_kereta_A + 40 - waktu_kereta_B
                print("Kereta B harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")
            else:
                if prioritas_kereta_B > prioritas_kereta_A:
                    waktu_tunggu = waktu_kereta_B + 40 - waktu_kereta_A
                    print("Kereta A harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")
                else:
                    if jarak_kereta_A < jarak_kereta_B:
                        waktu_tunggu = waktu_kereta_A + 40 - waktu_kereta_B
                        print("Kereta B harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")
                    else:
                        if jarak_kereta_B < jarak_kereta_A:
                            waktu_tunggu = waktu_kereta_B + 40 - waktu_kereta_A
                            print("Kereta A harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")
                        else:
                            waktu_tunggu = waktu_kereta_A + 40 - waktu_kereta_B
                            print("Kereta B harus berhenti dan menunggu selama", round(waktu_tunggu, 1), "detik.")

