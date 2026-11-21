"""**Problem 3**

Case 1
"""

# NIM / Nama: 15626007 / Ryssad Sabralnair
# Tanggal : 14 Oktober 2026
# Deskripsi : Program Pengatur Perjalanan Kereta Api di Stasiun Berkom

#Problem 3
#Case 1

# Input data Kereta A
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ").strip().lower()
DA = int(input("Masukkan jarak Kereta A (DA dalam meter): "))
VA = int(input("Masukkan kecepatan Kereta A (VA dalam m/s): "))

# Input data Kereta B
jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ").strip().lower()
DB = int(input("Masukkan jarak Kereta B (DB dalam meter): "))
VB = int(input("Masukkan kecepatan Kereta B (VB dalam m/s): "))

# Menghitung waktu tiba (TA dan TB)
TA = DA / VA
TB = DB / VB

# Menghitung selisih waktu secara manual tanpa fungsi abs()
selisih_waktu = TA - TB
if selisih_waktu < 0:
    selisih_waktu = -selisih_waktu

# Menentukan prioritas kelas Kereta A (Eksekutif = 3, Bisnis = 2, Kargo = 1)
if jenis_A == "eksekutif":
    prioritas_A = 3
elif jenis_A == "bisnis":
    prioritas_A = 2
else:
    prioritas_A = 1

# Menentukan prioritas kelas Kereta B
if jenis_B == "eksekutif":
    prioritas_B = 3
elif jenis_B == "bisnis":
    prioritas_B = 2
else:
    prioritas_B = 1

# Kondisi 1: Jalur aman jika selisih waktu minimal 30 detik (|TA - TB| >= 30.0)
if selisih_waktu >= 30.0:
    if TA < TB:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")

# Kondisi 2: Terjadi potensi konflik jika selisih waktu < 30 detik
else:
    kereta_prioritas = ""

    # Menentukan prioritas berdasarkan kelas kereta
    if prioritas_A > prioritas_B:
        kereta_prioritas = "A"
    elif prioritas_B > prioritas_A:
        kereta_prioritas = "B"
    else:
        # Jika kelas kereta sama, bandingkan waktu tiba (yang lebih cepat)
        if TA < TB:
            kereta_prioritas = "A"
        elif TB < TA:
            kereta_prioritas = "B"
        else:
            # Jika waktu tiba sama, bandingkan jarak (yang lebih dekat)
            if DA < DB:
                kereta_prioritas = "A"
            elif DB < DA:
                kereta_prioritas = "B"
            else:
                # Jika jarak juga sama, Kereta A diprioritaskan
                kereta_prioritas = "A"

    # Menghitung waktu tunggu kereta yang mengalah
    if kereta_prioritas == "A":
        waktu_tunggu = (TA + 40.0) - TB
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas. Kereta B harus berhenti dan menunggu selama", waktu_tunggu, "detik.")
    else:
        waktu_tunggu = (TB + 40.0) - TA
        print("Potensi konflik! Kereta B diprioritaskan melintas. Kereta A harus berhenti dan menunggu selama", waktu_tunggu, "detik.")

# NIM / Nama: 15626007 / Ryssad Sabralnair
# Tanggal : 14 Oktober 2026
# Deskripsi : Program Pengatur Perjalanan Kereta Api di Stasiun Berkom

#Problem 3
#Case 2

# Input data Kereta A
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ").strip().lower()
DA = int(input("Masukkan jarak Kereta A (DA dalam meter): "))
VA = int(input("Masukkan kecepatan Kereta A (VA dalam m/s): "))

# Input data Kereta B
jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ").strip().lower()
DB = int(input("Masukkan jarak Kereta B (DB dalam meter): "))
VB = int(input("Masukkan kecepatan Kereta B (VB dalam m/s): "))

# Menghitung waktu tiba (TA dan TB)
TA = DA / VA
TB = DB / VB

# Menghitung selisih waktu secara manual tanpa fungsi abs()
selisih_waktu = TA - TB
if selisih_waktu < 0:
    selisih_waktu = -selisih_waktu

# Menentukan prioritas kelas Kereta A (Eksekutif = 3, Bisnis = 2, Kargo = 1)
if jenis_A == "eksekutif":
    prioritas_A = 3
elif jenis_A == "bisnis":
    prioritas_A = 2
else:
    prioritas_A = 1

# Menentukan prioritas kelas Kereta B
if jenis_B == "eksekutif":
    prioritas_B = 3
elif jenis_B == "bisnis":
    prioritas_B = 2
else:
    prioritas_B = 1

