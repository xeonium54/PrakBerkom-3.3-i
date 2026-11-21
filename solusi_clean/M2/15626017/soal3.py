# NIM/Nama       : 15626017 / Naura Vira Vania Ramadhani
# Tanggal        : 14 Oktober 2026
# Deskripsi      : Program untuk mengatur prioritas lintasan kereta api di persimpangan rel tunggal.

# Membaca masukan Kereta A 
jenis_A = input("Masukkan jenis Kereta A (Eksekutif/Bisnis/Kargo): ")
jarak_A = int(input("Masukkan jarak Kereta A (m): "))
kecepatan_A = int(input("Masukkan kecepatan Kereta A (m/s): "))

# Membaca masukan Kereta B 
jenis_B = input("Masukkan jenis Kereta B (Eksekutif/Bisnis/Kargo): ")
jarak_B = int(input("Masukkan jarak Kereta B (m): "))
kecepatan_B = int(input("Masukkan kecepatan Kereta B (m/s): "))

# Menghitung waktu tiba masing-masing kereta (T = D / V)
T_A = jarak_A / kecepatan_A
T_B = jarak_B / kecepatan_B

# Menghitung selisih waktu tanpa menggunakan fungsi abs()
selisih_waktu = T_A - T_B
if selisih_waktu < 0:
    selisih_waktu = -selisih_waktu 

# Aturan 1 : jika selisih waktu tiba minimal 30 detik (tidak ada risiko tabrakan)
if selisih_waktu >= 30.0:
    if T_A < T_B:
        print(f"Jalur aman. Kereta A melintas duluan tanpa henti.")
    elif T_B < T_A:
        print(f"Jalur aman. Kereta B melintas duluan tanpa henti.")
    else:
        # Jika waktu tiba sama persis, cek jarak terdekat 
        if jarak_A < jarak_B:
            print(f"Jalur aman. Kereta A melintas duluan tanpa henti.")
        elif jarak_B < jarak_A:
            print(f"Jalur aman. Kereta B melintas duluan tanpa henti.")
        else:
            print(f"Jalur aman. Kereta A melintas duluan tanpa henti.")

# Aturan 2: Jika selisih waktu tiba kurang dari 30 detik (potensi konflik)
else:
    # Menentukan bobot prioritas jenis kereta (Eksekutif > Bisnis > Kargo)
    # Kita berikan nilai numerik: Eksekutif = 3, Bisnis = 2, Kargo = 1
    if jenis_A == "Eksekutif":
        prio_A = 3
    elif jenis_A == "Bisnis":
        prio_A = 2
    else:
        prio_A = 1

    if jenis_B == "Eksekutif":
        prio_B = 3 
    elif jenis_B == "Bisnis":
        prio_B = 2 
    else:
        prio_B = 1 

    # Pengecekan prioritas berdasarkan jenis kereta 
    if prio_A > prio_B:
        # Kereta A lebih diprioritaskan 
        waktu_tunggu = (T_A + 40.0) - T_B
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
        print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")
    elif prio_B > prio_A:
        # Kereta B lebih diprioritaskan 
        waktu_tunggu = (T_B + 40.0) - T_A
        print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
        print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")
    else:
        # Jenis kereta sama, bandingkan waktu tiba (T)
        if T_A < T_B:
            waktu_tunggu = (T_A + 40.0) - T_B
            print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
            print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")
        elif T_B < T_A:
            waktu_tunggu = (T_B + 40.0) - T_A
            print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
            print(f"Kereta A harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")
        else:
            # Jarak sama persis, Kereta A diprioritaskan karena di jalur utama 
            waktu_tunggu = (T_A + 40.0) - T_B
            print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
            print(f"Kereta B harus berhenti dan menunggu selama {waktu_tunggu:.1f} detik.")