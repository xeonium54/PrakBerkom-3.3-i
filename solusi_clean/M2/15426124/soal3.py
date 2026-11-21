# NIM/Nama : 15426124/Muhammad Naufal Hanif
# Tanggal : 14 Oktober 2026
# Deskripsi : Pengaturan Perjalanan Kereta Api 

# Masukkan parameter kereta api A 
Jenis_A = input("Masukkan Jenis Kereta Api A (Eksekutif/Bisnis/Kargo): ")
Jarak_A = int(input("Masukkan Jarak Kereta Api A (dalam m): "))
Kecepatan_A = int(input("Masukkan kecepatan Kereta Api A (dalam m/s): "))

# Masukkan parameter kereta api B
Jenis_B = input("Masukkan Jenis Kereta Api B (Eksekutif/Bisnis/Kargo): ")
Jarak_B = int(input("Masukkan Jarak Kereta Api B (dalam m): "))
Kecepatan_B = int(input("Masukkan kecepatan Kereta Api B (dalam m/s): "))

# Menghitung waktu tiba
Waktu_A = Jarak_A / Kecepatan_A
Waktu_B = Jarak_B / Kecepatan_B

# Menghitung selisih waktu
if Waktu_A >= Waktu_B:
    Selisih_Waktu = Waktu_A - Waktu_B
else:
    Selisih_Waktu = Waktu_B - Waktu_A
    
# Menentukan tingkat prioritas jenis kereta
if Jenis_A == "Eksekutif":
    Prioritas_A = 3
elif Jenis_A == "Bisnis":
    Prioritas_A = 2
else:
    Prioritas_A = 1
    
if Jenis_B == "Eksekutif":
    Prioritas_B = 3
elif Jenis_B == "Bisnis":
    Prioritas_B = 2
else:
    Prioritas_B = 1
    
# Pengecekan selisih waktu tiba
if Selisih_Waktu >= 30.0:
    if Waktu_A < Waktu_B:
        print("Jalur aman. Kereta A melintas duluan tanpa henti.")
    else:
        print("Jalur aman. Kereta B melintas duluan tanpa henti.")
else:
    # Terjadi potensi konflik (selisih waktu < 30.0 detik)
    if Prioritas_A > Prioritas_B:
        Waktu_Tunggu = (Waktu_A + 40.0) - Waktu_B
        print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
        print(f"Kereta B harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
    elif Prioritas_B > Prioritas_A:
        Waktu_Tunggu = (Waktu_B + 40.0) - Waktu_A
        print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
        print(f"Kereta A harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
    else:
        # Jenis kereta sama, bandingkan waktu tiba
        if Waktu_A < Waktu_B:
            Waktu_Tunggu = (Waktu_A + 40.0) - Waktu_B
            print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
            print(f"Kereta B harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
        elif Waktu_B < Waktu_A:
            Waktu_Tunggu = (Waktu_B + 40.0) - Waktu_A
            print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
            print(f"Kereta A harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
        else:
            # Waktu tiba sama, bandingkan jarak terdekat
            if Jarak_A < Jarak_B:
                Waktu_Tunggu = (Waktu_A + 40.0) - Waktu_B
                print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
                print(f"Kereta B harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
            elif Jarak_B < Jarak_A:
                Waktu_Tunggu = (Waktu_B + 40.0) - Waktu_A
                print("Konflik terdeteksi! Kereta B diprioritaskan melintas.")
                print(f"Kereta A harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
            else:
                # Jarak sama persis, Kereta A diprioritaskan karena di jalur utama
                Waktu_Tunggu = (Waktu_A + 40.0) - Waktu_B
                print("Konflik terdeteksi! Kereta A diprioritaskan melintas.")
                print(f"Kereta B harus berhenti dan menunggu selama {Waktu_Tunggu:.1f} detik.")