# Kondisi 1: Jalur aman jika selisih waktu minimal 30 detik (|TA - TB| >= 30.0)
if selisih_waktu >= 30.0:
    if TA < TB:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")

# Kondisi 2: Terjadi potensi konflik jika selisih waktu < 30 detik
else:
    kereta_prioritas = ""

    # Menentukan prioritas berdasarkan kelas kereta
    if prioritas_A > prioritas_B:
        kereta_prioritas = "A"
    elif prioritas_B > prioritas_A:
        kereta_prioritas = "B"
    else:
        # Jika kelas kereta sama, bandingkan waktu tiba (yang lebih cepat)
        if TA < TB:
            kereta_prioritas = "A"
        elif TB < TA:
            kereta_prioritas = "B"
        else:
            # Jika waktu tiba sama, bandingkan jarak (yang lebih dekat)
            if DA < DB:
                kereta_prioritas = "A"
            elif DB < DA:
                kereta_prioritas = "B"
            else:
                # Jika jarak juga sama, Kereta A diprioritaskan
                kereta_prioritas = "A"

    # Menghitung waktu tunggu kereta yang mengalah
    if kereta_prioritas == "A":
        waktu_tunggu = (TA + 40.0) - TB
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas. Kereta B harus berhenti dan menunggu selama", waktu_tunggu, "detik.")
    else:
        waktu_tunggu = (TB + 40.0) - TA
        print("Potensi konflik! Kereta B melintas duluan. Kereta A harus menunggu selama", waktu_tunggu, "detik.")

"""Case 3"""

# NIM / Nama: 15626007 / Ryssad Sabralnair
# Tanggal : 14 Oktober 2026
# Deskripsi : Program Pengatur Perjalanan Kereta Api di Stasiun Berkom

#Problem 3
#Case 3

# Input data Kereta A
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ").strip().lower()
DA = int(input("Masukkan jarak Kereta A (DA dalam meter): "))
VA = int(input("Masukkan kecepatan Kereta A (VA dalam m/s): "))

# Input data Kereta B
jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ").strip().lower()
DB = int(input("Masukkan jarak Kereta B (DB dalam meter): "))
VB = int(input("Masukkan kecepatan Kereta B (VB dalam m/s): "))

# Menghitung waktu tiba (TA dan TB)
TA = DA / VA
TB = DB / VB

# Menghitung selisih waktu secara manual tanpa fungsi abs()
selisih_waktu = TA - TB
if selisih_waktu < 0:
    selisih_waktu = -selisih_waktu

# Menentukan prioritas kelas Kereta A (Eksekutif = 3, Bisnis = 2, Kargo = 1)
if jenis_A == "eksekutif":
    prioritas_A = 3
elif jenis_A == "bisnis":
    prioritas_A = 2
else:
    prioritas_A = 1

# Menentukan prioritas kelas Kereta B
if jenis_B == "eksekutif":
    prioritas_B = 3
elif jenis_B == "bisnis":
    prioritas_B = 2
else:
    prioritas_B = 1

# Kondisi 1: Jalur aman jika selisih waktu minimal 30 detik (|TA - TB| >= 30.0)
if selisih_waktu >= 30.0:
    if TA < TB:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")

# Kondisi 2: Terjadi potensi konflik jika selisih waktu < 30 detik
else:
    kereta_prioritas = ""

    # Menentukan prioritas berdasarkan kelas kereta
    if prioritas_A > prioritas_B:
        kereta_prioritas = "A"
    elif prioritas_B > prioritas_A:
        kereta_prioritas = "B"
    else:
        # Jika kelas kereta sama, bandingkan waktu tiba (yang lebih cepat)
        if TA < TB:
            kereta_prioritas = "A"
        elif TB < TA:
            kereta_prioritas = "B"
        else:
            # Jika waktu tiba sama, bandingkan jarak (yang lebih dekat)
            if DA < DB:
                kereta_prioritas = "A"
            elif DB < DA:
                kereta_prioritas = "B"
            else:
                # Jika jarak juga sama, Kereta A diprioritaskan
                kereta_prioritas = "A"

    # Menghitung waktu tunggu kereta yang mengalah
    if kereta_prioritas == "A":
        waktu_tunggu = (TA + 40.0) - TB
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas. Kereta B harus berhenti dan menunggu selama", waktu_tunggu, "detik.")
    else:
        waktu_tunggu = (TB + 40.0) - TA
        print("Potensi konflik! Kereta B melintas duluan. Kereta A harus menunggu selama", waktu_tunggu, "detik.")