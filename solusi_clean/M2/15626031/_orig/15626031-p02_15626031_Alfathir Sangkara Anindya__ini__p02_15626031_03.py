# P02_NIM_03.py

# Input Kereta A
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
jarak_A = float(input("Masukkan jarak Kereta A (m): "))
kecepatan_A = float(input("Masukkan kecepatan Kereta A (m/s): "))

# Input Kereta B
jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
jarak_B = float(input("Masukkan jarak Kereta B (m): "))
kecepatan_B = float(input("Masukkan kecepatan Kereta B (m/s): "))

# Menghitung waktu tiba
TA = jarak_A / kecepatan_A
TB = jarak_B / kecepatan_B

# Menentukan prioritas jenis kereta
if jenis_A == "Eksekutif":
    prioritas_A = 3
else:
    if jenis_A == "Bisnis":
        prioritas_A = 2
    else:
        prioritas_A = 1

if jenis_B == "Eksekutif":
    prioritas_B = 3
else:
    if jenis_B == "Bisnis":
        prioritas_B = 2
    else:
        prioritas_B = 1

# Menghitung selisih waktu tanpa abs()
if TA >= TB:
    selisih = TA - TB
else:
    selisih = TB - TA

# Memeriksa konflik jalur
if selisih >= 30:
    print("Jalur aman.")

    if TA < TB:
        print("Kereta A melintas duluan tanpa henti.")
    else:
        print("Kereta B melintas duluan tanpa henti.")

else:
    print("Konflik terdeteksi! Kereta diprioritaskan melintas.")

    # Menentukan kereta yang diprioritaskan
    if prioritas_A > prioritas_B:
        waktu_tunggu = (TA + 40.0) - TB
        print("Kereta B harus berhenti dan menunggu.")
        print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")

    else:
        if prioritas_B > prioritas_A:
            waktu_tunggu = (TB + 40.0) - TA
            print("Kereta A harus berhenti dan menunggu.")
            print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")

        else:
            # Jika prioritas jenis sama, bandingkan waktu tiba
            if TA < TB:
                waktu_tunggu = (TA + 40.0) - TB
                print("Kereta B harus berhenti dan menunggu.")
                print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")

            else:
                if TB < TA:
                    waktu_tunggu = (TB + 40.0) - TA
                    print("Kereta A harus berhenti dan menunggu.")
                    print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")

                else:
                    # Jika waktu tiba sama, bandingkan jarak
                    if jarak_A <= jarak_B:
                        print("Kereta B harus berhenti dan menunggu.")
                        print("Kereta B harus berhenti dan menunggu selama 40.0 detik.")
                    else:
                        print("Kereta A harus berhenti dan menunggu.")
                        print("Kereta A harus berhenti dan menunggu selama 40.0 detik.")